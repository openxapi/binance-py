# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.api.copy_trading_api import CopyTradingApi


class TestCopyTradingApi(unittest.TestCase):
    """CopyTradingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CopyTradingApi()

    def tearDown(self) -> None:
        pass

    def test_get_copy_trading_futures_lead_symbol_v1(self) -> None:
        """Test case for get_copy_trading_futures_lead_symbol_v1

        Get Futures Lead Trading Symbol Whitelist(USER_DATA)
        """
        pass

    def test_get_copy_trading_futures_user_status_v1(self) -> None:
        """Test case for get_copy_trading_futures_user_status_v1

        Get Futures Lead Trader Status(TRADE)
        """
        pass


if __name__ == '__main__':
    unittest.main()
