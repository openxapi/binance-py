# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_historical_trades_v1_resp_item import UmfuturesGetHistoricalTradesV1RespItem

class TestUmfuturesGetHistoricalTradesV1RespItem(unittest.TestCase):
    """UmfuturesGetHistoricalTradesV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetHistoricalTradesV1RespItem:
        """Test UmfuturesGetHistoricalTradesV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetHistoricalTradesV1RespItem`
        """
        model = UmfuturesGetHistoricalTradesV1RespItem()
        if include_optional:
            return UmfuturesGetHistoricalTradesV1RespItem(
                id = 56,
                is_buyer_maker = True,
                price = '',
                qty = '',
                quote_qty = '',
                time = 56
            )
        else:
            return UmfuturesGetHistoricalTradesV1RespItem(
        )
        """

    def testUmfuturesGetHistoricalTradesV1RespItem(self):
        """Test UmfuturesGetHistoricalTradesV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
