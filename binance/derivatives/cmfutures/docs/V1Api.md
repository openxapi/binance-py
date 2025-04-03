# binance.derivatives.cmfutures.V1Api

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmfutures_create_batch_orders_v1**](V1Api.md#cmfutures_create_batch_orders_v1) | **POST** /dapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**cmfutures_create_countdown_cancel_all_v1**](V1Api.md#cmfutures_create_countdown_cancel_all_v1) | **POST** /dapi/v1/countdownCancelAll | Auto-Cancel All Open Orders (TRADE)
[**cmfutures_create_leverage_v1**](V1Api.md#cmfutures_create_leverage_v1) | **POST** /dapi/v1/leverage | Change Initial Leverage (TRADE)
[**cmfutures_create_listen_key_v1**](V1Api.md#cmfutures_create_listen_key_v1) | **POST** /dapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**cmfutures_create_margin_type_v1**](V1Api.md#cmfutures_create_margin_type_v1) | **POST** /dapi/v1/marginType | Change Margin Type (TRADE)
[**cmfutures_create_order_v1**](V1Api.md#cmfutures_create_order_v1) | **POST** /dapi/v1/order | New Order (TRADE)
[**cmfutures_create_position_margin_v1**](V1Api.md#cmfutures_create_position_margin_v1) | **POST** /dapi/v1/positionMargin | Modify Isolated Position Margin(TRADE)
[**cmfutures_create_position_side_dual_v1**](V1Api.md#cmfutures_create_position_side_dual_v1) | **POST** /dapi/v1/positionSide/dual | Change Position Mode(TRADE)
[**cmfutures_delete_all_open_orders_v1**](V1Api.md#cmfutures_delete_all_open_orders_v1) | **DELETE** /dapi/v1/allOpenOrders | Cancel All Open Orders(TRADE)
[**cmfutures_delete_batch_orders_v1**](V1Api.md#cmfutures_delete_batch_orders_v1) | **DELETE** /dapi/v1/batchOrders | Cancel Multiple Orders(TRADE)
[**cmfutures_delete_listen_key_v1**](V1Api.md#cmfutures_delete_listen_key_v1) | **DELETE** /dapi/v1/listenKey | Close User Data Stream(USER_STREAM)
[**cmfutures_delete_order_v1**](V1Api.md#cmfutures_delete_order_v1) | **DELETE** /dapi/v1/order | Cancel Order (TRADE)
[**cmfutures_get_account_v1**](V1Api.md#cmfutures_get_account_v1) | **GET** /dapi/v1/account | Account Information (USER_DATA)
[**cmfutures_get_adl_quantile_v1**](V1Api.md#cmfutures_get_adl_quantile_v1) | **GET** /dapi/v1/adlQuantile | Position ADL Quantile Estimation(USER_DATA)
[**cmfutures_get_agg_trades_v1**](V1Api.md#cmfutures_get_agg_trades_v1) | **GET** /dapi/v1/aggTrades | Compressed/Aggregate Trades List
[**cmfutures_get_all_orders_v1**](V1Api.md#cmfutures_get_all_orders_v1) | **GET** /dapi/v1/allOrders | All Orders (USER_DATA)
[**cmfutures_get_balance_v1**](V1Api.md#cmfutures_get_balance_v1) | **GET** /dapi/v1/balance | Futures Account Balance (USER_DATA)
[**cmfutures_get_commission_rate_v1**](V1Api.md#cmfutures_get_commission_rate_v1) | **GET** /dapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**cmfutures_get_constituents_v1**](V1Api.md#cmfutures_get_constituents_v1) | **GET** /dapi/v1/constituents | Query Index Price Constituents
[**cmfutures_get_continuous_klines_v1**](V1Api.md#cmfutures_get_continuous_klines_v1) | **GET** /dapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**cmfutures_get_depth_v1**](V1Api.md#cmfutures_get_depth_v1) | **GET** /dapi/v1/depth | Order Book
[**cmfutures_get_exchange_info_v1**](V1Api.md#cmfutures_get_exchange_info_v1) | **GET** /dapi/v1/exchangeInfo | Exchange Information
[**cmfutures_get_force_orders_v1**](V1Api.md#cmfutures_get_force_orders_v1) | **GET** /dapi/v1/forceOrders | User&#39;s Force Orders(USER_DATA)
[**cmfutures_get_funding_info_v1**](V1Api.md#cmfutures_get_funding_info_v1) | **GET** /dapi/v1/fundingInfo | Get Funding Rate Info
[**cmfutures_get_funding_rate_v1**](V1Api.md#cmfutures_get_funding_rate_v1) | **GET** /dapi/v1/fundingRate | Get Funding Rate History of Perpetual Futures
[**cmfutures_get_historical_trades_v1**](V1Api.md#cmfutures_get_historical_trades_v1) | **GET** /dapi/v1/historicalTrades | Old Trades Lookup(MARKET_DATA)
[**cmfutures_get_income_asyn_id_v1**](V1Api.md#cmfutures_get_income_asyn_id_v1) | **GET** /dapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**cmfutures_get_income_asyn_v1**](V1Api.md#cmfutures_get_income_asyn_v1) | **GET** /dapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**cmfutures_get_income_v1**](V1Api.md#cmfutures_get_income_v1) | **GET** /dapi/v1/income | Get Income History(USER_DATA)
[**cmfutures_get_index_price_klines_v1**](V1Api.md#cmfutures_get_index_price_klines_v1) | **GET** /dapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**cmfutures_get_klines_v1**](V1Api.md#cmfutures_get_klines_v1) | **GET** /dapi/v1/klines | Kline/Candlestick Data
[**cmfutures_get_leverage_bracket_v1**](V1Api.md#cmfutures_get_leverage_bracket_v1) | **GET** /dapi/v1/leverageBracket | Notional Bracket for Pair(USER_DATA)
[**cmfutures_get_mark_price_klines_v1**](V1Api.md#cmfutures_get_mark_price_klines_v1) | **GET** /dapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**cmfutures_get_open_interest_v1**](V1Api.md#cmfutures_get_open_interest_v1) | **GET** /dapi/v1/openInterest | Open Interest
[**cmfutures_get_open_order_v1**](V1Api.md#cmfutures_get_open_order_v1) | **GET** /dapi/v1/openOrder | Query Current Open Order(USER_DATA)
[**cmfutures_get_open_orders_v1**](V1Api.md#cmfutures_get_open_orders_v1) | **GET** /dapi/v1/openOrders | Current All Open Orders (USER_DATA)
[**cmfutures_get_order_amendment_v1**](V1Api.md#cmfutures_get_order_amendment_v1) | **GET** /dapi/v1/orderAmendment | Get Order Modify History (USER_DATA)
[**cmfutures_get_order_asyn_id_v1**](V1Api.md#cmfutures_get_order_asyn_id_v1) | **GET** /dapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**cmfutures_get_order_asyn_v1**](V1Api.md#cmfutures_get_order_asyn_v1) | **GET** /dapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**cmfutures_get_order_v1**](V1Api.md#cmfutures_get_order_v1) | **GET** /dapi/v1/order | Query Order (USER_DATA)
[**cmfutures_get_ping_v1**](V1Api.md#cmfutures_get_ping_v1) | **GET** /dapi/v1/ping | Test Connectivity
[**cmfutures_get_pm_account_info_v1**](V1Api.md#cmfutures_get_pm_account_info_v1) | **GET** /dapi/v1/pmAccountInfo | Classic Portfolio Margin Account Information (USER_DATA)
[**cmfutures_get_position_margin_history_v1**](V1Api.md#cmfutures_get_position_margin_history_v1) | **GET** /dapi/v1/positionMargin/history | Get Position Margin Change History(TRADE)
[**cmfutures_get_position_risk_v1**](V1Api.md#cmfutures_get_position_risk_v1) | **GET** /dapi/v1/positionRisk | Position Information(USER_DATA)
[**cmfutures_get_position_side_dual_v1**](V1Api.md#cmfutures_get_position_side_dual_v1) | **GET** /dapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**cmfutures_get_premium_index_klines_v1**](V1Api.md#cmfutures_get_premium_index_klines_v1) | **GET** /dapi/v1/premiumIndexKlines | Premium index Kline Data
[**cmfutures_get_premium_index_v1**](V1Api.md#cmfutures_get_premium_index_v1) | **GET** /dapi/v1/premiumIndex | Index Price and Mark Price
[**cmfutures_get_ticker24hr_v1**](V1Api.md#cmfutures_get_ticker24hr_v1) | **GET** /dapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**cmfutures_get_ticker_book_ticker_v1**](V1Api.md#cmfutures_get_ticker_book_ticker_v1) | **GET** /dapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**cmfutures_get_ticker_price_v1**](V1Api.md#cmfutures_get_ticker_price_v1) | **GET** /dapi/v1/ticker/price | Symbol Price Ticker
[**cmfutures_get_time_v1**](V1Api.md#cmfutures_get_time_v1) | **GET** /dapi/v1/time | Check Server time
[**cmfutures_get_trade_asyn_id_v1**](V1Api.md#cmfutures_get_trade_asyn_id_v1) | **GET** /dapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**cmfutures_get_trade_asyn_v1**](V1Api.md#cmfutures_get_trade_asyn_v1) | **GET** /dapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)
[**cmfutures_get_trades_v1**](V1Api.md#cmfutures_get_trades_v1) | **GET** /dapi/v1/trades | Recent Trades List
[**cmfutures_get_user_trades_v1**](V1Api.md#cmfutures_get_user_trades_v1) | **GET** /dapi/v1/userTrades | Account Trade List (USER_DATA)
[**cmfutures_update_batch_orders_v1**](V1Api.md#cmfutures_update_batch_orders_v1) | **PUT** /dapi/v1/batchOrders | Modify Multiple Orders(TRADE)
[**cmfutures_update_listen_key_v1**](V1Api.md#cmfutures_update_listen_key_v1) | **PUT** /dapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)
[**cmfutures_update_order_v1**](V1Api.md#cmfutures_update_order_v1) | **PUT** /dapi/v1/order | Modify Order (TRADE)


# **cmfutures_create_batch_orders_v1**
> List[CmfuturesCreateBatchOrdersV1RespInner] cmfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Place multiple orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_batch_order_v1_req_batch_orders_item import CmfuturesCreateBatchOrderV1ReqBatchOrdersItem
from binance.derivatives.cmfutures.models.cmfutures_create_batch_orders_v1_resp_inner import CmfuturesCreateBatchOrdersV1RespInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    batch_orders = [binance.derivatives.cmfutures.CmfuturesCreateBatchOrderV1ReqBatchOrdersItem()] # List[CmfuturesCreateBatchOrderV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.cmfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[CmfuturesCreateBatchOrderV1ReqBatchOrdersItem]**](CmfuturesCreateBatchOrderV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesCreateBatchOrdersV1RespInner]**](CmfuturesCreateBatchOrdersV1RespInner.md)

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

# **cmfutures_create_countdown_cancel_all_v1**
> CmfuturesCreateCountdownCancelAllV1Resp cmfutures_create_countdown_cancel_all_v1(countdown_time, symbol, timestamp, recv_window=recv_window)

Auto-Cancel All Open Orders (TRADE)

Cancel all open orders of the specified symbol at the end of the specified countdown. This rest endpoint means to ensure your open orders are canceled in case of an outage. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and repalced by a new one. The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function. We do not recommend setting the countdown time to be too precise or too small.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_countdown_cancel_all_v1_resp import CmfuturesCreateCountdownCancelAllV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    countdown_time = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Auto-Cancel All Open Orders (TRADE)
        api_response = api_instance.cmfutures_create_countdown_cancel_all_v1(countdown_time, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_time** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesCreateCountdownCancelAllV1Resp**](CmfuturesCreateCountdownCancelAllV1Resp.md)

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

# **cmfutures_create_leverage_v1**
> CmfuturesCreateLeverageV1Resp cmfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change Initial Leverage (TRADE)

Change user's initial leverage in the specific symbol market.
For Hedge Mode, LONG and SHORT positions of one symbol use the same initial leverage and share a total notional value.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_leverage_v1_resp import CmfuturesCreateLeverageV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Initial Leverage (TRADE)
        api_response = api_instance.cmfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesCreateLeverageV1Resp**](CmfuturesCreateLeverageV1Resp.md)

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

# **cmfutures_create_listen_key_v1**
> CmfuturesCreateListenKeyV1Resp cmfutures_create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_listen_key_v1_resp import CmfuturesCreateListenKeyV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.cmfutures_create_listen_key_v1()
        print("The response of V1Api->cmfutures_create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesCreateListenKeyV1Resp**](CmfuturesCreateListenKeyV1Resp.md)

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

# **cmfutures_create_margin_type_v1**
> CmfuturesCreateMarginTypeV1Resp cmfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)

Change Margin Type (TRADE)

Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.
With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_margin_type_v1_resp import CmfuturesCreateMarginTypeV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    margin_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Margin Type (TRADE)
        api_response = api_instance.cmfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_margin_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_margin_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesCreateMarginTypeV1Resp**](CmfuturesCreateMarginTypeV1Resp.md)

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

# **cmfutures_create_order_v1**
> CmfuturesCreateOrderV1Resp cmfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New Order (TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_order_v1_resp import CmfuturesCreateOrderV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
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
        # New Order (TRADE)
        api_response = api_instance.cmfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of V1Api->cmfutures_create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_order_v1: %s\n" % e)
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

[**CmfuturesCreateOrderV1Resp**](CmfuturesCreateOrderV1Resp.md)

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

# **cmfutures_create_position_margin_v1**
> CmfuturesCreatePositionMarginV1Resp cmfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)

Modify Isolated Position Margin(TRADE)

Modify Isolated Position Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_position_margin_v1_resp import CmfuturesCreatePositionMarginV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    amount = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Isolated Position Margin(TRADE)
        api_response = api_instance.cmfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_position_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_position_margin_v1: %s\n" % e)
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

[**CmfuturesCreatePositionMarginV1Resp**](CmfuturesCreatePositionMarginV1Resp.md)

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

# **cmfutures_create_position_side_dual_v1**
> CmfuturesCreatePositionSideDualV1Resp cmfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_position_side_dual_v1_resp import CmfuturesCreatePositionSideDualV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Position Mode(TRADE)
        api_response = api_instance.cmfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_create_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_create_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesCreatePositionSideDualV1Resp**](CmfuturesCreatePositionSideDualV1Resp.md)

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

# **cmfutures_delete_all_open_orders_v1**
> CmfuturesDeleteAllOpenOrdersV1Resp cmfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All Open Orders(TRADE)

Cancel All Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_delete_all_open_orders_v1_resp import CmfuturesDeleteAllOpenOrdersV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Open Orders(TRADE)
        api_response = api_instance.cmfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesDeleteAllOpenOrdersV1Resp**](CmfuturesDeleteAllOpenOrdersV1Resp.md)

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

# **cmfutures_delete_batch_orders_v1**
> List[CmfuturesDeleteBatchOrdersV1RespInner] cmfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)

Cancel Multiple Orders(TRADE)

Cancel Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_delete_batch_orders_v1_resp_inner import CmfuturesDeleteBatchOrdersV1RespInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id_list = [56] # List[int] | max length 10 <br/> e.g. [1234567,2345678] (optional)
    orig_client_order_id_list = ['orig_client_order_id_list_example'] # List[str] | max length 10<br/> e.g. [&#34;my_id_1&#34;,&#34;my_id_2&#34;], encode the double quotes. No space after comma. (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Orders(TRADE)
        api_response = api_instance.cmfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)
        print("The response of V1Api->cmfutures_delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_delete_batch_orders_v1: %s\n" % e)
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

[**List[CmfuturesDeleteBatchOrdersV1RespInner]**](CmfuturesDeleteBatchOrdersV1RespInner.md)

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

# **cmfutures_delete_listen_key_v1**
> object cmfutures_delete_listen_key_v1()

Close User Data Stream(USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Close User Data Stream(USER_STREAM)
        api_response = api_instance.cmfutures_delete_listen_key_v1()
        print("The response of V1Api->cmfutures_delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_delete_listen_key_v1: %s\n" % e)
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

# **cmfutures_delete_order_v1**
> CmfuturesDeleteOrderV1Resp cmfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_delete_order_v1_resp import CmfuturesDeleteOrderV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Order (TRADE)
        api_response = api_instance.cmfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->cmfutures_delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_delete_order_v1: %s\n" % e)
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

[**CmfuturesDeleteOrderV1Resp**](CmfuturesDeleteOrderV1Resp.md)

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

# **cmfutures_get_account_v1**
> CmfuturesGetAccountV1Resp cmfutures_get_account_v1(timestamp, recv_window=recv_window)

Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp import CmfuturesGetAccountV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information (USER_DATA)
        api_response = api_instance.cmfutures_get_account_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetAccountV1Resp**](CmfuturesGetAccountV1Resp.md)

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

# **cmfutures_get_adl_quantile_v1**
> List[CmfuturesGetAdlQuantileV1RespItem] cmfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

Position ADL Quantile Estimation(USER_DATA)

Query position ADL quantile estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_adl_quantile_v1_resp_item import CmfuturesGetAdlQuantileV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.cmfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetAdlQuantileV1RespItem]**](CmfuturesGetAdlQuantileV1RespItem.md)

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

# **cmfutures_get_agg_trades_v1**
> List[CmfuturesGetAggTradesV1RespItem] cmfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_agg_trades_v1_resp_item import CmfuturesGetAggTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.cmfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_agg_trades_v1: %s\n" % e)
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

[**List[CmfuturesGetAggTradesV1RespItem]**](CmfuturesGetAggTradesV1RespItem.md)

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

# **cmfutures_get_all_orders_v1**
> List[CmfuturesGetAllOrdersV1RespItem] cmfutures_get_all_orders_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_all_orders_v1_resp_item import CmfuturesGetAllOrdersV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # All Orders (USER_DATA)
        api_response = api_instance.cmfutures_get_all_orders_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetAllOrdersV1RespItem]**](CmfuturesGetAllOrdersV1RespItem.md)

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

# **cmfutures_get_balance_v1**
> List[CmfuturesGetBalanceV1RespItem] cmfutures_get_balance_v1(timestamp, recv_window=recv_window)

Futures Account Balance (USER_DATA)

Check futures account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_balance_v1_resp_item import CmfuturesGetBalanceV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance (USER_DATA)
        api_response = api_instance.cmfutures_get_balance_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetBalanceV1RespItem]**](CmfuturesGetBalanceV1RespItem.md)

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

# **cmfutures_get_commission_rate_v1**
> CmfuturesGetCommissionRateV1Resp cmfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

User Commission Rate (USER_DATA)

Query user commission rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_commission_rate_v1_resp import CmfuturesGetCommissionRateV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.cmfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetCommissionRateV1Resp**](CmfuturesGetCommissionRateV1Resp.md)

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

# **cmfutures_get_constituents_v1**
> CmfuturesGetConstituentsV1Resp cmfutures_get_constituents_v1(symbol)

Query Index Price Constituents

Query index price constituents

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_constituents_v1_resp import CmfuturesGetConstituentsV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.cmfutures_get_constituents_v1(symbol)
        print("The response of V1Api->cmfutures_get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_constituents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**CmfuturesGetConstituentsV1Resp**](CmfuturesGetConstituentsV1Resp.md)

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

# **cmfutures_get_continuous_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_continuous_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_depth_v1**
> CmfuturesGetDepthV1Resp cmfutures_get_depth_v1(symbol, limit=limit)

Order Book

Query orderbook on specific symbol

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_depth_v1_resp import CmfuturesGetDepthV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.cmfutures_get_depth_v1(symbol, limit=limit)
        print("The response of V1Api->cmfutures_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] | [optional] [default to 500]

### Return type

[**CmfuturesGetDepthV1Resp**](CmfuturesGetDepthV1Resp.md)

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

# **cmfutures_get_exchange_info_v1**
> CmfuturesGetExchangeInfoV1Resp cmfutures_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_exchange_info_v1_resp import CmfuturesGetExchangeInfoV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Exchange Information
        api_response = api_instance.cmfutures_get_exchange_info_v1()
        print("The response of V1Api->cmfutures_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesGetExchangeInfoV1Resp**](CmfuturesGetExchangeInfoV1Resp.md)

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

# **cmfutures_get_force_orders_v1**
> List[CmfuturesGetForceOrdersV1RespItem] cmfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, recv_window=recv_window, limit=limit, start_time=start_time, end_time=end_time)

User's Force Orders(USER_DATA)

User's Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_force_orders_v1_resp_item import CmfuturesGetForceOrdersV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # User's Force Orders(USER_DATA)
        api_response = api_instance.cmfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, recv_window=recv_window, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of V1Api->cmfutures_get_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **auto_close_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetForceOrdersV1RespItem]**](CmfuturesGetForceOrdersV1RespItem.md)

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

# **cmfutures_get_funding_info_v1**
> List[CmfuturesGetFundingInfoV1RespItem] cmfutures_get_funding_info_v1()

Get Funding Rate Info

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_funding_info_v1_resp_item import CmfuturesGetFundingInfoV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.cmfutures_get_funding_info_v1()
        print("The response of V1Api->cmfutures_get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_funding_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CmfuturesGetFundingInfoV1RespItem]**](CmfuturesGetFundingInfoV1RespItem.md)

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

# **cmfutures_get_funding_rate_v1**
> List[CmfuturesGetFundingRateV1RespItem] cmfutures_get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History of Perpetual Futures

Get Funding Rate History of Perpetual Futures

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_funding_rate_v1_resp_item import CmfuturesGetFundingRateV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History of Perpetual Futures
        api_response = api_instance.cmfutures_get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding rate from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding rate  until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]

### Return type

[**List[CmfuturesGetFundingRateV1RespItem]**](CmfuturesGetFundingRateV1RespItem.md)

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

# **cmfutures_get_historical_trades_v1**
> List[CmfuturesGetHistoricalTradesV1RespItem] cmfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)

Old Trades Lookup(MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_historical_trades_v1_resp_item import CmfuturesGetHistoricalTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup(MARKET_DATA)
        api_response = api_instance.cmfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of V1Api->cmfutures_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 500. | [optional] [default to 100]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[CmfuturesGetHistoricalTradesV1RespItem]**](CmfuturesGetHistoricalTradesV1RespItem.md)

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

# **cmfutures_get_income_asyn_id_v1**
> CmfuturesGetIncomeAsynIdV1Resp cmfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Transaction History Download Link by Id (USER_DATA)

Get futures transaction history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_asyn_id_v1_resp import CmfuturesGetIncomeAsynIdV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.cmfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetIncomeAsynIdV1Resp**](CmfuturesGetIncomeAsynIdV1Resp.md)

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

# **cmfutures_get_income_asyn_v1**
> CmfuturesGetIncomeAsynV1Resp cmfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Transaction History(USER_DATA)

Get download id for futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_asyn_v1_resp import CmfuturesGetIncomeAsynV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.cmfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetIncomeAsynV1Resp**](CmfuturesGetIncomeAsynV1Resp.md)

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

# **cmfutures_get_income_v1**
> List[CmfuturesGetIncomeV1RespItem] cmfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get Income History(USER_DATA)

Get income history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_v1_resp_item import CmfuturesGetIncomeV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | &#34;TRANSFER&#34;,&#34;WELCOME_BONUS&#34;, &#34;FUNDING_FEE&#34;, &#34;REALIZED_PNL&#34;, &#34;COMMISSION&#34;, &#34;INSURANCE_CLEAR&#34;, and &#34;DELIVERED_SETTELMENT&#34; (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History(USER_DATA)
        api_response = api_instance.cmfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| &amp;#34;TRANSFER&amp;#34;,&amp;#34;WELCOME_BONUS&amp;#34;, &amp;#34;FUNDING_FEE&amp;#34;, &amp;#34;REALIZED_PNL&amp;#34;, &amp;#34;COMMISSION&amp;#34;, &amp;#34;INSURANCE_CLEAR&amp;#34;, and &amp;#34;DELIVERED_SETTELMENT&amp;#34; | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetIncomeV1RespItem]**](CmfuturesGetIncomeV1RespItem.md)

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

# **cmfutures_get_index_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_index_price_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_leverage_bracket_v1**
> List[CmfuturesGetLeverageBracketV1RespItem] cmfutures_get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)

Notional Bracket for Pair(USER_DATA)

Not recommended to continue using this v1 endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_leverage_bracket_v1_resp_item import CmfuturesGetLeverageBracketV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Pair(USER_DATA)
        api_response = api_instance.cmfutures_get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetLeverageBracketV1RespItem]**](CmfuturesGetLeverageBracketV1RespItem.md)

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

# **cmfutures_get_mark_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_mark_price_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_open_interest_v1**
> CmfuturesGetOpenInterestV1Resp cmfutures_get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_open_interest_v1_resp import CmfuturesGetOpenInterestV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.cmfutures_get_open_interest_v1(symbol)
        print("The response of V1Api->cmfutures_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**CmfuturesGetOpenInterestV1Resp**](CmfuturesGetOpenInterestV1Resp.md)

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

# **cmfutures_get_open_order_v1**
> CmfuturesGetOpenOrderV1Resp cmfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current Open Order(USER_DATA)

Query Current Open Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_open_order_v1_resp import CmfuturesGetOpenOrderV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Order(USER_DATA)
        api_response = api_instance.cmfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_open_order_v1: %s\n" % e)
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

[**CmfuturesGetOpenOrderV1Resp**](CmfuturesGetOpenOrderV1Resp.md)

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

# **cmfutures_get_open_orders_v1**
> List[CmfuturesGetOpenOrdersV1RespItem] cmfutures_get_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)

Current All Open Orders (USER_DATA)

Get all open orders on a symbol. Careful when accessing this with no symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_open_orders_v1_resp_item import CmfuturesGetOpenOrdersV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Current All Open Orders (USER_DATA)
        api_response = api_instance.cmfutures_get_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetOpenOrdersV1RespItem]**](CmfuturesGetOpenOrdersV1RespItem.md)

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

# **cmfutures_get_order_amendment_v1**
> List[CmfuturesGetOrderAmendmentV1RespItem] cmfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Order Modify History (USER_DATA)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_amendment_v1_resp_item import CmfuturesGetOrderAmendmentV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
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
        api_response = api_instance.cmfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_order_amendment_v1: %s\n" % e)
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

[**List[CmfuturesGetOrderAmendmentV1RespItem]**](CmfuturesGetOrderAmendmentV1RespItem.md)

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

# **cmfutures_get_order_asyn_id_v1**
> CmfuturesGetOrderAsynIdV1Resp cmfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Order History Download Link by Id (USER_DATA)

Get futures order history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_asyn_id_v1_resp import CmfuturesGetOrderAsynIdV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.cmfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetOrderAsynIdV1Resp**](CmfuturesGetOrderAsynIdV1Resp.md)

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

# **cmfutures_get_order_asyn_v1**
> CmfuturesGetOrderAsynV1Resp cmfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_asyn_v1_resp import CmfuturesGetOrderAsynV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.cmfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetOrderAsynV1Resp**](CmfuturesGetOrderAsynV1Resp.md)

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

# **cmfutures_get_order_v1**
> CmfuturesGetOrderV1Resp cmfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_v1_resp import CmfuturesGetOrderV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Order (USER_DATA)
        api_response = api_instance.cmfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_order_v1: %s\n" % e)
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

[**CmfuturesGetOrderV1Resp**](CmfuturesGetOrderV1Resp.md)

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

# **cmfutures_get_ping_v1**
> object cmfutures_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.cmfutures_get_ping_v1()
        print("The response of V1Api->cmfutures_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_ping_v1: %s\n" % e)
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

# **cmfutures_get_pm_account_info_v1**
> CmfuturesGetPmAccountInfoV1Resp cmfutures_get_pm_account_info_v1(asset, recv_window=recv_window)

Classic Portfolio Margin Account Information (USER_DATA)

Get Classic Portfolio Margin current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_pm_account_info_v1_resp import CmfuturesGetPmAccountInfoV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    asset = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Classic Portfolio Margin Account Information (USER_DATA)
        api_response = api_instance.cmfutures_get_pm_account_info_v1(asset, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_pm_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_pm_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetPmAccountInfoV1Resp**](CmfuturesGetPmAccountInfoV1Resp.md)

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

# **cmfutures_get_position_margin_history_v1**
> List[CmfuturesGetPositionMarginHistoryV1RespItem] cmfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Position Margin Change History(TRADE)

Get position margin change history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_position_margin_history_v1_resp_item import CmfuturesGetPositionMarginHistoryV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1: Add position margin,2: Reduce position margin (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default: 50 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Get Position Margin Change History(TRADE)
        api_response = api_instance.cmfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_position_margin_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_position_margin_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1: Add position margin,2: Reduce position margin | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default: 50 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetPositionMarginHistoryV1RespItem]**](CmfuturesGetPositionMarginHistoryV1RespItem.md)

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

# **cmfutures_get_position_risk_v1**
> List[CmfuturesGetPositionRiskV1RespItem] cmfutures_get_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)

Position Information(USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_position_risk_v1_resp_item import CmfuturesGetPositionRiskV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    margin_asset = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information(USER_DATA)
        api_response = api_instance.cmfutures_get_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_position_risk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **margin_asset** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetPositionRiskV1RespItem]**](CmfuturesGetPositionRiskV1RespItem.md)

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

# **cmfutures_get_position_side_dual_v1**
> CmfuturesGetPositionSideDualV1Resp cmfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)

Get Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_position_side_dual_v1_resp import CmfuturesGetPositionSideDualV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.cmfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetPositionSideDualV1Resp**](CmfuturesGetPositionSideDualV1Resp.md)

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

# **cmfutures_get_premium_index_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.cmfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->cmfutures_get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_premium_index_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_premium_index_v1**
> List[CmfuturesGetPremiumIndexV1RespItem] cmfutures_get_premium_index_v1(symbol=symbol, pair=pair)

Index Price and Mark Price

Query index price and mark price

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_premium_index_v1_resp_item import CmfuturesGetPremiumIndexV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Index Price and Mark Price
        api_response = api_instance.cmfutures_get_premium_index_v1(symbol=symbol, pair=pair)
        print("The response of V1Api->cmfutures_get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetPremiumIndexV1RespItem]**](CmfuturesGetPremiumIndexV1RespItem.md)

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

# **cmfutures_get_ticker24hr_v1**
> List[CmfuturesGetTicker24hrV1RespItem] cmfutures_get_ticker24hr_v1(symbol=symbol, pair=pair)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker24hr_v1_resp_item import CmfuturesGetTicker24hrV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.cmfutures_get_ticker24hr_v1(symbol=symbol, pair=pair)
        print("The response of V1Api->cmfutures_get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTicker24hrV1RespItem]**](CmfuturesGetTicker24hrV1RespItem.md)

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

# **cmfutures_get_ticker_book_ticker_v1**
> List[CmfuturesGetTickerBookTickerV1RespItem] cmfutures_get_ticker_book_ticker_v1(symbol=symbol, pair=pair)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker_book_ticker_v1_resp_item import CmfuturesGetTickerBookTickerV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.cmfutures_get_ticker_book_ticker_v1(symbol=symbol, pair=pair)
        print("The response of V1Api->cmfutures_get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTickerBookTickerV1RespItem]**](CmfuturesGetTickerBookTickerV1RespItem.md)

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

# **cmfutures_get_ticker_price_v1**
> List[CmfuturesGetTickerPriceV1RespItem] cmfutures_get_ticker_price_v1(symbol=symbol, pair=pair)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker_price_v1_resp_item import CmfuturesGetTickerPriceV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.cmfutures_get_ticker_price_v1(symbol=symbol, pair=pair)
        print("The response of V1Api->cmfutures_get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTickerPriceV1RespItem]**](CmfuturesGetTickerPriceV1RespItem.md)

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

# **cmfutures_get_time_v1**
> CmfuturesGetTimeV1Resp cmfutures_get_time_v1()

Check Server time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_time_v1_resp import CmfuturesGetTimeV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Check Server time
        api_response = api_instance.cmfutures_get_time_v1()
        print("The response of V1Api->cmfutures_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesGetTimeV1Resp**](CmfuturesGetTimeV1Resp.md)

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

# **cmfutures_get_trade_asyn_id_v1**
> CmfuturesGetTradeAsynIdV1Resp cmfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Trade Download Link by Id(USER_DATA)

Get futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trade_asyn_id_v1_resp import CmfuturesGetTradeAsynIdV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.cmfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetTradeAsynIdV1Resp**](CmfuturesGetTradeAsynIdV1Resp.md)

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

# **cmfutures_get_trade_asyn_v1**
> CmfuturesGetTradeAsynV1Resp cmfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Trade History (USER_DATA)

Get download id for futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trade_asyn_v1_resp import CmfuturesGetTradeAsynV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.cmfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetTradeAsynV1Resp**](CmfuturesGetTradeAsynV1Resp.md)

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

# **cmfutures_get_trades_v1**
> List[CmfuturesGetTradesV1RespItem] cmfutures_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trades_v1_resp_item import CmfuturesGetTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.cmfutures_get_trades_v1(symbol, limit=limit)
        print("The response of V1Api->cmfutures_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[CmfuturesGetTradesV1RespItem]**](CmfuturesGetTradesV1RespItem.md)

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

# **cmfutures_get_user_trades_v1**
> List[CmfuturesGetUserTradesV1RespItem] cmfutures_get_user_trades_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_user_trades_v1_resp_item import CmfuturesGetUserTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 50 # int | Default 50; max 1000 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.cmfutures_get_user_trades_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of V1Api->cmfutures_get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_get_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 50; max 1000 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetUserTradesV1RespItem]**](CmfuturesGetUserTradesV1RespItem.md)

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

# **cmfutures_update_batch_orders_v1**
> List[CmfuturesUpdateBatchOrdersV1RespInner] cmfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Modify Multiple Orders(TRADE)

Modify Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_update_batch_orders_v1_resp_inner import CmfuturesUpdateBatchOrdersV1RespInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    batch_orders = None # object | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Modify Multiple Orders(TRADE)
        api_response = api_instance.cmfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of V1Api->cmfutures_update_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_update_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**object**](object.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesUpdateBatchOrdersV1RespInner]**](CmfuturesUpdateBatchOrdersV1RespInner.md)

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

# **cmfutures_update_listen_key_v1**
> object cmfutures_update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.cmfutures_update_listen_key_v1()
        print("The response of V1Api->cmfutures_update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_update_listen_key_v1: %s\n" % e)
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

# **cmfutures_update_order_v1**
> CmfuturesUpdateOrderV1Resp cmfutures_update_order_v1(side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window)

Modify Order (TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_update_order_v1_resp import CmfuturesUpdateOrderV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.V1Api(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Order (TRADE)
        api_response = api_instance.cmfutures_update_order_v1(side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window)
        print("The response of V1Api->cmfutures_update_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->cmfutures_update_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesUpdateOrderV1Resp**](CmfuturesUpdateOrderV1Resp.md)

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

