# coding: utf-8

"""
    Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import clever
from clever.api.schools_api import SchoolsApi  # noqa: E501
from clever.rest import ApiException


class TestSchoolsApi(unittest.TestCase):
    """SchoolsApi unit test stubs"""

    def setUp(self):
        self.api = SchoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_courses_for_school(self):
        """Test case for get_courses_for_school

        """
        pass

    def test_get_district_for_school(self):
        """Test case for get_district_for_school

        """
        pass

    def test_get_school(self):
        """Test case for get_school

        """
        pass

    def test_get_schools(self):
        """Test case for get_schools

        """
        pass

    def test_get_sections_for_school(self):
        """Test case for get_sections_for_school

        """
        pass

    def test_get_terms_for_school(self):
        """Test case for get_terms_for_school

        """
        pass

    def test_get_users_for_school(self):
        """Test case for get_users_for_school

        """
        pass


if __name__ == '__main__':
    unittest.main()
