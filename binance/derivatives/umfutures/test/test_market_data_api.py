# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.api.market_data_api import MarketDataApi


class TestMarketDataApi(unittest.TestCase):
    """MarketDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketDataApi()

    def tearDown(self) -> None:
        pass

    def test_umfutures_get_agg_trades_v1(self) -> None:
        """Test case for umfutures_get_agg_trades_v1

        Compressed/Aggregate Trades List
        """
        pass

    def test_umfutures_get_asset_index_v1(self) -> None:
        """Test case for umfutures_get_asset_index_v1

        Multi-Assets Mode Asset Index
        """
        pass

    def test_umfutures_get_constituents_v1(self) -> None:
        """Test case for umfutures_get_constituents_v1

        Query Index Price Constituents
        """
        pass

    def test_umfutures_get_continuous_klines_v1(self) -> None:
        """Test case for umfutures_get_continuous_klines_v1

        Continuous Contract Kline/Candlestick Data
        """
        pass

    def test_umfutures_get_depth_v1(self) -> None:
        """Test case for umfutures_get_depth_v1

        Order Book
        """
        pass

    def test_umfutures_get_exchange_info_v1(self) -> None:
        """Test case for umfutures_get_exchange_info_v1

        Exchange Information
        """
        pass

    def test_umfutures_get_funding_info_v1(self) -> None:
        """Test case for umfutures_get_funding_info_v1

        Get Funding Rate Info
        """
        pass

    def test_umfutures_get_funding_rate_v1(self) -> None:
        """Test case for umfutures_get_funding_rate_v1

        Get Funding Rate History
        """
        pass

    def test_umfutures_get_futures_data_basis(self) -> None:
        """Test case for umfutures_get_futures_data_basis

        Basis
        """
        pass

    def test_umfutures_get_futures_data_delivery_price(self) -> None:
        """Test case for umfutures_get_futures_data_delivery_price

        Quarterly Contract Settlement Price
        """
        pass

    def test_umfutures_get_futures_data_global_long_short_account_ratio(self) -> None:
        """Test case for umfutures_get_futures_data_global_long_short_account_ratio

        Long/Short Ratio
        """
        pass

    def test_umfutures_get_futures_data_open_interest_hist(self) -> None:
        """Test case for umfutures_get_futures_data_open_interest_hist

        Open Interest Statistics
        """
        pass

    def test_umfutures_get_futures_data_takerlongshort_ratio(self) -> None:
        """Test case for umfutures_get_futures_data_takerlongshort_ratio

        Taker Buy/Sell Volume
        """
        pass

    def test_umfutures_get_futures_data_top_long_short_account_ratio(self) -> None:
        """Test case for umfutures_get_futures_data_top_long_short_account_ratio

        Top Trader Long/Short Ratio (Accounts)
        """
        pass

    def test_umfutures_get_futures_data_top_long_short_position_ratio(self) -> None:
        """Test case for umfutures_get_futures_data_top_long_short_position_ratio

        Top Trader Long/Short Ratio (Positions)
        """
        pass

    def test_umfutures_get_historical_trades_v1(self) -> None:
        """Test case for umfutures_get_historical_trades_v1

        Old Trades Lookup (MARKET_DATA)
        """
        pass

    def test_umfutures_get_index_info_v1(self) -> None:
        """Test case for umfutures_get_index_info_v1

        Composite Index Symbol Information
        """
        pass

    def test_umfutures_get_index_price_klines_v1(self) -> None:
        """Test case for umfutures_get_index_price_klines_v1

        Index Price Kline/Candlestick Data
        """
        pass

    def test_umfutures_get_klines_v1(self) -> None:
        """Test case for umfutures_get_klines_v1

        Kline/Candlestick Data
        """
        pass

    def test_umfutures_get_mark_price_klines_v1(self) -> None:
        """Test case for umfutures_get_mark_price_klines_v1

        Mark Price Kline/Candlestick Data
        """
        pass

    def test_umfutures_get_open_interest_v1(self) -> None:
        """Test case for umfutures_get_open_interest_v1

        Open Interest
        """
        pass

    def test_umfutures_get_ping_v1(self) -> None:
        """Test case for umfutures_get_ping_v1

        Test Connectivity
        """
        pass

    def test_umfutures_get_premium_index_klines_v1(self) -> None:
        """Test case for umfutures_get_premium_index_klines_v1

        Premium index Kline Data
        """
        pass

    def test_umfutures_get_premium_index_v1(self) -> None:
        """Test case for umfutures_get_premium_index_v1

        Mark Price
        """
        pass

    def test_umfutures_get_ticker24hr_v1(self) -> None:
        """Test case for umfutures_get_ticker24hr_v1

        24hr Ticker Price Change Statistics
        """
        pass

    def test_umfutures_get_ticker_book_ticker_v1(self) -> None:
        """Test case for umfutures_get_ticker_book_ticker_v1

        Symbol Order Book Ticker
        """
        pass

    def test_umfutures_get_ticker_price_v1(self) -> None:
        """Test case for umfutures_get_ticker_price_v1

        Symbol Price Ticker
        """
        pass

    def test_umfutures_get_ticker_price_v2(self) -> None:
        """Test case for umfutures_get_ticker_price_v2

        Symbol Price Ticker V2
        """
        pass

    def test_umfutures_get_time_v1(self) -> None:
        """Test case for umfutures_get_time_v1

        Check Server Time
        """
        pass

    def test_umfutures_get_trades_v1(self) -> None:
        """Test case for umfutures_get_trades_v1

        Recent Trades List
        """
        pass


if __name__ == '__main__':
    unittest.main()
