# coding: utf-8

# flake8: noqa

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.1"

# import apis into sdk package
from binance.derivatives.umfutures.api.account_api import AccountApi
from binance.derivatives.umfutures.api.convert_api import ConvertApi
from binance.derivatives.umfutures.api.market_data_api import MarketDataApi
from binance.derivatives.umfutures.api.portfolio_margin_endpoints_api import PortfolioMarginEndpointsApi
from binance.derivatives.umfutures.api.trade_api import TradeApi
from binance.derivatives.umfutures.api.user_data_streams_api import UserDataStreamsApi

# import ApiClient
from binance.derivatives.umfutures.api_response import ApiResponse
from binance.derivatives.umfutures.api_client import ApiClient
from binance.derivatives.umfutures.configuration import Configuration
from binance.derivatives.umfutures.exceptions import OpenApiException
from binance.derivatives.umfutures.exceptions import ApiTypeError
from binance.derivatives.umfutures.exceptions import ApiValueError
from binance.derivatives.umfutures.exceptions import ApiKeyError
from binance.derivatives.umfutures.exceptions import ApiAttributeError
from binance.derivatives.umfutures.exceptions import ApiException

# import models into sdk package
from binance.derivatives.umfutures.models.api_error import APIError
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_req_batch_orders_item import UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_resp_inner import UmfuturesCreateBatchOrdersV1RespInner
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_resp_item import UmfuturesCreateBatchOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_create_convert_accept_quote_v1_resp import UmfuturesCreateConvertAcceptQuoteV1Resp
from binance.derivatives.umfutures.models.umfutures_create_convert_get_quote_v1_resp import UmfuturesCreateConvertGetQuoteV1Resp
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_resp import UmfuturesCreateCountdownCancelAllV1Resp
from binance.derivatives.umfutures.models.umfutures_create_fee_burn_v1_resp import UmfuturesCreateFeeBurnV1Resp
from binance.derivatives.umfutures.models.umfutures_create_leverage_v1_resp import UmfuturesCreateLeverageV1Resp
from binance.derivatives.umfutures.models.umfutures_create_listen_key_v1_resp import UmfuturesCreateListenKeyV1Resp
from binance.derivatives.umfutures.models.umfutures_create_margin_type_v1_resp import UmfuturesCreateMarginTypeV1Resp
from binance.derivatives.umfutures.models.umfutures_create_multi_assets_margin_v1_resp import UmfuturesCreateMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.models.umfutures_create_order_test_v1_resp import UmfuturesCreateOrderTestV1Resp
from binance.derivatives.umfutures.models.umfutures_create_order_v1_resp import UmfuturesCreateOrderV1Resp
from binance.derivatives.umfutures.models.umfutures_create_position_margin_v1_resp import UmfuturesCreatePositionMarginV1Resp
from binance.derivatives.umfutures.models.umfutures_create_position_side_dual_v1_resp import UmfuturesCreatePositionSideDualV1Resp
from binance.derivatives.umfutures.models.umfutures_delete_all_open_orders_v1_resp import UmfuturesDeleteAllOpenOrdersV1Resp
from binance.derivatives.umfutures.models.umfutures_delete_batch_orders_v1_resp_inner import UmfuturesDeleteBatchOrdersV1RespInner
from binance.derivatives.umfutures.models.umfutures_delete_batch_orders_v1_resp_item import UmfuturesDeleteBatchOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_delete_order_v1_resp import UmfuturesDeleteOrderV1Resp
from binance.derivatives.umfutures.models.umfutures_get_account_config_v1_resp import UmfuturesGetAccountConfigV1Resp
from binance.derivatives.umfutures.models.umfutures_get_account_v2_resp import UmfuturesGetAccountV2Resp
from binance.derivatives.umfutures.models.umfutures_get_account_v2_resp_assets_inner import UmfuturesGetAccountV2RespAssetsInner
from binance.derivatives.umfutures.models.umfutures_get_account_v2_resp_positions_inner import UmfuturesGetAccountV2RespPositionsInner
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp import UmfuturesGetAccountV3Resp
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp_assets_inner import UmfuturesGetAccountV3RespAssetsInner
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp_positions_inner import UmfuturesGetAccountV3RespPositionsInner
from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item import UmfuturesGetAdlQuantileV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item_adl_quantile import UmfuturesGetAdlQuantileV1RespItemAdlQuantile
from binance.derivatives.umfutures.models.umfutures_get_agg_trades_v1_resp_item import UmfuturesGetAggTradesV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_all_orders_v1_resp_item import UmfuturesGetAllOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_api_trading_status_v1_resp import UmfuturesGetApiTradingStatusV1Resp
from binance.derivatives.umfutures.models.umfutures_get_asset_index_v1_resp import UmfuturesGetAssetIndexV1Resp
from binance.derivatives.umfutures.models.umfutures_get_asset_index_v1_resp_item import UmfuturesGetAssetIndexV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_balance_v2_resp_item import UmfuturesGetBalanceV2RespItem
from binance.derivatives.umfutures.models.umfutures_get_balance_v3_resp_item import UmfuturesGetBalanceV3RespItem
from binance.derivatives.umfutures.models.umfutures_get_commission_rate_v1_resp import UmfuturesGetCommissionRateV1Resp
from binance.derivatives.umfutures.models.umfutures_get_constituents_v1_resp import UmfuturesGetConstituentsV1Resp
from binance.derivatives.umfutures.models.umfutures_get_constituents_v1_resp_constituents_inner import UmfuturesGetConstituentsV1RespConstituentsInner
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.models.umfutures_get_convert_exchange_info_v1_resp_item import UmfuturesGetConvertExchangeInfoV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_convert_order_status_v1_resp import UmfuturesGetConvertOrderStatusV1Resp
from binance.derivatives.umfutures.models.umfutures_get_depth_v1_resp import UmfuturesGetDepthV1Resp
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp import UmfuturesGetExchangeInfoV1Resp
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_assets_inner import UmfuturesGetExchangeInfoV1RespAssetsInner
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_rate_limits_inner import UmfuturesGetExchangeInfoV1RespRateLimitsInner
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner import UmfuturesGetExchangeInfoV1RespSymbolsInner
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner import UmfuturesGetExchangeInfoV1RespSymbolsInnerFiltersInner
from binance.derivatives.umfutures.models.umfutures_get_fee_burn_v1_resp import UmfuturesGetFeeBurnV1Resp
from binance.derivatives.umfutures.models.umfutures_get_force_orders_v1_resp_item import UmfuturesGetForceOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_funding_info_v1_resp_item import UmfuturesGetFundingInfoV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_funding_rate_v1_resp_item import UmfuturesGetFundingRateV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_basis_resp_item import UmfuturesGetFuturesDataBasisRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_delivery_price_resp_item import UmfuturesGetFuturesDataDeliveryPriceRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_global_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_open_interest_hist_resp_item import UmfuturesGetFuturesDataOpenInterestHistRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_takerlongshort_ratio_resp_item import UmfuturesGetFuturesDataTakerlongshortRatioRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem
from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_position_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortPositionRatioRespItem
from binance.derivatives.umfutures.models.umfutures_get_historical_trades_v1_resp_item import UmfuturesGetHistoricalTradesV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_id_v1_resp import UmfuturesGetIncomeAsynIdV1Resp
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_v1_resp import UmfuturesGetIncomeAsynV1Resp
from binance.derivatives.umfutures.models.umfutures_get_income_v1_resp_item import UmfuturesGetIncomeV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item import UmfuturesGetIndexInfoV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item_base_asset_list_inner import UmfuturesGetIndexInfoV1RespItemBaseAssetListInner
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp_item import UmfuturesGetLeverageBracketV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp_item_brackets_inner import UmfuturesGetLeverageBracketV1RespItemBracketsInner
from binance.derivatives.umfutures.models.umfutures_get_multi_assets_margin_v1_resp import UmfuturesGetMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.models.umfutures_get_open_interest_v1_resp import UmfuturesGetOpenInterestV1Resp
from binance.derivatives.umfutures.models.umfutures_get_open_order_v1_resp import UmfuturesGetOpenOrderV1Resp
from binance.derivatives.umfutures.models.umfutures_get_open_orders_v1_resp_item import UmfuturesGetOpenOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item import UmfuturesGetOrderAmendmentV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item_amendment import UmfuturesGetOrderAmendmentV1RespItemAmendment
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item_amendment_orig_qty import UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_id_v1_resp import UmfuturesGetOrderAsynIdV1Resp
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_v1_resp import UmfuturesGetOrderAsynV1Resp
from binance.derivatives.umfutures.models.umfutures_get_order_v1_resp import UmfuturesGetOrderV1Resp
from binance.derivatives.umfutures.models.umfutures_get_pm_account_info_v1_resp import UmfuturesGetPmAccountInfoV1Resp
from binance.derivatives.umfutures.models.umfutures_get_position_margin_history_v1_resp_item import UmfuturesGetPositionMarginHistoryV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_position_risk_v2_resp_item import UmfuturesGetPositionRiskV2RespItem
from binance.derivatives.umfutures.models.umfutures_get_position_risk_v3_resp_item import UmfuturesGetPositionRiskV3RespItem
from binance.derivatives.umfutures.models.umfutures_get_position_side_dual_v1_resp import UmfuturesGetPositionSideDualV1Resp
from binance.derivatives.umfutures.models.umfutures_get_premium_index_v1_resp import UmfuturesGetPremiumIndexV1Resp
from binance.derivatives.umfutures.models.umfutures_get_premium_index_v1_resp_item import UmfuturesGetPremiumIndexV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_rate_limit_order_v1_resp_item import UmfuturesGetRateLimitOrderV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_symbol_config_v1_resp_item import UmfuturesGetSymbolConfigV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_ticker24hr_v1_resp import UmfuturesGetTicker24hrV1Resp
from binance.derivatives.umfutures.models.umfutures_get_ticker24hr_v1_resp_item import UmfuturesGetTicker24hrV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp import UmfuturesGetTickerBookTickerV1Resp
from binance.derivatives.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp_item import UmfuturesGetTickerBookTickerV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v1_resp import UmfuturesGetTickerPriceV1Resp
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v1_resp_item import UmfuturesGetTickerPriceV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v2_resp import UmfuturesGetTickerPriceV2Resp
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v2_resp_item import UmfuturesGetTickerPriceV2RespItem
from binance.derivatives.umfutures.models.umfutures_get_time_v1_resp import UmfuturesGetTimeV1Resp
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_id_v1_resp import UmfuturesGetTradeAsynIdV1Resp
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_v1_resp import UmfuturesGetTradeAsynV1Resp
from binance.derivatives.umfutures.models.umfutures_get_trades_v1_resp_item import UmfuturesGetTradesV1RespItem
from binance.derivatives.umfutures.models.umfutures_get_user_trades_v1_resp_item import UmfuturesGetUserTradesV1RespItem
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_req_batch_orders_item import UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_resp_item import UmfuturesUpdateBatchOrdersV1RespItem
from binance.derivatives.umfutures.models.umfutures_update_listen_key_v1_resp import UmfuturesUpdateListenKeyV1Resp
from binance.derivatives.umfutures.models.umfutures_update_order_v1_resp import UmfuturesUpdateOrderV1Resp
