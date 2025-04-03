# binance.derivatives.pmargin.UserDataStreamsApi

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmargin_create_listen_key_v1**](UserDataStreamsApi.md#pmargin_create_listen_key_v1) | **POST** /papi/v1/listenKey | Start User Data Stream(USER_STREAM)
[**pmargin_delete_listen_key_v1**](UserDataStreamsApi.md#pmargin_delete_listen_key_v1) | **DELETE** /papi/v1/listenKey | Close User Data Stream(USER_STREAM)
[**pmargin_update_listen_key_v1**](UserDataStreamsApi.md#pmargin_update_listen_key_v1) | **PUT** /papi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)


# **pmargin_create_listen_key_v1**
> PmarginCreateListenKeyV1Resp pmargin_create_listen_key_v1()

Start User Data Stream(USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_listen_key_v1_resp import PmarginCreateListenKeyV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.UserDataStreamsApi(api_client)

    try:
        # Start User Data Stream(USER_STREAM)
        api_response = api_instance.pmargin_create_listen_key_v1()
        print("The response of UserDataStreamsApi->pmargin_create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->pmargin_create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PmarginCreateListenKeyV1Resp**](PmarginCreateListenKeyV1Resp.md)

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

# **pmargin_delete_listen_key_v1**
> object pmargin_delete_listen_key_v1()

Close User Data Stream(USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.UserDataStreamsApi(api_client)

    try:
        # Close User Data Stream(USER_STREAM)
        api_response = api_instance.pmargin_delete_listen_key_v1()
        print("The response of UserDataStreamsApi->pmargin_delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->pmargin_delete_listen_key_v1: %s\n" % e)
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

# **pmargin_update_listen_key_v1**
> object pmargin_update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.UserDataStreamsApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.pmargin_update_listen_key_v1()
        print("The response of UserDataStreamsApi->pmargin_update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamsApi->pmargin_update_listen_key_v1: %s\n" % e)
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

