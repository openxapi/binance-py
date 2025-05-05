# binance.spot.ConvertApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_convert_accept_quote_v1**](ConvertApi.md#create_convert_accept_quote_v1) | **POST** /sapi/v1/convert/acceptQuote | Accept Quote (TRADE)
[**create_convert_get_quote_v1**](ConvertApi.md#create_convert_get_quote_v1) | **POST** /sapi/v1/convert/getQuote | Send Quote Request(USER_DATA)
[**create_convert_limit_cancel_order_v1**](ConvertApi.md#create_convert_limit_cancel_order_v1) | **POST** /sapi/v1/convert/limit/cancelOrder | Cancel limit order (USER_DATA)
[**create_convert_limit_place_order_v1**](ConvertApi.md#create_convert_limit_place_order_v1) | **POST** /sapi/v1/convert/limit/placeOrder | Place limit order (USER_DATA)
[**create_convert_limit_query_open_orders_v1**](ConvertApi.md#create_convert_limit_query_open_orders_v1) | **POST** /sapi/v1/convert/limit/queryOpenOrders | Query limit open orders (USER_DATA)
[**get_convert_asset_info_v1**](ConvertApi.md#get_convert_asset_info_v1) | **GET** /sapi/v1/convert/assetInfo | Query order quantity precision per asset(USER_DATA)
[**get_convert_exchange_info_v1**](ConvertApi.md#get_convert_exchange_info_v1) | **GET** /sapi/v1/convert/exchangeInfo | List All Convert Pairs
[**get_convert_order_status_v1**](ConvertApi.md#get_convert_order_status_v1) | **GET** /sapi/v1/convert/orderStatus | Order status(USER_DATA)
[**get_convert_trade_flow_v1**](ConvertApi.md#get_convert_trade_flow_v1) | **GET** /sapi/v1/convert/tradeFlow | Get Convert Trade History(USER_DATA)


# **create_convert_accept_quote_v1**
> CreateConvertAcceptQuoteV1Resp create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)

Accept Quote (TRADE)

Accept the offered quote by quote ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_convert_accept_quote_v1_resp import CreateConvertAcceptQuoteV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
    quote_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept Quote (TRADE)
        api_response = api_instance.create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)
        print("The response of ConvertApi->create_convert_accept_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->create_convert_accept_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateConvertAcceptQuoteV1Resp**](CreateConvertAcceptQuoteV1Resp.md)

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

# **create_convert_get_quote_v1**
> CreateConvertGetQuoteV1Resp create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type)

Send Quote Request(USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_convert_get_quote_v1_resp import CreateConvertGetQuoteV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
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
        api_response = api_instance.create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type)
        print("The response of ConvertApi->create_convert_get_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->create_convert_get_quote_v1: %s\n" % e)
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

[**CreateConvertGetQuoteV1Resp**](CreateConvertGetQuoteV1Resp.md)

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

# **create_convert_limit_cancel_order_v1**
> CreateConvertLimitCancelOrderV1Resp create_convert_limit_cancel_order_v1(order_id, timestamp, recv_window=recv_window)

Cancel limit order (USER_DATA)

Enable users to cancel a limit order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_convert_limit_cancel_order_v1_resp import CreateConvertLimitCancelOrderV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
    order_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel limit order (USER_DATA)
        api_response = api_instance.create_convert_limit_cancel_order_v1(order_id, timestamp, recv_window=recv_window)
        print("The response of ConvertApi->create_convert_limit_cancel_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->create_convert_limit_cancel_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateConvertLimitCancelOrderV1Resp**](CreateConvertLimitCancelOrderV1Resp.md)

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

# **create_convert_limit_place_order_v1**
> CreateConvertLimitPlaceOrderV1Resp create_convert_limit_place_order_v1(base_asset, expired_type, limit_price, quote_asset, side, timestamp, base_amount=base_amount, quote_amount=quote_amount, recv_window=recv_window, wallet_type=wallet_type)

Place limit order (USER_DATA)

Enable users to place a limit order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_convert_limit_place_order_v1_resp import CreateConvertLimitPlaceOrderV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
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
        api_response = api_instance.create_convert_limit_place_order_v1(base_asset, expired_type, limit_price, quote_asset, side, timestamp, base_amount=base_amount, quote_amount=quote_amount, recv_window=recv_window, wallet_type=wallet_type)
        print("The response of ConvertApi->create_convert_limit_place_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->create_convert_limit_place_order_v1: %s\n" % e)
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

[**CreateConvertLimitPlaceOrderV1Resp**](CreateConvertLimitPlaceOrderV1Resp.md)

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

# **create_convert_limit_query_open_orders_v1**
> CreateConvertLimitQueryOpenOrdersV1Resp create_convert_limit_query_open_orders_v1(timestamp, recv_window=recv_window)

Query limit open orders (USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_convert_limit_query_open_orders_v1_resp import CreateConvertLimitQueryOpenOrdersV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query limit open orders (USER_DATA)
        api_response = api_instance.create_convert_limit_query_open_orders_v1(timestamp, recv_window=recv_window)
        print("The response of ConvertApi->create_convert_limit_query_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->create_convert_limit_query_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateConvertLimitQueryOpenOrdersV1Resp**](CreateConvertLimitQueryOpenOrdersV1Resp.md)

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

# **get_convert_asset_info_v1**
> List[GetConvertAssetInfoV1RespItem] get_convert_asset_info_v1(timestamp, recv_window=recv_window)

Query order quantity precision per asset(USER_DATA)

Query for supported asset’s precision information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_convert_asset_info_v1_resp_item import GetConvertAssetInfoV1RespItem
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
    api_instance = binance.spot.ConvertApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query order quantity precision per asset(USER_DATA)
        api_response = api_instance.get_convert_asset_info_v1(timestamp, recv_window=recv_window)
        print("The response of ConvertApi->get_convert_asset_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->get_convert_asset_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[GetConvertAssetInfoV1RespItem]**](GetConvertAssetInfoV1RespItem.md)

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

# **get_convert_exchange_info_v1**
> List[GetConvertExchangeInfoV1RespItem] get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)

List All Convert Pairs

Query for all convertible token pairs and the tokens’ respective upper/lower limits

### Example


```python
import binance.spot
from binance.spot.models.get_convert_exchange_info_v1_resp_item import GetConvertExchangeInfoV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.ConvertApi(api_client)
    from_asset = '' # str | User spends coin (optional) (default to '')
    to_asset = '' # str | User receives coin (optional) (default to '')

    try:
        # List All Convert Pairs
        api_response = api_instance.get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)
        print("The response of ConvertApi->get_convert_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->get_convert_exchange_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**| User spends coin | [optional] [default to &#39;&#39;]
 **to_asset** | **str**| User receives coin | [optional] [default to &#39;&#39;]

### Return type

[**List[GetConvertExchangeInfoV1RespItem]**](GetConvertExchangeInfoV1RespItem.md)

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

# **get_convert_order_status_v1**
> GetConvertOrderStatusV1Resp get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)

Order status(USER_DATA)

Query order status by order ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_convert_order_status_v1_resp import GetConvertOrderStatusV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
    order_id = '' # str | Either orderId or quoteId is required (optional) (default to '')
    quote_id = '' # str | Either orderId or quoteId is required (optional) (default to '')

    try:
        # Order status(USER_DATA)
        api_response = api_instance.get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)
        print("The response of ConvertApi->get_convert_order_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->get_convert_order_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]
 **quote_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]

### Return type

[**GetConvertOrderStatusV1Resp**](GetConvertOrderStatusV1Resp.md)

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

# **get_convert_trade_flow_v1**
> GetConvertTradeFlowV1Resp get_convert_trade_flow_v1(start_time, end_time, timestamp, limit=limit, recv_window=recv_window)

Get Convert Trade History(USER_DATA)

Get Convert Trade History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_convert_trade_flow_v1_resp import GetConvertTradeFlowV1Resp
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
    api_instance = binance.spot.ConvertApi(api_client)
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    limit = 100 # int | Default 100, Max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Convert Trade History(USER_DATA)
        api_response = api_instance.get_convert_trade_flow_v1(start_time, end_time, timestamp, limit=limit, recv_window=recv_window)
        print("The response of ConvertApi->get_convert_trade_flow_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->get_convert_trade_flow_v1: %s\n" % e)
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

[**GetConvertTradeFlowV1Resp**](GetConvertTradeFlowV1Resp.md)

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

