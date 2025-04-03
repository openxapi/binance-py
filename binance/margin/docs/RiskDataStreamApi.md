# binance.margin.RiskDataStreamApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_create_margin_listen_key_v1**](RiskDataStreamApi.md#margin_create_margin_listen_key_v1) | **POST** /sapi/v1/margin/listen-key | Start User Data Stream (USER_STREAM)
[**margin_delete_margin_listen_key_v1**](RiskDataStreamApi.md#margin_delete_margin_listen_key_v1) | **DELETE** /sapi/v1/margin/listen-key | Close User Data Stream (USER_STREAM)
[**margin_update_margin_listen_key_v1**](RiskDataStreamApi.md#margin_update_margin_listen_key_v1) | **PUT** /sapi/v1/margin/listen-key | Keepalive User Data Stream (USER_STREAM)


# **margin_create_margin_listen_key_v1**
> MarginCreateMarginListenKeyV1Resp margin_create_margin_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_listen_key_v1_resp import MarginCreateMarginListenKeyV1Resp
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
    api_instance = binance.margin.RiskDataStreamApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.margin_create_margin_listen_key_v1()
        print("The response of RiskDataStreamApi->margin_create_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskDataStreamApi->margin_create_margin_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MarginCreateMarginListenKeyV1Resp**](MarginCreateMarginListenKeyV1Resp.md)

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

# **margin_delete_margin_listen_key_v1**
> object margin_delete_margin_listen_key_v1()

Close User Data Stream (USER_STREAM)

Close out a user data stream.

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
    api_instance = binance.margin.RiskDataStreamApi(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.margin_delete_margin_listen_key_v1()
        print("The response of RiskDataStreamApi->margin_delete_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskDataStreamApi->margin_delete_margin_listen_key_v1: %s\n" % e)
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

# **margin_update_margin_listen_key_v1**
> object margin_update_margin_listen_key_v1(listen_key)

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out.

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
    api_instance = binance.margin.RiskDataStreamApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.margin_update_margin_listen_key_v1(listen_key)
        print("The response of RiskDataStreamApi->margin_update_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskDataStreamApi->margin_update_margin_listen_key_v1: %s\n" % e)
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

