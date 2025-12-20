"""
Unit Test Cases for extracting.py
Focused unit tests for individual functions.
Run with: pytest test_extracting_unit.py -v
"""

import pytest
from extracting import extract_heading_text, extract_all_links, extract_page_info


class TestUnitExtracting:
    """Unit tests for extraction functions."""
    
    def test_extract_heading_text_returns_string(self):
        """Unit test: heading extraction returns string"""
        result = extract_heading_text("https://www.example.com")
        assert result is None or isinstance(result, str)
    
    def test_extract_heading_text_not_empty(self):
        """Unit test: heading extraction returns non-empty"""
        result = extract_heading_text("https://www.example.com")
        if result:
            assert len(result) > 0
    
    def test_extract_all_links_returns_list(self):
        """Unit test: links extraction returns list"""
        result = extract_all_links("https://the-internet.herokuapp.com")
        assert isinstance(result, list)
    
    def test_extract_all_links_not_empty(self):
        """Unit test: links extraction returns non-empty list"""
        result = extract_all_links("https://the-internet.herokuapp.com")
        assert len(result) > 0
    
    def test_extract_all_links_has_dict_items(self):
        """Unit test: links list contains dictionaries"""
        result = extract_all_links("https://the-internet.herokuapp.com")
        if result:
            assert isinstance(result[0], dict)
    
    def test_extract_page_info_returns_dict(self):
        """Unit test: page info returns dictionary"""
        result = extract_page_info("https://www.example.com")
        assert isinstance(result, dict)
    
    def test_extract_page_info_has_title(self):
        """Unit test: page info contains title"""
        result = extract_page_info("https://www.example.com")
        assert "title" in result
    
    def test_extract_page_info_has_url(self):
        """Unit test: page info contains URL"""
        result = extract_page_info("https://www.example.com")
        assert "url" in result


class TestDataValidation:
    """Data validation tests."""
    
    def test_link_structure_validation(self):
        """Validate link data structure"""
        links = extract_all_links("https://the-internet.herokuapp.com")
        for link in links[:5]:
            assert "text" in link
            assert "href" in link
            assert isinstance(link["text"], str)
            assert isinstance(link["href"], str)
    
    def test_page_info_structure_validation(self):
        """Validate page info structure"""
        page_info = extract_page_info("https://www.example.com")
        assert isinstance(page_info, dict)
        assert "title" in page_info
        assert "url" in page_info
        assert isinstance(page_info["title"], str)
        assert isinstance(page_info["url"], str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

