# binance.algo.SpotAlgoApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algo_create_algo_spot_new_order_twap_v1**](SpotAlgoApi.md#algo_create_algo_spot_new_order_twap_v1) | **POST** /sapi/v1/algo/spot/newOrderTwap | Time-Weighted Average Price(Twap) New Order(TRADE)
[**algo_delete_algo_spot_order_v1**](SpotAlgoApi.md#algo_delete_algo_spot_order_v1) | **DELETE** /sapi/v1/algo/spot/order | Cancel Algo Order(TRADE)
[**algo_get_algo_spot_historical_orders_v1**](SpotAlgoApi.md#algo_get_algo_spot_historical_orders_v1) | **GET** /sapi/v1/algo/spot/historicalOrders | Query Historical Algo Orders(USER_DATA)
[**algo_get_algo_spot_open_orders_v1**](SpotAlgoApi.md#algo_get_algo_spot_open_orders_v1) | **GET** /sapi/v1/algo/spot/openOrders | Query Current Algo Open Orders(USER_DATA)
[**algo_get_algo_spot_sub_orders_v1**](SpotAlgoApi.md#algo_get_algo_spot_sub_orders_v1) | **GET** /sapi/v1/algo/spot/subOrders | Query Sub Orders(USER_DATA)


# **algo_create_algo_spot_new_order_twap_v1**
> AlgoCreateAlgoSpotNewOrderTwapV1Resp algo_create_algo_spot_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price)

Time-Weighted Average Price(Twap) New Order(TRADE)

Place a new spot TWAP order with Algo service.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.algo
from binance.algo.models.algo_create_algo_spot_new_order_twap_v1_resp import AlgoCreateAlgoSpotNewOrderTwapV1Resp
from binance.algo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.algo.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.algo.Configuration(
    auth=binance.algo.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.algo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.algo.SpotAlgoApi(api_client)
    duration = 56 # int | 
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    client_algo_id = '' # str |  (optional) (default to '')
    limit_price = '' # str |  (optional) (default to '')

    try:
        # Time-Weighted Average Price(Twap) New Order(TRADE)
        api_response = api_instance.algo_create_algo_spot_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price)
        print("The response of SpotAlgoApi->algo_create_algo_spot_new_order_twap_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotAlgoApi->algo_create_algo_spot_new_order_twap_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duration** | **int**|  | 
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **client_algo_id** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_price** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**AlgoCreateAlgoSpotNewOrderTwapV1Resp**](AlgoCreateAlgoSpotNewOrderTwapV1Resp.md)

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

# **algo_delete_algo_spot_order_v1**
> AlgoDeleteAlgoSpotOrderV1Resp algo_delete_algo_spot_order_v1(algo_id, timestamp, recv_window=recv_window)

Cancel Algo Order(TRADE)

Cancel an open TWAP order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.algo
from binance.algo.models.algo_delete_algo_spot_order_v1_resp import AlgoDeleteAlgoSpotOrderV1Resp
from binance.algo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.algo.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.algo.Configuration(
    auth=binance.algo.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.algo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.algo.SpotAlgoApi(api_client)
    algo_id = 56 # int | eg. 14511
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Algo Order(TRADE)
        api_response = api_instance.algo_delete_algo_spot_order_v1(algo_id, timestamp, recv_window=recv_window)
        print("The response of SpotAlgoApi->algo_delete_algo_spot_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotAlgoApi->algo_delete_algo_spot_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**| eg. 14511 | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**AlgoDeleteAlgoSpotOrderV1Resp**](AlgoDeleteAlgoSpotOrderV1Resp.md)

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

# **algo_get_algo_spot_historical_orders_v1**
> AlgoGetAlgoSpotHistoricalOrdersV1Resp algo_get_algo_spot_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)

Query Historical Algo Orders(USER_DATA)

Get all historical SPOT TWAP orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.algo
from binance.algo.models.algo_get_algo_spot_historical_orders_v1_resp import AlgoGetAlgoSpotHistoricalOrdersV1Resp
from binance.algo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.algo.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.algo.Configuration(
    auth=binance.algo.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.algo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.algo.SpotAlgoApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | Trading symbol eg. BTCUSDT (optional) (default to '')
    side = '' # str | BUY or SELL (optional) (default to '')
    start_time = 56 # int | in milliseconds  eg.1641522717552 (optional)
    end_time = 56 # int | in milliseconds  eg.1641522526562 (optional)
    page = 56 # int | Default is 1 (optional)
    page_size = 100 # int | MIN 1, MAX 100; Default 100 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Query Historical Algo Orders(USER_DATA)
        api_response = api_instance.algo_get_algo_spot_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of SpotAlgoApi->algo_get_algo_spot_historical_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotAlgoApi->algo_get_algo_spot_historical_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| Trading symbol eg. BTCUSDT | [optional] [default to &#39;&#39;]
 **side** | **str**| BUY or SELL | [optional] [default to &#39;&#39;]
 **start_time** | **int**| in milliseconds  eg.1641522717552 | [optional] 
 **end_time** | **int**| in milliseconds  eg.1641522526562 | [optional] 
 **page** | **int**| Default is 1 | [optional] 
 **page_size** | **int**| MIN 1, MAX 100; Default 100 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**AlgoGetAlgoSpotHistoricalOrdersV1Resp**](AlgoGetAlgoSpotHistoricalOrdersV1Resp.md)

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

# **algo_get_algo_spot_open_orders_v1**
> AlgoGetAlgoSpotOpenOrdersV1Resp algo_get_algo_spot_open_orders_v1(timestamp, recv_window=recv_window)

Query Current Algo Open Orders(USER_DATA)

Get all open SPOT TWAP orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.algo
from binance.algo.models.algo_get_algo_spot_open_orders_v1_resp import AlgoGetAlgoSpotOpenOrdersV1Resp
from binance.algo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.algo.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.algo.Configuration(
    auth=binance.algo.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.algo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.algo.SpotAlgoApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Algo Open Orders(USER_DATA)
        api_response = api_instance.algo_get_algo_spot_open_orders_v1(timestamp, recv_window=recv_window)
        print("The response of SpotAlgoApi->algo_get_algo_spot_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotAlgoApi->algo_get_algo_spot_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**AlgoGetAlgoSpotOpenOrdersV1Resp**](AlgoGetAlgoSpotOpenOrdersV1Resp.md)

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

# **algo_get_algo_spot_sub_orders_v1**
> AlgoGetAlgoSpotSubOrdersV1Resp algo_get_algo_spot_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)

Query Sub Orders(USER_DATA)

Get respective sub orders for a specified algoId

### Example

* Api Key Authentication (ApiKey):

```python
import binance.algo
from binance.algo.models.algo_get_algo_spot_sub_orders_v1_resp import AlgoGetAlgoSpotSubOrdersV1Resp
from binance.algo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.algo.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.algo.Configuration(
    auth=binance.algo.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.algo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.algo.SpotAlgoApi(api_client)
    algo_id = 56 # int | 
    timestamp = 56 # int | 
    page = 56 # int | Default is 1 (optional)
    page_size = 100 # int | MIN 1, MAX 100; Default 100 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Orders(USER_DATA)
        api_response = api_instance.algo_get_algo_spot_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of SpotAlgoApi->algo_get_algo_spot_sub_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotAlgoApi->algo_get_algo_spot_sub_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **page** | **int**| Default is 1 | [optional] 
 **page_size** | **int**| MIN 1, MAX 100; Default 100 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**AlgoGetAlgoSpotSubOrdersV1Resp**](AlgoGetAlgoSpotSubOrdersV1Resp.md)

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

