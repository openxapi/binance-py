# binance.derivatives.options.MarketMakerEndpointsApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_create_countdown_cancel_all_heart_beat_v1**](MarketMakerEndpointsApi.md#options_create_countdown_cancel_all_heart_beat_v1) | **POST** /eapi/v1/countdownCancelAllHeartBeat | Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
[**options_create_countdown_cancel_all_v1**](MarketMakerEndpointsApi.md#options_create_countdown_cancel_all_v1) | **POST** /eapi/v1/countdownCancelAll | Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**options_create_mmp_reset_v1**](MarketMakerEndpointsApi.md#options_create_mmp_reset_v1) | **POST** /eapi/v1/mmpReset | Reset Market Maker Protection Config (TRADE)
[**options_create_mmp_set_v1**](MarketMakerEndpointsApi.md#options_create_mmp_set_v1) | **POST** /eapi/v1/mmpSet | Set Market Maker Protection Config (TRADE)
[**options_get_countdown_cancel_all_v1**](MarketMakerEndpointsApi.md#options_get_countdown_cancel_all_v1) | **GET** /eapi/v1/countdownCancelAll | Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
[**options_get_margin_account_v1**](MarketMakerEndpointsApi.md#options_get_margin_account_v1) | **GET** /eapi/v1/marginAccount | Option Margin Account Information (USER_DATA)
[**options_get_mmp_v1**](MarketMakerEndpointsApi.md#options_get_mmp_v1) | **GET** /eapi/v1/mmp | Get Market Maker Protection Config (TRADE)


# **options_create_countdown_cancel_all_heart_beat_v1**
> OptionsCreateCountdownCancelAllHeartBeatV1Resp options_create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)

Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)

This endpoint resets the time from which the countdown will begin to the time this messaged is received.  It should be called repeatedly as heartbeats.  Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_countdown_cancel_all_heart_beat_v1_resp import OptionsCreateCountdownCancelAllHeartBeatV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    underlyings = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)
        api_response = api_instance.options_create_countdown_cancel_all_heart_beat_v1(timestamp, underlyings, recv_window=recv_window)
        print("The response of MarketMakerEndpointsApi->options_create_countdown_cancel_all_heart_beat_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_create_countdown_cancel_all_heart_beat_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlyings** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateCountdownCancelAllHeartBeatV1Resp**](OptionsCreateCountdownCancelAllHeartBeatV1Resp.md)

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

# **options_create_countdown_cancel_all_v1**
> OptionsCreateCountdownCancelAllV1Resp options_create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)

Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker protection and non market maker protection order types) of the underlying symbol at the end of the specified countdown time period if no heartbeat message is sent.  After the countdown time period, all open orders will be cancelled and new orders will be rejected with error code -2010 until either a heartbeat message is sent or the auto-cancel feature is turned off by setting countdownTime to 0.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_countdown_cancel_all_v1_resp import OptionsCreateCountdownCancelAllV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    countdown_time = 56 # int | 
    timestamp = 56 # int | 
    underlying = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.options_create_countdown_cancel_all_v1(countdown_time, timestamp, underlying, recv_window=recv_window)
        print("The response of MarketMakerEndpointsApi->options_create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **underlying** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateCountdownCancelAllV1Resp**](OptionsCreateCountdownCancelAllV1Resp.md)

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

# **options_create_mmp_reset_v1**
> OptionsCreateMmpResetV1Resp options_create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)

Reset Market Maker Protection Config (TRADE)

Reset MMP, start MMP order again.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_mmp_reset_v1_resp import OptionsCreateMmpResetV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')

    try:
        # Reset Market Maker Protection Config (TRADE)
        api_response = api_instance.options_create_mmp_reset_v1(timestamp, recv_window=recv_window, underlying=underlying)
        print("The response of MarketMakerEndpointsApi->options_create_mmp_reset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_create_mmp_reset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**OptionsCreateMmpResetV1Resp**](OptionsCreateMmpResetV1Resp.md)

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

# **options_create_mmp_set_v1**
> OptionsCreateMmpSetV1Resp options_create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)

Set Market Maker Protection Config (TRADE)

Set config for MMP.
Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_create_mmp_set_v1_resp import OptionsCreateMmpSetV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    delta_limit = '' # str |  (optional) (default to '')
    frozen_time_in_milliseconds = 56 # int |  (optional)
    qty_limit = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    underlying = '' # str |  (optional) (default to '')
    window_time_in_milliseconds = 56 # int |  (optional)

    try:
        # Set Market Maker Protection Config (TRADE)
        api_response = api_instance.options_create_mmp_set_v1(timestamp, delta_limit=delta_limit, frozen_time_in_milliseconds=frozen_time_in_milliseconds, qty_limit=qty_limit, recv_window=recv_window, underlying=underlying, window_time_in_milliseconds=window_time_in_milliseconds)
        print("The response of MarketMakerEndpointsApi->options_create_mmp_set_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_create_mmp_set_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **delta_limit** | **str**|  | [optional] [default to &#39;&#39;]
 **frozen_time_in_milliseconds** | **int**|  | [optional] 
 **qty_limit** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **underlying** | **str**|  | [optional] [default to &#39;&#39;]
 **window_time_in_milliseconds** | **int**|  | [optional] 

### Return type

[**OptionsCreateMmpSetV1Resp**](OptionsCreateMmpSetV1Resp.md)

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

# **options_get_countdown_cancel_all_v1**
> OptionsGetCountdownCancelAllV1Resp options_get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_countdown_cancel_all_v1_resp import OptionsGetCountdownCancelAllV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | Option underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)
        api_response = api_instance.options_get_countdown_cancel_all_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of MarketMakerEndpointsApi->options_get_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_get_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| Option underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetCountdownCancelAllV1Resp**](OptionsGetCountdownCancelAllV1Resp.md)

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

# **options_get_margin_account_v1**
> OptionsGetMarginAccountV1Resp options_get_margin_account_v1(timestamp, recv_window=recv_window)

Option Margin Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_margin_account_v1_resp import OptionsGetMarginAccountV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Margin Account Information (USER_DATA)
        api_response = api_instance.options_get_margin_account_v1(timestamp, recv_window=recv_window)
        print("The response of MarketMakerEndpointsApi->options_get_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_get_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetMarginAccountV1Resp**](OptionsGetMarginAccountV1Resp.md)

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

# **options_get_mmp_v1**
> OptionsGetMmpV1Resp options_get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)

Get Market Maker Protection Config (TRADE)

Get config for MMP.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_mmp_v1_resp import OptionsGetMmpV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketMakerEndpointsApi(api_client)
    timestamp = 56 # int | 
    underlying = '' # str | underlying, e.g BTCUSDT (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Market Maker Protection Config (TRADE)
        api_response = api_instance.options_get_mmp_v1(timestamp, underlying=underlying, recv_window=recv_window)
        print("The response of MarketMakerEndpointsApi->options_get_mmp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerEndpointsApi->options_get_mmp_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **underlying** | **str**| underlying, e.g BTCUSDT | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetMmpV1Resp**](OptionsGetMmpV1Resp.md)

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

