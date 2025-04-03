# binance.wallet.AccountApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_account_disable_fast_withdraw_switch_v1**](AccountApi.md#wallet_create_account_disable_fast_withdraw_switch_v1) | **POST** /sapi/v1/account/disableFastWithdrawSwitch | Disable Fast Withdraw Switch (USER_DATA)
[**wallet_create_account_enable_fast_withdraw_switch_v1**](AccountApi.md#wallet_create_account_enable_fast_withdraw_switch_v1) | **POST** /sapi/v1/account/enableFastWithdrawSwitch | Enable Fast Withdraw Switch (USER_DATA)
[**wallet_get_account_api_restrictions_v1**](AccountApi.md#wallet_get_account_api_restrictions_v1) | **GET** /sapi/v1/account/apiRestrictions | Get API Key Permission (USER_DATA)
[**wallet_get_account_api_trading_status_v1**](AccountApi.md#wallet_get_account_api_trading_status_v1) | **GET** /sapi/v1/account/apiTradingStatus | Account API Trading Status (USER_DATA)
[**wallet_get_account_info_v1**](AccountApi.md#wallet_get_account_info_v1) | **GET** /sapi/v1/account/info | Account info (USER_DATA)
[**wallet_get_account_snapshot_v1**](AccountApi.md#wallet_get_account_snapshot_v1) | **GET** /sapi/v1/accountSnapshot | Daily Account Snapshot (USER_DATA)
[**wallet_get_account_status_v1**](AccountApi.md#wallet_get_account_status_v1) | **GET** /sapi/v1/account/status | Account Status (USER_DATA)


# **wallet_create_account_disable_fast_withdraw_switch_v1**
> object wallet_create_account_disable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)

Disable Fast Withdraw Switch (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Disable Fast Withdraw Switch (USER_DATA)
        api_response = api_instance.wallet_create_account_disable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_create_account_disable_fast_withdraw_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_create_account_disable_fast_withdraw_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

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

# **wallet_create_account_enable_fast_withdraw_switch_v1**
> object wallet_create_account_enable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)

Enable Fast Withdraw Switch (USER_DATA)

Enable Fast Withdraw Switch (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Fast Withdraw Switch (USER_DATA)
        api_response = api_instance.wallet_create_account_enable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_create_account_enable_fast_withdraw_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_create_account_enable_fast_withdraw_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

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

# **wallet_get_account_api_restrictions_v1**
> WalletGetAccountApiRestrictionsV1Resp wallet_get_account_api_restrictions_v1(timestamp, recv_window=recv_window)

Get API Key Permission (USER_DATA)

Get API Key Permission

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_api_restrictions_v1_resp import WalletGetAccountApiRestrictionsV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get API Key Permission (USER_DATA)
        api_response = api_instance.wallet_get_account_api_restrictions_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_get_account_api_restrictions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_get_account_api_restrictions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountApiRestrictionsV1Resp**](WalletGetAccountApiRestrictionsV1Resp.md)

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

# **wallet_get_account_api_trading_status_v1**
> WalletGetAccountApiTradingStatusV1Resp wallet_get_account_api_trading_status_v1(timestamp, recv_window=recv_window)

Account API Trading Status (USER_DATA)

Fetch account api trading status detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_api_trading_status_v1_resp import WalletGetAccountApiTradingStatusV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account API Trading Status (USER_DATA)
        api_response = api_instance.wallet_get_account_api_trading_status_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_get_account_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_get_account_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountApiTradingStatusV1Resp**](WalletGetAccountApiTradingStatusV1Resp.md)

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

# **wallet_get_account_info_v1**
> WalletGetAccountInfoV1Resp wallet_get_account_info_v1(timestamp, recv_window=recv_window)

Account info (USER_DATA)

Fetch account info detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_info_v1_resp import WalletGetAccountInfoV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account info (USER_DATA)
        api_response = api_instance.wallet_get_account_info_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_get_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_get_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountInfoV1Resp**](WalletGetAccountInfoV1Resp.md)

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

# **wallet_get_account_snapshot_v1**
> WalletGetAccountSnapshotV1Resp wallet_get_account_snapshot_v1(type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Daily Account Snapshot (USER_DATA)

Daily account snapshot

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_snapshot_v1_resp import WalletGetAccountSnapshotV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    type = '' # str | &#34;SPOT&#34;, &#34;MARGIN&#34;, &#34;FUTURES&#34; (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 7 # int | min 7, max 30, default 7 (optional) (default to 7)
    recv_window = 56 # int |  (optional)

    try:
        # Daily Account Snapshot (USER_DATA)
        api_response = api_instance.wallet_get_account_snapshot_v1(type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->wallet_get_account_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_get_account_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &amp;#34;SPOT&amp;#34;, &amp;#34;MARGIN&amp;#34;, &amp;#34;FUTURES&amp;#34; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| min 7, max 30, default 7 | [optional] [default to 7]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountSnapshotV1Resp**](WalletGetAccountSnapshotV1Resp.md)

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

# **wallet_get_account_status_v1**
> WalletGetAccountStatusV1Resp wallet_get_account_status_v1(timestamp, recv_window=recv_window)

Account Status (USER_DATA)

Fetch account status detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_status_v1_resp import WalletGetAccountStatusV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Status (USER_DATA)
        api_response = api_instance.wallet_get_account_status_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->wallet_get_account_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->wallet_get_account_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountStatusV1Resp**](WalletGetAccountStatusV1Resp.md)

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

