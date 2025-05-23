# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_convert_exchange_info_v1_resp_item import GetConvertExchangeInfoV1RespItem

class TestGetConvertExchangeInfoV1RespItem(unittest.TestCase):
    """GetConvertExchangeInfoV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetConvertExchangeInfoV1RespItem:
        """Test GetConvertExchangeInfoV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetConvertExchangeInfoV1RespItem`
        """
        model = GetConvertExchangeInfoV1RespItem()
        if include_optional:
            return GetConvertExchangeInfoV1RespItem(
                from_asset = '',
                from_asset_max_amount = '',
                from_asset_min_amount = '',
                to_asset = '',
                to_asset_max_amount = '',
                to_asset_min_amount = ''
            )
        else:
            return GetConvertExchangeInfoV1RespItem(
        )
        """

    def testGetConvertExchangeInfoV1RespItem(self):
        """Test GetConvertExchangeInfoV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
