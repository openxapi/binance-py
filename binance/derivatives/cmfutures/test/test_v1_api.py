# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.api.v1_api import V1Api


class TestV1Api(unittest.TestCase):
    """V1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = V1Api()

    def tearDown(self) -> None:
        pass

    def test_cmfutures_create_batch_orders_v1(self) -> None:
        """Test case for cmfutures_create_batch_orders_v1

        Place Multiple Orders(TRADE)
        """
        pass

    def test_cmfutures_create_countdown_cancel_all_v1(self) -> None:
        """Test case for cmfutures_create_countdown_cancel_all_v1

        Auto-Cancel All Open Orders (TRADE)
        """
        pass

    def test_cmfutures_create_leverage_v1(self) -> None:
        """Test case for cmfutures_create_leverage_v1

        Change Initial Leverage (TRADE)
        """
        pass

    def test_cmfutures_create_listen_key_v1(self) -> None:
        """Test case for cmfutures_create_listen_key_v1

        Start User Data Stream (USER_STREAM)
        """
        pass

    def test_cmfutures_create_margin_type_v1(self) -> None:
        """Test case for cmfutures_create_margin_type_v1

        Change Margin Type (TRADE)
        """
        pass

    def test_cmfutures_create_order_v1(self) -> None:
        """Test case for cmfutures_create_order_v1

        New Order (TRADE)
        """
        pass

    def test_cmfutures_create_position_margin_v1(self) -> None:
        """Test case for cmfutures_create_position_margin_v1

        Modify Isolated Position Margin(TRADE)
        """
        pass

    def test_cmfutures_create_position_side_dual_v1(self) -> None:
        """Test case for cmfutures_create_position_side_dual_v1

        Change Position Mode(TRADE)
        """
        pass

    def test_cmfutures_delete_all_open_orders_v1(self) -> None:
        """Test case for cmfutures_delete_all_open_orders_v1

        Cancel All Open Orders(TRADE)
        """
        pass

    def test_cmfutures_delete_batch_orders_v1(self) -> None:
        """Test case for cmfutures_delete_batch_orders_v1

        Cancel Multiple Orders(TRADE)
        """
        pass

    def test_cmfutures_delete_listen_key_v1(self) -> None:
        """Test case for cmfutures_delete_listen_key_v1

        Close User Data Stream(USER_STREAM)
        """
        pass

    def test_cmfutures_delete_order_v1(self) -> None:
        """Test case for cmfutures_delete_order_v1

        Cancel Order (TRADE)
        """
        pass

    def test_cmfutures_get_account_v1(self) -> None:
        """Test case for cmfutures_get_account_v1

        Account Information (USER_DATA)
        """
        pass

    def test_cmfutures_get_adl_quantile_v1(self) -> None:
        """Test case for cmfutures_get_adl_quantile_v1

        Position ADL Quantile Estimation(USER_DATA)
        """
        pass

    def test_cmfutures_get_agg_trades_v1(self) -> None:
        """Test case for cmfutures_get_agg_trades_v1

        Compressed/Aggregate Trades List
        """
        pass

    def test_cmfutures_get_all_orders_v1(self) -> None:
        """Test case for cmfutures_get_all_orders_v1

        All Orders (USER_DATA)
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

    def test_cmfutures_get_constituents_v1(self) -> None:
        """Test case for cmfutures_get_constituents_v1

        Query Index Price Constituents
        """
        pass

    def test_cmfutures_get_continuous_klines_v1(self) -> None:
        """Test case for cmfutures_get_continuous_klines_v1

        Continuous Contract Kline/Candlestick Data
        """
        pass

    def test_cmfutures_get_depth_v1(self) -> None:
        """Test case for cmfutures_get_depth_v1

        Order Book
        """
        pass

    def test_cmfutures_get_exchange_info_v1(self) -> None:
        """Test case for cmfutures_get_exchange_info_v1

        Exchange Information
        """
        pass

    def test_cmfutures_get_force_orders_v1(self) -> None:
        """Test case for cmfutures_get_force_orders_v1

        User's Force Orders(USER_DATA)
        """
        pass

    def test_cmfutures_get_funding_info_v1(self) -> None:
        """Test case for cmfutures_get_funding_info_v1

        Get Funding Rate Info
        """
        pass

    def test_cmfutures_get_funding_rate_v1(self) -> None:
        """Test case for cmfutures_get_funding_rate_v1

        Get Funding Rate History of Perpetual Futures
        """
        pass

    def test_cmfutures_get_historical_trades_v1(self) -> None:
        """Test case for cmfutures_get_historical_trades_v1

        Old Trades Lookup(MARKET_DATA)
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

    def test_cmfutures_get_index_price_klines_v1(self) -> None:
        """Test case for cmfutures_get_index_price_klines_v1

        Index Price Kline/Candlestick Data
        """
        pass

    def test_cmfutures_get_klines_v1(self) -> None:
        """Test case for cmfutures_get_klines_v1

        Kline/Candlestick Data
        """
        pass

    def test_cmfutures_get_leverage_bracket_v1(self) -> None:
        """Test case for cmfutures_get_leverage_bracket_v1

        Notional Bracket for Pair(USER_DATA)
        """
        pass

    def test_cmfutures_get_mark_price_klines_v1(self) -> None:
        """Test case for cmfutures_get_mark_price_klines_v1

        Mark Price Kline/Candlestick Data
        """
        pass

    def test_cmfutures_get_open_interest_v1(self) -> None:
        """Test case for cmfutures_get_open_interest_v1

        Open Interest
        """
        pass

    def test_cmfutures_get_open_order_v1(self) -> None:
        """Test case for cmfutures_get_open_order_v1

        Query Current Open Order(USER_DATA)
        """
        pass

    def test_cmfutures_get_open_orders_v1(self) -> None:
        """Test case for cmfutures_get_open_orders_v1

        Current All Open Orders (USER_DATA)
        """
        pass

    def test_cmfutures_get_order_amendment_v1(self) -> None:
        """Test case for cmfutures_get_order_amendment_v1

        Get Order Modify History (USER_DATA)
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

    def test_cmfutures_get_order_v1(self) -> None:
        """Test case for cmfutures_get_order_v1

        Query Order (USER_DATA)
        """
        pass

    def test_cmfutures_get_ping_v1(self) -> None:
        """Test case for cmfutures_get_ping_v1

        Test Connectivity
        """
        pass

    def test_cmfutures_get_pm_account_info_v1(self) -> None:
        """Test case for cmfutures_get_pm_account_info_v1

        Classic Portfolio Margin Account Information (USER_DATA)
        """
        pass

    def test_cmfutures_get_position_margin_history_v1(self) -> None:
        """Test case for cmfutures_get_position_margin_history_v1

        Get Position Margin Change History(TRADE)
        """
        pass

    def test_cmfutures_get_position_risk_v1(self) -> None:
        """Test case for cmfutures_get_position_risk_v1

        Position Information(USER_DATA)
        """
        pass

    def test_cmfutures_get_position_side_dual_v1(self) -> None:
        """Test case for cmfutures_get_position_side_dual_v1

        Get Current Position Mode(USER_DATA)
        """
        pass

    def test_cmfutures_get_premium_index_klines_v1(self) -> None:
        """Test case for cmfutures_get_premium_index_klines_v1

        Premium index Kline Data
        """
        pass

    def test_cmfutures_get_premium_index_v1(self) -> None:
        """Test case for cmfutures_get_premium_index_v1

        Index Price and Mark Price
        """
        pass

    def test_cmfutures_get_ticker24hr_v1(self) -> None:
        """Test case for cmfutures_get_ticker24hr_v1

        24hr Ticker Price Change Statistics
        """
        pass

    def test_cmfutures_get_ticker_book_ticker_v1(self) -> None:
        """Test case for cmfutures_get_ticker_book_ticker_v1

        Symbol Order Book Ticker
        """
        pass

    def test_cmfutures_get_ticker_price_v1(self) -> None:
        """Test case for cmfutures_get_ticker_price_v1

        Symbol Price Ticker
        """
        pass

    def test_cmfutures_get_time_v1(self) -> None:
        """Test case for cmfutures_get_time_v1

        Check Server time
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

    def test_cmfutures_get_trades_v1(self) -> None:
        """Test case for cmfutures_get_trades_v1

        Recent Trades List
        """
        pass

    def test_cmfutures_get_user_trades_v1(self) -> None:
        """Test case for cmfutures_get_user_trades_v1

        Account Trade List (USER_DATA)
        """
        pass

    def test_cmfutures_update_batch_orders_v1(self) -> None:
        """Test case for cmfutures_update_batch_orders_v1

        Modify Multiple Orders(TRADE)
        """
        pass

    def test_cmfutures_update_listen_key_v1(self) -> None:
        """Test case for cmfutures_update_listen_key_v1

        Keepalive User Data Stream (USER_STREAM)
        """
        pass

    def test_cmfutures_update_order_v1(self) -> None:
        """Test case for cmfutures_update_order_v1

        Modify Order (TRADE)
        """
        pass


if __name__ == '__main__':
    unittest.main()
