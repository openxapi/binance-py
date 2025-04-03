# binance.derivatives.umfutures.PortfolioMarginEndpointsApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_get_pm_account_info_v1**](PortfolioMarginEndpointsApi.md#umfutures_get_pm_account_info_v1) | **GET** /fapi/v1/pmAccountInfo | Classic Portfolio Margin Account Information (USER_DATA)


# **umfutures_get_pm_account_info_v1**
> UmfuturesGetPmAccountInfoV1Resp umfutures_get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)

Classic Portfolio Margin Account Information (USER_DATA)

Get Classic Portfolio Margin current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_pm_account_info_v1_resp import UmfuturesGetPmAccountInfoV1Resp
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
    api_instance = binance.derivatives.umfutures.PortfolioMarginEndpointsApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Classic Portfolio Margin Account Information (USER_DATA)
        api_response = api_instance.umfutures_get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginEndpointsApi->umfutures_get_pm_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginEndpointsApi->umfutures_get_pm_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetPmAccountInfoV1Resp**](UmfuturesGetPmAccountInfoV1Resp.md)

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

