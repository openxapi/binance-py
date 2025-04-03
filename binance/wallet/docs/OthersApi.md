# binance.wallet.OthersApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_get_system_status_v1**](OthersApi.md#wallet_get_system_status_v1) | **GET** /sapi/v1/system/status | System Status (System)


# **wallet_get_system_status_v1**
> WalletGetSystemStatusV1Resp wallet_get_system_status_v1()

System Status (System)

Fetch system status.

### Example


```python
import binance.wallet
from binance.wallet.models.wallet_get_system_status_v1_resp import WalletGetSystemStatusV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.OthersApi(api_client)

    try:
        # System Status (System)
        api_response = api_instance.wallet_get_system_status_v1()
        print("The response of OthersApi->wallet_get_system_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->wallet_get_system_status_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletGetSystemStatusV1Resp**](WalletGetSystemStatusV1Resp.md)

### Authorization

No authorization required

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

