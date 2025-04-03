# binance.subaccount.V4Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_get_sub_account_assets_v4**](V4Api.md#subaccount_get_sub_account_assets_v4) | **GET** /sapi/v4/sub-account/assets | Query Sub-account Assets (For Master Account)(USER_DATA)


# **subaccount_get_sub_account_assets_v4**
> SubaccountGetSubAccountAssetsV4Resp subaccount_get_sub_account_assets_v4(email, timestamp, recv_window=recv_window)

Query Sub-account Assets (For Master Account)(USER_DATA)

Fetch sub-account assets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_assets_v4_resp import SubaccountGetSubAccountAssetsV4Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.subaccount.Configuration(
    auth=binance.subaccount.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.V4Api(api_client)
    email = '' # str | Sub Account Email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Assets (For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_sub_account_assets_v4(email, timestamp, recv_window=recv_window)
        print("The response of V4Api->subaccount_get_sub_account_assets_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V4Api->subaccount_get_sub_account_assets_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub Account Email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountAssetsV4Resp**](SubaccountGetSubAccountAssetsV4Resp.md)

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

