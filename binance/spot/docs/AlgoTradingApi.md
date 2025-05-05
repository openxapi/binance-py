# binance.spot.AlgoTradingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_algo_futures_new_order_twap_v1**](AlgoTradingApi.md#create_algo_futures_new_order_twap_v1) | **POST** /sapi/v1/algo/futures/newOrderTwap | Time-Weighted Average Price(Twap) New Order(TRADE)
[**create_algo_futures_new_order_vp_v1**](AlgoTradingApi.md#create_algo_futures_new_order_vp_v1) | **POST** /sapi/v1/algo/futures/newOrderVp | Volume Participation(VP) New Order (TRADE)
[**create_algo_spot_new_order_twap_v1**](AlgoTradingApi.md#create_algo_spot_new_order_twap_v1) | **POST** /sapi/v1/algo/spot/newOrderTwap | Time-Weighted Average Price(Twap) New Order(TRADE)
[**delete_algo_futures_order_v1**](AlgoTradingApi.md#delete_algo_futures_order_v1) | **DELETE** /sapi/v1/algo/futures/order | Cancel Algo Order(TRADE)
[**delete_algo_spot_order_v1**](AlgoTradingApi.md#delete_algo_spot_order_v1) | **DELETE** /sapi/v1/algo/spot/order | Cancel Algo Order(TRADE)
[**get_algo_futures_historical_orders_v1**](AlgoTradingApi.md#get_algo_futures_historical_orders_v1) | **GET** /sapi/v1/algo/futures/historicalOrders | Query Historical Algo Orders(USER_DATA)
[**get_algo_futures_open_orders_v1**](AlgoTradingApi.md#get_algo_futures_open_orders_v1) | **GET** /sapi/v1/algo/futures/openOrders | Query Current Algo Open Orders(USER_DATA)
[**get_algo_futures_sub_orders_v1**](AlgoTradingApi.md#get_algo_futures_sub_orders_v1) | **GET** /sapi/v1/algo/futures/subOrders | Query Sub Orders(USER_DATA)
[**get_algo_spot_historical_orders_v1**](AlgoTradingApi.md#get_algo_spot_historical_orders_v1) | **GET** /sapi/v1/algo/spot/historicalOrders | Query Historical Algo Orders(USER_DATA)
[**get_algo_spot_open_orders_v1**](AlgoTradingApi.md#get_algo_spot_open_orders_v1) | **GET** /sapi/v1/algo/spot/openOrders | Query Current Algo Open Orders(USER_DATA)
[**get_algo_spot_sub_orders_v1**](AlgoTradingApi.md#get_algo_spot_sub_orders_v1) | **GET** /sapi/v1/algo/spot/subOrders | Query Sub Orders(USER_DATA)


# **create_algo_futures_new_order_twap_v1**
> CreateAlgoFuturesNewOrderTwapV1Resp create_algo_futures_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price, position_side=position_side, recv_window=recv_window, reduce_only=reduce_only)

Time-Weighted Average Price(Twap) New Order(TRADE)

Send in a Twap new order.
Only support on USDⓈ-M Contracts.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_algo_futures_new_order_twap_v1_resp import CreateAlgoFuturesNewOrderTwapV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    duration = 56 # int | 
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    client_algo_id = '' # str |  (optional) (default to '')
    limit_price = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = True # bool |  (optional)

    try:
        # Time-Weighted Average Price(Twap) New Order(TRADE)
        api_response = api_instance.create_algo_futures_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price, position_side=position_side, recv_window=recv_window, reduce_only=reduce_only)
        print("The response of AlgoTradingApi->create_algo_futures_new_order_twap_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->create_algo_futures_new_order_twap_v1: %s\n" % e)
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
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **bool**|  | [optional] 

### Return type

[**CreateAlgoFuturesNewOrderTwapV1Resp**](CreateAlgoFuturesNewOrderTwapV1Resp.md)

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

# **create_algo_futures_new_order_vp_v1**
> CreateAlgoFuturesNewOrderVpV1Resp create_algo_futures_new_order_vp_v1(quantity, side, symbol, timestamp, urgency, client_algo_id=client_algo_id, limit_price=limit_price, position_side=position_side, recv_window=recv_window, reduce_only=reduce_only)

Volume Participation(VP) New Order (TRADE)

Send in a VP new order.
Only support on USDⓈ-M Contracts.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_algo_futures_new_order_vp_v1_resp import CreateAlgoFuturesNewOrderVpV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    urgency = '' # str |  (default to '')
    client_algo_id = '' # str |  (optional) (default to '')
    limit_price = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = True # bool |  (optional)

    try:
        # Volume Participation(VP) New Order (TRADE)
        api_response = api_instance.create_algo_futures_new_order_vp_v1(quantity, side, symbol, timestamp, urgency, client_algo_id=client_algo_id, limit_price=limit_price, position_side=position_side, recv_window=recv_window, reduce_only=reduce_only)
        print("The response of AlgoTradingApi->create_algo_futures_new_order_vp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->create_algo_futures_new_order_vp_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **urgency** | **str**|  | [default to &#39;&#39;]
 **client_algo_id** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_price** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **bool**|  | [optional] 

### Return type

[**CreateAlgoFuturesNewOrderVpV1Resp**](CreateAlgoFuturesNewOrderVpV1Resp.md)

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

# **create_algo_spot_new_order_twap_v1**
> CreateAlgoSpotNewOrderTwapV1Resp create_algo_spot_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price)

Time-Weighted Average Price(Twap) New Order(TRADE)

Place a new spot TWAP order with Algo service.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_algo_spot_new_order_twap_v1_resp import CreateAlgoSpotNewOrderTwapV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    duration = 56 # int | 
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    client_algo_id = '' # str |  (optional) (default to '')
    limit_price = '' # str |  (optional) (default to '')

    try:
        # Time-Weighted Average Price(Twap) New Order(TRADE)
        api_response = api_instance.create_algo_spot_new_order_twap_v1(duration, quantity, side, symbol, timestamp, client_algo_id=client_algo_id, limit_price=limit_price)
        print("The response of AlgoTradingApi->create_algo_spot_new_order_twap_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->create_algo_spot_new_order_twap_v1: %s\n" % e)
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

[**CreateAlgoSpotNewOrderTwapV1Resp**](CreateAlgoSpotNewOrderTwapV1Resp.md)

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

# **delete_algo_futures_order_v1**
> DeleteAlgoFuturesOrderV1Resp delete_algo_futures_order_v1(algo_id, timestamp, recv_window=recv_window)

Cancel Algo Order(TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_algo_futures_order_v1_resp import DeleteAlgoFuturesOrderV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    algo_id = 56 # int | eg. 14511
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Algo Order(TRADE)
        api_response = api_instance.delete_algo_futures_order_v1(algo_id, timestamp, recv_window=recv_window)
        print("The response of AlgoTradingApi->delete_algo_futures_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->delete_algo_futures_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**| eg. 14511 | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteAlgoFuturesOrderV1Resp**](DeleteAlgoFuturesOrderV1Resp.md)

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

# **delete_algo_spot_order_v1**
> DeleteAlgoSpotOrderV1Resp delete_algo_spot_order_v1(algo_id, timestamp, recv_window=recv_window)

Cancel Algo Order(TRADE)

Cancel an open TWAP order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_algo_spot_order_v1_resp import DeleteAlgoSpotOrderV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    algo_id = 56 # int | eg. 14511
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Algo Order(TRADE)
        api_response = api_instance.delete_algo_spot_order_v1(algo_id, timestamp, recv_window=recv_window)
        print("The response of AlgoTradingApi->delete_algo_spot_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->delete_algo_spot_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**| eg. 14511 | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteAlgoSpotOrderV1Resp**](DeleteAlgoSpotOrderV1Resp.md)

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

# **get_algo_futures_historical_orders_v1**
> GetAlgoFuturesHistoricalOrdersV1Resp get_algo_futures_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)

Query Historical Algo Orders(USER_DATA)

Query Historical Algo Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_futures_historical_orders_v1_resp import GetAlgoFuturesHistoricalOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
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
        api_response = api_instance.get_algo_futures_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_futures_historical_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_futures_historical_orders_v1: %s\n" % e)
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

[**GetAlgoFuturesHistoricalOrdersV1Resp**](GetAlgoFuturesHistoricalOrdersV1Resp.md)

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

# **get_algo_futures_open_orders_v1**
> GetAlgoFuturesOpenOrdersV1Resp get_algo_futures_open_orders_v1(timestamp, recv_window=recv_window)

Query Current Algo Open Orders(USER_DATA)

Query Current Algo Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_futures_open_orders_v1_resp import GetAlgoFuturesOpenOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Algo Open Orders(USER_DATA)
        api_response = api_instance.get_algo_futures_open_orders_v1(timestamp, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_futures_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_futures_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAlgoFuturesOpenOrdersV1Resp**](GetAlgoFuturesOpenOrdersV1Resp.md)

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

# **get_algo_futures_sub_orders_v1**
> GetAlgoFuturesSubOrdersV1Resp get_algo_futures_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)

Query Sub Orders(USER_DATA)

Get respective sub orders for a specified algoId

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_futures_sub_orders_v1_resp import GetAlgoFuturesSubOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    algo_id = 56 # int | 
    timestamp = 56 # int | 
    page = 56 # int | Default is 1 (optional)
    page_size = 100 # int | MIN 1, MAX 100; Default 100 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Orders(USER_DATA)
        api_response = api_instance.get_algo_futures_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_futures_sub_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_futures_sub_orders_v1: %s\n" % e)
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

[**GetAlgoFuturesSubOrdersV1Resp**](GetAlgoFuturesSubOrdersV1Resp.md)

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

# **get_algo_spot_historical_orders_v1**
> GetAlgoSpotHistoricalOrdersV1Resp get_algo_spot_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)

Query Historical Algo Orders(USER_DATA)

Get all historical SPOT TWAP orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_spot_historical_orders_v1_resp import GetAlgoSpotHistoricalOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
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
        api_response = api_instance.get_algo_spot_historical_orders_v1(timestamp, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_spot_historical_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_spot_historical_orders_v1: %s\n" % e)
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

[**GetAlgoSpotHistoricalOrdersV1Resp**](GetAlgoSpotHistoricalOrdersV1Resp.md)

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

# **get_algo_spot_open_orders_v1**
> GetAlgoSpotOpenOrdersV1Resp get_algo_spot_open_orders_v1(timestamp, recv_window=recv_window)

Query Current Algo Open Orders(USER_DATA)

Get all open SPOT TWAP orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_spot_open_orders_v1_resp import GetAlgoSpotOpenOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Algo Open Orders(USER_DATA)
        api_response = api_instance.get_algo_spot_open_orders_v1(timestamp, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_spot_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_spot_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAlgoSpotOpenOrdersV1Resp**](GetAlgoSpotOpenOrdersV1Resp.md)

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

# **get_algo_spot_sub_orders_v1**
> GetAlgoSpotSubOrdersV1Resp get_algo_spot_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)

Query Sub Orders(USER_DATA)

Get respective sub orders for a specified algoId

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_algo_spot_sub_orders_v1_resp import GetAlgoSpotSubOrdersV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.AlgoTradingApi(api_client)
    algo_id = 56 # int | 
    timestamp = 56 # int | 
    page = 56 # int | Default is 1 (optional)
    page_size = 100 # int | MIN 1, MAX 100; Default 100 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Orders(USER_DATA)
        api_response = api_instance.get_algo_spot_sub_orders_v1(algo_id, timestamp, page=page, page_size=page_size, recv_window=recv_window)
        print("The response of AlgoTradingApi->get_algo_spot_sub_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgoTradingApi->get_algo_spot_sub_orders_v1: %s\n" % e)
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

[**GetAlgoSpotSubOrdersV1Resp**](GetAlgoSpotSubOrdersV1Resp.md)

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

