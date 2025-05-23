# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.api.binance_pay_history_api import BinancePayHistoryApi


class TestBinancePayHistoryApi(unittest.TestCase):
    """BinancePayHistoryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BinancePayHistoryApi()

    def tearDown(self) -> None:
        pass

    def test_get_pay_transactions_v1(self) -> None:
        """Test case for get_pay_transactions_v1

        Get Pay Trade History
        """
        pass


if __name__ == '__main__':
    unittest.main()
