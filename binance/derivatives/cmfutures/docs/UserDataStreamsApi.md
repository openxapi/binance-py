# binance.derivatives.cmfutures.UserDataStreamsApi

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmfutures_create_listen_key_v1**](UserDataStreamsApi.md#cmfutures_create_listen_key_v1) | **POST** /dapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**cmfutures_delete_listen_key_v1**](UserDataStreamsApi.md#cmfutures_delete_listen_key_v1) | **DELETE** /dapi/v1/listenKey | Close User Data Stream(USER_STREAM)
[**cmfutures_update_listen_key_v1**](UserDataStreamsApi.md#cmfutures_update_listen_key_v1) | **PUT** /dapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)


# **cmfutures_create_listen_key_v1**
> CmfuturesCreateListenKeyV1Resp cmfutures_create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_create_listen_key_v1_resp import CmfuturesCreateListenKeyV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.UserDataStreamsApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.cmfutures_create_listen_key_v1()
        print("The response of UserDataStreamsApi->cmfutures_create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->cmfutures_create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesCreateListenKeyV1Resp**](CmfuturesCreateListenKeyV1Resp.md)

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

# **cmfutures_delete_listen_key_v1**
> object cmfutures_delete_listen_key_v1()

Close User Data Stream(USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.UserDataStreamsApi(api_client)

    try:
        # Close User Data Stream(USER_STREAM)
        api_response = api_instance.cmfutures_delete_listen_key_v1()
        print("The response of UserDataStreamsApi->cmfutures_delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->cmfutures_delete_listen_key_v1: %s\n" % e)
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

# **cmfutures_update_listen_key_v1**
> object cmfutures_update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.cmfutures.Configuration(
    auth=binance.derivatives.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.UserDataStreamsApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.cmfutures_update_listen_key_v1()
        print("The response of UserDataStreamsApi->cmfutures_update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->cmfutures_update_listen_key_v1: %s\n" % e)
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

