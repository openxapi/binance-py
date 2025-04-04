# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.api.account_api import AccountApi


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountApi()

    def tearDown(self) -> None:
        pass

    def test_cmfutures_get_account_v1(self) -> None:
        """Test case for cmfutures_get_account_v1

        Account Information (USER_DATA)
        """
        pass

    def test_cmfutures_get_balance_v1(self) -> None:
        """Test case for cmfutures_get_balance_v1

        Futures Account Balance (USER_DATA)
        """
        pass

    def test_cmfutures_get_commission_rate_v1(self) -> None:
        """Test case for cmfutures_get_commission_rate_v1

        User Commission Rate (USER_DATA)
        """
        pass

    def test_cmfutures_get_income_asyn_id_v1(self) -> None:
        """Test case for cmfutures_get_income_asyn_id_v1

        Get Futures Transaction History Download Link by Id (USER_DATA)
        """
        pass

    def test_cmfutures_get_income_asyn_v1(self) -> None:
        """Test case for cmfutures_get_income_asyn_v1

        Get Download Id For Futures Transaction History(USER_DATA)
        """
        pass

    def test_cmfutures_get_income_v1(self) -> None:
        """Test case for cmfutures_get_income_v1

        Get Income History(USER_DATA)
        """
        pass

    def test_cmfutures_get_leverage_bracket_v1(self) -> None:
        """Test case for cmfutures_get_leverage_bracket_v1

        Notional Bracket for Pair(USER_DATA)
        """
        pass

    def test_cmfutures_get_leverage_bracket_v2(self) -> None:
        """Test case for cmfutures_get_leverage_bracket_v2

        Notional Bracket for Symbol(USER_DATA)
        """
        pass

    def test_cmfutures_get_order_asyn_id_v1(self) -> None:
        """Test case for cmfutures_get_order_asyn_id_v1

        Get Futures Order History Download Link by Id (USER_DATA)
        """
        pass

    def test_cmfutures_get_order_asyn_v1(self) -> None:
        """Test case for cmfutures_get_order_asyn_v1

        Get Download Id For Futures Order History (USER_DATA)
        """
        pass

    def test_cmfutures_get_position_side_dual_v1(self) -> None:
        """Test case for cmfutures_get_position_side_dual_v1

        Get Current Position Mode(USER_DATA)
        """
        pass

    def test_cmfutures_get_trade_asyn_id_v1(self) -> None:
        """Test case for cmfutures_get_trade_asyn_id_v1

        Get Futures Trade Download Link by Id(USER_DATA)
        """
        pass

    def test_cmfutures_get_trade_asyn_v1(self) -> None:
        """Test case for cmfutures_get_trade_asyn_v1

        Get Download Id For Futures Trade History (USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
