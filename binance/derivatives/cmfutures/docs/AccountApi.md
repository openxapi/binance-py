# binance.derivatives.cmfutures.AccountApi

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmfutures_get_account_v1**](AccountApi.md#cmfutures_get_account_v1) | **GET** /dapi/v1/account | Account Information (USER_DATA)
[**cmfutures_get_balance_v1**](AccountApi.md#cmfutures_get_balance_v1) | **GET** /dapi/v1/balance | Futures Account Balance (USER_DATA)
[**cmfutures_get_commission_rate_v1**](AccountApi.md#cmfutures_get_commission_rate_v1) | **GET** /dapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**cmfutures_get_income_asyn_id_v1**](AccountApi.md#cmfutures_get_income_asyn_id_v1) | **GET** /dapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**cmfutures_get_income_asyn_v1**](AccountApi.md#cmfutures_get_income_asyn_v1) | **GET** /dapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**cmfutures_get_income_v1**](AccountApi.md#cmfutures_get_income_v1) | **GET** /dapi/v1/income | Get Income History(USER_DATA)
[**cmfutures_get_leverage_bracket_v1**](AccountApi.md#cmfutures_get_leverage_bracket_v1) | **GET** /dapi/v1/leverageBracket | Notional Bracket for Pair(USER_DATA)
[**cmfutures_get_leverage_bracket_v2**](AccountApi.md#cmfutures_get_leverage_bracket_v2) | **GET** /dapi/v2/leverageBracket | Notional Bracket for Symbol(USER_DATA)
[**cmfutures_get_order_asyn_id_v1**](AccountApi.md#cmfutures_get_order_asyn_id_v1) | **GET** /dapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**cmfutures_get_order_asyn_v1**](AccountApi.md#cmfutures_get_order_asyn_v1) | **GET** /dapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**cmfutures_get_position_side_dual_v1**](AccountApi.md#cmfutures_get_position_side_dual_v1) | **GET** /dapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**cmfutures_get_trade_asyn_id_v1**](AccountApi.md#cmfutures_get_trade_asyn_id_v1) | **GET** /dapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**cmfutures_get_trade_asyn_v1**](AccountApi.md#cmfutures_get_trade_asyn_v1) | **GET** /dapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)


# **cmfutures_get_account_v1**
> CmfuturesGetAccountV1Resp cmfutures_get_account_v1(timestamp, recv_window=recv_window)

Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp import CmfuturesGetAccountV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information (USER_DATA)
        api_response = api_instance.cmfutures_get_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetAccountV1Resp**](CmfuturesGetAccountV1Resp.md)

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

# **cmfutures_get_balance_v1**
> List[CmfuturesGetBalanceV1RespItem] cmfutures_get_balance_v1(timestamp, recv_window=recv_window)

Futures Account Balance (USER_DATA)

Check futures account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_balance_v1_resp_item import CmfuturesGetBalanceV1RespItem
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance (USER_DATA)
        api_response = api_instance.cmfutures_get_balance_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetBalanceV1RespItem]**](CmfuturesGetBalanceV1RespItem.md)

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

# **cmfutures_get_commission_rate_v1**
> CmfuturesGetCommissionRateV1Resp cmfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

User Commission Rate (USER_DATA)

Query user commission rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_commission_rate_v1_resp import CmfuturesGetCommissionRateV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.cmfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetCommissionRateV1Resp**](CmfuturesGetCommissionRateV1Resp.md)

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

# **cmfutures_get_income_asyn_id_v1**
> CmfuturesGetIncomeAsynIdV1Resp cmfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Transaction History Download Link by Id (USER_DATA)

Get futures transaction history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_asyn_id_v1_resp import CmfuturesGetIncomeAsynIdV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.cmfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetIncomeAsynIdV1Resp**](CmfuturesGetIncomeAsynIdV1Resp.md)

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

# **cmfutures_get_income_asyn_v1**
> CmfuturesGetIncomeAsynV1Resp cmfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Transaction History(USER_DATA)

Get download id for futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_asyn_v1_resp import CmfuturesGetIncomeAsynV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.cmfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetIncomeAsynV1Resp**](CmfuturesGetIncomeAsynV1Resp.md)

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

