# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.api.trade_api import TradeApi


class TestTradeApi(unittest.TestCase):
    """TradeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TradeApi()

    def tearDown(self) -> None:
        pass

    def test_umfutures_create_batch_orders_v1(self) -> None:
        """Test case for umfutures_create_batch_orders_v1

        Place Multiple Orders(TRADE)
        """
        pass

    def test_umfutures_create_countdown_cancel_all_v1(self) -> None:
        """Test case for umfutures_create_countdown_cancel_all_v1

        Auto-Cancel All Open Orders (TRADE)
        """
        pass

    def test_umfutures_create_leverage_v1(self) -> None:
        """Test case for umfutures_create_leverage_v1

        Change Initial Leverage(TRADE)
        """
        pass

    def test_umfutures_create_margin_type_v1(self) -> None:
        """Test case for umfutures_create_margin_type_v1

        Change Margin Type(TRADE)
        """
        pass

    def test_umfutures_create_multi_assets_margin_v1(self) -> None:
        """Test case for umfutures_create_multi_assets_margin_v1

        Change Multi-Assets Mode (TRADE)
        """
        pass

    def test_umfutures_create_order_test_v1(self) -> None:
        """Test case for umfutures_create_order_test_v1

        Test Order(TRADE)
        """
        pass

    def test_umfutures_create_order_v1(self) -> None:
        """Test case for umfutures_create_order_v1

        New Order(TRADE)
        """
        pass

    def test_umfutures_create_position_margin_v1(self) -> None:
        """Test case for umfutures_create_position_margin_v1

        Modify Isolated Position Margin(TRADE)
        """
        pass

    def test_umfutures_create_position_side_dual_v1(self) -> None:
        """Test case for umfutures_create_position_side_dual_v1

        Change Position Mode(TRADE)
        """
        pass

    def test_umfutures_delete_all_open_orders_v1(self) -> None:
        """Test case for umfutures_delete_all_open_orders_v1

        Cancel All Open Orders (TRADE)
        """
        pass

    def test_umfutures_delete_batch_orders_v1(self) -> None:
        """Test case for umfutures_delete_batch_orders_v1

        Cancel Multiple Orders (TRADE)
        """
        pass

    def test_umfutures_delete_order_v1(self) -> None:
        """Test case for umfutures_delete_order_v1

        Cancel Order (TRADE)
        """
        pass

    def test_umfutures_get_adl_quantile_v1(self) -> None:
        """Test case for umfutures_get_adl_quantile_v1

        Position ADL Quantile Estimation(USER_DATA)
        """
        pass

    def test_umfutures_get_all_orders_v1(self) -> None:
        """Test case for umfutures_get_all_orders_v1

        All Orders (USER_DATA)
        """
        pass

    def test_umfutures_get_force_orders_v1(self) -> None:
        """Test case for umfutures_get_force_orders_v1

        User's Force Orders (USER_DATA)
        """
        pass

    def test_umfutures_get_open_order_v1(self) -> None:
        """Test case for umfutures_get_open_order_v1

        Query Current Open Order (USER_DATA)
        """
        pass

    def test_umfutures_get_open_orders_v1(self) -> None:
        """Test case for umfutures_get_open_orders_v1

        Current All Open Orders (USER_DATA)
        """
        pass

    def test_umfutures_get_order_amendment_v1(self) -> None:
        """Test case for umfutures_get_order_amendment_v1

        Get Order Modify History (USER_DATA)
        """
        pass

    def test_umfutures_get_order_v1(self) -> None:
        """Test case for umfutures_get_order_v1

        Query Order (USER_DATA)
        """
        pass

    def test_umfutures_get_position_margin_history_v1(self) -> None:
        """Test case for umfutures_get_position_margin_history_v1

        Get Position Margin Change History (TRADE)
        """
        pass

    def test_umfutures_get_position_risk_v2(self) -> None:
        """Test case for umfutures_get_position_risk_v2

        Position Information V2 (USER_DATA)
        """
        pass

    def test_umfutures_get_position_risk_v3(self) -> None:
        """Test case for umfutures_get_position_risk_v3

        Position Information V3 (USER_DATA)
        """
        pass

    def test_umfutures_get_user_trades_v1(self) -> None:
        """Test case for umfutures_get_user_trades_v1

        Account Trade List (USER_DATA)
        """
        pass

    def test_umfutures_update_batch_orders_v1(self) -> None:
        """Test case for umfutures_update_batch_orders_v1

        Modify Multiple Orders(TRADE)
        """
        pass

    def test_umfutures_update_order_v1(self) -> None:
        """Test case for umfutures_update_order_v1

        Modify Order (TRADE)
        """
        pass


if __name__ == '__main__':
    unittest.main()
