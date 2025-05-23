# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.umfutures_get_exchange_info_v1_resp_assets_inner import UmfuturesGetExchangeInfoV1RespAssetsInner

class TestUmfuturesGetExchangeInfoV1RespAssetsInner(unittest.TestCase):
    """UmfuturesGetExchangeInfoV1RespAssetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetExchangeInfoV1RespAssetsInner:
        """Test UmfuturesGetExchangeInfoV1RespAssetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetExchangeInfoV1RespAssetsInner`
        """
        model = UmfuturesGetExchangeInfoV1RespAssetsInner()
        if include_optional:
            return UmfuturesGetExchangeInfoV1RespAssetsInner(
                asset = '',
                auto_asset_exchange = 56,
                margin_available = True
            )
        else:
            return UmfuturesGetExchangeInfoV1RespAssetsInner(
        )
        """

    def testUmfuturesGetExchangeInfoV1RespAssetsInner(self):
        """Test UmfuturesGetExchangeInfoV1RespAssetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
