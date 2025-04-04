# coding: utf-8

"""
    Binance Convert API

    OpenAPI specification for Binance exchange - Convert API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.convert.api.market_data_api import MarketDataApi


class TestMarketDataApi(unittest.TestCase):
    """MarketDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketDataApi()

    def tearDown(self) -> None:
        pass

    def test_convert_get_convert_asset_info_v1(self) -> None:
        """Test case for convert_get_convert_asset_info_v1

        Query order quantity precision per asset(USER_DATA)
        """
        pass

    def test_convert_get_convert_exchange_info_v1(self) -> None:
        """Test case for convert_get_convert_exchange_info_v1

        List All Convert Pairs
        """
        pass


if __name__ == '__main__':
    unittest.main()