# **cmfutures_get_income_v1**
> List[CmfuturesGetIncomeV1RespItem] cmfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get Income History(USER_DATA)

Get income history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_income_v1_resp_item import CmfuturesGetIncomeV1RespItem
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | &#34;TRANSFER&#34;,&#34;WELCOME_BONUS&#34;, &#34;FUNDING_FEE&#34;, &#34;REALIZED_PNL&#34;, &#34;COMMISSION&#34;, &#34;INSURANCE_CLEAR&#34;, and &#34;DELIVERED_SETTELMENT&#34; (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History(USER_DATA)
        api_response = api_instance.cmfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| &amp;#34;TRANSFER&amp;#34;,&amp;#34;WELCOME_BONUS&amp;#34;, &amp;#34;FUNDING_FEE&amp;#34;, &amp;#34;REALIZED_PNL&amp;#34;, &amp;#34;COMMISSION&amp;#34;, &amp;#34;INSURANCE_CLEAR&amp;#34;, and &amp;#34;DELIVERED_SETTELMENT&amp;#34; | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetIncomeV1RespItem]**](CmfuturesGetIncomeV1RespItem.md)

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

# **cmfutures_get_leverage_bracket_v1**
> List[CmfuturesGetLeverageBracketV1RespItem] cmfutures_get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)

Notional Bracket for Pair(USER_DATA)

Not recommended to continue using this v1 endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_leverage_bracket_v1_resp_item import CmfuturesGetLeverageBracketV1RespItem
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Pair(USER_DATA)
        api_response = api_instance.cmfutures_get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetLeverageBracketV1RespItem]**](CmfuturesGetLeverageBracketV1RespItem.md)

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

# **cmfutures_get_leverage_bracket_v2**
> List[CmfuturesGetLeverageBracketV2RespItem] cmfutures_get_leverage_bracket_v2(timestamp, symbol=symbol, recv_window=recv_window)

Notional Bracket for Symbol(USER_DATA)

Get the symbol's notional bracket list.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_leverage_bracket_v2_resp_item import CmfuturesGetLeverageBracketV2RespItem
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Symbol(USER_DATA)
        api_response = api_instance.cmfutures_get_leverage_bracket_v2(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_leverage_bracket_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_leverage_bracket_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetLeverageBracketV2RespItem]**](CmfuturesGetLeverageBracketV2RespItem.md)

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

# **cmfutures_get_order_asyn_id_v1**
> CmfuturesGetOrderAsynIdV1Resp cmfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Order History Download Link by Id (USER_DATA)

Get futures order history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_asyn_id_v1_resp import CmfuturesGetOrderAsynIdV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.cmfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetOrderAsynIdV1Resp**](CmfuturesGetOrderAsynIdV1Resp.md)

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

# **cmfutures_get_order_asyn_v1**
> CmfuturesGetOrderAsynV1Resp cmfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_order_asyn_v1_resp import CmfuturesGetOrderAsynV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.cmfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetOrderAsynV1Resp**](CmfuturesGetOrderAsynV1Resp.md)

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

# **cmfutures_get_position_side_dual_v1**
> CmfuturesGetPositionSideDualV1Resp cmfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)

Get Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_position_side_dual_v1_resp import CmfuturesGetPositionSideDualV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.cmfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetPositionSideDualV1Resp**](CmfuturesGetPositionSideDualV1Resp.md)

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

# **cmfutures_get_trade_asyn_id_v1**
> CmfuturesGetTradeAsynIdV1Resp cmfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Trade Download Link by Id(USER_DATA)

Get futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trade_asyn_id_v1_resp import CmfuturesGetTradeAsynIdV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.cmfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetTradeAsynIdV1Resp**](CmfuturesGetTradeAsynIdV1Resp.md)

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

# **cmfutures_get_trade_asyn_v1**
> CmfuturesGetTradeAsynV1Resp cmfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Trade History (USER_DATA)

Get download id for futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trade_asyn_v1_resp import CmfuturesGetTradeAsynV1Resp
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
    api_instance = binance.derivatives.cmfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.cmfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->cmfutures_get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->cmfutures_get_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CmfuturesGetTradeAsynV1Resp**](CmfuturesGetTradeAsynV1Resp.md)

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

