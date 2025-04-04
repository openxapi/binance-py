# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_convert_exchange_info_v1_resp_item import UmfuturesGetConvertExchangeInfoV1RespItem

class TestUmfuturesGetConvertExchangeInfoV1RespItem(unittest.TestCase):
    """UmfuturesGetConvertExchangeInfoV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetConvertExchangeInfoV1RespItem:
        """Test UmfuturesGetConvertExchangeInfoV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetConvertExchangeInfoV1RespItem`
        """
        model = UmfuturesGetConvertExchangeInfoV1RespItem()
        if include_optional:
            return UmfuturesGetConvertExchangeInfoV1RespItem(
                from_asset = '',
                from_asset_max_amount = '',
                from_asset_min_amount = '',
                to_asset = '',
                to_asset_max_amount = '',
                to_asset_min_amount = ''
            )
        else:
            return UmfuturesGetConvertExchangeInfoV1RespItem(
        )
        """

    def testUmfuturesGetConvertExchangeInfoV1RespItem(self):
        """Test UmfuturesGetConvertExchangeInfoV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
