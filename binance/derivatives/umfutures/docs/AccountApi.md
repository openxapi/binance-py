# binance.derivatives.umfutures.AccountApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_create_fee_burn_v1**](AccountApi.md#umfutures_create_fee_burn_v1) | **POST** /fapi/v1/feeBurn | Toggle BNB Burn On Futures Trade (TRADE)
[**umfutures_get_account_config_v1**](AccountApi.md#umfutures_get_account_config_v1) | **GET** /fapi/v1/accountConfig | Futures Account Configuration(USER_DATA)
[**umfutures_get_account_v2**](AccountApi.md#umfutures_get_account_v2) | **GET** /fapi/v2/account | Account Information V2(USER_DATA)
[**umfutures_get_account_v3**](AccountApi.md#umfutures_get_account_v3) | **GET** /fapi/v3/account | Account Information V3(USER_DATA)
[**umfutures_get_api_trading_status_v1**](AccountApi.md#umfutures_get_api_trading_status_v1) | **GET** /fapi/v1/apiTradingStatus | Futures Trading Quantitative Rules Indicators (USER_DATA)
[**umfutures_get_balance_v2**](AccountApi.md#umfutures_get_balance_v2) | **GET** /fapi/v2/balance | Futures Account Balance V2 (USER_DATA)
[**umfutures_get_balance_v3**](AccountApi.md#umfutures_get_balance_v3) | **GET** /fapi/v3/balance | Futures Account Balance V3 (USER_DATA)
[**umfutures_get_commission_rate_v1**](AccountApi.md#umfutures_get_commission_rate_v1) | **GET** /fapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**umfutures_get_fee_burn_v1**](AccountApi.md#umfutures_get_fee_burn_v1) | **GET** /fapi/v1/feeBurn | Get BNB Burn Status (USER_DATA)
[**umfutures_get_income_asyn_id_v1**](AccountApi.md#umfutures_get_income_asyn_id_v1) | **GET** /fapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**umfutures_get_income_asyn_v1**](AccountApi.md#umfutures_get_income_asyn_v1) | **GET** /fapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**umfutures_get_income_v1**](AccountApi.md#umfutures_get_income_v1) | **GET** /fapi/v1/income | Get Income History (USER_DATA)
[**umfutures_get_leverage_bracket_v1**](AccountApi.md#umfutures_get_leverage_bracket_v1) | **GET** /fapi/v1/leverageBracket | Notional and Leverage Brackets (USER_DATA)
[**umfutures_get_multi_assets_margin_v1**](AccountApi.md#umfutures_get_multi_assets_margin_v1) | **GET** /fapi/v1/multiAssetsMargin | Get Current Multi-Assets Mode (USER_DATA)
[**umfutures_get_order_asyn_id_v1**](AccountApi.md#umfutures_get_order_asyn_id_v1) | **GET** /fapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**umfutures_get_order_asyn_v1**](AccountApi.md#umfutures_get_order_asyn_v1) | **GET** /fapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**umfutures_get_position_side_dual_v1**](AccountApi.md#umfutures_get_position_side_dual_v1) | **GET** /fapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**umfutures_get_rate_limit_order_v1**](AccountApi.md#umfutures_get_rate_limit_order_v1) | **GET** /fapi/v1/rateLimit/order | Query User Rate Limit (USER_DATA)
[**umfutures_get_symbol_config_v1**](AccountApi.md#umfutures_get_symbol_config_v1) | **GET** /fapi/v1/symbolConfig | Symbol Configuration(USER_DATA)
[**umfutures_get_trade_asyn_id_v1**](AccountApi.md#umfutures_get_trade_asyn_id_v1) | **GET** /fapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**umfutures_get_trade_asyn_v1**](AccountApi.md#umfutures_get_trade_asyn_v1) | **GET** /fapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)


# **umfutures_create_fee_burn_v1**
> UmfuturesCreateFeeBurnV1Resp umfutures_create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)

Toggle BNB Burn On Futures Trade (TRADE)

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_fee_burn_v1_resp import UmfuturesCreateFeeBurnV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    fee_burn = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Toggle BNB Burn On Futures Trade (TRADE)
        api_response = api_instance.umfutures_create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_create_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_create_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_burn** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateFeeBurnV1Resp**](UmfuturesCreateFeeBurnV1Resp.md)

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

# **umfutures_get_account_config_v1**
> UmfuturesGetAccountConfigV1Resp umfutures_get_account_config_v1(timestamp, recv_window=recv_window)

Futures Account Configuration(USER_DATA)

Query account configuration

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_account_config_v1_resp import UmfuturesGetAccountConfigV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Configuration(USER_DATA)
        api_response = api_instance.umfutures_get_account_config_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_account_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_account_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetAccountConfigV1Resp**](UmfuturesGetAccountConfigV1Resp.md)

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

# **umfutures_get_account_v2**
> UmfuturesGetAccountV2Resp umfutures_get_account_v2(timestamp, recv_window=recv_window)

Account Information V2(USER_DATA)

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_account_v2_resp import UmfuturesGetAccountV2Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information V2(USER_DATA)
        api_response = api_instance.umfutures_get_account_v2(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetAccountV2Resp**](UmfuturesGetAccountV2Resp.md)

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

# **umfutures_get_account_v3**
> UmfuturesGetAccountV3Resp umfutures_get_account_v3(timestamp, recv_window=recv_window)

Account Information V3(USER_DATA)

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp import UmfuturesGetAccountV3Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information V3(USER_DATA)
        api_response = api_instance.umfutures_get_account_v3(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_account_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_account_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetAccountV3Resp**](UmfuturesGetAccountV3Resp.md)

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

# **umfutures_get_api_trading_status_v1**
> UmfuturesGetApiTradingStatusV1Resp umfutures_get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)

Futures Trading Quantitative Rules Indicators (USER_DATA)

Futures trading quantitative rules indicators, for more information on this, please refer to the Futures Trading Quantitative Rules

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_api_trading_status_v1_resp import UmfuturesGetApiTradingStatusV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Futures Trading Quantitative Rules Indicators (USER_DATA)
        api_response = api_instance.umfutures_get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetApiTradingStatusV1Resp**](UmfuturesGetApiTradingStatusV1Resp.md)

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

# **umfutures_get_balance_v2**
> List[UmfuturesGetBalanceV2RespItem] umfutures_get_balance_v2(timestamp, recv_window=recv_window)

Futures Account Balance V2 (USER_DATA)

Query account balance info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_balance_v2_resp_item import UmfuturesGetBalanceV2RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance V2 (USER_DATA)
        api_response = api_instance.umfutures_get_balance_v2(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_balance_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_balance_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetBalanceV2RespItem]**](UmfuturesGetBalanceV2RespItem.md)

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

# **umfutures_get_balance_v3**
> List[UmfuturesGetBalanceV3RespItem] umfutures_get_balance_v3(timestamp, recv_window=recv_window)

Futures Account Balance V3 (USER_DATA)

Query account balance info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_balance_v3_resp_item import UmfuturesGetBalanceV3RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance V3 (USER_DATA)
        api_response = api_instance.umfutures_get_balance_v3(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_balance_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_balance_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetBalanceV3RespItem]**](UmfuturesGetBalanceV3RespItem.md)

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

# **umfutures_get_commission_rate_v1**
> UmfuturesGetCommissionRateV1Resp umfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

User Commission Rate (USER_DATA)

Get User Commission Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_commission_rate_v1_resp import UmfuturesGetCommissionRateV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.umfutures_get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetCommissionRateV1Resp**](UmfuturesGetCommissionRateV1Resp.md)

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

# **umfutures_get_fee_burn_v1**
> UmfuturesGetFeeBurnV1Resp umfutures_get_fee_burn_v1(timestamp, recv_window=recv_window)

Get BNB Burn Status (USER_DATA)

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_fee_burn_v1_resp import UmfuturesGetFeeBurnV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get BNB Burn Status (USER_DATA)
        api_response = api_instance.umfutures_get_fee_burn_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetFeeBurnV1Resp**](UmfuturesGetFeeBurnV1Resp.md)

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

# **umfutures_get_income_asyn_id_v1**
> UmfuturesGetIncomeAsynIdV1Resp umfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Transaction History Download Link by Id (USER_DATA)

Get futures transaction history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_id_v1_resp import UmfuturesGetIncomeAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.umfutures_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetIncomeAsynIdV1Resp**](UmfuturesGetIncomeAsynIdV1Resp.md)

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

# **umfutures_get_income_asyn_v1**
> UmfuturesGetIncomeAsynV1Resp umfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Transaction History(USER_DATA)

Get download id for futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_asyn_v1_resp import UmfuturesGetIncomeAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.umfutures_get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetIncomeAsynV1Resp**](UmfuturesGetIncomeAsynV1Resp.md)

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

# **umfutures_get_income_v1**
> List[UmfuturesGetIncomeV1RespItem] umfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get Income History (USER_DATA)

Query income history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_income_v1_resp_item import UmfuturesGetIncomeV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History (USER_DATA)
        api_response = api_instance.umfutures_get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetIncomeV1RespItem]**](UmfuturesGetIncomeV1RespItem.md)

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

