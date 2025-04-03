# coding: utf-8

"""
    Binance Convert API

    OpenAPI specification for Binance exchange - Convert API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.convert.api.trade_api import TradeApi


class TestTradeApi(unittest.TestCase):
    """TradeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TradeApi()

    def tearDown(self) -> None:
        pass

    def test_convert_create_convert_accept_quote_v1(self) -> None:
        """Test case for convert_create_convert_accept_quote_v1

        Accept Quote (TRADE)
        """
        pass

    def test_convert_create_convert_get_quote_v1(self) -> None:
        """Test case for convert_create_convert_get_quote_v1

        Send Quote Request(USER_DATA)
        """
        pass

    def test_convert_create_convert_limit_cancel_order_v1(self) -> None:
        """Test case for convert_create_convert_limit_cancel_order_v1

        Cancel limit order (USER_DATA)
        """
        pass

    def test_convert_create_convert_limit_place_order_v1(self) -> None:
        """Test case for convert_create_convert_limit_place_order_v1

        Place limit order (USER_DATA)
        """
        pass

    def test_convert_create_convert_limit_query_open_orders_v1(self) -> None:
        """Test case for convert_create_convert_limit_query_open_orders_v1

        Query limit open orders (USER_DATA)
        """
        pass

    def test_convert_get_convert_order_status_v1(self) -> None:
        """Test case for convert_get_convert_order_status_v1

        Order status(USER_DATA)
        """
        pass

    def test_convert_get_convert_trade_flow_v1(self) -> None:
        """Test case for convert_get_convert_trade_flow_v1

        Get Convert Trade History(USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
