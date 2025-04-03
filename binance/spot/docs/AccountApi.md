# binance.spot.AccountApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spot_get_account_commission_v3**](AccountApi.md#spot_get_account_commission_v3) | **GET** /api/v3/account/commission | Query Commission Rates (USER_DATA)
[**spot_get_account_v3**](AccountApi.md#spot_get_account_v3) | **GET** /api/v3/account | Account information (USER_DATA)
[**spot_get_my_allocations_v3**](AccountApi.md#spot_get_my_allocations_v3) | **GET** /api/v3/myAllocations | Query Allocations (USER_DATA)
[**spot_get_my_prevented_matches_v3**](AccountApi.md#spot_get_my_prevented_matches_v3) | **GET** /api/v3/myPreventedMatches | Query Prevented Matches (USER_DATA)
[**spot_get_my_trades_v3**](AccountApi.md#spot_get_my_trades_v3) | **GET** /api/v3/myTrades | Account trade list (USER_DATA)
[**spot_get_rate_limit_order_v3**](AccountApi.md#spot_get_rate_limit_order_v3) | **GET** /api/v3/rateLimit/order | Query Unfilled Order Count (USER_DATA)


# **spot_get_account_commission_v3**
> SpotGetAccountCommissionV3Resp spot_get_account_commission_v3(symbol)

Query Commission Rates (USER_DATA)

Get current account commission rates.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_account_commission_v3_resp import SpotGetAccountCommissionV3Resp
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
    api_instance = binance.spot.AccountApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Commission Rates (USER_DATA)
        api_response = api_instance.spot_get_account_commission_v3(symbol)
        print("The response of AccountApi->spot_get_account_commission_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_account_commission_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**SpotGetAccountCommissionV3Resp**](SpotGetAccountCommissionV3Resp.md)

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

# **spot_get_account_v3**
> SpotGetAccountV3Resp spot_get_account_v3(timestamp, omit_zero_balances=omit_zero_balances, recv_window=recv_window)

Account information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_account_v3_resp import SpotGetAccountV3Resp
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
    api_instance = binance.spot.AccountApi(api_client)
    timestamp = 56 # int | 
    omit_zero_balances = True # bool | When set to `true`, emits only the non-zero balances of an account. <br/>Default value: `false` (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Account information (USER_DATA)
        api_response = api_instance.spot_get_account_v3(timestamp, omit_zero_balances=omit_zero_balances, recv_window=recv_window)
        print("The response of AccountApi->spot_get_account_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_account_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **omit_zero_balances** | **bool**| When set to &#x60;true&#x60;, emits only the non-zero balances of an account. &lt;br/&gt;Default value: &#x60;false&#x60; | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**SpotGetAccountV3Resp**](SpotGetAccountV3Resp.md)

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

# **spot_get_my_allocations_v3**
> List[SpotGetMyAllocationsV3RespItem] spot_get_my_allocations_v3(symbol, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window, timestamp=timestamp)

Query Allocations (USER_DATA)

Retrieves allocations resulting from SOR order placement.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_my_allocations_v3_resp_item import SpotGetMyAllocationsV3RespItem
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
    api_instance = binance.spot.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_allocation_id = 56 # int |  (optional)
    limit = 500 # int | Default 500;Max 1000 (optional) (default to 500)
    order_id = 56 # int |  (optional)
    recv_window = 56 # int | The value cannot be greater than `60000`. (optional)
    timestamp = 56 # int |  (optional)

    try:
        # Query Allocations (USER_DATA)
        api_response = api_instance.spot_get_my_allocations_v3(symbol, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window, timestamp=timestamp)
        print("The response of AccountApi->spot_get_my_allocations_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_my_allocations_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_allocation_id** | **int**|  | [optional] 
 **limit** | **int**| Default 500;Max 1000 | [optional] [default to 500]
 **order_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60;. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**List[SpotGetMyAllocationsV3RespItem]**](SpotGetMyAllocationsV3RespItem.md)

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

# **spot_get_my_prevented_matches_v3**
> List[SpotGetMyPreventedMatchesV3RespItem] spot_get_my_prevented_matches_v3(symbol, timestamp, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)

Query Prevented Matches (USER_DATA)

Displays the list of orders that were expired due to STP.
These are the combinations supported:
- symbol + preventedMatchId
- symbol + orderId
- symbol + orderId + fromPreventedMatchId (limit will default to 500)
- symbol + orderId + fromPreventedMatchId + limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_my_prevented_matches_v3_resp_item import SpotGetMyPreventedMatchesV3RespItem
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
    api_instance = binance.spot.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    prevented_match_id = 56 # int |  (optional)
    order_id = 56 # int |  (optional)
    from_prevented_match_id = 56 # int |  (optional)
    limit = 500 # int | Default: `500`; Max: `1000` (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Prevented Matches (USER_DATA)
        api_response = api_instance.spot_get_my_prevented_matches_v3(symbol, timestamp, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->spot_get_my_prevented_matches_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_my_prevented_matches_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **prevented_match_id** | **int**|  | [optional] 
 **order_id** | **int**|  | [optional] 
 **from_prevented_match_id** | **int**|  | [optional] 
 **limit** | **int**| Default: &#x60;500&#x60;; Max: &#x60;1000&#x60; | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[SpotGetMyPreventedMatchesV3RespItem]**](SpotGetMyPreventedMatchesV3RespItem.md)

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

# **spot_get_my_trades_v3**
> List[SpotGetMyTradesV3RespItem] spot_get_my_trades_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account trade list (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_my_trades_v3_resp_item import SpotGetMyTradesV3RespItem
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
    api_instance = binance.spot.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | This can only be used in combination with `symbol`. (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Account trade list (USER_DATA)
        api_response = api_instance.spot_get_my_trades_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->spot_get_my_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_my_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| This can only be used in combination with &#x60;symbol&#x60;. | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[SpotGetMyTradesV3RespItem]**](SpotGetMyTradesV3RespItem.md)

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

# **spot_get_rate_limit_order_v3**
> List[SpotGetRateLimitOrderV3RespItem] spot_get_rate_limit_order_v3(timestamp, recv_window=recv_window)

Query Unfilled Order Count (USER_DATA)

Displays the user's unfilled order count for all intervals.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_rate_limit_order_v3_resp_item import SpotGetRateLimitOrderV3RespItem
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
    api_instance = binance.spot.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Unfilled Order Count (USER_DATA)
        api_response = api_instance.spot_get_rate_limit_order_v3(timestamp, recv_window=recv_window)
        print("The response of AccountApi->spot_get_rate_limit_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->spot_get_rate_limit_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[SpotGetRateLimitOrderV3RespItem]**](SpotGetRateLimitOrderV3RespItem.md)

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

