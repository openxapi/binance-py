# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.api.v2_api import V2Api


class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = V2Api()

    def tearDown(self) -> None:
        pass

    def test_umfutures_get_account_v2(self) -> None:
        """Test case for umfutures_get_account_v2

        Account Information V2(USER_DATA)
        """
        pass

    def test_umfutures_get_balance_v2(self) -> None:
        """Test case for umfutures_get_balance_v2

        Futures Account Balance V2 (USER_DATA)
        """
        pass

    def test_umfutures_get_position_risk_v2(self) -> None:
        """Test case for umfutures_get_position_risk_v2

        Position Information V2 (USER_DATA)
        """
        pass

    def test_umfutures_get_ticker_price_v2(self) -> None:
        """Test case for umfutures_get_ticker_price_v2

        Symbol Price Ticker V2
        """
        pass


if __name__ == '__main__':
    unittest.main()
