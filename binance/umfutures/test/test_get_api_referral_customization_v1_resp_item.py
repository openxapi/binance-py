# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.get_api_referral_customization_v1_resp_item import GetApiReferralCustomizationV1RespItem

class TestGetApiReferralCustomizationV1RespItem(unittest.TestCase):
    """GetApiReferralCustomizationV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiReferralCustomizationV1RespItem:
        """Test GetApiReferralCustomizationV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiReferralCustomizationV1RespItem`
        """
        model = GetApiReferralCustomizationV1RespItem()
        if include_optional:
            return GetApiReferralCustomizationV1RespItem(
                customer_id = '',
                email = ''
            )
        else:
            return GetApiReferralCustomizationV1RespItem(
        )
        """

    def testGetApiReferralCustomizationV1RespItem(self):
        """Test GetApiReferralCustomizationV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