# **umfutures_get_leverage_bracket_v1**
> UmfuturesGetLeverageBracketV1Resp umfutures_get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

Notional and Leverage Brackets (USER_DATA)

Query user notional and leverage bracket on speicfic symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional and Leverage Brackets (USER_DATA)
        api_response = api_instance.umfutures_get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetLeverageBracketV1Resp**](UmfuturesGetLeverageBracketV1Resp.md)

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

# **umfutures_get_multi_assets_margin_v1**
> UmfuturesGetMultiAssetsMarginV1Resp umfutures_get_multi_assets_margin_v1(timestamp, recv_window=recv_window)

Get Current Multi-Assets Mode (USER_DATA)

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_multi_assets_margin_v1_resp import UmfuturesGetMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Multi-Assets Mode (USER_DATA)
        api_response = api_instance.umfutures_get_multi_assets_margin_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetMultiAssetsMarginV1Resp**](UmfuturesGetMultiAssetsMarginV1Resp.md)

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

# **umfutures_get_order_asyn_id_v1**
> UmfuturesGetOrderAsynIdV1Resp umfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Order History Download Link by Id (USER_DATA)

Get futures order history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_id_v1_resp import UmfuturesGetOrderAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.umfutures_get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderAsynIdV1Resp**](UmfuturesGetOrderAsynIdV1Resp.md)

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

