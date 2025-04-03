# binance.derivatives.umfutures.ConvertApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_create_convert_accept_quote_v1**](ConvertApi.md#umfutures_create_convert_accept_quote_v1) | **POST** /fapi/v1/convert/acceptQuote | Accept the offered quote (USER_DATA)
[**umfutures_create_convert_get_quote_v1**](ConvertApi.md#umfutures_create_convert_get_quote_v1) | **POST** /fapi/v1/convert/getQuote | Send Quote Request(USER_DATA)
[**umfutures_get_convert_exchange_info_v1**](ConvertApi.md#umfutures_get_convert_exchange_info_v1) | **GET** /fapi/v1/convert/exchangeInfo | List All Convert Pairs
[**umfutures_get_convert_order_status_v1**](ConvertApi.md#umfutures_get_convert_order_status_v1) | **GET** /fapi/v1/convert/orderStatus | Order status(USER_DATA)


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
    api_instance = binance.derivatives.umfutures.ConvertApi(api_client)
    quote_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept the offered quote (USER_DATA)
        api_response = api_instance.umfutures_create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)
        print("The response of ConvertApi->umfutures_create_convert_accept_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->umfutures_create_convert_accept_quote_v1: %s\n" % e)
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
    api_instance = binance.derivatives.umfutures.ConvertApi(api_client)
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
        print("The response of ConvertApi->umfutures_create_convert_get_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->umfutures_create_convert_get_quote_v1: %s\n" % e)
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
    api_instance = binance.derivatives.umfutures.ConvertApi(api_client)
    from_asset = '' # str | User spends coin (optional) (default to '')
    to_asset = '' # str | User receives coin (optional) (default to '')

    try:
        # List All Convert Pairs
        api_response = api_instance.umfutures_get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)
        print("The response of ConvertApi->umfutures_get_convert_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->umfutures_get_convert_exchange_info_v1: %s\n" % e)
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
    api_instance = binance.derivatives.umfutures.ConvertApi(api_client)
    order_id = '' # str | Either orderId or quoteId is required (optional) (default to '')
    quote_id = '' # str | Either orderId or quoteId is required (optional) (default to '')

    try:
        # Order status(USER_DATA)
        api_response = api_instance.umfutures_get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)
        print("The response of ConvertApi->umfutures_get_convert_order_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertApi->umfutures_get_convert_order_status_v1: %s\n" % e)
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

