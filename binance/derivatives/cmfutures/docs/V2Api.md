# binance.derivatives.cmfutures.V2Api

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmfutures_get_leverage_bracket_v2**](V2Api.md#cmfutures_get_leverage_bracket_v2) | **GET** /dapi/v2/leverageBracket | Notional Bracket for Symbol(USER_DATA)


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
    api_instance = binance.derivatives.cmfutures.V2Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Symbol(USER_DATA)
        api_response = api_instance.cmfutures_get_leverage_bracket_v2(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V2Api->cmfutures_get_leverage_bracket_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->cmfutures_get_leverage_bracket_v2: %s\n" % e)
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

