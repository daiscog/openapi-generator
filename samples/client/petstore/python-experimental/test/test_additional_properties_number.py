# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.additional_properties_number import AdditionalPropertiesNumber


class TestAdditionalPropertiesNumber(unittest.TestCase):
    """AdditionalPropertiesNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdditionalPropertiesNumber(self):
        """Test AdditionalPropertiesNumber"""
        # can make model without additional properties
        model = AdditionalPropertiesNumber()

        # can make one with additional properties
        model = AdditionalPropertiesNumber(some_key=11.3)
        assert model['some_key'] == 11.3

        # type checking works on additional properties
        with self.assertRaises(petstore_api.ApiTypeError) as exc:
            model = AdditionalPropertiesNumber(some_key=10)


if __name__ == '__main__':
    unittest.main()
