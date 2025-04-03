# binance.wallet.V3Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_asset_get_user_asset_v3**](V3Api.md#wallet_create_asset_get_user_asset_v3) | **POST** /sapi/v3/asset/getUserAsset | User Asset (USER_DATA)


# **wallet_create_asset_get_user_asset_v3**
> List[WalletCreateAssetGetUserAssetV3RespItem] wallet_create_asset_get_user_asset_v3(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)

User Asset (USER_DATA)

Get user assets, just for positive data.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_get_user_asset_v3_resp_item import WalletCreateAssetGetUserAssetV3RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.V3Api(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    need_btc_valuation = True # bool |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # User Asset (USER_DATA)
        api_response = api_instance.wallet_create_asset_get_user_asset_v3(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
        print("The response of V3Api->wallet_create_asset_get_user_asset_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->wallet_create_asset_get_user_asset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **need_btc_valuation** | **bool**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletCreateAssetGetUserAssetV3RespItem]**](WalletCreateAssetGetUserAssetV3RespItem.md)

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

