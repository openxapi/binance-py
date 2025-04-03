# binance.convert.TradeApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_create_convert_accept_quote_v1**](TradeApi.md#convert_create_convert_accept_quote_v1) | **POST** /sapi/v1/convert/acceptQuote | Accept Quote (TRADE)
[**convert_create_convert_get_quote_v1**](TradeApi.md#convert_create_convert_get_quote_v1) | **POST** /sapi/v1/convert/getQuote | Send Quote Request(USER_DATA)
[**convert_create_convert_limit_cancel_order_v1**](TradeApi.md#convert_create_convert_limit_cancel_order_v1) | **POST** /sapi/v1/convert/limit/cancelOrder | Cancel limit order (USER_DATA)
[**convert_create_convert_limit_place_order_v1**](TradeApi.md#convert_create_convert_limit_place_order_v1) | **POST** /sapi/v1/convert/limit/placeOrder | Place limit order (USER_DATA)
[**convert_create_convert_limit_query_open_orders_v1**](TradeApi.md#convert_create_convert_limit_query_open_orders_v1) | **POST** /sapi/v1/convert/limit/queryOpenOrders | Query limit open orders (USER_DATA)
[**convert_get_convert_order_status_v1**](TradeApi.md#convert_get_convert_order_status_v1) | **GET** /sapi/v1/convert/orderStatus | Order status(USER_DATA)
[**convert_get_convert_trade_flow_v1**](TradeApi.md#convert_get_convert_trade_flow_v1) | **GET** /sapi/v1/convert/tradeFlow | Get Convert Trade History(USER_DATA)


# **convert_create_convert_accept_quote_v1**
> ConvertCreateConvertAcceptQuoteV1Resp convert_create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)

Accept Quote (TRADE)

Accept the offered quote by quote ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_create_convert_accept_quote_v1_resp import ConvertCreateConvertAcceptQuoteV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    quote_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept Quote (TRADE)
        api_response = api_instance.convert_create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)
        print("The response of TradeApi->convert_create_convert_accept_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_create_convert_accept_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**ConvertCreateConvertAcceptQuoteV1Resp**](ConvertCreateConvertAcceptQuoteV1Resp.md)

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

# **convert_create_convert_get_quote_v1**
> ConvertCreateConvertGetQuoteV1Resp convert_create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type)

Send Quote Request(USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_create_convert_get_quote_v1_resp import ConvertCreateConvertGetQuoteV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    from_asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_asset = '' # str |  (default to '')
    from_amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_amount = '' # str |  (optional) (default to '')
    valid_time = '10' # str |  (optional) (default to '10')
    wallet_type = '' # str |  (optional) (default to '')

    try:
        # Send Quote Request(USER_DATA)
        api_response = api_instance.convert_create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type)
        print("The response of TradeApi->convert_create_convert_get_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_create_convert_get_quote_v1: %s\n" % e)
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
 **wallet_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ConvertCreateConvertGetQuoteV1Resp**](ConvertCreateConvertGetQuoteV1Resp.md)

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

# **convert_create_convert_limit_cancel_order_v1**
> ConvertCreateConvertLimitCancelOrderV1Resp convert_create_convert_limit_cancel_order_v1(order_id, timestamp, recv_window=recv_window)

Cancel limit order (USER_DATA)

Enable users to cancel a limit order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_create_convert_limit_cancel_order_v1_resp import ConvertCreateConvertLimitCancelOrderV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    order_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel limit order (USER_DATA)
        api_response = api_instance.convert_create_convert_limit_cancel_order_v1(order_id, timestamp, recv_window=recv_window)
        print("The response of TradeApi->convert_create_convert_limit_cancel_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_create_convert_limit_cancel_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**ConvertCreateConvertLimitCancelOrderV1Resp**](ConvertCreateConvertLimitCancelOrderV1Resp.md)

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

# **convert_create_convert_limit_place_order_v1**
> ConvertCreateConvertLimitPlaceOrderV1Resp convert_create_convert_limit_place_order_v1(base_asset, expired_type, limit_price, quote_asset, side, timestamp, base_amount=base_amount, quote_amount=quote_amount, recv_window=recv_window, wallet_type=wallet_type)

Place limit order (USER_DATA)

Enable users to place a limit order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_create_convert_limit_place_order_v1_resp import ConvertCreateConvertLimitPlaceOrderV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    base_asset = '' # str |  (default to '')
    expired_type = '' # str |  (default to '')
    limit_price = '' # str |  (default to '')
    quote_asset = '' # str |  (default to '')
    side = '' # str |  (default to '')
    timestamp = 56 # int | 
    base_amount = '' # str |  (optional) (default to '')
    quote_amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    wallet_type = '' # str |  (optional) (default to '')

    try:
        # Place limit order (USER_DATA)
        api_response = api_instance.convert_create_convert_limit_place_order_v1(base_asset, expired_type, limit_price, quote_asset, side, timestamp, base_amount=base_amount, quote_amount=quote_amount, recv_window=recv_window, wallet_type=wallet_type)
        print("The response of TradeApi->convert_create_convert_limit_place_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_create_convert_limit_place_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset** | **str**|  | [default to &#39;&#39;]
 **expired_type** | **str**|  | [default to &#39;&#39;]
 **limit_price** | **str**|  | [default to &#39;&#39;]
 **quote_asset** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **base_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **quote_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **wallet_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ConvertCreateConvertLimitPlaceOrderV1Resp**](ConvertCreateConvertLimitPlaceOrderV1Resp.md)

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

# **convert_create_convert_limit_query_open_orders_v1**
> ConvertCreateConvertLimitQueryOpenOrdersV1Resp convert_create_convert_limit_query_open_orders_v1(timestamp, recv_window=recv_window)

Query limit open orders (USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_create_convert_limit_query_open_orders_v1_resp import ConvertCreateConvertLimitQueryOpenOrdersV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query limit open orders (USER_DATA)
        api_response = api_instance.convert_create_convert_limit_query_open_orders_v1(timestamp, recv_window=recv_window)
        print("The response of TradeApi->convert_create_convert_limit_query_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_create_convert_limit_query_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**ConvertCreateConvertLimitQueryOpenOrdersV1Resp**](ConvertCreateConvertLimitQueryOpenOrdersV1Resp.md)

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

# **convert_get_convert_order_status_v1**
> ConvertGetConvertOrderStatusV1Resp convert_get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)

Order status(USER_DATA)

Query order status by order ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_get_convert_order_status_v1_resp import ConvertGetConvertOrderStatusV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    order_id = '' # str | Either orderId or quoteId is required (optional) (default to '')
    quote_id = '' # str | Either orderId or quoteId is required (optional) (default to '')

    try:
        # Order status(USER_DATA)
        api_response = api_instance.convert_get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)
        print("The response of TradeApi->convert_get_convert_order_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_get_convert_order_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]
 **quote_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]

### Return type

[**ConvertGetConvertOrderStatusV1Resp**](ConvertGetConvertOrderStatusV1Resp.md)

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

# **convert_get_convert_trade_flow_v1**
> ConvertGetConvertTradeFlowV1Resp convert_get_convert_trade_flow_v1(start_time, end_time, timestamp, limit=limit, recv_window=recv_window)

Get Convert Trade History(USER_DATA)

Get Convert Trade History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_get_convert_trade_flow_v1_resp import ConvertGetConvertTradeFlowV1Resp
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.TradeApi(api_client)
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    limit = 100 # int | Default 100, Max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Convert Trade History(USER_DATA)
        api_response = api_instance.convert_get_convert_trade_flow_v1(start_time, end_time, timestamp, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->convert_get_convert_trade_flow_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->convert_get_convert_trade_flow_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **limit** | **int**| Default 100, Max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**ConvertGetConvertTradeFlowV1Resp**](ConvertGetConvertTradeFlowV1Resp.md)

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

