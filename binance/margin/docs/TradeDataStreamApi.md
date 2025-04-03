# binance.margin.TradeDataStreamApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_create_user_data_stream_isolated_v1**](TradeDataStreamApi.md#margin_create_user_data_stream_isolated_v1) | **POST** /sapi/v1/userDataStream/isolated | Start Isolated Margin User Data Stream (USER_STREAM)
[**margin_create_user_data_stream_v1**](TradeDataStreamApi.md#margin_create_user_data_stream_v1) | **POST** /sapi/v1/userDataStream | Start Margin User Data Stream (USER_STREAM)
[**margin_delete_user_data_stream_isolated_v1**](TradeDataStreamApi.md#margin_delete_user_data_stream_isolated_v1) | **DELETE** /sapi/v1/userDataStream/isolated | Close Isolated Margin User Data Stream (USER_STREAM)
[**margin_delete_user_data_stream_v1**](TradeDataStreamApi.md#margin_delete_user_data_stream_v1) | **DELETE** /sapi/v1/userDataStream | Close Margin User Data Stream (USER_STREAM)
[**margin_update_user_data_stream_isolated_v1**](TradeDataStreamApi.md#margin_update_user_data_stream_isolated_v1) | **PUT** /sapi/v1/userDataStream/isolated | Keepalive Isolated Margin User Data Stream (USER_STREAM)
[**margin_update_user_data_stream_v1**](TradeDataStreamApi.md#margin_update_user_data_stream_v1) | **PUT** /sapi/v1/userDataStream | Keepalive Margin User Data Stream (USER_STREAM)


# **margin_create_user_data_stream_isolated_v1**
> MarginCreateUserDataStreamIsolatedV1Resp margin_create_user_data_stream_isolated_v1(symbol)

Start Isolated Margin User Data Stream (USER_STREAM)

Start a new isolated margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_user_data_stream_isolated_v1_resp import MarginCreateUserDataStreamIsolatedV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Start Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_create_user_data_stream_isolated_v1(symbol)
        print("The response of TradeDataStreamApi->margin_create_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_create_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**MarginCreateUserDataStreamIsolatedV1Resp**](MarginCreateUserDataStreamIsolatedV1Resp.md)

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

# **margin_create_user_data_stream_v1**
> MarginCreateUserDataStreamV1Resp margin_create_user_data_stream_v1()

Start Margin User Data Stream (USER_STREAM)

Start a new margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_user_data_stream_v1_resp import MarginCreateUserDataStreamV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)

    try:
        # Start Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_create_user_data_stream_v1()
        print("The response of TradeDataStreamApi->margin_create_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_create_user_data_stream_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MarginCreateUserDataStreamV1Resp**](MarginCreateUserDataStreamV1Resp.md)

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

# **margin_delete_user_data_stream_isolated_v1**
> object margin_delete_user_data_stream_isolated_v1(symbol, listenkey)

Close Isolated Margin User Data Stream (USER_STREAM)

Close out a isolated margin user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)
    symbol = '' # str |  (default to '')
    listenkey = '' # str |  (default to '')

    try:
        # Close Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_delete_user_data_stream_isolated_v1(symbol, listenkey)
        print("The response of TradeDataStreamApi->margin_delete_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_delete_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **listenkey** | **str**|  | [default to &#39;&#39;]

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

# **margin_delete_user_data_stream_v1**
> object margin_delete_user_data_stream_v1(listenkey)

Close Margin User Data Stream (USER_STREAM)

Close out a Margin user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)
    listenkey = '' # str |  (default to '')

    try:
        # Close Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_delete_user_data_stream_v1(listenkey)
        print("The response of TradeDataStreamApi->margin_delete_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_delete_user_data_stream_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenkey** | **str**|  | [default to &#39;&#39;]

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

# **margin_update_user_data_stream_isolated_v1**
> object margin_update_user_data_stream_isolated_v1(listen_key, symbol)

Keepalive Isolated Margin User Data Stream (USER_STREAM)

Keepalive an isolated margin user data stream to prevent a time out.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)
    listen_key = '' # str |  (default to '')
    symbol = '' # str |  (default to '')

    try:
        # Keepalive Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_update_user_data_stream_isolated_v1(listen_key, symbol)
        print("The response of TradeDataStreamApi->margin_update_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_update_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

**object**

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

# **margin_update_user_data_stream_v1**
> object margin_update_user_data_stream_v1(listen_key)

Keepalive Margin User Data Stream (USER_STREAM)

Keepalive a margin user data stream to prevent a time out.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeDataStreamApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive Margin User Data Stream (USER_STREAM)
        api_response = api_instance.margin_update_user_data_stream_v1(listen_key)
        print("The response of TradeDataStreamApi->margin_update_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeDataStreamApi->margin_update_user_data_stream_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**|  | [default to &#39;&#39;]

### Return type

**object**

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

