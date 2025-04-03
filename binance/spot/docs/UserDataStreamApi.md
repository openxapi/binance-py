# binance.spot.UserDataStreamApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spot_create_user_data_stream_v3**](UserDataStreamApi.md#spot_create_user_data_stream_v3) | **POST** /api/v3/userDataStream | Start user data stream (USER_STREAM)
[**spot_delete_user_data_stream_v3**](UserDataStreamApi.md#spot_delete_user_data_stream_v3) | **DELETE** /api/v3/userDataStream | Close user data stream (USER_STREAM)
[**spot_update_user_data_stream_v3**](UserDataStreamApi.md#spot_update_user_data_stream_v3) | **PUT** /api/v3/userDataStream | Keepalive user data stream (USER_STREAM)


# **spot_create_user_data_stream_v3**
> SpotCreateUserDataStreamV3Resp spot_create_user_data_stream_v3()

Start user data stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_user_data_stream_v3_resp import SpotCreateUserDataStreamV3Resp
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
    api_instance = binance.spot.UserDataStreamApi(api_client)

    try:
        # Start user data stream (USER_STREAM)
        api_response = api_instance.spot_create_user_data_stream_v3()
        print("The response of UserDataStreamApi->spot_create_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamApi->spot_create_user_data_stream_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpotCreateUserDataStreamV3Resp**](SpotCreateUserDataStreamV3Resp.md)

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

# **spot_delete_user_data_stream_v3**
> object spot_delete_user_data_stream_v3(listen_key)

Close user data stream (USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
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
    api_instance = binance.spot.UserDataStreamApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Close user data stream (USER_STREAM)
        api_response = api_instance.spot_delete_user_data_stream_v3(listen_key)
        print("The response of UserDataStreamApi->spot_delete_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamApi->spot_delete_user_data_stream_v3: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spot_update_user_data_stream_v3**
> object spot_update_user_data_stream_v3(listen_key)

Keepalive user data stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
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
    api_instance = binance.spot.UserDataStreamApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive user data stream (USER_STREAM)
        api_response = api_instance.spot_update_user_data_stream_v3(listen_key)
        print("The response of UserDataStreamApi->spot_update_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataStreamApi->spot_update_user_data_stream_v3: %s\n" % e)
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

