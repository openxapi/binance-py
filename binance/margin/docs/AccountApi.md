# binance.margin.AccountApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_create_margin_isolated_account_v1**](AccountApi.md#margin_create_margin_isolated_account_v1) | **POST** /sapi/v1/margin/isolated/account | Enable Isolated Margin Account (TRADE)
[**margin_create_margin_max_leverage_v1**](AccountApi.md#margin_create_margin_max_leverage_v1) | **POST** /sapi/v1/margin/max-leverage | Adjust cross margin max leverage (USER_DATA)
[**margin_delete_margin_isolated_account_v1**](AccountApi.md#margin_delete_margin_isolated_account_v1) | **DELETE** /sapi/v1/margin/isolated/account | Disable Isolated Margin Account (TRADE)
[**margin_get_bnb_burn_v1**](AccountApi.md#margin_get_bnb_burn_v1) | **GET** /sapi/v1/bnbBurn | Get BNB Burn Status (USER_DATA)
[**margin_get_margin_account_v1**](AccountApi.md#margin_get_margin_account_v1) | **GET** /sapi/v1/margin/account | Query Cross Margin Account Details (USER_DATA)
[**margin_get_margin_capital_flow_v1**](AccountApi.md#margin_get_margin_capital_flow_v1) | **GET** /sapi/v1/margin/capital-flow | Query Cross Isolated Margin Capital Flow (USER_DATA)
[**margin_get_margin_cross_margin_data_v1**](AccountApi.md#margin_get_margin_cross_margin_data_v1) | **GET** /sapi/v1/margin/crossMarginData | Query Cross Margin Fee Data (USER_DATA)
[**margin_get_margin_isolated_account_limit_v1**](AccountApi.md#margin_get_margin_isolated_account_limit_v1) | **GET** /sapi/v1/margin/isolated/accountLimit | Query Enabled Isolated Margin Account Limit (USER_DATA)
[**margin_get_margin_isolated_account_v1**](AccountApi.md#margin_get_margin_isolated_account_v1) | **GET** /sapi/v1/margin/isolated/account | Query Isolated Margin Account Info (USER_DATA)
[**margin_get_margin_isolated_margin_data_v1**](AccountApi.md#margin_get_margin_isolated_margin_data_v1) | **GET** /sapi/v1/margin/isolatedMarginData | Query Isolated Margin Fee Data (USER_DATA)
[**margin_get_margin_trade_coeff_v1**](AccountApi.md#margin_get_margin_trade_coeff_v1) | **GET** /sapi/v1/margin/tradeCoeff | Get Summary of Margin account (USER_DATA)


# **margin_create_margin_isolated_account_v1**
> MarginCreateMarginIsolatedAccountV1Resp margin_create_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)

Enable Isolated Margin Account (TRADE)

Enable isolated margin account for a specific symbol(Only supports activation of previously disabled accounts).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_isolated_account_v1_resp import MarginCreateMarginIsolatedAccountV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Isolated Margin Account (TRADE)
        api_response = api_instance.margin_create_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_create_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_create_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**MarginCreateMarginIsolatedAccountV1Resp**](MarginCreateMarginIsolatedAccountV1Resp.md)

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

# **margin_create_margin_max_leverage_v1**
> MarginCreateMarginMaxLeverageV1Resp margin_create_margin_max_leverage_v1(max_leverage)

Adjust cross margin max leverage (USER_DATA)

Adjust cross margin max leverage

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_max_leverage_v1_resp import MarginCreateMarginMaxLeverageV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    max_leverage = 56 # int | 

    try:
        # Adjust cross margin max leverage (USER_DATA)
        api_response = api_instance.margin_create_margin_max_leverage_v1(max_leverage)
        print("The response of AccountApi->margin_create_margin_max_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_create_margin_max_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_leverage** | **int**|  | 

### Return type

[**MarginCreateMarginMaxLeverageV1Resp**](MarginCreateMarginMaxLeverageV1Resp.md)

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

# **margin_delete_margin_isolated_account_v1**
> MarginDeleteMarginIsolatedAccountV1Resp margin_delete_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)

Disable Isolated Margin Account (TRADE)

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24
hours.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_delete_margin_isolated_account_v1_resp import MarginDeleteMarginIsolatedAccountV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Disable Isolated Margin Account (TRADE)
        api_response = api_instance.margin_delete_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_delete_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_delete_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**MarginDeleteMarginIsolatedAccountV1Resp**](MarginDeleteMarginIsolatedAccountV1Resp.md)

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

# **margin_get_bnb_burn_v1**
> MarginGetBnbBurnV1Resp margin_get_bnb_burn_v1(timestamp, recv_window=recv_window)

Get BNB Burn Status (USER_DATA)

Get BNB Burn Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_bnb_burn_v1_resp import MarginGetBnbBurnV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Get BNB Burn Status (USER_DATA)
        api_response = api_instance.margin_get_bnb_burn_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_get_bnb_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_bnb_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**MarginGetBnbBurnV1Resp**](MarginGetBnbBurnV1Resp.md)

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

# **margin_get_margin_account_v1**
> MarginGetMarginAccountV1Resp margin_get_margin_account_v1(timestamp, recv_window=recv_window)

Query Cross Margin Account Details (USER_DATA)

Query Cross Margin Account Details

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_account_v1_resp import MarginGetMarginAccountV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Cross Margin Account Details (USER_DATA)
        api_response = api_instance.margin_get_margin_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginAccountV1Resp**](MarginGetMarginAccountV1Resp.md)

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

# **margin_get_margin_capital_flow_v1**
> List[MarginGetMarginCapitalFlowV1RespItem] margin_get_margin_capital_flow_v1(timestamp, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Query Cross Isolated Margin Capital Flow (USER_DATA)

Query Cross Isolated Margin Capital Flow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_capital_flow_v1_resp_item import MarginGetMarginCapitalFlowV1RespItem
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    symbol = '' # str | 查询逐仓数据时必填 (optional) (default to '')
    type = '' # str |  (optional) (default to '')
    start_time = 56 # int | 只支持查询最近90天的数据 (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | 如设置fromId, 将返回id &gt; fromId的数据。否则将返回最新数据 (optional)
    limit = 56 # int | 每次返回的数据条数限制。默认 500; 最大 1000. (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Cross Isolated Margin Capital Flow (USER_DATA)
        api_response = api_instance.margin_get_margin_capital_flow_v1(timestamp, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_capital_flow_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_capital_flow_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **symbol** | **str**| 查询逐仓数据时必填 | [optional] [default to &#39;&#39;]
 **type** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| 只支持查询最近90天的数据 | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| 如设置fromId, 将返回id &amp;gt; fromId的数据。否则将返回最新数据 | [optional] 
 **limit** | **int**| 每次返回的数据条数限制。默认 500; 最大 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginCapitalFlowV1RespItem]**](MarginGetMarginCapitalFlowV1RespItem.md)

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

# **margin_get_margin_cross_margin_data_v1**
> List[MarginGetMarginCrossMarginDataV1RespItem] margin_get_margin_cross_margin_data_v1(timestamp, vip_level=vip_level, coin=coin, recv_window=recv_window)

Query Cross Margin Fee Data (USER_DATA)

Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_cross_margin_data_v1_resp_item import MarginGetMarginCrossMarginDataV1RespItem
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    vip_level = 56 # int | User&#39;s current specific margin data will be returned if vipLevel is omitted (optional)
    coin = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Cross Margin Fee Data (USER_DATA)
        api_response = api_instance.margin_get_margin_cross_margin_data_v1(timestamp, vip_level=vip_level, coin=coin, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_cross_margin_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_cross_margin_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **vip_level** | **int**| User&amp;#39;s current specific margin data will be returned if vipLevel is omitted | [optional] 
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginCrossMarginDataV1RespItem]**](MarginGetMarginCrossMarginDataV1RespItem.md)

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

# **margin_get_margin_isolated_account_limit_v1**
> MarginGetMarginIsolatedAccountLimitV1Resp margin_get_margin_isolated_account_limit_v1(timestamp, recv_window=recv_window)

Query Enabled Isolated Margin Account Limit (USER_DATA)

Query enabled isolated margin account limit.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_isolated_account_limit_v1_resp import MarginGetMarginIsolatedAccountLimitV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Enabled Isolated Margin Account Limit (USER_DATA)
        api_response = api_instance.margin_get_margin_isolated_account_limit_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_isolated_account_limit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_isolated_account_limit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**MarginGetMarginIsolatedAccountLimitV1Resp**](MarginGetMarginIsolatedAccountLimitV1Resp.md)

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

# **margin_get_margin_isolated_account_v1**
> MarginGetMarginIsolatedAccountV1Resp margin_get_margin_isolated_account_v1(timestamp, symbols=symbols, recv_window=recv_window)

Query Isolated Margin Account Info (USER_DATA)

Query Isolated Margin Account Info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_isolated_account_v1_resp import MarginGetMarginIsolatedAccountV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbols = '' # str | Max 5 symbols can be sent; separated by &#34;,&#34;. e.g. &#34;BTCUSDT,BNBUSDT,ADAUSDT&#34; (optional) (default to '')
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Isolated Margin Account Info (USER_DATA)
        api_response = api_instance.margin_get_margin_isolated_account_v1(timestamp, symbols=symbols, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbols** | **str**| Max 5 symbols can be sent; separated by &amp;#34;,&amp;#34;. e.g. &amp;#34;BTCUSDT,BNBUSDT,ADAUSDT&amp;#34; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**MarginGetMarginIsolatedAccountV1Resp**](MarginGetMarginIsolatedAccountV1Resp.md)

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

# **margin_get_margin_isolated_margin_data_v1**
> List[MarginGetMarginIsolatedMarginDataV1RespItem] margin_get_margin_isolated_margin_data_v1(timestamp, vip_level=vip_level, symbol=symbol, recv_window=recv_window)

Query Isolated Margin Fee Data (USER_DATA)

Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_isolated_margin_data_v1_resp_item import MarginGetMarginIsolatedMarginDataV1RespItem
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    vip_level = 56 # int | User&#39;s current specific margin data will be returned if vipLevel is omitted (optional)
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Isolated Margin Fee Data (USER_DATA)
        api_response = api_instance.margin_get_margin_isolated_margin_data_v1(timestamp, vip_level=vip_level, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_isolated_margin_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_isolated_margin_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **vip_level** | **int**| User&amp;#39;s current specific margin data will be returned if vipLevel is omitted | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginIsolatedMarginDataV1RespItem]**](MarginGetMarginIsolatedMarginDataV1RespItem.md)

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

# **margin_get_margin_trade_coeff_v1**
> MarginGetMarginTradeCoeffV1Resp margin_get_margin_trade_coeff_v1(timestamp, recv_window=recv_window)

Get Summary of Margin account (USER_DATA)

Get personal margin level information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_trade_coeff_v1_resp import MarginGetMarginTradeCoeffV1Resp
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
    api_instance = binance.margin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Margin account (USER_DATA)
        api_response = api_instance.margin_get_margin_trade_coeff_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->margin_get_margin_trade_coeff_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->margin_get_margin_trade_coeff_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**MarginGetMarginTradeCoeffV1Resp**](MarginGetMarginTradeCoeffV1Resp.md)

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

