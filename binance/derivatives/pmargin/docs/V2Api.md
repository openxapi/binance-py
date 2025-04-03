# binance.derivatives.pmargin.V2Api

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmargin_get_um_account_v2**](V2Api.md#pmargin_get_um_account_v2) | **GET** /papi/v2/um/account | Get UM Account Detail V2(USER_DATA)


# **pmargin_get_um_account_v2**
> PmarginGetUmAccountV2Resp pmargin_get_um_account_v2(timestamp, recv_window=recv_window)

Get UM Account Detail V2(USER_DATA)

Get current UM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp import PmarginGetUmAccountV2Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.V2Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Account Detail V2(USER_DATA)
        api_response = api_instance.pmargin_get_um_account_v2(timestamp, recv_window=recv_window)
        print("The response of V2Api->pmargin_get_um_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->pmargin_get_um_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmAccountV2Resp**](PmarginGetUmAccountV2Resp.md)

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

