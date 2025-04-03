# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.api.portfolio_margin_endpoints_api import PortfolioMarginEndpointsApi


class TestPortfolioMarginEndpointsApi(unittest.TestCase):
    """PortfolioMarginEndpointsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortfolioMarginEndpointsApi()

    def tearDown(self) -> None:
        pass

    def test_cmfutures_get_pm_account_info_v1(self) -> None:
        """Test case for cmfutures_get_pm_account_info_v1

        Classic Portfolio Margin Account Information (USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
