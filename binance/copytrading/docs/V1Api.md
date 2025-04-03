# binance.copytrading.V1Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copytrading_get_copy_trading_futures_lead_symbol_v1**](V1Api.md#copytrading_get_copy_trading_futures_lead_symbol_v1) | **GET** /sapi/v1/copyTrading/futures/leadSymbol | Get Futures Lead Trading Symbol Whitelist(USER_DATA)
[**copytrading_get_copy_trading_futures_user_status_v1**](V1Api.md#copytrading_get_copy_trading_futures_user_status_v1) | **GET** /sapi/v1/copyTrading/futures/userStatus | Get Futures Lead Trader Status(TRADE)


# **copytrading_get_copy_trading_futures_lead_symbol_v1**
> CopytradingGetCopyTradingFuturesLeadSymbolV1Resp copytrading_get_copy_trading_futures_lead_symbol_v1(timestamp, recv_window=recv_window)

Get Futures Lead Trading Symbol Whitelist(USER_DATA)

Get Futures Lead Trading Symbol Whitelist

### Example

* Api Key Authentication (ApiKey):

```python
import binance.copytrading
from binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp import CopytradingGetCopyTradingFuturesLeadSymbolV1Resp
from binance.copytrading.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.copytrading.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.copytrading.Configuration(
    auth=binance.copytrading.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.copytrading.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.copytrading.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Lead Trading Symbol Whitelist(USER_DATA)
        api_response = api_instance.copytrading_get_copy_trading_futures_lead_symbol_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->copytrading_get_copy_trading_futures_lead_symbol_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->copytrading_get_copy_trading_futures_lead_symbol_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CopytradingGetCopyTradingFuturesLeadSymbolV1Resp**](CopytradingGetCopyTradingFuturesLeadSymbolV1Resp.md)

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

# **copytrading_get_copy_trading_futures_user_status_v1**
> CopytradingGetCopyTradingFuturesUserStatusV1Resp copytrading_get_copy_trading_futures_user_status_v1(timestamp, recv_window=recv_window)

Get Futures Lead Trader Status(TRADE)

Get Futures Lead Trader Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.copytrading
from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp import CopytradingGetCopyTradingFuturesUserStatusV1Resp
from binance.copytrading.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.copytrading.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.copytrading.Configuration(
    auth=binance.copytrading.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.copytrading.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.copytrading.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Lead Trader Status(TRADE)
        api_response = api_instance.copytrading_get_copy_trading_futures_user_status_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->copytrading_get_copy_trading_futures_user_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->copytrading_get_copy_trading_futures_user_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CopytradingGetCopyTradingFuturesUserStatusV1Resp**](CopytradingGetCopyTradingFuturesUserStatusV1Resp.md)

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

