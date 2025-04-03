# binance.derivatives.options.V1Api

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_create_batch_orders_v1**](V1Api.md#options_create_batch_orders_v1) | **POST** /eapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**options_create_block_order_create_v1**](V1Api.md#options_create_block_order_create_v1) | **POST** /eapi/v1/block/order/create | New Block Trade Order (TRADE)
[**options_create_block_order_execute_v1**](V1Api.md#options_create_block_order_execute_v1) | **POST** /eapi/v1/block/order/execute | Accept Block Trade Order (TRADE)
[**options_create_countdown_cancel_all_heart_beat_v1**](V1Api.md#options_create_countdown_cancel_all_heart_beat_v1) | **POST** /eapi/v1/countdownCancelAllHeartBeat | Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
[**options_create_countdown_cancel_all_v1**](V1Api.md#options_create_countdown_cancel_all_v1) | **POST** /eapi/v1/countdownCancelAll | Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**options_create_listen_key_v1**](V1Api.md#options_create_listen_key_v1) | **POST** /eapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**options_create_mmp_reset_v1**](V1Api.md#options_create_mmp_reset_v1) | **POST** /eapi/v1/mmpReset | Reset Market Maker Protection Config (TRADE)
[**options_create_mmp_set_v1**](V1Api.md#options_create_mmp_set_v1) | **POST** /eapi/v1/mmpSet | Set Market Maker Protection Config (TRADE)
[**options_create_order_v1**](V1Api.md#options_create_order_v1) | **POST** /eapi/v1/order | New Order (TRADE)
[**options_delete_all_open_orders_by_underlying_v1**](V1Api.md#options_delete_all_open_orders_by_underlying_v1) | **DELETE** /eapi/v1/allOpenOrdersByUnderlying | Cancel All Option Orders By Underlying (TRADE)
[**options_delete_all_open_orders_v1**](V1Api.md#options_delete_all_open_orders_v1) | **DELETE** /eapi/v1/allOpenOrders | Cancel all Option orders on specific symbol (TRADE)
[**options_delete_batch_orders_v1**](V1Api.md#options_delete_batch_orders_v1) | **DELETE** /eapi/v1/batchOrders | Cancel Multiple Option Orders (TRADE)
[**options_delete_block_order_create_v1**](V1Api.md#options_delete_block_order_create_v1) | **DELETE** /eapi/v1/block/order/create | Cancel Block Trade Order (TRADE)
[**options_delete_listen_key_v1**](V1Api.md#options_delete_listen_key_v1) | **DELETE** /eapi/v1/listenKey | Close User Data Stream (USER_STREAM)
[**options_delete_order_v1**](V1Api.md#options_delete_order_v1) | **DELETE** /eapi/v1/order | Cancel Option Order (TRADE)
[**options_get_account_v1**](V1Api.md#options_get_account_v1) | **GET** /eapi/v1/account | Option Account Information(TRADE)
[**options_get_bill_v1**](V1Api.md#options_get_bill_v1) | **GET** /eapi/v1/bill | Account Funding Flow (USER_DATA)
[**options_get_block_order_execute_v1**](V1Api.md#options_get_block_order_execute_v1) | **GET** /eapi/v1/block/order/execute | Query Block Trade Details (USER_DATA)
[**options_get_block_order_orders_v1**](V1Api.md#options_get_block_order_orders_v1) | **GET** /eapi/v1/block/order/orders | Query Block Trade Order (TRADE)
[**options_get_block_trades_v1**](V1Api.md#options_get_block_trades_v1) | **GET** /eapi/v1/blockTrades | Recent Block Trades List
[**options_get_block_user_trades_v1**](V1Api.md#options_get_block_user_trades_v1) | **GET** /eapi/v1/block/user-trades | Account Block Trade List (USER_DATA)
[**options_get_countdown_cancel_all_v1**](V1Api.md#options_get_countdown_cancel_all_v1) | **GET** /eapi/v1/countdownCancelAll | Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**options_get_depth_v1**](V1Api.md#options_get_depth_v1) | **GET** /eapi/v1/depth | Order Book
[**options_get_exchange_info_v1**](V1Api.md#options_get_exchange_info_v1) | **GET** /eapi/v1/exchangeInfo | Exchange Information
[**options_get_exercise_history_v1**](V1Api.md#options_get_exercise_history_v1) | **GET** /eapi/v1/exerciseHistory | Historical Exercise Records
[**options_get_exercise_record_v1**](V1Api.md#options_get_exercise_record_v1) | **GET** /eapi/v1/exerciseRecord | User Exercise Record (USER_DATA)
[**options_get_historical_trades_v1**](V1Api.md#options_get_historical_trades_v1) | **GET** /eapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**options_get_history_orders_v1**](V1Api.md#options_get_history_orders_v1) | **GET** /eapi/v1/historyOrders | Query Option Order History (TRADE)
[**options_get_income_asyn_id_v1**](V1Api.md#options_get_income_asyn_id_v1) | **GET** /eapi/v1/income/asyn/id | Get Option Transaction History Download Link by Id (USER_DATA)
[**options_get_income_asyn_v1**](V1Api.md#options_get_income_asyn_v1) | **GET** /eapi/v1/income/asyn | Get Download Id For Option Transaction History (USER_DATA)
[**options_get_index_v1**](V1Api.md#options_get_index_v1) | **GET** /eapi/v1/index | Symbol Price Ticker
[**options_get_klines_v1**](V1Api.md#options_get_klines_v1) | **GET** /eapi/v1/klines | Kline/Candlestick Data
[**options_get_margin_account_v1**](V1Api.md#options_get_margin_account_v1) | **GET** /eapi/v1/marginAccount | Option Margin Account Information (USER_DATA)
[**options_get_mark_v1**](V1Api.md#options_get_mark_v1) | **GET** /eapi/v1/mark | Option Mark Price
[**options_get_mmp_v1**](V1Api.md#options_get_mmp_v1) | **GET** /eapi/v1/mmp | Get Market Maker Protection Config (TRADE)
[**options_get_open_interest_v1**](V1Api.md#options_get_open_interest_v1) | **GET** /eapi/v1/openInterest | Open Interest
[**options_get_open_orders_v1**](V1Api.md#options_get_open_orders_v1) | **GET** /eapi/v1/openOrders | Query Current Open Option Orders (USER_DATA)
[**options_get_order_v1**](V1Api.md#options_get_order_v1) | **GET** /eapi/v1/order | Query Single Order (TRADE)
[**options_get_ping_v1**](V1Api.md#options_get_ping_v1) | **GET** /eapi/v1/ping | Test Connectivity
[**options_get_position_v1**](V1Api.md#options_get_position_v1) | **GET** /eapi/v1/position | Option Position Information (USER_DATA)
[**options_get_ticker_v1**](V1Api.md#options_get_ticker_v1) | **GET** /eapi/v1/ticker | 24hr Ticker Price Change Statistics
[**options_get_time_v1**](V1Api.md#options_get_time_v1) | **GET** /eapi/v1/time | Check Server Time
[**options_get_trades_v1**](V1Api.md#options_get_trades_v1) | **GET** /eapi/v1/trades | Recent Trades List
[**options_get_user_trades_v1**](V1Api.md#options_get_user_trades_v1) | **GET** /eapi/v1/userTrades | Account Trade List (USER_DATA)
[**options_update_block_order_create_v1**](V1Api.md#options_update_block_order_create_v1) | **PUT** /eapi/v1/block/order/create | Extend Block Trade Order (TRADE)
[**options_update_listen_key_v1**](V1Api.md#options_update_listen_key_v1) | **PUT** /eapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)


# **options_create_batch_orders_v1**
> List[OptionsCreateBatchOrdersV1RespInner] options_create_batch_orders_v1(orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Send multiple option orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_batch_orders_v1_req_orders_item import OptionsCreateBatchOrdersV1ReqOrdersItem
from binance.derivatives.options.models.options_create_batch_orders_v1_resp_inner import OptionsCreateBatchOrdersV1RespInner
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    orders = [binance.derivatives.options.OptionsCreateBatchOrdersV1ReqOrdersItem()] # List[OptionsCreateBatchOrdersV1ReqOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.options_create_batch_orders_v1(orders, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders** | [**List[OptionsCreateBatchOrdersV1ReqOrdersItem]**](OptionsCreateBatchOrdersV1ReqOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsCreateBatchOrdersV1RespInner]**](OptionsCreateBatchOrdersV1RespInner.md)

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

# **options_create_block_order_create_v1**
> OptionsCreateBlockOrderCreateV1Resp options_create_block_order_create_v1(legs, liquidity, price, quantity, side, symbol, timestamp, recv_window=recv_window)

New Block Trade Order (TRADE)

Send in a new block trade order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_block_order_create_v1_resp import OptionsCreateBlockOrderCreateV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    legs = ['legs_example'] # List[str] | 
    liquidity = '' # str |  (default to '')
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # New Block Trade Order (TRADE)
        api_response = api_instance.options_create_block_order_create_v1(legs, liquidity, price, quantity, side, symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_create_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legs** | [**List[str]**](str.md)|  | 
 **liquidity** | **str**|  | [default to &#39;&#39;]
 **price** | **str**|  | [default to &#39;&#39;]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateBlockOrderCreateV1Resp**](OptionsCreateBlockOrderCreateV1Resp.md)

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

# **options_create_block_order_execute_v1**
> OptionsCreateBlockOrderExecuteV1Resp options_create_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Accept Block Trade Order (TRADE)

Accept a block trade order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_block_order_execute_v1_resp import OptionsCreateBlockOrderExecuteV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept Block Trade Order (TRADE)
        api_response = api_instance.options_create_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_create_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_block_order_execute_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateBlockOrderExecuteV1Resp**](OptionsCreateBlockOrderExecuteV1Resp.md)

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

# **options_create_countdown_cancel_all_heart_beat_v1**
> OptionsCreateCountdownCancelAllHeartBeatV1Resp options_create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)

Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)

This endpoint resets the time from which the countdown will begin to the time this messaged is received.  It should be called repeatedly as heartbeats.  Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_countdown_cancel_all_heart_beat_v1_resp import OptionsCreateCountdownCancelAllHeartBeatV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    underlyings = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
        api_response = api_instance.options_create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)
        print("The response of V1Api->options_create_countdown_cancel_all_heart_beat_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_countdown_cancel_all_heart_beat_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlyings** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateCountdownCancelAllHeartBeatV1Resp**](OptionsCreateCountdownCancelAllHeartBeatV1Resp.md)

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

# **options_create_countdown_cancel_all_v1**
> OptionsCreateCountdownCancelAllV1Resp options_create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)

Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker protection and non market maker protection order types) of the underlying symbol at the end of the specified countdown time period if no heartbeat message is sent.  After the countdown time period, all open orders will be cancelled and new orders will be rejected with error code -2010 until either a heartbeat message is sent or the auto-cancel feature is turned off by setting countdownTime to 0.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_countdown_cancel_all_v1_resp import OptionsCreateCountdownCancelAllV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    countdown_time = 56 # int | 
    timestamp = 56 # int | 
    underlying = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.options_create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)
        print("The response of V1Api->options_create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **underlying** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateCountdownCancelAllV1Resp**](OptionsCreateCountdownCancelAllV1Resp.md)

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

# **options_create_listen_key_v1**
> OptionsCreateListenKeyV1Resp options_create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_listen_key_v1_resp import OptionsCreateListenKeyV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.options_create_listen_key_v1()
        print("The response of V1Api->options_create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsCreateListenKeyV1Resp**](OptionsCreateListenKeyV1Resp.md)

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

# **options_create_mmp_reset_v1**
> OptionsCreateMmpResetV1Resp options_create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)

Reset Market Maker Protection Config (TRADE)

Reset MMP, start MMP order again.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_mmp_reset_v1_resp import OptionsCreateMmpResetV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')

    try:
        # Reset Market Maker Protection Config (TRADE)
        api_response = api_instance.options_create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)
        print("The response of V1Api->options_create_mmp_reset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_mmp_reset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**OptionsCreateMmpResetV1Resp**](OptionsCreateMmpResetV1Resp.md)

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

# **options_create_mmp_set_v1**
> OptionsCreateMmpSetV1Resp options_create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)

Set Market Maker Protection Config (TRADE)

Set config for MMP.
Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_mmp_set_v1_resp import OptionsCreateMmpSetV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    delta_limit = '' # str |  (optional) (default to '')
    frozen_time_in_milliseconds = 56 # int |  (optional)
    qty_limit = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    window_time_in_milliseconds = 56 # int |  (optional)

    try:
        # Set Market Maker Protection Config (TRADE)
        api_response = api_instance.options_create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)
        print("The response of V1Api->options_create_mmp_set_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_mmp_set_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **delta_limit** | **str**|  | [optional] [default to &#39;&#39;]
 **frozen_time_in_milliseconds** | **int**|  | [optional] 
 **qty_limit** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]
 **window_time_in_milliseconds** | **int**|  | [optional] 

### Return type

[**OptionsCreateMmpSetV1Resp**](OptionsCreateMmpSetV1Resp.md)

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

# **options_create_order_v1**
> OptionsCreateOrderV1Resp options_create_order_v1(quantity, side, symbol, timestamp, type, client_order_id=client_order_id, is_mmp=is_mmp, new_order_resp_type=new_order_resp_type, post_only=post_only, price=price, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)

New Order (TRADE)

Send a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_order_v1_resp import OptionsCreateOrderV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    client_order_id = '' # str |  (optional) (default to '')
    is_mmp = True # bool |  (optional)
    new_order_resp_type = '' # str |  (optional) (default to '')
    post_only = False # bool |  (optional) (default to False)
    price = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = False # bool |  (optional) (default to False)
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # New Order (TRADE)
        api_response = api_instance.options_create_order_v1(quantity, side, symbol, timestamp, type, client_order_id=client_order_id, is_mmp=is_mmp, new_order_resp_type=new_order_resp_type, post_only=post_only, price=price, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)
        print("The response of V1Api->options_create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_create_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **is_mmp** | **bool**|  | [optional] 
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **post_only** | **bool**|  | [optional] [default to False]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **bool**|  | [optional] [default to False]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**OptionsCreateOrderV1Resp**](OptionsCreateOrderV1Resp.md)

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

# **options_delete_all_open_orders_by_underlying_v1**
> OptionsDeleteAllOpenOrdersByUnderlyingV1Resp options_delete_all_open_orders_by_underlying_v1(underlying, timestamp, recv_window=recv_window)

Cancel All Option Orders By Underlying (TRADE)

Cancel all active orders on specified underlying.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_delete_all_open_orders_by_underlying_v1_resp import OptionsDeleteAllOpenOrdersByUnderlyingV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    underlying = '' # str | Option underlying, e.g BTCUSDT (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Option Orders By Underlying (TRADE)
        api_response = api_instance.options_delete_all_open_orders_by_underlying_v1(underlying, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_delete_all_open_orders_by_underlying_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_all_open_orders_by_underlying_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying, e.g BTCUSDT | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsDeleteAllOpenOrdersByUnderlyingV1Resp**](OptionsDeleteAllOpenOrdersByUnderlyingV1Resp.md)

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

# **options_delete_all_open_orders_v1**
> OptionsDeleteAllOpenOrdersV1Resp options_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel all Option orders on specific symbol (TRADE)

Cancel all active order on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_delete_all_open_orders_v1_resp import OptionsDeleteAllOpenOrdersV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel all Option orders on specific symbol (TRADE)
        api_response = api_instance.options_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsDeleteAllOpenOrdersV1Resp**](OptionsDeleteAllOpenOrdersV1Resp.md)

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

# **options_delete_batch_orders_v1**
> List[OptionsDeleteBatchOrdersV1RespInner] options_delete_batch_orders_v1(symbol, timestamp, order_ids=order_ids, client_order_ids=client_order_ids, recv_window=recv_window)

Cancel Multiple Option Orders (TRADE)

Cancel multiple orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_delete_batch_orders_v1_resp_inner import OptionsDeleteBatchOrdersV1RespInner
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_ids = [56] # List[int] | Order ID, e.g [4611875134427365377,4611875134427365378] (optional)
    client_order_ids = ['client_order_ids_example'] # List[str] | User-defined order ID, e.g [&#34;my_id_1&#34;,&#34;my_id_2&#34;] (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Option Orders (TRADE)
        api_response = api_instance.options_delete_batch_orders_v1(symbol, timestamp, order_ids=order_ids, client_order_ids=client_order_ids, recv_window=recv_window)
        print("The response of V1Api->options_delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_ids** | [**List[int]**](int.md)| Order ID, e.g [4611875134427365377,4611875134427365378] | [optional] 
 **client_order_ids** | [**List[str]**](str.md)| User-defined order ID, e.g [&amp;#34;my_id_1&amp;#34;,&amp;#34;my_id_2&amp;#34;] | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsDeleteBatchOrdersV1RespInner]**](OptionsDeleteBatchOrdersV1RespInner.md)

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

# **options_delete_block_order_create_v1**
> object options_delete_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Cancel Block Trade Order (TRADE)

Cancel a block trade order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Block Trade Order (TRADE)
        api_response = api_instance.options_delete_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_delete_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

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

# **options_delete_listen_key_v1**
> object options_delete_listen_key_v1()

Close User Data Stream (USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.options_delete_listen_key_v1()
        print("The response of V1Api->options_delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_listen_key_v1: %s\n" % e)
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

# **options_delete_order_v1**
> OptionsDeleteOrderV1Resp options_delete_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)

Cancel Option Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_delete_order_v1_resp import OptionsDeleteOrderV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order ID, e.g 4611875134427365377 (optional)
    client_order_id = '' # str | User-defined order ID, e.g 10000 (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Option Order (TRADE)
        api_response = api_instance.options_delete_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of V1Api->options_delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_delete_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| Order ID, e.g 4611875134427365377 | [optional] 
 **client_order_id** | **str**| User-defined order ID, e.g 10000 | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsDeleteOrderV1Resp**](OptionsDeleteOrderV1Resp.md)

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

# **options_get_account_v1**
> OptionsGetAccountV1Resp options_get_account_v1(timestamp, recv_window=recv_window)

Option Account Information(TRADE)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_account_v1_resp import OptionsGetAccountV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Account Information(TRADE)
        api_response = api_instance.options_get_account_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->options_get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetAccountV1Resp**](OptionsGetAccountV1Resp.md)

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

# **options_get_bill_v1**
> List[OptionsGetBillV1RespItem] options_get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Account Funding Flow (USER_DATA)

Query account funding flows.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_bill_v1_resp_item import OptionsGetBillV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    currency = '' # str | Asset type, only support USDT  as of now (default to '')
    timestamp = 56 # int | 
    record_id = 56 # int | Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 (optional)
    start_time = 56 # int | Start Time, e.g 1593511200000 (optional)
    end_time = 56 # int | End Time, e.g 1593512200000 (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Account Funding Flow (USER_DATA)
        api_response = api_instance.options_get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->options_get_bill_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_bill_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Asset type, only support USDT  as of now | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **record_id** | **int**| Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 | [optional] 
 **start_time** | **int**| Start Time, e.g 1593511200000 | [optional] 
 **end_time** | **int**| End Time, e.g 1593512200000 | [optional] 
 **limit** | **int**| Number of result sets returned Default:100 Max:1000 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetBillV1RespItem]**](OptionsGetBillV1RespItem.md)

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

# **options_get_block_order_execute_v1**
> OptionsGetBlockOrderExecuteV1Resp options_get_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Query Block Trade Details (USER_DATA)

Query block trade details; returns block trade details from counterparty's perspective.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_block_order_execute_v1_resp import OptionsGetBlockOrderExecuteV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Details (USER_DATA)
        api_response = api_instance.options_get_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_get_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_block_order_execute_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**OptionsGetBlockOrderExecuteV1Resp**](OptionsGetBlockOrderExecuteV1Resp.md)

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

# **options_get_block_order_orders_v1**
> List[OptionsGetBlockOrderOrdersV1RespItem] options_get_block_order_orders_v1(timestamp, block_order_matching_key=block_order_matching_key, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)

Query Block Trade Order (TRADE)

Check block trade order status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_block_order_orders_v1_resp_item import OptionsGetBlockOrderOrdersV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    block_order_matching_key = '' # str | If specified, returns the specific block trade associated with the blockOrderMatchingKey (optional) (default to '')
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Order (TRADE)
        api_response = api_instance.options_get_block_order_orders_v1(timestamp, block_order_matching_key=block_order_matching_key, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of V1Api->options_get_block_order_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_block_order_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **block_order_matching_key** | **str**| If specified, returns the specific block trade associated with the blockOrderMatchingKey | [optional] [default to &#39;&#39;]
 **end_time** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[OptionsGetBlockOrderOrdersV1RespItem]**](OptionsGetBlockOrderOrdersV1RespItem.md)

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

# **options_get_block_trades_v1**
> List[OptionsGetBlockTradesV1RespItem] options_get_block_trades_v1(symbol=symbol, limit=limit)

Recent Block Trades List

Get recent block trades

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_block_trades_v1_resp_item import OptionsGetBlockTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g. BTC-200730-9000-C (optional) (default to '')
    limit = 100 # int | Number of records; Default: 100 and Max: 500 (optional) (default to 100)

    try:
        # Recent Block Trades List
        api_response = api_instance.options_get_block_trades_v1(symbol=symbol, limit=limit)
        print("The response of V1Api->options_get_block_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_block_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g. BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **limit** | **int**| Number of records; Default: 100 and Max: 500 | [optional] [default to 100]

### Return type

[**List[OptionsGetBlockTradesV1RespItem]**](OptionsGetBlockTradesV1RespItem.md)

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

# **options_get_block_user_trades_v1**
> List[OptionsGetBlockUserTradesV1RespItem] options_get_block_user_trades_v1(timestamp, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)

Account Block Trade List (USER_DATA)

Gets block trades for a specific account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_block_user_trades_v1_resp_item import OptionsGetBlockUserTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Account Block Trade List (USER_DATA)
        api_response = api_instance.options_get_block_user_trades_v1(timestamp, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of V1Api->options_get_block_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_block_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **end_time** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[OptionsGetBlockUserTradesV1RespItem]**](OptionsGetBlockUserTradesV1RespItem.md)

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

# **options_get_countdown_cancel_all_v1**
> OptionsGetCountdownCancelAllV1Resp options_get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_countdown_cancel_all_v1_resp import OptionsGetCountdownCancelAllV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | Option underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.options_get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of V1Api->options_get_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| Option underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetCountdownCancelAllV1Resp**](OptionsGetCountdownCancelAllV1Resp.md)

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

# **options_get_depth_v1**
> OptionsGetDepthV1Resp options_get_depth_v1(symbol, limit=limit)

Order Book

Check orderbook depth on specific symbol

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_depth_v1_resp import OptionsGetDepthV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] (optional)

    try:
        # Order Book
        api_response = api_instance.options_get_depth_v1(symbol, limit=limit)
        print("The response of V1Api->options_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] | [optional] 

### Return type

[**OptionsGetDepthV1Resp**](OptionsGetDepthV1Resp.md)

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

# **options_get_exchange_info_v1**
> OptionsGetExchangeInfoV1Resp options_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_exchange_info_v1_resp import OptionsGetExchangeInfoV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Exchange Information
        api_response = api_instance.options_get_exchange_info_v1()
        print("The response of V1Api->options_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetExchangeInfoV1Resp**](OptionsGetExchangeInfoV1Resp.md)

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

# **options_get_exercise_history_v1**
> List[OptionsGetExerciseHistoryV1RespItem] options_get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)

Historical Exercise Records

Get historical exercise records.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_exercise_history_v1_resp_item import OptionsGetExerciseHistoryV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    underlying = '' # str | Underlying index like BTCUSDT (optional) (default to '')
    start_time = 56 # int | Start Time (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:100 Max:100 (optional)

    try:
        # Historical Exercise Records
        api_response = api_instance.options_get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->options_get_exercise_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_exercise_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying index like BTCUSDT | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Start Time | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of records Default:100 Max:100 | [optional] 

### Return type

[**List[OptionsGetExerciseHistoryV1RespItem]**](OptionsGetExerciseHistoryV1RespItem.md)

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

# **options_get_exercise_record_v1**
> List[OptionsGetExerciseRecordV1RespItem] options_get_exercise_record_v1(timestamp, symbol=symbol, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

User Exercise Record (USER_DATA)

Get account exercise records.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_exercise_record_v1_resp_item import OptionsGetExerciseRecordV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    start_time = 56 # int | startTime (optional)
    end_time = 56 # int | endTime (optional)
    limit = 1000 # int | default 1000, max 1000 (optional) (default to 1000)
    recv_window = 56 # int |  (optional)

    try:
        # User Exercise Record (USER_DATA)
        api_response = api_instance.options_get_exercise_record_v1(timestamp, symbol=symbol, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->options_get_exercise_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_exercise_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **limit** | **int**| default 1000, max 1000 | [optional] [default to 1000]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetExerciseRecordV1RespItem]**](OptionsGetExerciseRecordV1RespItem.md)

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

# **options_get_historical_trades_v1**
> List[OptionsGetHistoricalTradesV1RespItem] options_get_historical_trades_v1(symbol, from_id=from_id, limit=limit)

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_historical_trades_v1_resp_item import OptionsGetHistoricalTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    from_id = 56 # int | The UniqueId ID from which to return. The latest deal record is returned by default (optional)
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.options_get_historical_trades_v1(symbol, from_id=from_id, limit=limit)
        print("The response of V1Api->options_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **from_id** | **int**| The UniqueId ID from which to return. The latest deal record is returned by default | [optional] 
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[OptionsGetHistoricalTradesV1RespItem]**](OptionsGetHistoricalTradesV1RespItem.md)

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

# **options_get_history_orders_v1**
> List[OptionsGetHistoryOrdersV1RespItem] options_get_history_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Option Order History (TRADE)

Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_history_orders_v1_resp_item import OptionsGetHistoryOrdersV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Returns the orderId and subsequent orders, the most recent order is returned by default (optional)
    start_time = 56 # int | Start Time, e.g 1593511200000 (optional)
    end_time = 56 # int | End Time, e.g 1593512200000 (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Option Order History (TRADE)
        api_response = api_instance.options_get_history_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->options_get_history_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_history_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| Returns the orderId and subsequent orders, the most recent order is returned by default | [optional] 
 **start_time** | **int**| Start Time, e.g 1593511200000 | [optional] 
 **end_time** | **int**| End Time, e.g 1593512200000 | [optional] 
 **limit** | **int**| Number of result sets returned Default:100 Max:1000 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetHistoryOrdersV1RespItem]**](OptionsGetHistoryOrdersV1RespItem.md)

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

# **options_get_income_asyn_id_v1**
> OptionsGetIncomeAsynIdV1Resp options_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Option Transaction History Download Link by Id (USER_DATA)

Get option transaction history download Link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_income_asyn_id_v1_resp import OptionsGetIncomeAsynIdV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Option Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.options_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetIncomeAsynIdV1Resp**](OptionsGetIncomeAsynIdV1Resp.md)

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

# **options_get_income_asyn_v1**
> OptionsGetIncomeAsynV1Resp options_get_income_asyn_v1()

Get Download Id For Option Transaction History (USER_DATA)

Get download id for option transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_income_asyn_v1_resp import OptionsGetIncomeAsynV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Get Download Id For Option Transaction History (USER_DATA)
        api_response = api_instance.options_get_income_asyn_v1()
        print("The response of V1Api->options_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_income_asyn_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetIncomeAsynV1Resp**](OptionsGetIncomeAsynV1Resp.md)

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

# **options_get_index_v1**
> OptionsGetIndexV1Resp options_get_index_v1(underlying)

Symbol Price Ticker

Get spot index price for option underlying.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_index_v1_resp import OptionsGetIndexV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    underlying = '' # str | Spot pair（Option contract underlying asset, e.g BTCUSDT) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.options_get_index_v1(underlying)
        print("The response of V1Api->options_get_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Spot pair（Option contract underlying asset, e.g BTCUSDT) | [default to &#39;&#39;]

### Return type

[**OptionsGetIndexV1Resp**](OptionsGetIndexV1Resp.md)

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

# **options_get_klines_v1**
> List[OptionsGetKlinesV1RespItem] options_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for an option symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_klines_v1_resp_item import OptionsGetKlinesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    interval = '' # str | Time interval (default to '')
    start_time = 56 # int | Start Time  1592317127349 (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:500 Max:1500 (optional)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.options_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of V1Api->options_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **interval** | **str**| Time interval | [default to &#39;&#39;]
 **start_time** | **int**| Start Time  1592317127349 | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of records Default:500 Max:1500 | [optional] 

### Return type

[**List[OptionsGetKlinesV1RespItem]**](OptionsGetKlinesV1RespItem.md)

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

# **options_get_margin_account_v1**
> OptionsGetMarginAccountV1Resp options_get_margin_account_v1(timestamp, recv_window=recv_window)

Option Margin Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_margin_account_v1_resp import OptionsGetMarginAccountV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Margin Account Information (USER_DATA)
        api_response = api_instance.options_get_margin_account_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->options_get_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetMarginAccountV1Resp**](OptionsGetMarginAccountV1Resp.md)

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

# **options_get_mark_v1**
> List[OptionsGetMarkV1RespItem] options_get_mark_v1(symbol=symbol)

Option Mark Price

Option mark price and greek info.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_mark_v1_resp_item import OptionsGetMarkV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # Option Mark Price
        api_response = api_instance.options_get_mark_v1(symbol=symbol)
        print("The response of V1Api->options_get_mark_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_mark_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[OptionsGetMarkV1RespItem]**](OptionsGetMarkV1RespItem.md)

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

# **options_get_mmp_v1**
> OptionsGetMmpV1Resp options_get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Market Maker Protection Config (TRADE)

Get config for MMP.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_mmp_v1_resp import OptionsGetMmpV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Market Maker Protection Config (TRADE)
        api_response = api_instance.options_get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of V1Api->options_get_mmp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_mmp_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetMmpV1Resp**](OptionsGetMmpV1Resp.md)

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

# **options_get_open_interest_v1**
> List[OptionsGetOpenInterestV1RespItem] options_get_open_interest_v1(underlying_asset, expiration)

Open Interest

Get open interest for specific underlying asset on specific expiration date.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_open_interest_v1_resp_item import OptionsGetOpenInterestV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    underlying_asset = '' # str | underlying asset, e.g ETH/BTC (default to '')
    expiration = '' # str | expiration date, e.g 221225 (default to '')

    try:
        # Open Interest
        api_response = api_instance.options_get_open_interest_v1(underlying_asset, expiration)
        print("The response of V1Api->options_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying_asset** | **str**| underlying asset, e.g ETH/BTC | [default to &#39;&#39;]
 **expiration** | **str**| expiration date, e.g 221225 | [default to &#39;&#39;]

### Return type

[**List[OptionsGetOpenInterestV1RespItem]**](OptionsGetOpenInterestV1RespItem.md)

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

# **options_get_open_orders_v1**
> List[OptionsGetOpenOrdersV1RespItem] options_get_open_orders_v1(timestamp, symbol=symbol, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Current Open Option Orders (USER_DATA)

Query current all open orders, status: ACCEPTED PARTIALLY_FILLED

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_open_orders_v1_resp_item import OptionsGetOpenOrdersV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | return all orders if don&#39;t pass, Option trading pair, e.g BTC-200730-9000-C, (optional) (default to '')
    order_id = 56 # int | Returns the orderId and subsequent orders, the most recent order is returned by default (optional)
    start_time = 56 # int | Start Time (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Option Orders (USER_DATA)
        api_response = api_instance.options_get_open_orders_v1(timestamp, symbol=symbol, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->options_get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| return all orders if don&amp;#39;t pass, Option trading pair, e.g BTC-200730-9000-C, | [optional] [default to &#39;&#39;]
 **order_id** | **int**| Returns the orderId and subsequent orders, the most recent order is returned by default | [optional] 
 **start_time** | **int**| Start Time | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of result sets returned Default:100 Max:1000 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetOpenOrdersV1RespItem]**](OptionsGetOpenOrdersV1RespItem.md)

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

# **options_get_order_v1**
> OptionsGetOrderV1Resp options_get_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)

Query Single Order (TRADE)

Check an order status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_order_v1_resp import OptionsGetOrderV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order id (optional)
    client_order_id = '' # str | User-defined order ID cannot be repeated in pending orders (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Single Order (TRADE)
        api_response = api_instance.options_get_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of V1Api->options_get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| Order id | [optional] 
 **client_order_id** | **str**| User-defined order ID cannot be repeated in pending orders | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetOrderV1Resp**](OptionsGetOrderV1Resp.md)

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

# **options_get_ping_v1**
> object options_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.options_get_ping_v1()
        print("The response of V1Api->options_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_ping_v1: %s\n" % e)
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

# **options_get_position_v1**
> List[OptionsGetPositionV1RespItem] options_get_position_v1(timestamp, symbol=symbol, recv_window=recv_window)

Option Position Information (USER_DATA)

Get current position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_position_v1_resp_item import OptionsGetPositionV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Option Position Information (USER_DATA)
        api_response = api_instance.options_get_position_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->options_get_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetPositionV1RespItem]**](OptionsGetPositionV1RespItem.md)

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

# **options_get_ticker_v1**
> List[OptionsGetTickerV1RespItem] options_get_ticker_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_ticker_v1_resp_item import OptionsGetTickerV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.options_get_ticker_v1(symbol=symbol)
        print("The response of V1Api->options_get_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[OptionsGetTickerV1RespItem]**](OptionsGetTickerV1RespItem.md)

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

# **options_get_time_v1**
> OptionsGetTimeV1Resp options_get_time_v1()

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_time_v1_resp import OptionsGetTimeV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Check Server Time
        api_response = api_instance.options_get_time_v1()
        print("The response of V1Api->options_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetTimeV1Resp**](OptionsGetTimeV1Resp.md)

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

# **options_get_trades_v1**
> List[OptionsGetTradesV1RespItem] options_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_trades_v1_resp_item import OptionsGetTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Recent Trades List
        api_response = api_instance.options_get_trades_v1(symbol, limit=limit)
        print("The response of V1Api->options_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[OptionsGetTradesV1RespItem]**](OptionsGetTradesV1RespItem.md)

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

# **options_get_user_trades_v1**
> List[OptionsGetUserTradesV1RespItem] options_get_user_trades_v1(timestamp, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_user_trades_v1_resp_item import OptionsGetUserTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option symbol, e.g BTC-200730-9000-C (optional) (default to '')
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376 (optional)
    start_time = 56 # int | Start time, e.g 1593511200000 (optional)
    end_time = 56 # int | End time, e.g 1593512200000 (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.options_get_user_trades_v1(timestamp, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->options_get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_get_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| Option symbol, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376 | [optional] 
 **start_time** | **int**| Start time, e.g 1593511200000 | [optional] 
 **end_time** | **int**| End time, e.g 1593512200000 | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetUserTradesV1RespItem]**](OptionsGetUserTradesV1RespItem.md)

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

# **options_update_block_order_create_v1**
> OptionsUpdateBlockOrderCreateV1Resp options_update_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Extend Block Trade Order (TRADE)

Extends a block trade expire time by 30 mins from the current time.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_update_block_order_create_v1_resp import OptionsUpdateBlockOrderCreateV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Extend Block Trade Order (TRADE)
        api_response = api_instance.options_update_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of V1Api->options_update_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_update_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsUpdateBlockOrderCreateV1Resp**](OptionsUpdateBlockOrderCreateV1Resp.md)

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

# **options_update_listen_key_v1**
> object options_update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.V1Api(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.options_update_listen_key_v1()
        print("The response of V1Api->options_update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->options_update_listen_key_v1: %s\n" % e)
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

