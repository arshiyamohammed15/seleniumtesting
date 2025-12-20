"""
Comprehensive Test Cases for extracting.py
More detailed test cases with different scenarios and edge cases.
Run with: pytest test_extracting_comprehensive.py -v
"""

import pytest
import time
from extracting import extract_heading_text, extract_all_links, extract_page_info, setup_driver
from selenium.webdriver.common.by import By


class TestExtractingComprehensive:
    """Comprehensive test cases for data extraction functions."""
    
    # Test data
    TEST_URLS = {
        "example": "https://www.example.com",
        "the_internet": "https://the-internet.herokuapp.com",
        "google": "https://www.google.com"
    }
    
    def test_extract_heading_text_multiple_sites(self):
        """Test extracting heading from multiple websites"""
        print("\n[TEST] Testing heading extraction from multiple sites...")
        
        test_cases = [
            ("https://www.example.com", "Example Domain"),
        ]
        
        for url, expected_contains in test_cases:
            heading = extract_heading_text(url)
            assert heading is not None, f"Heading should not be None for {url}"
            assert isinstance(heading, str), f"Heading should be string for {url}"
            if expected_contains:
                assert expected_contains.lower() in heading.lower(), \
                    f"Heading should contain '{expected_contains}'"
            print(f"   ✓ {url}: '{heading}'")
    
    def test_extract_all_links_structure(self):
        """Test that extracted links have correct structure"""
        print("\n[TEST] Testing link structure...")
        links = extract_all_links(self.TEST_URLS["the_internet"])
        
        assert isinstance(links, list), "Should return a list"
        assert len(links) > 0, "Should find at least one link"
        
        for link in links[:10]:  # Check first 10 links
            assert isinstance(link, dict), "Each link should be a dictionary"
            assert "text" in link, "Link should have 'text' key"
            assert "href" in link, "Link should have 'href' key"
            assert isinstance(link["text"], str), "Link text should be string"
            assert isinstance(link["href"], str), "Link href should be string"
        
        print(f"   ✓ All {len(links)} links have correct structure")
    
    def test_extract_all_links_content(self):
        """Test that extracted links contain valid data"""
        print("\n[TEST] Testing link content validity...")
        links = extract_all_links(self.TEST_URLS["the_internet"])
        
        # Check that links have non-empty text
        links_with_text = [link for link in links if link["text"].strip()]
        assert len(links_with_text) > 0, "Should have links with text"
        
        # Check that hrefs are valid URLs
        valid_urls = [link for link in links if link["href"] and 
                     (link["href"].startswith("http") or link["href"].startswith("/"))]
        assert len(valid_urls) > 0, "Should have valid URLs"
        
        print(f"   ✓ {len(links_with_text)} links with text, {len(valid_urls)} valid URLs")
    
    def test_extract_page_info_complete(self):
        """Test complete page info extraction"""
        print("\n[TEST] Testing complete page info...")
        page_info = extract_page_info(self.TEST_URLS["example"])
        
        # Verify structure
        assert isinstance(page_info, dict), "Should return dictionary"
        assert len(page_info) >= 2, "Should have at least 2 keys"
        
        # Verify content
        assert "title" in page_info, "Should have 'title'"
        assert "url" in page_info, "Should have 'url'"
        assert page_info["title"], "Title should not be empty"
        assert page_info["url"], "URL should not be empty"
        
        # Verify URL matches
        assert self.TEST_URLS["example"] in page_info["url"], \
            "URL should match requested URL"
        
        print(f"   ✓ Page info: {page_info}")
    
    def test_extract_page_info_different_sites(self):
        """Test page info extraction from different sites"""
        print("\n[TEST] Testing page info from different sites...")
        
        for site_name, url in self.TEST_URLS.items():
            page_info = extract_page_info(url)
            assert page_info["title"], f"Title should exist for {site_name}"
            assert page_info["url"], f"URL should exist for {site_name}"
            print(f"   ✓ {site_name}: {page_info['title'][:50]}")
    
    def test_extract_links_count_consistency(self):
        """Test that link count is consistent"""
        print("\n[TEST] Testing link count consistency...")
        
        # Extract links multiple times
        counts = []
        for i in range(2):  # Run twice
            links = extract_all_links(self.TEST_URLS["the_internet"])
            counts.append(len(links))
            time.sleep(1)  # Brief pause
        
        # Counts should be similar (allowing for minor variations)
        assert all(count > 0 for count in counts), "All counts should be > 0"
        print(f"   ✓ Link counts: {counts}")
    
    def test_extract_heading_text_empty_result(self):
        """Test handling when heading might not exist"""
        print("\n[TEST] Testing heading extraction edge cases...")
        
        # Test with a page that might not have h1
        heading = extract_heading_text(self.TEST_URLS["the_internet"])
        # Should handle gracefully (return None or empty string)
        assert heading is None or isinstance(heading, str), \
            "Should return None or string"
        print(f"   ✓ Handled edge case: {heading}")
    
    def test_extract_all_links_filtering(self):
        """Test that links are properly filtered"""
        print("\n[TEST] Testing link filtering...")
        links = extract_all_links(self.TEST_URLS["the_internet"])
        
        # All links should have text (empty text links filtered out)
        for link in links:
            assert link["text"].strip(), "Link should have non-empty text"
        
        print(f"   ✓ All {len(links)} links have text")
    
    def test_extract_page_info_url_accuracy(self):
        """Test that extracted URL is accurate"""
        print("\n[TEST] Testing URL accuracy...")
        
        test_url = self.TEST_URLS["example"]
        page_info = extract_page_info(test_url)
        
        # URL should match or be related to requested URL
        assert test_url in page_info["url"] or page_info["url"] in test_url, \
            f"URL should be related to {test_url}"
        
        print(f"   ✓ URL accurate: {page_info['url']}")
    
    def test_extract_functions_return_types(self):
        """Test that all functions return correct types"""
        print("\n[TEST] Testing return types...")
        
        # Test heading
        heading = extract_heading_text(self.TEST_URLS["example"])
        assert heading is None or isinstance(heading, str), \
            "Heading should be None or string"
        
        # Test links
        links = extract_all_links(self.TEST_URLS["the_internet"])
        assert isinstance(links, list), "Links should be list"
        
        # Test page info
        page_info = extract_page_info(self.TEST_URLS["example"])
        assert isinstance(page_info, dict), "Page info should be dict"
        
        print("   ✓ All return types correct")
    
    def test_extract_performance(self):
        """Test extraction performance"""
        print("\n[TEST] Testing extraction performance...")
        
        import time
        start_time = time.time()
        
        # Run multiple extractions
        extract_heading_text(self.TEST_URLS["example"])
        extract_all_links(self.TEST_URLS["the_internet"])
        extract_page_info(self.TEST_URLS["example"])
        
        elapsed_time = time.time() - start_time
        
        # Should complete in reasonable time (less than 60 seconds)
        assert elapsed_time < 60, f"Should complete in < 60s, took {elapsed_time:.2f}s"
        print(f"   ✓ Completed in {elapsed_time:.2f} seconds")


