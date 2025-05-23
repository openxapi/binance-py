# coding: utf-8

# flake8: noqa

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.3.0"

# import apis into sdk package
from binance.pmargin.api.portfolio_margin_api import PortfolioMarginApi

# import ApiClient
from binance.pmargin.api_response import ApiResponse
from binance.pmargin.api_client import ApiClient
from binance.pmargin.configuration import Configuration
from binance.pmargin.exceptions import OpenApiException
from binance.pmargin.exceptions import ApiTypeError
from binance.pmargin.exceptions import ApiValueError
from binance.pmargin.exceptions import ApiKeyError
from binance.pmargin.exceptions import ApiAttributeError
from binance.pmargin.exceptions import ApiException

# import models into sdk package
from binance.pmargin.models.api_error import APIError
from binance.pmargin.models.create_asset_collection_v1_resp import CreateAssetCollectionV1Resp
from binance.pmargin.models.create_auto_collection_v1_resp import CreateAutoCollectionV1Resp
from binance.pmargin.models.create_bnb_transfer_v1_resp import CreateBnbTransferV1Resp
from binance.pmargin.models.create_cm_conditional_order_v1_resp import CreateCmConditionalOrderV1Resp
from binance.pmargin.models.create_cm_leverage_v1_resp import CreateCmLeverageV1Resp
from binance.pmargin.models.create_cm_order_v1_resp import CreateCmOrderV1Resp
from binance.pmargin.models.create_cm_position_side_dual_v1_resp import CreateCmPositionSideDualV1Resp
from binance.pmargin.models.create_listen_key_v1_resp import CreateListenKeyV1Resp
from binance.pmargin.models.create_margin_loan_v1_resp import CreateMarginLoanV1Resp
from binance.pmargin.models.create_margin_order_oco_v1_resp import CreateMarginOrderOcoV1Resp
from binance.pmargin.models.create_margin_order_oco_v1_resp_order_reports_inner import CreateMarginOrderOcoV1RespOrderReportsInner
from binance.pmargin.models.create_margin_order_oco_v1_resp_orders_inner import CreateMarginOrderOcoV1RespOrdersInner
from binance.pmargin.models.create_margin_order_v1_resp import CreateMarginOrderV1Resp
from binance.pmargin.models.create_margin_order_v1_resp_fills_inner import CreateMarginOrderV1RespFillsInner
from binance.pmargin.models.create_margin_repay_debt_v1_resp import CreateMarginRepayDebtV1Resp
from binance.pmargin.models.create_repay_futures_negative_balance_v1_resp import CreateRepayFuturesNegativeBalanceV1Resp
from binance.pmargin.models.create_repay_futures_switch_v1_resp import CreateRepayFuturesSwitchV1Resp
from binance.pmargin.models.create_repay_loan_v1_resp import CreateRepayLoanV1Resp
from binance.pmargin.models.create_um_conditional_order_v1_resp import CreateUmConditionalOrderV1Resp
from binance.pmargin.models.create_um_fee_burn_v1_resp import CreateUmFeeBurnV1Resp
from binance.pmargin.models.create_um_leverage_v1_resp import CreateUmLeverageV1Resp
from binance.pmargin.models.create_um_order_v1_resp import CreateUmOrderV1Resp
from binance.pmargin.models.create_um_position_side_dual_v1_resp import CreateUmPositionSideDualV1Resp
from binance.pmargin.models.delete_cm_all_open_orders_v1_resp import DeleteCmAllOpenOrdersV1Resp
from binance.pmargin.models.delete_cm_conditional_all_open_orders_v1_resp import DeleteCmConditionalAllOpenOrdersV1Resp
from binance.pmargin.models.delete_cm_conditional_order_v1_resp import DeleteCmConditionalOrderV1Resp
from binance.pmargin.models.delete_cm_order_v1_resp import DeleteCmOrderV1Resp
from binance.pmargin.models.delete_margin_order_list_v1_resp import DeleteMarginOrderListV1Resp
from binance.pmargin.models.delete_margin_order_list_v1_resp_order_reports_inner import DeleteMarginOrderListV1RespOrderReportsInner
from binance.pmargin.models.delete_margin_order_v1_resp import DeleteMarginOrderV1Resp
from binance.pmargin.models.delete_um_all_open_orders_v1_resp import DeleteUmAllOpenOrdersV1Resp
from binance.pmargin.models.delete_um_conditional_all_open_orders_v1_resp import DeleteUmConditionalAllOpenOrdersV1Resp
from binance.pmargin.models.delete_um_conditional_order_v1_resp import DeleteUmConditionalOrderV1Resp
from binance.pmargin.models.delete_um_order_v1_resp import DeleteUmOrderV1Resp
from binance.pmargin.models.get_account_v1_resp import GetAccountV1Resp
from binance.pmargin.models.get_cm_account_v1_resp import GetCmAccountV1Resp
from binance.pmargin.models.get_cm_account_v1_resp_assets_inner import GetCmAccountV1RespAssetsInner
from binance.pmargin.models.get_cm_account_v1_resp_positions_inner import GetCmAccountV1RespPositionsInner
from binance.pmargin.models.get_cm_adl_quantile_v1_resp_item import GetCmAdlQuantileV1RespItem
from binance.pmargin.models.get_cm_adl_quantile_v1_resp_item_adl_quantile import GetCmAdlQuantileV1RespItemAdlQuantile
from binance.pmargin.models.get_cm_all_orders_v1_resp_item import GetCmAllOrdersV1RespItem
from binance.pmargin.models.get_cm_commission_rate_v1_resp import GetCmCommissionRateV1Resp
from binance.pmargin.models.get_cm_conditional_all_orders_v1_resp_item import GetCmConditionalAllOrdersV1RespItem
from binance.pmargin.models.get_cm_conditional_open_order_v1_resp import GetCmConditionalOpenOrderV1Resp
from binance.pmargin.models.get_cm_conditional_open_orders_v1_resp_item import GetCmConditionalOpenOrdersV1RespItem
from binance.pmargin.models.get_cm_conditional_order_history_v1_resp import GetCmConditionalOrderHistoryV1Resp
from binance.pmargin.models.get_cm_force_orders_v1_resp_item import GetCmForceOrdersV1RespItem
from binance.pmargin.models.get_cm_income_v1_resp_item import GetCmIncomeV1RespItem
from binance.pmargin.models.get_cm_leverage_bracket_v1_resp_item import GetCmLeverageBracketV1RespItem
from binance.pmargin.models.get_cm_leverage_bracket_v1_resp_item_brackets_inner import GetCmLeverageBracketV1RespItemBracketsInner
from binance.pmargin.models.get_cm_open_order_v1_resp import GetCmOpenOrderV1Resp
from binance.pmargin.models.get_cm_open_orders_v1_resp_item import GetCmOpenOrdersV1RespItem
from binance.pmargin.models.get_cm_order_amendment_v1_resp_item import GetCmOrderAmendmentV1RespItem
from binance.pmargin.models.get_cm_order_amendment_v1_resp_item_amendment import GetCmOrderAmendmentV1RespItemAmendment
from binance.pmargin.models.get_cm_order_amendment_v1_resp_item_amendment_orig_qty import GetCmOrderAmendmentV1RespItemAmendmentOrigQty
from binance.pmargin.models.get_cm_order_v1_resp import GetCmOrderV1Resp
from binance.pmargin.models.get_cm_position_risk_v1_resp_item import GetCmPositionRiskV1RespItem
from binance.pmargin.models.get_cm_position_side_dual_v1_resp import GetCmPositionSideDualV1Resp
from binance.pmargin.models.get_cm_user_trades_v1_resp_item import GetCmUserTradesV1RespItem
from binance.pmargin.models.get_margin_all_order_list_v1_resp_item import GetMarginAllOrderListV1RespItem
from binance.pmargin.models.get_margin_all_orders_v1_resp_item import GetMarginAllOrdersV1RespItem
from binance.pmargin.models.get_margin_force_orders_v1_resp import GetMarginForceOrdersV1Resp
from binance.pmargin.models.get_margin_force_orders_v1_resp_rows_inner import GetMarginForceOrdersV1RespRowsInner
from binance.pmargin.models.get_margin_margin_interest_history_v1_resp import GetMarginMarginInterestHistoryV1Resp
from binance.pmargin.models.get_margin_margin_interest_history_v1_resp_rows_inner import GetMarginMarginInterestHistoryV1RespRowsInner
from binance.pmargin.models.get_margin_margin_loan_v1_resp import GetMarginMarginLoanV1Resp
from binance.pmargin.models.get_margin_margin_loan_v1_resp_rows_inner import GetMarginMarginLoanV1RespRowsInner
from binance.pmargin.models.get_margin_max_borrowable_v1_resp import GetMarginMaxBorrowableV1Resp
from binance.pmargin.models.get_margin_max_withdraw_v1_resp import GetMarginMaxWithdrawV1Resp
from binance.pmargin.models.get_margin_my_trades_v1_resp_item import GetMarginMyTradesV1RespItem
from binance.pmargin.models.get_margin_open_order_list_v1_resp_item import GetMarginOpenOrderListV1RespItem
from binance.pmargin.models.get_margin_open_orders_v1_resp_item import GetMarginOpenOrdersV1RespItem
from binance.pmargin.models.get_margin_order_list_v1_resp import GetMarginOrderListV1Resp
from binance.pmargin.models.get_margin_order_v1_resp import GetMarginOrderV1Resp
from binance.pmargin.models.get_margin_repay_loan_v1_resp import GetMarginRepayLoanV1Resp
from binance.pmargin.models.get_margin_repay_loan_v1_resp_rows_inner import GetMarginRepayLoanV1RespRowsInner
from binance.pmargin.models.get_portfolio_interest_history_v1_resp_item import GetPortfolioInterestHistoryV1RespItem
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp import GetPortfolioNegativeBalanceExchangeRecordV1Resp
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner import GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInner
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner import GetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner
from binance.pmargin.models.get_rate_limit_order_v1_resp_item import GetRateLimitOrderV1RespItem
from binance.pmargin.models.get_repay_futures_switch_v1_resp import GetRepayFuturesSwitchV1Resp
from binance.pmargin.models.get_um_account_config_v1_resp import GetUmAccountConfigV1Resp
from binance.pmargin.models.get_um_account_v1_resp import GetUmAccountV1Resp
from binance.pmargin.models.get_um_account_v1_resp_positions_inner import GetUmAccountV1RespPositionsInner
from binance.pmargin.models.get_um_account_v2_resp import GetUmAccountV2Resp
from binance.pmargin.models.get_um_account_v2_resp_positions_inner import GetUmAccountV2RespPositionsInner
from binance.pmargin.models.get_um_adl_quantile_v1_resp_item import GetUmAdlQuantileV1RespItem
from binance.pmargin.models.get_um_all_orders_v1_resp_item import GetUmAllOrdersV1RespItem
from binance.pmargin.models.get_um_api_trading_status_v1_resp import GetUmApiTradingStatusV1Resp
from binance.pmargin.models.get_um_api_trading_status_v1_resp_indicators import GetUmApiTradingStatusV1RespIndicators
from binance.pmargin.models.get_um_api_trading_status_v1_resp_indicators_btcusdt_inner import GetUmApiTradingStatusV1RespIndicatorsBTCUSDTInner
from binance.pmargin.models.get_um_commission_rate_v1_resp import GetUmCommissionRateV1Resp
from binance.pmargin.models.get_um_conditional_all_orders_v1_resp_item import GetUmConditionalAllOrdersV1RespItem
from binance.pmargin.models.get_um_conditional_open_order_v1_resp import GetUmConditionalOpenOrderV1Resp
from binance.pmargin.models.get_um_conditional_open_orders_v1_resp_item import GetUmConditionalOpenOrdersV1RespItem
from binance.pmargin.models.get_um_conditional_order_history_v1_resp import GetUmConditionalOrderHistoryV1Resp
from binance.pmargin.models.get_um_fee_burn_v1_resp import GetUmFeeBurnV1Resp
from binance.pmargin.models.get_um_force_orders_v1_resp_item import GetUmForceOrdersV1RespItem
from binance.pmargin.models.get_um_income_asyn_id_v1_resp import GetUmIncomeAsynIdV1Resp
from binance.pmargin.models.get_um_income_asyn_v1_resp import GetUmIncomeAsynV1Resp
from binance.pmargin.models.get_um_income_v1_resp_item import GetUmIncomeV1RespItem
from binance.pmargin.models.get_um_leverage_bracket_v1_resp_item import GetUmLeverageBracketV1RespItem
from binance.pmargin.models.get_um_leverage_bracket_v1_resp_item_brackets_inner import GetUmLeverageBracketV1RespItemBracketsInner
from binance.pmargin.models.get_um_open_order_v1_resp import GetUmOpenOrderV1Resp
from binance.pmargin.models.get_um_open_orders_v1_resp_item import GetUmOpenOrdersV1RespItem
from binance.pmargin.models.get_um_order_amendment_v1_resp_item import GetUmOrderAmendmentV1RespItem
from binance.pmargin.models.get_um_order_asyn_id_v1_resp import GetUmOrderAsynIdV1Resp
from binance.pmargin.models.get_um_order_asyn_v1_resp import GetUmOrderAsynV1Resp
from binance.pmargin.models.get_um_order_v1_resp import GetUmOrderV1Resp
from binance.pmargin.models.get_um_position_risk_v1_resp_item import GetUmPositionRiskV1RespItem
from binance.pmargin.models.get_um_position_side_dual_v1_resp import GetUmPositionSideDualV1Resp
from binance.pmargin.models.get_um_symbol_config_v1_resp_item import GetUmSymbolConfigV1RespItem
from binance.pmargin.models.get_um_trade_asyn_id_v1_resp import GetUmTradeAsynIdV1Resp
from binance.pmargin.models.get_um_trade_asyn_v1_resp import GetUmTradeAsynV1Resp
from binance.pmargin.models.get_um_user_trades_v1_resp_item import GetUmUserTradesV1RespItem
from binance.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_inner import PmarginDeleteMarginAllOpenOrdersV1RespInner
from binance.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_order import PmarginDeleteMarginAllOpenOrdersV1RespOrder
from binance.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_order_list import PmarginDeleteMarginAllOpenOrdersV1RespOrderList
from binance.pmargin.models.pmargin_get_balance_v1_resp import PmarginGetBalanceV1Resp
from binance.pmargin.models.pmargin_get_balance_v1_resp_item import PmarginGetBalanceV1RespItem
from binance.pmargin.models.update_cm_order_v1_resp import UpdateCmOrderV1Resp
from binance.pmargin.models.update_um_order_v1_resp import UpdateUmOrderV1Resp
