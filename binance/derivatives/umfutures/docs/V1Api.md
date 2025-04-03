# binance.derivatives.umfutures.V1Api

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_create_batch_orders_v1**](V1Api.md#umfutures_create_batch_orders_v1) | **POST** /fapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**umfutures_create_convert_accept_quote_v1**](V1Api.md#umfutures_create_convert_accept_quote_v1) | **POST** /fapi/v1/convert/acceptQuote | Accept the offered quote (USER_DATA)
[**umfutures_create_convert_get_quote_v1**](V1Api.md#umfutures_create_convert_get_quote_v1) | **POST** /fapi/v1/convert/getQuote | Send Quote Request(USER_DATA)
[**umfutures_create_countdown_cancel_all_v1**](V1Api.md#umfutures_create_countdown_cancel_all_v1) | **POST** /fapi/v1/countdownCancelAll | Auto-Cancel All Open Orders (TRADE)
[**umfutures_create_fee_burn_v1**](V1Api.md#umfutures_create_fee_burn_v1) | **POST** /fapi/v1/feeBurn | Toggle BNB Burn On Futures Trade (TRADE)
[**umfutures_create_leverage_v1**](V1Api.md#umfutures_create_leverage_v1) | **POST** /fapi/v1/leverage | Change Initial Leverage(TRADE)
[**umfutures_create_listen_key_v1**](V1Api.md#umfutures_create_listen_key_v1) | **POST** /fapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**umfutures_create_margin_type_v1**](V1Api.md#umfutures_create_margin_type_v1) | **POST** /fapi/v1/marginType | Change Margin Type(TRADE)
[**umfutures_create_multi_assets_margin_v1**](V1Api.md#umfutures_create_multi_assets_margin_v1) | **POST** /fapi/v1/multiAssetsMargin | Change Multi-Assets Mode (TRADE)
[**umfutures_create_order_test_v1**](V1Api.md#umfutures_create_order_test_v1) | **POST** /fapi/v1/order/test | Test Order(TRADE)
[**umfutures_create_order_v1**](V1Api.md#umfutures_create_order_v1) | **POST** /fapi/v1/order | New Order(TRADE)
[**umfutures_create_position_margin_v1**](V1Api.md#umfutures_create_position_margin_v1) | **POST** /fapi/v1/positionMargin | Modify Isolated Position Margin(TRADE)
[**umfutures_create_position_side_dual_v1**](V1Api.md#umfutures_create_position_side_dual_v1) | **POST** /fapi/v1/positionSide/dual | Change Position Mode(TRADE)
[**umfutures_delete_all_open_orders_v1**](V1Api.md#umfutures_delete_all_open_orders_v1) | **DELETE** /fapi/v1/allOpenOrders | Cancel All Open Orders (TRADE)
[**umfutures_delete_batch_orders_v1**](V1Api.md#umfutures_delete_batch_orders_v1) | **DELETE** /fapi/v1/batchOrders | Cancel Multiple Orders (TRADE)
[**umfutures_delete_listen_key_v1**](V1Api.md#umfutures_delete_listen_key_v1) | **DELETE** /fapi/v1/listenKey | Close User Data Stream (USER_STREAM)
[**umfutures_delete_order_v1**](V1Api.md#umfutures_delete_order_v1) | **DELETE** /fapi/v1/order | Cancel Order (TRADE)
[**umfutures_get_account_config_v1**](V1Api.md#umfutures_get_account_config_v1) | **GET** /fapi/v1/accountConfig | Futures Account Configuration(USER_DATA)
[**umfutures_get_adl_quantile_v1**](V1Api.md#umfutures_get_adl_quantile_v1) | **GET** /fapi/v1/adlQuantile | Position ADL Quantile Estimation(USER_DATA)
[**umfutures_get_agg_trades_v1**](V1Api.md#umfutures_get_agg_trades_v1) | **GET** /fapi/v1/aggTrades | Compressed/Aggregate Trades List
[**umfutures_get_all_orders_v1**](V1Api.md#umfutures_get_all_orders_v1) | **GET** /fapi/v1/allOrders | All Orders (USER_DATA)
[**umfutures_get_api_trading_status_v1**](V1Api.md#umfutures_get_api_trading_status_v1) | **GET** /fapi/v1/apiTradingStatus | Futures Trading Quantitative Rules Indicators (USER_DATA)
[**umfutures_get_asset_index_v1**](V1Api.md#umfutures_get_asset_index_v1) | **GET** /fapi/v1/assetIndex | Multi-Assets Mode Asset Index
[**umfutures_get_commission_rate_v1**](V1Api.md#umfutures_get_commission_rate_v1) | **GET** /fapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**umfutures_get_constituents_v1**](V1Api.md#umfutures_get_constituents_v1) | **GET** /fapi/v1/constituents | Query Index Price Constituents
[**umfutures_get_continuous_klines_v1**](V1Api.md#umfutures_get_continuous_klines_v1) | **GET** /fapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**umfutures_get_convert_exchange_info_v1**](V1Api.md#umfutures_get_convert_exchange_info_v1) | **GET** /fapi/v1/convert/exchangeInfo | List All Convert Pairs
[**umfutures_get_convert_order_status_v1**](V1Api.md#umfutures_get_convert_order_status_v1) | **GET** /fapi/v1/convert/orderStatus | Order status(USER_DATA)
[**umfutures_get_depth_v1**](V1Api.md#umfutures_get_depth_v1) | **GET** /fapi/v1/depth | Order Book
[**umfutures_get_exchange_info_v1**](V1Api.md#umfutures_get_exchange_info_v1) | **GET** /fapi/v1/exchangeInfo | Exchange Information
[**umfutures_get_fee_burn_v1**](V1Api.md#umfutures_get_fee_burn_v1) | **GET** /fapi/v1/feeBurn | Get BNB Burn Status (USER_DATA)
[**umfutures_get_force_orders_v1**](V1Api.md#umfutures_get_force_orders_v1) | **GET** /fapi/v1/forceOrders | User&#39;s Force Orders (USER_DATA)
[**umfutures_get_funding_info_v1**](V1Api.md#umfutures_get_funding_info_v1) | **GET** /fapi/v1/fundingInfo | Get Funding Rate Info
[**umfutures_get_funding_rate_v1**](V1Api.md#umfutures_get_funding_rate_v1) | **GET** /fapi/v1/fundingRate | Get Funding Rate History
[**umfutures_get_historical_trades_v1**](V1Api.md#umfutures_get_historical_trades_v1) | **GET** /fapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**umfutures_get_income_asyn_id_v1**](V1Api.md#umfutures_get_income_asyn_id_v1) | **GET** /fapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**umfutures_get_income_asyn_v1**](V1Api.md#umfutures_get_income_asyn_v1) | **GET** /fapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**umfutures_get_income_v1**](V1Api.md#umfutures_get_income_v1) | **GET** /fapi/v1/income | Get Income History (USER_DATA)
[**umfutures_get_index_info_v1**](V1Api.md#umfutures_get_index_info_v1) | **GET** /fapi/v1/indexInfo | Composite Index Symbol Information
[**umfutures_get_index_price_klines_v1**](V1Api.md#umfutures_get_index_price_klines_v1) | **GET** /fapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**umfutures_get_klines_v1**](V1Api.md#umfutures_get_klines_v1) | **GET** /fapi/v1/klines | Kline/Candlestick Data
[**umfutures_get_leverage_bracket_v1**](V1Api.md#umfutures_get_leverage_bracket_v1) | **GET** /fapi/v1/leverageBracket | Notional and Leverage Brackets (USER_DATA)
[**umfutures_get_mark_price_klines_v1**](V1Api.md#umfutures_get_mark_price_klines_v1) | **GET** /fapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**umfutures_get_multi_assets_margin_v1**](V1Api.md#umfutures_get_multi_assets_margin_v1) | **GET** /fapi/v1/multiAssetsMargin | Get Current Multi-Assets Mode (USER_DATA)
[**umfutures_get_open_interest_v1**](V1Api.md#umfutures_get_open_interest_v1) | **GET** /fapi/v1/openInterest | Open Interest
[**umfutures_get_open_order_v1**](V1Api.md#umfutures_get_open_order_v1) | **GET** /fapi/v1/openOrder | Query Current Open Order (USER_DATA)
[**umfutures_get_open_orders_v1**](V1Api.md#umfutures_get_open_orders_v1) | **GET** /fapi/v1/openOrders | Current All Open Orders (USER_DATA)
[**umfutures_get_order_amendment_v1**](V1Api.md#umfutures_get_order_amendment_v1) | **GET** /fapi/v1/orderAmendment | Get Order Modify History (USER_DATA)
[**umfutures_get_order_asyn_id_v1**](V1Api.md#umfutures_get_order_asyn_id_v1) | **GET** /fapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**umfutures_get_order_asyn_v1**](V1Api.md#umfutures_get_order_asyn_v1) | **GET** /fapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**umfutures_get_order_v1**](V1Api.md#umfutures_get_order_v1) | **GET** /fapi/v1/order | Query Order (USER_DATA)
[**umfutures_get_ping_v1**](V1Api.md#umfutures_get_ping_v1) | **GET** /fapi/v1/ping | Test Connectivity
[**umfutures_get_pm_account_info_v1**](V1Api.md#umfutures_get_pm_account_info_v1) | **GET** /fapi/v1/pmAccountInfo | Classic Portfolio Margin Account Information (USER_DATA)
[**umfutures_get_position_margin_history_v1**](V1Api.md#umfutures_get_position_margin_history_v1) | **GET** /fapi/v1/positionMargin/history | Get Position Margin Change History (TRADE)
[**umfutures_get_position_side_dual_v1**](V1Api.md#umfutures_get_position_side_dual_v1) | **GET** /fapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**umfutures_get_premium_index_klines_v1**](V1Api.md#umfutures_get_premium_index_klines_v1) | **GET** /fapi/v1/premiumIndexKlines | Premium index Kline Data
[**umfutures_get_premium_index_v1**](V1Api.md#umfutures_get_premium_index_v1) | **GET** /fapi/v1/premiumIndex | Mark Price
[**umfutures_get_rate_limit_order_v1**](V1Api.md#umfutures_get_rate_limit_order_v1) | **GET** /fapi/v1/rateLimit/order | Query User Rate Limit (USER_DATA)
[**umfutures_get_symbol_config_v1**](V1Api.md#umfutures_get_symbol_config_v1) | **GET** /fapi/v1/symbolConfig | Symbol Configuration(USER_DATA)
[**umfutures_get_ticker24hr_v1**](V1Api.md#umfutures_get_ticker24hr_v1) | **GET** /fapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**umfutures_get_ticker_book_ticker_v1**](V1Api.md#umfutures_get_ticker_book_ticker_v1) | **GET** /fapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**umfutures_get_ticker_price_v1**](V1Api.md#umfutures_get_ticker_price_v1) | **GET** /fapi/v1/ticker/price | Symbol Price Ticker
[**umfutures_get_time_v1**](V1Api.md#umfutures_get_time_v1) | **GET** /fapi/v1/time | Check Server Time
[**umfutures_get_trade_asyn_id_v1**](V1Api.md#umfutures_get_trade_asyn_id_v1) | **GET** /fapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**umfutures_get_trade_asyn_v1**](V1Api.md#umfutures_get_trade_asyn_v1) | **GET** /fapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)
[**umfutures_get_trades_v1**](V1Api.md#umfutures_get_trades_v1) | **GET** /fapi/v1/trades | Recent Trades List
[**umfutures_get_user_trades_v1**](V1Api.md#umfutures_get_user_trades_v1) | **GET** /fapi/v1/userTrades | Account Trade List (USER_DATA)
[**umfutures_update_batch_orders_v1**](V1Api.md#umfutures_update_batch_orders_v1) | **PUT** /fapi/v1/batchOrders | Modify Multiple Orders(TRADE)
[**umfutures_update_listen_key_v1**](V1Api.md#umfutures_update_listen_key_v1) | **PUT** /fapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)
[**umfutures_update_order_v1**](V1Api.md#umfutures_update_order_v1) | **PUT** /fapi/v1/order | Modify Order (TRADE)


# **umfutures_create_batch_orders_v1**
> List[UmfuturesCreateBatchOrdersV1RespInner] umfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Place Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_req_batch_orders_item import UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_resp_inner import UmfuturesCreateBatchOrdersV1RespInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    batch_orders = [binance.derivatives.umfutures.UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.umfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem]**](UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesCreateBatchOrdersV1RespInner]**](UmfuturesCreateBatchOrdersV1RespInner.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_convert_accept_quote_v1**
> UmfuturesCreateConvertAcceptQuoteV1Resp umfutures_create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)

Accept the offered quote (USER_DATA)

Accept the offered quote by quote ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_convert_accept_quote_v1_resp import UmfuturesCreateConvertAcceptQuoteV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    quote_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept the offered quote (USER_DATA)
        api_response = api_instance.umfutures_create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_convert_accept_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_convert_accept_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateConvertAcceptQuoteV1Resp**](UmfuturesCreateConvertAcceptQuoteV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_convert_get_quote_v1**
> UmfuturesCreateConvertGetQuoteV1Resp umfutures_create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time)

Send Quote Request(USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_convert_get_quote_v1_resp import UmfuturesCreateConvertGetQuoteV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    from_asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_asset = '' # str |  (default to '')
    from_amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_amount = '' # str |  (optional) (default to '')
    valid_time = '10' # str |  (optional) (default to '10')

    try:
        # Send Quote Request(USER_DATA)
        api_response = api_instance.umfutures_create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time)
        print("The response of V1Api->umfutures_create_convert_get_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_convert_get_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_asset** | **str**|  | [default to &#39;&#39;]
 **from_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **valid_time** | **str**|  | [optional] [default to &#39;10&#39;]

### Return type

[**UmfuturesCreateConvertGetQuoteV1Resp**](UmfuturesCreateConvertGetQuoteV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_countdown_cancel_all_v1**
> UmfuturesCreateCountdownCancelAllV1Resp umfutures_create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)

Auto-Cancel All Open Orders (TRADE)

Cancel all open orders of the specified symbol at the end of the specified countdown.
The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_resp import UmfuturesCreateCountdownCancelAllV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    umfutures_create_countdown_cancel_all_v1_req = binance.derivatives.umfutures.UmfuturesCreateCountdownCancelAllV1Req() # UmfuturesCreateCountdownCancelAllV1Req |  (optional)

    try:
        # Auto-Cancel All Open Orders (TRADE)
        api_response = api_instance.umfutures_create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)
        print("The response of V1Api->umfutures_create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **umfutures_create_countdown_cancel_all_v1_req** | [**UmfuturesCreateCountdownCancelAllV1Req**](UmfuturesCreateCountdownCancelAllV1Req.md)|  | [optional] 

### Return type

[**UmfuturesCreateCountdownCancelAllV1Resp**](UmfuturesCreateCountdownCancelAllV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_fee_burn_v1**
> UmfuturesCreateFeeBurnV1Resp umfutures_create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)

Toggle BNB Burn On Futures Trade (TRADE)

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_fee_burn_v1_resp import UmfuturesCreateFeeBurnV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    fee_burn = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Toggle BNB Burn On Futures Trade (TRADE)
        api_response = api_instance.umfutures_create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_burn** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateFeeBurnV1Resp**](UmfuturesCreateFeeBurnV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_leverage_v1**
> UmfuturesCreateLeverageV1Resp umfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change Initial Leverage(TRADE)

Change user's initial leverage of specific symbol market.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_leverage_v1_resp import UmfuturesCreateLeverageV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Initial Leverage(TRADE)
        api_response = api_instance.umfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateLeverageV1Resp**](UmfuturesCreateLeverageV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_listen_key_v1**
> UmfuturesCreateListenKeyV1Resp umfutures_create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_listen_key_v1_resp import UmfuturesCreateListenKeyV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.umfutures_create_listen_key_v1()
        print("The response of V1Api->umfutures_create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesCreateListenKeyV1Resp**](UmfuturesCreateListenKeyV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_margin_type_v1**
> UmfuturesCreateMarginTypeV1Resp umfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)

Change Margin Type(TRADE)

Change symbol level margin type

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_margin_type_v1_resp import UmfuturesCreateMarginTypeV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    margin_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Margin Type(TRADE)
        api_response = api_instance.umfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_margin_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_margin_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateMarginTypeV1Resp**](UmfuturesCreateMarginTypeV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_multi_assets_margin_v1**
> UmfuturesCreateMultiAssetsMarginV1Resp umfutures_create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)

Change Multi-Assets Mode (TRADE)

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_multi_assets_margin_v1_resp import UmfuturesCreateMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    multi_assets_margin = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Multi-Assets Mode (TRADE)
        api_response = api_instance.umfutures_create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_assets_margin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateMultiAssetsMarginV1Resp**](UmfuturesCreateMultiAssetsMarginV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_order_test_v1**
> UmfuturesCreateOrderTestV1Resp umfutures_create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

Test Order(TRADE)

Testing order request, this order will not be submitted to matching engine

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_order_test_v1_resp import UmfuturesCreateOrderTestV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
    good_till_date = 56 # int |  (optional)
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    price_protect = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')
    working_type = '' # str |  (optional) (default to '')

    try:
        # Test Order(TRADE)
        api_response = api_instance.umfutures_create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of V1Api->umfutures_create_order_test_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_order_test_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **activation_price** | **str**|  | [optional] [default to &#39;&#39;]
 **callback_rate** | **str**|  | [optional] [default to &#39;&#39;]
 **close_position** | **str**|  | [optional] [default to &#39;&#39;]
 **good_till_date** | **int**|  | [optional] 
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **price_protect** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **working_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesCreateOrderTestV1Resp**](UmfuturesCreateOrderTestV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_order_v1**
> UmfuturesCreateOrderV1Resp umfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New Order(TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_order_v1_resp import UmfuturesCreateOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
    good_till_date = 56 # int |  (optional)
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    price_protect = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')
    working_type = '' # str |  (optional) (default to '')

    try:
        # New Order(TRADE)
        api_response = api_instance.umfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of V1Api->umfutures_create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **activation_price** | **str**|  | [optional] [default to &#39;&#39;]
 **callback_rate** | **str**|  | [optional] [default to &#39;&#39;]
 **close_position** | **str**|  | [optional] [default to &#39;&#39;]
 **good_till_date** | **int**|  | [optional] 
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **price_protect** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **working_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesCreateOrderV1Resp**](UmfuturesCreateOrderV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_position_margin_v1**
> UmfuturesCreatePositionMarginV1Resp umfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)

Modify Isolated Position Margin(TRADE)

Modify Isolated Position Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_position_margin_v1_resp import UmfuturesCreatePositionMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    amount = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Isolated Position Margin(TRADE)
        api_response = api_instance.umfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_position_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_position_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**|  | 
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreatePositionMarginV1Resp**](UmfuturesCreatePositionMarginV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_create_position_side_dual_v1**
> UmfuturesCreatePositionSideDualV1Resp umfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_position_side_dual_v1_resp import UmfuturesCreatePositionSideDualV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Position Mode(TRADE)
        api_response = api_instance.umfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_create_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_create_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreatePositionSideDualV1Resp**](UmfuturesCreatePositionSideDualV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_delete_all_open_orders_v1**
> UmfuturesDeleteAllOpenOrdersV1Resp umfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All Open Orders (TRADE)

Cancel All Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_all_open_orders_v1_resp import UmfuturesDeleteAllOpenOrdersV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Open Orders (TRADE)
        api_response = api_instance.umfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesDeleteAllOpenOrdersV1Resp**](UmfuturesDeleteAllOpenOrdersV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_delete_batch_orders_v1**
> List[UmfuturesDeleteBatchOrdersV1RespInner] umfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)

Cancel Multiple Orders (TRADE)

Cancel Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_batch_orders_v1_resp_inner import UmfuturesDeleteBatchOrdersV1RespInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id_list = [56] # List[int] | max length 10 <br/> e.g. [1234567,2345678] (optional)
    orig_client_order_id_list = ['orig_client_order_id_list_example'] # List[str] | max length 10<br/> e.g. [&#34;my_id_1&#34;,&#34;my_id_2&#34;], encode the double quotes. No space after comma. (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Orders (TRADE)
        api_response = api_instance.umfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)
        print("The response of V1Api->umfutures_delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_delete_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id_list** | [**List[int]**](int.md)| max length 10 &lt;br/&gt; e.g. [1234567,2345678] | [optional] 
 **orig_client_order_id_list** | [**List[str]**](str.md)| max length 10&lt;br/&gt; e.g. [&amp;#34;my_id_1&amp;#34;,&amp;#34;my_id_2&amp;#34;], encode the double quotes. No space after comma. | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesDeleteBatchOrdersV1RespInner]**](UmfuturesDeleteBatchOrdersV1RespInner.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_delete_listen_key_v1**
> object umfutures_delete_listen_key_v1()

Close User Data Stream (USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.umfutures_delete_listen_key_v1()
        print("The response of V1Api->umfutures_delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_delete_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_delete_order_v1**
> UmfuturesDeleteOrderV1Resp umfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_order_v1_resp import UmfuturesDeleteOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Order (TRADE)
        api_response = api_instance.umfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->umfutures_delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_delete_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesDeleteOrderV1Resp**](UmfuturesDeleteOrderV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_account_config_v1**
> UmfuturesGetAccountConfigV1Resp umfutures_get_account_config_v1(timestamp, recv_window=recv_window)

Futures Account Configuration(USER_DATA)

Query account configuration

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_account_config_v1_resp import UmfuturesGetAccountConfigV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Configuration(USER_DATA)
        api_response = api_instance.umfutures_get_account_config_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_account_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_account_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetAccountConfigV1Resp**](UmfuturesGetAccountConfigV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_adl_quantile_v1**
> List[UmfuturesGetAdlQuantileV1RespItem] umfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

Position ADL Quantile Estimation(USER_DATA)

Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item import UmfuturesGetAdlQuantileV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.umfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetAdlQuantileV1RespItem]**](UmfuturesGetAdlQuantileV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_agg_trades_v1**
> List[UmfuturesGetAggTradesV1RespItem] umfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate market trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_agg_trades_v1_resp_item import UmfuturesGetAggTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.umfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_agg_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **from_id** | **int**| ID to get aggregate trades from INCLUSIVE. | [optional] 
 **start_time** | **int**| Timestamp in ms to get aggregate trades from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get aggregate trades until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[UmfuturesGetAggTradesV1RespItem]**](UmfuturesGetAggTradesV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_all_orders_v1**
> List[UmfuturesGetAllOrdersV1RespItem] umfutures_get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_all_orders_v1_resp_item import UmfuturesGetAllOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # All Orders (USER_DATA)
        api_response = api_instance.umfutures_get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetAllOrdersV1RespItem]**](UmfuturesGetAllOrdersV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_api_trading_status_v1**
> UmfuturesGetApiTradingStatusV1Resp umfutures_get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)

Futures Trading Quantitative Rules Indicators (USER_DATA)

Futures trading quantitative rules indicators, for more information on this, please refer to the Futures Trading Quantitative Rules

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_api_trading_status_v1_resp import UmfuturesGetApiTradingStatusV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Futures Trading Quantitative Rules Indicators (USER_DATA)
        api_response = api_instance.umfutures_get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetApiTradingStatusV1Resp**](UmfuturesGetApiTradingStatusV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_asset_index_v1**
> UmfuturesGetAssetIndexV1Resp umfutures_get_asset_index_v1(symbol=symbol)

Multi-Assets Mode Asset Index

asset index for Multi-Assets mode

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_asset_index_v1_resp import UmfuturesGetAssetIndexV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str | Asset pair (optional) (default to '')

    try:
        # Multi-Assets Mode Asset Index
        api_response = api_instance.umfutures_get_asset_index_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_asset_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_asset_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Asset pair | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetAssetIndexV1Resp**](UmfuturesGetAssetIndexV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_commission_rate_v1**
> UmfuturesGetCommissionRateV1Resp umfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

User Commission Rate (USER_DATA)

Get User Commission Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_commission_rate_v1_resp import UmfuturesGetCommissionRateV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.umfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetCommissionRateV1Resp**](UmfuturesGetCommissionRateV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_constituents_v1**
> UmfuturesGetConstituentsV1Resp umfutures_get_constituents_v1(symbol)

Query Index Price Constituents

Query index price constituents

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_constituents_v1_resp import UmfuturesGetConstituentsV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.umfutures_get_constituents_v1(symbol)
        print("The response of V1Api->umfutures_get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_constituents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**UmfuturesGetConstituentsV1Resp**](UmfuturesGetConstituentsV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_continuous_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.umfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_continuous_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **contract_type** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_convert_exchange_info_v1**
> List[UmfuturesGetConvertExchangeInfoV1RespItem] umfutures_get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)

List All Convert Pairs

Query for all convertible token pairs and the tokens’ respective upper/lower limits

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_convert_exchange_info_v1_resp_item import UmfuturesGetConvertExchangeInfoV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    from_asset = '' # str | User spends coin (optional) (default to '')
    to_asset = '' # str | User receives coin (optional) (default to '')

    try:
        # List All Convert Pairs
        api_response = api_instance.umfutures_get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)
        print("The response of V1Api->umfutures_get_convert_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_convert_exchange_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**| User spends coin | [optional] [default to &#39;&#39;]
 **to_asset** | **str**| User receives coin | [optional] [default to &#39;&#39;]

### Return type

[**List[UmfuturesGetConvertExchangeInfoV1RespItem]**](UmfuturesGetConvertExchangeInfoV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_convert_order_status_v1**
> UmfuturesGetConvertOrderStatusV1Resp umfutures_get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)

Order status(USER_DATA)

Query order status by order ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_convert_order_status_v1_resp import UmfuturesGetConvertOrderStatusV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    order_id = '' # str | Either orderId or quoteId is required (optional) (default to '')
    quote_id = '' # str | Either orderId or quoteId is required (optional) (default to '')

    try:
        # Order status(USER_DATA)
        api_response = api_instance.umfutures_get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)
        print("The response of V1Api->umfutures_get_convert_order_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_convert_order_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]
 **quote_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetConvertOrderStatusV1Resp**](UmfuturesGetConvertOrderStatusV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_depth_v1**
> UmfuturesGetDepthV1Resp umfutures_get_depth_v1(symbol, limit=limit)

Order Book

Query symbol orderbook

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_depth_v1_resp import UmfuturesGetDepthV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.umfutures_get_depth_v1(symbol, limit=limit)
        print("The response of V1Api->umfutures_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] | [optional] [default to 500]

### Return type

[**UmfuturesGetDepthV1Resp**](UmfuturesGetDepthV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_exchange_info_v1**
> UmfuturesGetExchangeInfoV1Resp umfutures_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp import UmfuturesGetExchangeInfoV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Exchange Information
        api_response = api_instance.umfutures_get_exchange_info_v1()
        print("The response of V1Api->umfutures_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesGetExchangeInfoV1Resp**](UmfuturesGetExchangeInfoV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_fee_burn_v1**
> UmfuturesGetFeeBurnV1Resp umfutures_get_fee_burn_v1(timestamp, recv_window=recv_window)

Get BNB Burn Status (USER_DATA)

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_fee_burn_v1_resp import UmfuturesGetFeeBurnV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get BNB Burn Status (USER_DATA)
        api_response = api_instance.umfutures_get_fee_burn_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetFeeBurnV1Resp**](UmfuturesGetFeeBurnV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_force_orders_v1**
> List[UmfuturesGetForceOrdersV1RespItem] umfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

User's Force Orders (USER_DATA)

Query user's Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_force_orders_v1_resp_item import UmfuturesGetForceOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | &#34;LIQUIDATION&#34; for liquidation orders, &#34;ADL&#34; for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # User's Force Orders (USER_DATA)
        api_response = api_instance.umfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **auto_close_type** | **str**| &amp;#34;LIQUIDATION&amp;#34; for liquidation orders, &amp;#34;ADL&amp;#34; for ADL orders. | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetForceOrdersV1RespItem]**](UmfuturesGetForceOrdersV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_funding_info_v1**
> List[UmfuturesGetFundingInfoV1RespItem] umfutures_get_funding_info_v1()

Get Funding Rate Info

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_funding_info_v1_resp_item import UmfuturesGetFundingInfoV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.umfutures_get_funding_info_v1()
        print("The response of V1Api->umfutures_get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_funding_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UmfuturesGetFundingInfoV1RespItem]**](UmfuturesGetFundingInfoV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_funding_rate_v1**
> List[UmfuturesGetFundingRateV1RespItem] umfutures_get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History

Get Funding Rate History

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_funding_rate_v1_resp_item import UmfuturesGetFundingRateV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History
        api_response = api_instance.umfutures_get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding rate from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding rate  until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]

### Return type

[**List[UmfuturesGetFundingRateV1RespItem]**](UmfuturesGetFundingRateV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_historical_trades_v1**
> List[UmfuturesGetHistoricalTradesV1RespItem] umfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_historical_trades_v1_resp_item import UmfuturesGetHistoricalTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.umfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of V1Api->umfutures_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 500. | [optional] [default to 100]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[UmfuturesGetHistoricalTradesV1RespItem]**](UmfuturesGetHistoricalTradesV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_income_asyn_id_v1**
> UmfuturesGetIncomeAsynIdV1Resp umfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Transaction History Download Link by Id (USER_DATA)

Get futures transaction history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_id_v1_resp import UmfuturesGetIncomeAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.umfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetIncomeAsynIdV1Resp**](UmfuturesGetIncomeAsynIdV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_income_asyn_v1**
> UmfuturesGetIncomeAsynV1Resp umfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Transaction History(USER_DATA)

Get download id for futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_v1_resp import UmfuturesGetIncomeAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.umfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetIncomeAsynV1Resp**](UmfuturesGetIncomeAsynV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_income_v1**
> List[UmfuturesGetIncomeV1RespItem] umfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get Income History (USER_DATA)

Query income history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_v1_resp_item import UmfuturesGetIncomeV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History (USER_DATA)
        api_response = api_instance.umfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetIncomeV1RespItem]**](UmfuturesGetIncomeV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_index_info_v1**
> List[UmfuturesGetIndexInfoV1RespItem] umfutures_get_index_info_v1(symbol=symbol)

Composite Index Symbol Information

Query composite index symbol information

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item import UmfuturesGetIndexInfoV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Composite Index Symbol Information
        api_response = api_instance.umfutures_get_index_info_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_index_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_index_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[UmfuturesGetIndexInfoV1RespItem]**](UmfuturesGetIndexInfoV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_index_price_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.umfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_index_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.umfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_leverage_bracket_v1**
> UmfuturesGetLeverageBracketV1Resp umfutures_get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

Notional and Leverage Brackets (USER_DATA)

Query user notional and leverage bracket on speicfic symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional and Leverage Brackets (USER_DATA)
        api_response = api_instance.umfutures_get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetLeverageBracketV1Resp**](UmfuturesGetLeverageBracketV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_mark_price_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.umfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_mark_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_multi_assets_margin_v1**
> UmfuturesGetMultiAssetsMarginV1Resp umfutures_get_multi_assets_margin_v1(timestamp, recv_window=recv_window)

Get Current Multi-Assets Mode (USER_DATA)

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_multi_assets_margin_v1_resp import UmfuturesGetMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Multi-Assets Mode (USER_DATA)
        api_response = api_instance.umfutures_get_multi_assets_margin_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetMultiAssetsMarginV1Resp**](UmfuturesGetMultiAssetsMarginV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_open_interest_v1**
> UmfuturesGetOpenInterestV1Resp umfutures_get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_interest_v1_resp import UmfuturesGetOpenInterestV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.umfutures_get_open_interest_v1(symbol)
        print("The response of V1Api->umfutures_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**UmfuturesGetOpenInterestV1Resp**](UmfuturesGetOpenInterestV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_open_order_v1**
> UmfuturesGetOpenOrderV1Resp umfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current Open Order (USER_DATA)

Query open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_order_v1_resp import UmfuturesGetOpenOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Order (USER_DATA)
        api_response = api_instance.umfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_open_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOpenOrderV1Resp**](UmfuturesGetOpenOrderV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_open_orders_v1**
> List[UmfuturesGetOpenOrdersV1RespItem] umfutures_get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Current All Open Orders (USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_orders_v1_resp_item import UmfuturesGetOpenOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Current All Open Orders (USER_DATA)
        api_response = api_instance.umfutures_get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetOpenOrdersV1RespItem]**](UmfuturesGetOpenOrdersV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_order_amendment_v1**
> List[UmfuturesGetOrderAmendmentV1RespItem] umfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Order Modify History (USER_DATA)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item import UmfuturesGetOrderAmendmentV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get modification history from INCLUSIVE (optional)
    end_time = 56 # int | Timestamp in ms to get modification history until INCLUSIVE (optional)
    limit = 50 # int | Default 50; max 100 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Get Order Modify History (USER_DATA)
        api_response = api_instance.umfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_order_amendment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get modification history from INCLUSIVE | [optional] 
 **end_time** | **int**| Timestamp in ms to get modification history until INCLUSIVE | [optional] 
 **limit** | **int**| Default 50; max 100 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetOrderAmendmentV1RespItem]**](UmfuturesGetOrderAmendmentV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_order_asyn_id_v1**
> UmfuturesGetOrderAsynIdV1Resp umfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Order History Download Link by Id (USER_DATA)

Get futures order history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_id_v1_resp import UmfuturesGetOrderAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.umfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderAsynIdV1Resp**](UmfuturesGetOrderAsynIdV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_order_asyn_v1**
> UmfuturesGetOrderAsynV1Resp umfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_v1_resp import UmfuturesGetOrderAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.umfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderAsynV1Resp**](UmfuturesGetOrderAsynV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_order_v1**
> UmfuturesGetOrderV1Resp umfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_v1_resp import UmfuturesGetOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Order (USER_DATA)
        api_response = api_instance.umfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderV1Resp**](UmfuturesGetOrderV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_ping_v1**
> object umfutures_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.umfutures_get_ping_v1()
        print("The response of V1Api->umfutures_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_ping_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_pm_account_info_v1**
> UmfuturesGetPmAccountInfoV1Resp umfutures_get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)

Classic Portfolio Margin Account Information (USER_DATA)

Get Classic Portfolio Margin current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_pm_account_info_v1_resp import UmfuturesGetPmAccountInfoV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Classic Portfolio Margin Account Information (USER_DATA)
        api_response = api_instance.umfutures_get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_pm_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_pm_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetPmAccountInfoV1Resp**](UmfuturesGetPmAccountInfoV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_position_margin_history_v1**
> List[UmfuturesGetPositionMarginHistoryV1RespItem] umfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Position Margin Change History (TRADE)

Get Position Margin Change History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_margin_history_v1_resp_item import UmfuturesGetPositionMarginHistoryV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1: Add position margin，2: Reduce position margin (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int | Default current time if not pass (optional)
    limit = 500 # int | Default: 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Position Margin Change History (TRADE)
        api_response = api_instance.umfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_position_margin_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_position_margin_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1: Add position margin，2: Reduce position margin | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**| Default current time if not pass | [optional] 
 **limit** | **int**| Default: 500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetPositionMarginHistoryV1RespItem]**](UmfuturesGetPositionMarginHistoryV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_position_side_dual_v1**
> UmfuturesGetPositionSideDualV1Resp umfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)

Get Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_side_dual_v1_resp import UmfuturesGetPositionSideDualV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.umfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetPositionSideDualV1Resp**](UmfuturesGetPositionSideDualV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_premium_index_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.umfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->umfutures_get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_premium_index_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_premium_index_v1**
> UmfuturesGetPremiumIndexV1Resp umfutures_get_premium_index_v1(symbol=symbol)

Mark Price

Mark Price and Funding Rate

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_premium_index_v1_resp import UmfuturesGetPremiumIndexV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Mark Price
        api_response = api_instance.umfutures_get_premium_index_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetPremiumIndexV1Resp**](UmfuturesGetPremiumIndexV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_rate_limit_order_v1**
> List[UmfuturesGetRateLimitOrderV1RespItem] umfutures_get_rate_limit_order_v1(timestamp, recv_window=recv_window)

Query User Rate Limit (USER_DATA)

Query User Rate Limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_rate_limit_order_v1_resp_item import UmfuturesGetRateLimitOrderV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query User Rate Limit (USER_DATA)
        api_response = api_instance.umfutures_get_rate_limit_order_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetRateLimitOrderV1RespItem]**](UmfuturesGetRateLimitOrderV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_symbol_config_v1**
> List[UmfuturesGetSymbolConfigV1RespItem] umfutures_get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)

Symbol Configuration(USER_DATA)

Get current account symbol configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_symbol_config_v1_resp_item import UmfuturesGetSymbolConfigV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Symbol Configuration(USER_DATA)
        api_response = api_instance.umfutures_get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_symbol_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_symbol_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetSymbolConfigV1RespItem]**](UmfuturesGetSymbolConfigV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_ticker24hr_v1**
> UmfuturesGetTicker24hrV1Resp umfutures_get_ticker24hr_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.
Careful when accessing this with no symbol.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker24hr_v1_resp import UmfuturesGetTicker24hrV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.umfutures_get_ticker24hr_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTicker24hrV1Resp**](UmfuturesGetTicker24hrV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_ticker_book_ticker_v1**
> UmfuturesGetTickerBookTickerV1Resp umfutures_get_ticker_book_ticker_v1(symbol=symbol)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp import UmfuturesGetTickerBookTickerV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.umfutures_get_ticker_book_ticker_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerBookTickerV1Resp**](UmfuturesGetTickerBookTickerV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_ticker_price_v1**
> UmfuturesGetTickerPriceV1Resp umfutures_get_ticker_price_v1(symbol=symbol)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v1_resp import UmfuturesGetTickerPriceV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.umfutures_get_ticker_price_v1(symbol=symbol)
        print("The response of V1Api->umfutures_get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerPriceV1Resp**](UmfuturesGetTickerPriceV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_time_v1**
> UmfuturesGetTimeV1Resp umfutures_get_time_v1()

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_time_v1_resp import UmfuturesGetTimeV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Check Server Time
        api_response = api_instance.umfutures_get_time_v1()
        print("The response of V1Api->umfutures_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesGetTimeV1Resp**](UmfuturesGetTimeV1Resp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_trade_asyn_id_v1**
> UmfuturesGetTradeAsynIdV1Resp umfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Trade Download Link by Id(USER_DATA)

Get futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_id_v1_resp import UmfuturesGetTradeAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.umfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetTradeAsynIdV1Resp**](UmfuturesGetTradeAsynIdV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_trade_asyn_v1**
> UmfuturesGetTradeAsynV1Resp umfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Trade History (USER_DATA)

Get download id for futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_v1_resp import UmfuturesGetTradeAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.umfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetTradeAsynV1Resp**](UmfuturesGetTradeAsynV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_trades_v1**
> List[UmfuturesGetTradesV1RespItem] umfutures_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trades_v1_resp_item import UmfuturesGetTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.umfutures_get_trades_v1(symbol, limit=limit)
        print("The response of V1Api->umfutures_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[UmfuturesGetTradesV1RespItem]**](UmfuturesGetTradesV1RespItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_get_user_trades_v1**
> List[UmfuturesGetUserTradesV1RespItem] umfutures_get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_user_trades_v1_resp_item import UmfuturesGetUserTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | This can only be used in combination with `symbol` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.umfutures_get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of V1Api->umfutures_get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_get_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| This can only be used in combination with &#x60;symbol&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetUserTradesV1RespItem]**](UmfuturesGetUserTradesV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_update_batch_orders_v1**
> List[UmfuturesUpdateBatchOrdersV1RespItem] umfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Modify Multiple Orders(TRADE)

Modify Multiple Orders (TRADE)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_req_batch_orders_item import UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_resp_item import UmfuturesUpdateBatchOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    batch_orders = [binance.derivatives.umfutures.UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Modify Multiple Orders(TRADE)
        api_response = api_instance.umfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of V1Api->umfutures_update_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_update_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem]**](UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesUpdateBatchOrdersV1RespItem]**](UmfuturesUpdateBatchOrdersV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_update_listen_key_v1**
> UmfuturesUpdateListenKeyV1Resp umfutures_update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_update_listen_key_v1_resp import UmfuturesUpdateListenKeyV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.umfutures_update_listen_key_v1()
        print("The response of V1Api->umfutures_update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_update_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesUpdateListenKeyV1Resp**](UmfuturesUpdateListenKeyV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **umfutures_update_order_v1**
> UmfuturesUpdateOrderV1Resp umfutures_update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify Order (TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_update_order_v1_resp import UmfuturesUpdateOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.V1Api(api_client)
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Order (TRADE)
        api_response = api_instance.umfutures_update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of V1Api->umfutures_update_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->umfutures_update_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | **str**|  | [default to &#39;&#39;]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesUpdateOrderV1Resp**](UmfuturesUpdateOrderV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

