# coding: utf-8

# flake8: noqa

"""
    Binance Copy Trading API

    OpenAPI specification for Binance exchange - Copytrading API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.0"

# import apis into sdk package
from binance.copytrading.api.future_copy_trading_api import FutureCopyTradingApi
from binance.copytrading.api.v1_api import V1Api

# import ApiClient
from binance.copytrading.api_response import ApiResponse
from binance.copytrading.api_client import ApiClient
from binance.copytrading.configuration import Configuration
from binance.copytrading.exceptions import OpenApiException
from binance.copytrading.exceptions import ApiTypeError
from binance.copytrading.exceptions import ApiValueError
from binance.copytrading.exceptions import ApiKeyError
from binance.copytrading.exceptions import ApiAttributeError
from binance.copytrading.exceptions import ApiException

# import models into sdk package
from binance.copytrading.models.api_error import APIError
from binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp import CopytradingGetCopyTradingFuturesLeadSymbolV1Resp
from binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp_data_inner import CopytradingGetCopyTradingFuturesLeadSymbolV1RespDataInner
from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp import CopytradingGetCopyTradingFuturesUserStatusV1Resp
from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp_data import CopytradingGetCopyTradingFuturesUserStatusV1RespData
