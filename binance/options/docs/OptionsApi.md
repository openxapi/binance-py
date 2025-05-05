# binance.options.OptionsApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_orders_v1**](OptionsApi.md#create_batch_orders_v1) | **POST** /eapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**create_block_order_execute_v1**](OptionsApi.md#create_block_order_execute_v1) | **POST** /eapi/v1/block/order/execute | Accept Block Trade Order (TRADE)
[**create_countdown_cancel_all_heart_beat_v1**](OptionsApi.md#create_countdown_cancel_all_heart_beat_v1) | **POST** /eapi/v1/countdownCancelAllHeartBeat | Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
[**create_countdown_cancel_all_v1**](OptionsApi.md#create_countdown_cancel_all_v1) | **POST** /eapi/v1/countdownCancelAll | Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**create_listen_key_v1**](OptionsApi.md#create_listen_key_v1) | **POST** /eapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**create_mmp_reset_v1**](OptionsApi.md#create_mmp_reset_v1) | **POST** /eapi/v1/mmpReset | Reset Market Maker Protection Config (TRADE)
[**create_mmp_set_v1**](OptionsApi.md#create_mmp_set_v1) | **POST** /eapi/v1/mmpSet | Set Market Maker Protection Config (TRADE)
[**create_order_v1**](OptionsApi.md#create_order_v1) | **POST** /eapi/v1/order | New Order (TRADE)
[**delete_all_open_orders_by_underlying_v1**](OptionsApi.md#delete_all_open_orders_by_underlying_v1) | **DELETE** /eapi/v1/allOpenOrdersByUnderlying | Cancel All Option Orders By Underlying (TRADE)
[**delete_all_open_orders_v1**](OptionsApi.md#delete_all_open_orders_v1) | **DELETE** /eapi/v1/allOpenOrders | Cancel all Option orders on specific symbol (TRADE)
[**delete_batch_orders_v1**](OptionsApi.md#delete_batch_orders_v1) | **DELETE** /eapi/v1/batchOrders | Cancel Multiple Option Orders (TRADE)
[**delete_listen_key_v1**](OptionsApi.md#delete_listen_key_v1) | **DELETE** /eapi/v1/listenKey | Close User Data Stream (USER_STREAM)
[**delete_order_v1**](OptionsApi.md#delete_order_v1) | **DELETE** /eapi/v1/order | Cancel Option Order (TRADE)
[**get_account_v1**](OptionsApi.md#get_account_v1) | **GET** /eapi/v1/account | Option Account Information(TRADE)
[**get_bill_v1**](OptionsApi.md#get_bill_v1) | **GET** /eapi/v1/bill | Account Funding Flow (USER_DATA)
[**get_block_order_execute_v1**](OptionsApi.md#get_block_order_execute_v1) | **GET** /eapi/v1/block/order/execute | Query Block Trade Details (USER_DATA)
[**get_block_order_orders_v1**](OptionsApi.md#get_block_order_orders_v1) | **GET** /eapi/v1/block/order/orders | Query Block Trade Order (TRADE)
[**get_block_trades_v1**](OptionsApi.md#get_block_trades_v1) | **GET** /eapi/v1/blockTrades | Recent Block Trades List
[**get_block_user_trades_v1**](OptionsApi.md#get_block_user_trades_v1) | **GET** /eapi/v1/block/user-trades | Account Block Trade List (USER_DATA)
[**get_countdown_cancel_all_v1**](OptionsApi.md#get_countdown_cancel_all_v1) | **GET** /eapi/v1/countdownCancelAll | Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**get_depth_v1**](OptionsApi.md#get_depth_v1) | **GET** /eapi/v1/depth | Order Book
[**get_exchange_info_v1**](OptionsApi.md#get_exchange_info_v1) | **GET** /eapi/v1/exchangeInfo | Exchange Information
[**get_exercise_history_v1**](OptionsApi.md#get_exercise_history_v1) | **GET** /eapi/v1/exerciseHistory | Historical Exercise Records
[**get_exercise_record_v1**](OptionsApi.md#get_exercise_record_v1) | **GET** /eapi/v1/exerciseRecord | User Exercise Record (USER_DATA)
[**get_historical_trades_v1**](OptionsApi.md#get_historical_trades_v1) | **GET** /eapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**get_history_orders_v1**](OptionsApi.md#get_history_orders_v1) | **GET** /eapi/v1/historyOrders | Query Option Order History (TRADE)
[**get_income_asyn_id_v1**](OptionsApi.md#get_income_asyn_id_v1) | **GET** /eapi/v1/income/asyn/id | Get Option Transaction History Download Link by Id (USER_DATA)
[**get_income_asyn_v1**](OptionsApi.md#get_income_asyn_v1) | **GET** /eapi/v1/income/asyn | Get Download Id For Option Transaction History (USER_DATA)
[**get_index_v1**](OptionsApi.md#get_index_v1) | **GET** /eapi/v1/index | Symbol Price Ticker
[**get_klines_v1**](OptionsApi.md#get_klines_v1) | **GET** /eapi/v1/klines | Kline/Candlestick Data
[**get_margin_account_v1**](OptionsApi.md#get_margin_account_v1) | **GET** /eapi/v1/marginAccount | Option Margin Account Information (USER_DATA)
[**get_mark_v1**](OptionsApi.md#get_mark_v1) | **GET** /eapi/v1/mark | Option Mark Price
[**get_mmp_v1**](OptionsApi.md#get_mmp_v1) | **GET** /eapi/v1/mmp | Get Market Maker Protection Config (TRADE)
[**get_open_interest_v1**](OptionsApi.md#get_open_interest_v1) | **GET** /eapi/v1/openInterest | Open Interest
[**get_open_orders_v1**](OptionsApi.md#get_open_orders_v1) | **GET** /eapi/v1/openOrders | Query Current Open Option Orders (USER_DATA)
[**get_order_v1**](OptionsApi.md#get_order_v1) | **GET** /eapi/v1/order | Query Single Order (TRADE)
[**get_ping_v1**](OptionsApi.md#get_ping_v1) | **GET** /eapi/v1/ping | Test Connectivity
[**get_position_v1**](OptionsApi.md#get_position_v1) | **GET** /eapi/v1/position | Option Position Information (USER_DATA)
[**get_ticker_v1**](OptionsApi.md#get_ticker_v1) | **GET** /eapi/v1/ticker | 24hr Ticker Price Change Statistics
[**get_time_v1**](OptionsApi.md#get_time_v1) | **GET** /eapi/v1/time | Check Server Time
[**get_trades_v1**](OptionsApi.md#get_trades_v1) | **GET** /eapi/v1/trades | Recent Trades List
[**get_user_trades_v1**](OptionsApi.md#get_user_trades_v1) | **GET** /eapi/v1/userTrades | Account Trade List (USER_DATA)
[**update_block_order_create_v1**](OptionsApi.md#update_block_order_create_v1) | **PUT** /eapi/v1/block/order/create | Extend Block Trade Order (TRADE)
[**update_listen_key_v1**](OptionsApi.md#update_listen_key_v1) | **PUT** /eapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)


# **create_batch_orders_v1**
> List[OptionsCreateBatchOrdersV1RespInner] create_batch_orders_v1(orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Send multiple option orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.options_create_batch_orders_v1_req_orders_item import OptionsCreateBatchOrdersV1ReqOrdersItem
from binance.options.models.options_create_batch_orders_v1_resp_inner import OptionsCreateBatchOrdersV1RespInner
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    orders = [binance.options.OptionsCreateBatchOrdersV1ReqOrdersItem()] # List[OptionsCreateBatchOrdersV1ReqOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.create_batch_orders_v1(orders, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_batch_orders_v1: %s\n" % e)
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

# **create_block_order_execute_v1**
> CreateBlockOrderExecuteV1Resp create_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Accept Block Trade Order (TRADE)

Accept a block trade order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_block_order_execute_v1_resp import CreateBlockOrderExecuteV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept Block Trade Order (TRADE)
        api_response = api_instance.create_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->create_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_block_order_execute_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBlockOrderExecuteV1Resp**](CreateBlockOrderExecuteV1Resp.md)

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

# **create_countdown_cancel_all_heart_beat_v1**
> CreateCountdownCancelAllHeartBeatV1Resp create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)

Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)

This endpoint resets the time from which the countdown will begin to the time this messaged is received.  It should be called repeatedly as heartbeats.  Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_countdown_cancel_all_heart_beat_v1_resp import CreateCountdownCancelAllHeartBeatV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    underlyings = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
        api_response = api_instance.create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)
        print("The response of OptionsApi->create_countdown_cancel_all_heart_beat_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_countdown_cancel_all_heart_beat_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlyings** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateCountdownCancelAllHeartBeatV1Resp**](CreateCountdownCancelAllHeartBeatV1Resp.md)

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

# **create_countdown_cancel_all_v1**
> CreateCountdownCancelAllV1Resp create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)

Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker protection and non market maker protection order types) of the underlying symbol at the end of the specified countdown time period if no heartbeat message is sent.  After the countdown time period, all open orders will be cancelled and new orders will be rejected with error code -2010 until either a heartbeat message is sent or the auto-cancel feature is turned off by setting countdownTime to 0.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_countdown_cancel_all_v1_resp import CreateCountdownCancelAllV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    countdown_time = 56 # int | 
    timestamp = 56 # int | 
    underlying = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)
        print("The response of OptionsApi->create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **underlying** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateCountdownCancelAllV1Resp**](CreateCountdownCancelAllV1Resp.md)

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

# **create_listen_key_v1**
> CreateListenKeyV1Resp create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_listen_key_v1_resp import CreateListenKeyV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.create_listen_key_v1()
        print("The response of OptionsApi->create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateListenKeyV1Resp**](CreateListenKeyV1Resp.md)

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

# **create_mmp_reset_v1**
> CreateMmpResetV1Resp create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)

Reset Market Maker Protection Config (TRADE)

Reset MMP, start MMP order again.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_mmp_reset_v1_resp import CreateMmpResetV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')

    try:
        # Reset Market Maker Protection Config (TRADE)
        api_response = api_instance.create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)
        print("The response of OptionsApi->create_mmp_reset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_mmp_reset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMmpResetV1Resp**](CreateMmpResetV1Resp.md)

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

# **create_mmp_set_v1**
> CreateMmpSetV1Resp create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)

Set Market Maker Protection Config (TRADE)

Set config for MMP.
Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.create_mmp_set_v1_resp import CreateMmpSetV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    delta_limit = '' # str |  (optional) (default to '')
    frozen_time_in_milliseconds = 56 # int |  (optional)
    qty_limit = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    window_time_in_milliseconds = 56 # int |  (optional)

    try:
        # Set Market Maker Protection Config (TRADE)
        api_response = api_instance.create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)
        print("The response of OptionsApi->create_mmp_set_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_mmp_set_v1: %s\n" % e)
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

[**CreateMmpSetV1Resp**](CreateMmpSetV1Resp.md)

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

# **create_order_v1**
> OptionsCreateOrderV1Resp create_order_v1(quantity, side, symbol, timestamp, type, client_order_id=client_order_id, is_mmp=is_mmp, new_order_resp_type=new_order_resp_type, post_only=post_only, price=price, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)

New Order (TRADE)

Send a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.options_create_order_v1_resp import OptionsCreateOrderV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
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
        api_response = api_instance.create_order_v1(quantity, side, symbol, timestamp, type, client_order_id=client_order_id, is_mmp=is_mmp, new_order_resp_type=new_order_resp_type, post_only=post_only, price=price, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)
        print("The response of OptionsApi->create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_order_v1: %s\n" % e)
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

# **delete_all_open_orders_by_underlying_v1**
> DeleteAllOpenOrdersByUnderlyingV1Resp delete_all_open_orders_by_underlying_v1(underlying, timestamp, recv_window=recv_window)

Cancel All Option Orders By Underlying (TRADE)

Cancel all active orders on specified underlying.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.delete_all_open_orders_by_underlying_v1_resp import DeleteAllOpenOrdersByUnderlyingV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    underlying = '' # str | Option underlying, e.g BTCUSDT (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Option Orders By Underlying (TRADE)
        api_response = api_instance.delete_all_open_orders_by_underlying_v1(underlying, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->delete_all_open_orders_by_underlying_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_all_open_orders_by_underlying_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying, e.g BTCUSDT | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteAllOpenOrdersByUnderlyingV1Resp**](DeleteAllOpenOrdersByUnderlyingV1Resp.md)

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

# **delete_all_open_orders_v1**
> DeleteAllOpenOrdersV1Resp delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel all Option orders on specific symbol (TRADE)

Cancel all active order on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.delete_all_open_orders_v1_resp import DeleteAllOpenOrdersV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel all Option orders on specific symbol (TRADE)
        api_response = api_instance.delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteAllOpenOrdersV1Resp**](DeleteAllOpenOrdersV1Resp.md)

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

# **delete_batch_orders_v1**
> List[OptionsDeleteBatchOrdersV1RespInner] delete_batch_orders_v1(symbol, timestamp, order_ids=order_ids, client_order_ids=client_order_ids, recv_window=recv_window)

Cancel Multiple Option Orders (TRADE)

Cancel multiple orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.options_delete_batch_orders_v1_resp_inner import OptionsDeleteBatchOrdersV1RespInner
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_ids = [56] # List[int] | Order ID, e.g [4611875134427365377,4611875134427365378] (optional)
    client_order_ids = ['client_order_ids_example'] # List[str] | User-defined order ID, e.g [&#34;my_id_1&#34;,&#34;my_id_2&#34;] (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Option Orders (TRADE)
        api_response = api_instance.delete_batch_orders_v1(symbol, timestamp, order_ids=order_ids, client_order_ids=client_order_ids, recv_window=recv_window)
        print("The response of OptionsApi->delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_batch_orders_v1: %s\n" % e)
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

# **delete_listen_key_v1**
> object delete_listen_key_v1()

Close User Data Stream (USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.delete_listen_key_v1()
        print("The response of OptionsApi->delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_listen_key_v1: %s\n" % e)
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

# **delete_order_v1**
> DeleteOrderV1Resp delete_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)

Cancel Option Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.delete_order_v1_resp import DeleteOrderV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order ID, e.g 4611875134427365377 (optional)
    client_order_id = '' # str | User-defined order ID, e.g 10000 (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Option Order (TRADE)
        api_response = api_instance.delete_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of OptionsApi->delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_order_v1: %s\n" % e)
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

[**DeleteOrderV1Resp**](DeleteOrderV1Resp.md)

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

# **get_account_v1**
> GetAccountV1Resp get_account_v1(timestamp, recv_window=recv_window)

Option Account Information(TRADE)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_account_v1_resp import GetAccountV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Account Information(TRADE)
        api_response = api_instance.get_account_v1(timestamp, recv_window=recv_window)
        print("The response of OptionsApi->get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAccountV1Resp**](GetAccountV1Resp.md)

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

# **get_bill_v1**
> List[GetBillV1RespItem] get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Account Funding Flow (USER_DATA)

Query account funding flows.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_bill_v1_resp_item import GetBillV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    currency = '' # str | Asset type, only support USDT  as of now (default to '')
    timestamp = 56 # int | 
    record_id = 56 # int | Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 (optional)
    start_time = 56 # int | Start Time, e.g 1593511200000 (optional)
    end_time = 56 # int | End Time, e.g 1593512200000 (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Account Funding Flow (USER_DATA)
        api_response = api_instance.get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of OptionsApi->get_bill_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_bill_v1: %s\n" % e)
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

[**List[GetBillV1RespItem]**](GetBillV1RespItem.md)

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

# **get_block_order_execute_v1**
> GetBlockOrderExecuteV1Resp get_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Query Block Trade Details (USER_DATA)

Query block trade details; returns block trade details from counterparty's perspective.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_block_order_execute_v1_resp import GetBlockOrderExecuteV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Details (USER_DATA)
        api_response = api_instance.get_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->get_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_block_order_execute_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetBlockOrderExecuteV1Resp**](GetBlockOrderExecuteV1Resp.md)

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

# **get_block_order_orders_v1**
> List[GetBlockOrderOrdersV1RespItem] get_block_order_orders_v1(timestamp, block_order_matching_key=block_order_matching_key, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)

Query Block Trade Order (TRADE)

Check block trade order status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_block_order_orders_v1_resp_item import GetBlockOrderOrdersV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    block_order_matching_key = '' # str | If specified, returns the specific block trade associated with the blockOrderMatchingKey (optional) (default to '')
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Order (TRADE)
        api_response = api_instance.get_block_order_orders_v1(timestamp, block_order_matching_key=block_order_matching_key, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of OptionsApi->get_block_order_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_block_order_orders_v1: %s\n" % e)
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

[**List[GetBlockOrderOrdersV1RespItem]**](GetBlockOrderOrdersV1RespItem.md)

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

# **get_block_trades_v1**
> List[GetBlockTradesV1RespItem] get_block_trades_v1(symbol=symbol, limit=limit)

Recent Block Trades List

Get recent block trades

### Example


```python
import binance.options
from binance.options.models.get_block_trades_v1_resp_item import GetBlockTradesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g. BTC-200730-9000-C (optional) (default to '')
    limit = 100 # int | Number of records; Default: 100 and Max: 500 (optional) (default to 100)

    try:
        # Recent Block Trades List
        api_response = api_instance.get_block_trades_v1(symbol=symbol, limit=limit)
        print("The response of OptionsApi->get_block_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_block_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g. BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **limit** | **int**| Number of records; Default: 100 and Max: 500 | [optional] [default to 100]

### Return type

[**List[GetBlockTradesV1RespItem]**](GetBlockTradesV1RespItem.md)

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

# **get_block_user_trades_v1**
> List[GetBlockUserTradesV1RespItem] get_block_user_trades_v1(timestamp, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)

Account Block Trade List (USER_DATA)

Gets block trades for a specific account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_block_user_trades_v1_resp_item import GetBlockUserTradesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Account Block Trade List (USER_DATA)
        api_response = api_instance.get_block_user_trades_v1(timestamp, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of OptionsApi->get_block_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_block_user_trades_v1: %s\n" % e)
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

[**List[GetBlockUserTradesV1RespItem]**](GetBlockUserTradesV1RespItem.md)

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

# **get_countdown_cancel_all_v1**
> GetCountdownCancelAllV1Resp get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_countdown_cancel_all_v1_resp import GetCountdownCancelAllV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | Option underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of OptionsApi->get_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| Option underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetCountdownCancelAllV1Resp**](GetCountdownCancelAllV1Resp.md)

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

# **get_depth_v1**
> GetDepthV1Resp get_depth_v1(symbol, limit=limit)

Order Book

Check orderbook depth on specific symbol

### Example


```python
import binance.options
from binance.options.models.get_depth_v1_resp import GetDepthV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] (optional)

    try:
        # Order Book
        api_response = api_instance.get_depth_v1(symbol, limit=limit)
        print("The response of OptionsApi->get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] | [optional] 

### Return type

[**GetDepthV1Resp**](GetDepthV1Resp.md)

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

# **get_exchange_info_v1**
> OptionsGetExchangeInfoV1Resp get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.options
from binance.options.models.options_get_exchange_info_v1_resp import OptionsGetExchangeInfoV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.get_exchange_info_v1()
        print("The response of OptionsApi->get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_exchange_info_v1: %s\n" % e)
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

# **get_exercise_history_v1**
> List[GetExerciseHistoryV1RespItem] get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)

Historical Exercise Records

Get historical exercise records.

### Example


```python
import binance.options
from binance.options.models.get_exercise_history_v1_resp_item import GetExerciseHistoryV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    underlying = '' # str | Underlying index like BTCUSDT (optional) (default to '')
    start_time = 56 # int | Start Time (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:100 Max:100 (optional)

    try:
        # Historical Exercise Records
        api_response = api_instance.get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of OptionsApi->get_exercise_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_exercise_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying index like BTCUSDT | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Start Time | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of records Default:100 Max:100 | [optional] 

### Return type

[**List[GetExerciseHistoryV1RespItem]**](GetExerciseHistoryV1RespItem.md)

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

# **get_exercise_record_v1**
> List[GetExerciseRecordV1RespItem] get_exercise_record_v1(timestamp, symbol=symbol, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

User Exercise Record (USER_DATA)

Get account exercise records.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_exercise_record_v1_resp_item import GetExerciseRecordV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    start_time = 56 # int | startTime (optional)
    end_time = 56 # int | endTime (optional)
    limit = 1000 # int | default 1000, max 1000 (optional) (default to 1000)
    recv_window = 56 # int |  (optional)

    try:
        # User Exercise Record (USER_DATA)
        api_response = api_instance.get_exercise_record_v1(timestamp, symbol=symbol, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of OptionsApi->get_exercise_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_exercise_record_v1: %s\n" % e)
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

[**List[GetExerciseRecordV1RespItem]**](GetExerciseRecordV1RespItem.md)

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

# **get_historical_trades_v1**
> List[GetHistoricalTradesV1RespItem] get_historical_trades_v1(symbol, from_id=from_id, limit=limit)

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.options
from binance.options.models.get_historical_trades_v1_resp_item import GetHistoricalTradesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    from_id = 56 # int | The UniqueId ID from which to return. The latest deal record is returned by default (optional)
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.get_historical_trades_v1(symbol, from_id=from_id, limit=limit)
        print("The response of OptionsApi->get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **from_id** | **int**| The UniqueId ID from which to return. The latest deal record is returned by default | [optional] 
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[GetHistoricalTradesV1RespItem]**](GetHistoricalTradesV1RespItem.md)

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

# **get_history_orders_v1**
> List[GetHistoryOrdersV1RespItem] get_history_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Option Order History (TRADE)

Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_history_orders_v1_resp_item import GetHistoryOrdersV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Returns the orderId and subsequent orders, the most recent order is returned by default (optional)
    start_time = 56 # int | Start Time, e.g 1593511200000 (optional)
    end_time = 56 # int | End Time, e.g 1593512200000 (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Option Order History (TRADE)
        api_response = api_instance.get_history_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of OptionsApi->get_history_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_history_orders_v1: %s\n" % e)
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

[**List[GetHistoryOrdersV1RespItem]**](GetHistoryOrdersV1RespItem.md)

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

# **get_income_asyn_id_v1**
> GetIncomeAsynIdV1Resp get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Option Transaction History Download Link by Id (USER_DATA)

Get option transaction history download Link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_income_asyn_id_v1_resp import GetIncomeAsynIdV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Option Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetIncomeAsynIdV1Resp**](GetIncomeAsynIdV1Resp.md)

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

# **get_income_asyn_v1**
> GetIncomeAsynV1Resp get_income_asyn_v1()

Get Download Id For Option Transaction History (USER_DATA)

Get download id for option transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_income_asyn_v1_resp import GetIncomeAsynV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Get Download Id For Option Transaction History (USER_DATA)
        api_response = api_instance.get_income_asyn_v1()
        print("The response of OptionsApi->get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_income_asyn_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIncomeAsynV1Resp**](GetIncomeAsynV1Resp.md)

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

# **get_index_v1**
> GetIndexV1Resp get_index_v1(underlying)

Symbol Price Ticker

Get spot index price for option underlying.

### Example


```python
import binance.options
from binance.options.models.get_index_v1_resp import GetIndexV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    underlying = '' # str | Spot pair（Option contract underlying asset, e.g BTCUSDT) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.get_index_v1(underlying)
        print("The response of OptionsApi->get_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Spot pair（Option contract underlying asset, e.g BTCUSDT) | [default to &#39;&#39;]

### Return type

[**GetIndexV1Resp**](GetIndexV1Resp.md)

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

# **get_klines_v1**
> List[GetKlinesV1RespItem] get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for an option symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.options
from binance.options.models.get_klines_v1_resp_item import GetKlinesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    interval = '' # str | Time interval (default to '')
    start_time = 56 # int | Start Time  1592317127349 (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:500 Max:1500 (optional)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of OptionsApi->get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_klines_v1: %s\n" % e)
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

[**List[GetKlinesV1RespItem]**](GetKlinesV1RespItem.md)

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

# **get_margin_account_v1**
> GetMarginAccountV1Resp get_margin_account_v1(timestamp, recv_window=recv_window)

Option Margin Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_margin_account_v1_resp import GetMarginAccountV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Margin Account Information (USER_DATA)
        api_response = api_instance.get_margin_account_v1(timestamp, recv_window=recv_window)
        print("The response of OptionsApi->get_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMarginAccountV1Resp**](GetMarginAccountV1Resp.md)

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

# **get_mark_v1**
> List[GetMarkV1RespItem] get_mark_v1(symbol=symbol)

Option Mark Price

Option mark price and greek info.

### Example


```python
import binance.options
from binance.options.models.get_mark_v1_resp_item import GetMarkV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # Option Mark Price
        api_response = api_instance.get_mark_v1(symbol=symbol)
        print("The response of OptionsApi->get_mark_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_mark_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[GetMarkV1RespItem]**](GetMarkV1RespItem.md)

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

# **get_mmp_v1**
> GetMmpV1Resp get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Market Maker Protection Config (TRADE)

Get config for MMP.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_mmp_v1_resp import GetMmpV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Market Maker Protection Config (TRADE)
        api_response = api_instance.get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of OptionsApi->get_mmp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_mmp_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMmpV1Resp**](GetMmpV1Resp.md)

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

# **get_open_interest_v1**
> List[GetOpenInterestV1RespItem] get_open_interest_v1(underlying_asset, expiration)

Open Interest

Get open interest for specific underlying asset on specific expiration date.

### Example


```python
import binance.options
from binance.options.models.get_open_interest_v1_resp_item import GetOpenInterestV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    underlying_asset = '' # str | underlying asset, e.g ETH/BTC (default to '')
    expiration = '' # str | expiration date, e.g 221225 (default to '')

    try:
        # Open Interest
        api_response = api_instance.get_open_interest_v1(underlying_asset, expiration)
        print("The response of OptionsApi->get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying_asset** | **str**| underlying asset, e.g ETH/BTC | [default to &#39;&#39;]
 **expiration** | **str**| expiration date, e.g 221225 | [default to &#39;&#39;]

### Return type

[**List[GetOpenInterestV1RespItem]**](GetOpenInterestV1RespItem.md)

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

# **get_open_orders_v1**
> List[GetOpenOrdersV1RespItem] get_open_orders_v1(timestamp, symbol=symbol, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Current Open Option Orders (USER_DATA)

Query current all open orders, status: ACCEPTED PARTIALLY_FILLED

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_open_orders_v1_resp_item import GetOpenOrdersV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | return all orders if don&#39;t pass, Option trading pair, e.g BTC-200730-9000-C, (optional) (default to '')
    order_id = 56 # int | Returns the orderId and subsequent orders, the most recent order is returned by default (optional)
    start_time = 56 # int | Start Time (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Option Orders (USER_DATA)
        api_response = api_instance.get_open_orders_v1(timestamp, symbol=symbol, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of OptionsApi->get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_open_orders_v1: %s\n" % e)
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

[**List[GetOpenOrdersV1RespItem]**](GetOpenOrdersV1RespItem.md)

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

# **get_order_v1**
> GetOrderV1Resp get_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)

Query Single Order (TRADE)

Check an order status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_order_v1_resp import GetOrderV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order id (optional)
    client_order_id = '' # str | User-defined order ID cannot be repeated in pending orders (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Single Order (TRADE)
        api_response = api_instance.get_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of OptionsApi->get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_order_v1: %s\n" % e)
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

[**GetOrderV1Resp**](GetOrderV1Resp.md)

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

# **get_ping_v1**
> object get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.options
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.get_ping_v1()
        print("The response of OptionsApi->get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_ping_v1: %s\n" % e)
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

# **get_position_v1**
> List[GetPositionV1RespItem] get_position_v1(timestamp, symbol=symbol, recv_window=recv_window)

Option Position Information (USER_DATA)

Get current position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_position_v1_resp_item import GetPositionV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Option Position Information (USER_DATA)
        api_response = api_instance.get_position_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of OptionsApi->get_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPositionV1RespItem]**](GetPositionV1RespItem.md)

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

# **get_ticker_v1**
> List[GetTickerV1RespItem] get_ticker_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.options
from binance.options.models.get_ticker_v1_resp_item import GetTickerV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.get_ticker_v1(symbol=symbol)
        print("The response of OptionsApi->get_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[GetTickerV1RespItem]**](GetTickerV1RespItem.md)

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

# **get_time_v1**
> GetTimeV1Resp get_time_v1()

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.options
from binance.options.models.get_time_v1_resp import GetTimeV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Check Server Time
        api_response = api_instance.get_time_v1()
        print("The response of OptionsApi->get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTimeV1Resp**](GetTimeV1Resp.md)

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

# **get_trades_v1**
> List[GetTradesV1RespItem] get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.options
from binance.options.models.get_trades_v1_resp_item import GetTradesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Recent Trades List
        api_response = api_instance.get_trades_v1(symbol, limit=limit)
        print("The response of OptionsApi->get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[GetTradesV1RespItem]**](GetTradesV1RespItem.md)

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

# **get_user_trades_v1**
> List[GetUserTradesV1RespItem] get_user_trades_v1(timestamp, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.get_user_trades_v1_resp_item import GetUserTradesV1RespItem
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option symbol, e.g BTC-200730-9000-C (optional) (default to '')
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376 (optional)
    start_time = 56 # int | Start time, e.g 1593511200000 (optional)
    end_time = 56 # int | End time, e.g 1593512200000 (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.get_user_trades_v1(timestamp, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of OptionsApi->get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_user_trades_v1: %s\n" % e)
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

[**List[GetUserTradesV1RespItem]**](GetUserTradesV1RespItem.md)

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

# **update_block_order_create_v1**
> UpdateBlockOrderCreateV1Resp update_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Extend Block Trade Order (TRADE)

Extends a block trade expire time by 30 mins from the current time.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.update_block_order_create_v1_resp import UpdateBlockOrderCreateV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Extend Block Trade Order (TRADE)
        api_response = api_instance.update_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of OptionsApi->update_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->update_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UpdateBlockOrderCreateV1Resp**](UpdateBlockOrderCreateV1Resp.md)

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

# **update_listen_key_v1**
> object update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.OptionsApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.update_listen_key_v1()
        print("The response of OptionsApi->update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->update_listen_key_v1: %s\n" % e)
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

