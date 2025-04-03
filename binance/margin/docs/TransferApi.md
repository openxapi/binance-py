# binance.margin.TransferApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_get_margin_max_transferable_v1**](TransferApi.md#margin_get_margin_max_transferable_v1) | **GET** /sapi/v1/margin/maxTransferable | Query Max Transfer-Out Amount (USER_DATA)
[**margin_get_margin_transfer_v1**](TransferApi.md#margin_get_margin_transfer_v1) | **GET** /sapi/v1/margin/transfer | Get Cross Margin Transfer History (USER_DATA)


# **margin_get_margin_max_transferable_v1**
> MarginGetMarginMaxTransferableV1Resp margin_get_margin_max_transferable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Transfer-Out Amount (USER_DATA)

Query Max Transfer-Out Amount

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_max_transferable_v1_resp import MarginGetMarginMaxTransferableV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TransferApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Max Transfer-Out Amount (USER_DATA)
        api_response = api_instance.margin_get_margin_max_transferable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of TransferApi->margin_get_margin_max_transferable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->margin_get_margin_max_transferable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginMaxTransferableV1Resp**](MarginGetMarginMaxTransferableV1Resp.md)

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

# **margin_get_margin_transfer_v1**
> MarginGetMarginTransferV1Resp margin_get_margin_transfer_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, isolated_symbol=isolated_symbol, recv_window=recv_window)

Get Cross Margin Transfer History (USER_DATA)

Get Cross Margin Transfer History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_transfer_v1_resp import MarginGetMarginTransferV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TransferApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    type = '' # str | Transfer Type: ROLL_IN, ROLL_OUT (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    isolated_symbol = '' # str | Symbol in Isolated Margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Cross Margin Transfer History (USER_DATA)
        api_response = api_instance.margin_get_margin_transfer_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of TransferApi->margin_get_margin_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->margin_get_margin_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **type** | **str**| Transfer Type: ROLL_IN, ROLL_OUT | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **isolated_symbol** | **str**| Symbol in Isolated Margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginTransferV1Resp**](MarginGetMarginTransferV1Resp.md)

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