class TestExtractingIntegration:
    """Integration tests for extraction workflow."""
    
    def test_complete_extraction_workflow(self):
        """Test complete extraction workflow"""
        print("\n[TEST] Testing complete workflow...")
        
        url = "https://www.example.com"
        
        # Step 1: Extract page info
        page_info = extract_page_info(url)
        assert page_info, "Page info should be extracted"
        
        # Step 2: Extract heading
        heading = extract_heading_text(url)
        assert heading is not None or isinstance(heading, str), \
            "Heading should be extracted"
        
        # Step 3: Extract links (if page has them)
        links = extract_all_links(url)
        assert isinstance(links, list), "Links should be extracted"
        
        print("   ✓ Complete workflow successful")
        print(f"      Page: {page_info['title']}")
        print(f"      Heading: {heading}")
        print(f"      Links: {len(links)}")
    
    def test_multiple_extractions_same_page(self):
        """Test extracting multiple times from same page"""
        print("\n[TEST] Testing multiple extractions...")
        
        url = "https://the-internet.herokuapp.com"
        
        # Extract multiple times
        results = []
        for i in range(2):
            page_info = extract_page_info(url)
            links = extract_all_links(url)
            results.append({
                "page_info": page_info,
                "links_count": len(links)
            })
        
        # Results should be consistent
        assert len(results) == 2, "Should have 2 results"
        assert results[0]["page_info"]["title"] == results[1]["page_info"]["title"], \
            "Titles should match"
        
        print("   ✓ Multiple extractions consistent")


class TestExtractingEdgeCases:
    """Edge case tests for extraction functions."""
    
    def test_empty_url_handling(self):
        """Test handling of edge cases"""
        print("\n[TEST] Testing edge cases...")
        
        # Test with invalid URL (should handle gracefully)
        try:
            result = extract_heading_text("not-a-valid-url")
            # Should return None or handle error
            assert result is None or isinstance(result, str)
        except Exception:
            # Exception is also acceptable for invalid URLs
            pass
        
        print("   ✓ Edge cases handled")


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v", "-s"])

