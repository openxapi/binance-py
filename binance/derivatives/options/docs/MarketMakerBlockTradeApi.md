# binance.derivatives.options.MarketMakerBlockTradeApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_create_block_order_create_v1**](MarketMakerBlockTradeApi.md#options_create_block_order_create_v1) | **POST** /eapi/v1/block/order/create | New Block Trade Order (TRADE)
[**options_create_block_order_execute_v1**](MarketMakerBlockTradeApi.md#options_create_block_order_execute_v1) | **POST** /eapi/v1/block/order/execute | Accept Block Trade Order (TRADE)
[**options_delete_block_order_create_v1**](MarketMakerBlockTradeApi.md#options_delete_block_order_create_v1) | **DELETE** /eapi/v1/block/order/create | Cancel Block Trade Order (TRADE)
[**options_get_block_order_execute_v1**](MarketMakerBlockTradeApi.md#options_get_block_order_execute_v1) | **GET** /eapi/v1/block/order/execute | Query Block Trade Details (USER_DATA)
[**options_get_block_order_orders_v1**](MarketMakerBlockTradeApi.md#options_get_block_order_orders_v1) | **GET** /eapi/v1/block/order/orders | Query Block Trade Order (TRADE)
[**options_get_block_user_trades_v1**](MarketMakerBlockTradeApi.md#options_get_block_user_trades_v1) | **GET** /eapi/v1/block/user-trades | Account Block Trade List (USER_DATA)
[**options_update_block_order_create_v1**](MarketMakerBlockTradeApi.md#options_update_block_order_create_v1) | **PUT** /eapi/v1/block/order/create | Extend Block Trade Order (TRADE)


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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
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
        print("The response of MarketMakerBlockTradeApi->options_create_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_create_block_order_create_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept Block Trade Order (TRADE)
        api_response = api_instance.options_create_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_create_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_create_block_order_execute_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Block Trade Order (TRADE)
        api_response = api_instance.options_delete_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_delete_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_delete_block_order_create_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Details (USER_DATA)
        api_response = api_instance.options_get_block_order_execute_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_get_block_order_execute_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_get_block_order_execute_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    timestamp = 56 # int | 
    block_order_matching_key = '' # str | If specified, returns the specific block trade associated with the blockOrderMatchingKey (optional) (default to '')
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Block Trade Order (TRADE)
        api_response = api_instance.options_get_block_order_orders_v1(timestamp, block_order_matching_key=block_order_matching_key, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_get_block_order_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_get_block_order_orders_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    timestamp = 56 # int | 
    end_time = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Account Block Trade List (USER_DATA)
        api_response = api_instance.options_get_block_user_trades_v1(timestamp, end_time=end_time, start_time=start_time, underlying=underlying, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_get_block_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_get_block_user_trades_v1: %s\n" % e)
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
    api_instance = binance.derivatives.options.MarketMakerBlockTradeApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Extend Block Trade Order (TRADE)
        api_response = api_instance.options_update_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->options_update_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->options_update_block_order_create_v1: %s\n" % e)
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

