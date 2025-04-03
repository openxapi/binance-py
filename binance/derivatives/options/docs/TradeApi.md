# binance.derivatives.options.TradeApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_create_batch_orders_v1**](TradeApi.md#options_create_batch_orders_v1) | **POST** /eapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**options_create_order_v1**](TradeApi.md#options_create_order_v1) | **POST** /eapi/v1/order | New Order (TRADE)
[**options_delete_all_open_orders_by_underlying_v1**](TradeApi.md#options_delete_all_open_orders_by_underlying_v1) | **DELETE** /eapi/v1/allOpenOrdersByUnderlying | Cancel All Option Orders By Underlying (TRADE)
[**options_delete_all_open_orders_v1**](TradeApi.md#options_delete_all_open_orders_v1) | **DELETE** /eapi/v1/allOpenOrders | Cancel all Option orders on specific symbol (TRADE)
[**options_delete_batch_orders_v1**](TradeApi.md#options_delete_batch_orders_v1) | **DELETE** /eapi/v1/batchOrders | Cancel Multiple Option Orders (TRADE)
[**options_delete_order_v1**](TradeApi.md#options_delete_order_v1) | **DELETE** /eapi/v1/order | Cancel Option Order (TRADE)
[**options_get_exercise_record_v1**](TradeApi.md#options_get_exercise_record_v1) | **GET** /eapi/v1/exerciseRecord | User Exercise Record (USER_DATA)
[**options_get_history_orders_v1**](TradeApi.md#options_get_history_orders_v1) | **GET** /eapi/v1/historyOrders | Query Option Order History (TRADE)
[**options_get_open_orders_v1**](TradeApi.md#options_get_open_orders_v1) | **GET** /eapi/v1/openOrders | Query Current Open Option Orders (USER_DATA)
[**options_get_order_v1**](TradeApi.md#options_get_order_v1) | **GET** /eapi/v1/order | Query Single Order (TRADE)
[**options_get_position_v1**](TradeApi.md#options_get_position_v1) | **GET** /eapi/v1/position | Option Position Information (USER_DATA)
[**options_get_user_trades_v1**](TradeApi.md#options_get_user_trades_v1) | **GET** /eapi/v1/userTrades | Account Trade List (USER_DATA)


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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    orders = [binance.derivatives.options.OptionsCreateBatchOrdersV1ReqOrdersItem()] # List[OptionsCreateBatchOrdersV1ReqOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.options_create_batch_orders_v1(orders, timestamp, recv_window=recv_window)
        print("The response of TradeApi->options_create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_create_batch_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
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
        print("The response of TradeApi->options_create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_create_order_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    underlying = '' # str | Option underlying, e.g BTCUSDT (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Option Orders By Underlying (TRADE)
        api_response = api_instance.options_delete_all_open_orders_by_underlying_v1(underlying, timestamp, recv_window=recv_window)
        print("The response of TradeApi->options_delete_all_open_orders_by_underlying_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_delete_all_open_orders_by_underlying_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel all Option orders on specific symbol (TRADE)
        api_response = api_instance.options_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->options_delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_delete_all_open_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_ids = [56] # List[int] | Order ID, e.g [4611875134427365377,4611875134427365378] (optional)
    client_order_ids = ['client_order_ids_example'] # List[str] | User-defined order ID, e.g [&#34;my_id_1&#34;,&#34;my_id_2&#34;] (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Option Orders (TRADE)
        api_response = api_instance.options_delete_batch_orders_v1(symbol, timestamp, order_ids=order_ids, client_order_ids=client_order_ids, recv_window=recv_window)
        print("The response of TradeApi->options_delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_delete_batch_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order ID, e.g 4611875134427365377 (optional)
    client_order_id = '' # str | User-defined order ID, e.g 10000 (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Option Order (TRADE)
        api_response = api_instance.options_delete_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of TradeApi->options_delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_delete_order_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    start_time = 56 # int | startTime (optional)
    end_time = 56 # int | endTime (optional)
    limit = 1000 # int | default 1000, max 1000 (optional) (default to 1000)
    recv_window = 56 # int |  (optional)

    try:
        # User Exercise Record (USER_DATA)
        api_response = api_instance.options_get_exercise_record_v1(timestamp, symbol=symbol, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->options_get_exercise_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_exercise_record_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
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
        print("The response of TradeApi->options_get_history_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_history_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
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
        print("The response of TradeApi->options_get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_open_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | Order id (optional)
    client_order_id = '' # str | User-defined order ID cannot be repeated in pending orders (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Single Order (TRADE)
        api_response = api_instance.options_get_order_v1(symbol, timestamp, order_id=order_id, client_order_id=client_order_id, recv_window=recv_window)
        print("The response of TradeApi->options_get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_order_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Option Position Information (USER_DATA)
        api_response = api_instance.options_get_position_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->options_get_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_position_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.TradeApi(api_client)
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
        print("The response of TradeApi->options_get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->options_get_user_trades_v1: %s\n" % e)
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

