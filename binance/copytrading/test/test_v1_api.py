# coding: utf-8

"""
    Binance Copy Trading API

    OpenAPI specification for Binance exchange - Copytrading API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.copytrading.api.v1_api import V1Api


class TestV1Api(unittest.TestCase):
    """V1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = V1Api()

    def tearDown(self) -> None:
        pass

    def test_copytrading_get_copy_trading_futures_lead_symbol_v1(self) -> None:
        """Test case for copytrading_get_copy_trading_futures_lead_symbol_v1

        Get Futures Lead Trading Symbol Whitelist(USER_DATA)
        """
        pass

    def test_copytrading_get_copy_trading_futures_user_status_v1(self) -> None:
        """Test case for copytrading_get_copy_trading_futures_user_status_v1

        Get Futures Lead Trader Status(TRADE)
        """
        pass


if __name__ == '__main__':
    unittest.main()
