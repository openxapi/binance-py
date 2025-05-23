# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.options.api.market_maker_block_trade_api import MarketMakerBlockTradeApi


class TestMarketMakerBlockTradeApi(unittest.TestCase):
    """MarketMakerBlockTradeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketMakerBlockTradeApi()

    def tearDown(self) -> None:
        pass

    def test_create_block_order_create_v1(self) -> None:
        """Test case for create_block_order_create_v1

        New Block Trade Order (TRADE)
        """
        pass

    def test_delete_block_order_create_v1(self) -> None:
        """Test case for delete_block_order_create_v1

        Cancel Block Trade Order (TRADE)
        """
        pass


if __name__ == '__main__':
    unittest.main()
