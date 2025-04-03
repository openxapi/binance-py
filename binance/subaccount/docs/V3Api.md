# binance.subaccount.V3Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_get_sub_account_assets_v3**](V3Api.md#subaccount_get_sub_account_assets_v3) | **GET** /sapi/v3/sub-account/assets | Query Sub-account Assets(For Master Account)


# **subaccount_get_sub_account_assets_v3**
> SubaccountGetSubAccountAssetsV3Resp subaccount_get_sub_account_assets_v3(email, timestamp, recv_window=recv_window)

Query Sub-account Assets(For Master Account)

Fetch sub-account assets

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_assets_v3_resp import SubaccountGetSubAccountAssetsV3Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.V3Api(api_client)
    email = '' # str | Sub account email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Assets(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_assets_v3(email, timestamp, recv_window=recv_window)
        print("The response of V3Api->subaccount_get_sub_account_assets_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->subaccount_get_sub_account_assets_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub account email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountAssetsV3Resp**](SubaccountGetSubAccountAssetsV3Resp.md)

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

