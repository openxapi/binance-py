# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.api.v3_api import V3Api


class TestV3Api(unittest.TestCase):
    """V3Api unit test stubs"""

    def setUp(self) -> None:
        self.api = V3Api()

    def tearDown(self) -> None:
        pass

    def test_umfutures_get_account_v3(self) -> None:
        """Test case for umfutures_get_account_v3

        Account Information V3(USER_DATA)
        """
        pass

    def test_umfutures_get_balance_v3(self) -> None:
        """Test case for umfutures_get_balance_v3

        Futures Account Balance V3 (USER_DATA)
        """
        pass

    def test_umfutures_get_position_risk_v3(self) -> None:
        """Test case for umfutures_get_position_risk_v3

        Position Information V3 (USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
