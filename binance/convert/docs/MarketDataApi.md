# binance.convert.MarketDataApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_get_convert_asset_info_v1**](MarketDataApi.md#convert_get_convert_asset_info_v1) | **GET** /sapi/v1/convert/assetInfo | Query order quantity precision per asset(USER_DATA)
[**convert_get_convert_exchange_info_v1**](MarketDataApi.md#convert_get_convert_exchange_info_v1) | **GET** /sapi/v1/convert/exchangeInfo | List All Convert Pairs


# **convert_get_convert_asset_info_v1**
> List[ConvertGetConvertAssetInfoV1RespItem] convert_get_convert_asset_info_v1(timestamp, recv_window=recv_window)

Query order quantity precision per asset(USER_DATA)

Query for supported asset’s precision information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.convert
from binance.convert.models.convert_get_convert_asset_info_v1_resp_item import ConvertGetConvertAssetInfoV1RespItem
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.convert.Configuration(
    auth=binance.convert.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.MarketDataApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query order quantity precision per asset(USER_DATA)
        api_response = api_instance.convert_get_convert_asset_info_v1(timestamp, recv_window=recv_window)
        print("The response of MarketDataApi->convert_get_convert_asset_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->convert_get_convert_asset_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[ConvertGetConvertAssetInfoV1RespItem]**](ConvertGetConvertAssetInfoV1RespItem.md)

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

# **convert_get_convert_exchange_info_v1**
> List[ConvertGetConvertExchangeInfoV1RespItem] convert_get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)

List All Convert Pairs

Query for all convertible token pairs and the tokens’ respective upper/lower limits

### Example


```python
import binance.convert
from binance.convert.models.convert_get_convert_exchange_info_v1_resp_item import ConvertGetConvertExchangeInfoV1RespItem
from binance.convert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.convert.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.convert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.convert.MarketDataApi(api_client)
    from_asset = '' # str | User spends coin (optional) (default to '')
    to_asset = '' # str | User receives coin (optional) (default to '')

    try:
        # List All Convert Pairs
        api_response = api_instance.convert_get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)
        print("The response of MarketDataApi->convert_get_convert_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->convert_get_convert_exchange_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**| User spends coin | [optional] [default to &#39;&#39;]
 **to_asset** | **str**| User receives coin | [optional] [default to &#39;&#39;]

### Return type

[**List[ConvertGetConvertExchangeInfoV1RespItem]**](ConvertGetConvertExchangeInfoV1RespItem.md)

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

