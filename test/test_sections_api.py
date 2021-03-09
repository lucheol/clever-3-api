# coding: utf-8

"""
    Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import clever3
from clever3.api.sections_api import SectionsApi  # noqa: E501
from clever3.rest import ApiException


class TestSectionsApi(unittest.TestCase):
    """SectionsApi unit test stubs"""

    def setUp(self):
        self.api = SectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_course_for_section(self):
        """Test case for get_course_for_section

        """
        pass

    def test_get_district_for_section(self):
        """Test case for get_district_for_section

        """
        pass

    def test_get_resources_for_section(self):
        """Test case for get_resources_for_section

        """
        pass

    def test_get_school_for_section(self):
        """Test case for get_school_for_section

        """
        pass

    def test_get_section(self):
        """Test case for get_section

        """
        pass

    def test_get_sections(self):
        """Test case for get_sections

        """
        pass

    def test_get_term_for_section(self):
        """Test case for get_term_for_section

        """
        pass

    def test_get_users_for_section(self):
        """Test case for get_users_for_section

        """
        pass


if __name__ == '__main__':
    unittest.main()
