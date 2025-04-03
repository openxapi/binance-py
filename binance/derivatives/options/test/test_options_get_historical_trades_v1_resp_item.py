# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_historical_trades_v1_resp_item import OptionsGetHistoricalTradesV1RespItem

class TestOptionsGetHistoricalTradesV1RespItem(unittest.TestCase):
    """OptionsGetHistoricalTradesV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetHistoricalTradesV1RespItem:
        """Test OptionsGetHistoricalTradesV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetHistoricalTradesV1RespItem`
        """
        model = OptionsGetHistoricalTradesV1RespItem()
        if include_optional:
            return OptionsGetHistoricalTradesV1RespItem(
                id = '',
                price = '',
                qty = '',
                quote_qty = '',
                side = 56,
                time = 56,
                trade_id = ''
            )
        else:
            return OptionsGetHistoricalTradesV1RespItem(
        )
        """

    def testOptionsGetHistoricalTradesV1RespItem(self):
        """Test OptionsGetHistoricalTradesV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