# **umfutures_get_order_asyn_v1**
> UmfuturesGetOrderAsynV1Resp umfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_asyn_v1_resp import UmfuturesGetOrderAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.umfutures_get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderAsynV1Resp**](UmfuturesGetOrderAsynV1Resp.md)

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

# **umfutures_get_position_side_dual_v1**
> UmfuturesGetPositionSideDualV1Resp umfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)

Get Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_side_dual_v1_resp import UmfuturesGetPositionSideDualV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.umfutures_get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetPositionSideDualV1Resp**](UmfuturesGetPositionSideDualV1Resp.md)

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

# **umfutures_get_rate_limit_order_v1**
> List[UmfuturesGetRateLimitOrderV1RespItem] umfutures_get_rate_limit_order_v1(timestamp, recv_window=recv_window)

Query User Rate Limit (USER_DATA)

Query User Rate Limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_rate_limit_order_v1_resp_item import UmfuturesGetRateLimitOrderV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query User Rate Limit (USER_DATA)
        api_response = api_instance.umfutures_get_rate_limit_order_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetRateLimitOrderV1RespItem]**](UmfuturesGetRateLimitOrderV1RespItem.md)

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

# **umfutures_get_symbol_config_v1**
> List[UmfuturesGetSymbolConfigV1RespItem] umfutures_get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)

Symbol Configuration(USER_DATA)

Get current account symbol configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_symbol_config_v1_resp_item import UmfuturesGetSymbolConfigV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Symbol Configuration(USER_DATA)
        api_response = api_instance.umfutures_get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_symbol_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_symbol_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetSymbolConfigV1RespItem]**](UmfuturesGetSymbolConfigV1RespItem.md)

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

# **umfutures_get_trade_asyn_id_v1**
> UmfuturesGetTradeAsynIdV1Resp umfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Trade Download Link by Id(USER_DATA)

Get futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_id_v1_resp import UmfuturesGetTradeAsynIdV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.umfutures_get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetTradeAsynIdV1Resp**](UmfuturesGetTradeAsynIdV1Resp.md)

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

# **umfutures_get_trade_asyn_v1**
> UmfuturesGetTradeAsynV1Resp umfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Trade History (USER_DATA)

Get download id for futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trade_asyn_v1_resp import UmfuturesGetTradeAsynV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.umfutures_get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->umfutures_get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->umfutures_get_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetTradeAsynV1Resp**](UmfuturesGetTradeAsynV1Resp.md)

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

