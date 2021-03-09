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
from clever3.api.terms_api import TermsApi  # noqa: E501
from clever3.rest import ApiException


class TestTermsApi(unittest.TestCase):
    """TermsApi unit test stubs"""

    def setUp(self):
        self.api = TermsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_district_for_term(self):
        """Test case for get_district_for_term

        """
        pass

    def test_get_schools_for_term(self):
        """Test case for get_schools_for_term

        """
        pass

    def test_get_sections_for_term(self):
        """Test case for get_sections_for_term

        """
        pass

    def test_get_term(self):
        """Test case for get_term

        """
        pass

    def test_get_terms(self):
        """Test case for get_terms

        """
        pass


if __name__ == '__main__':
    unittest.main()
