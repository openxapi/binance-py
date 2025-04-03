# binance.derivatives.futuresdata.MarketDataApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**futuresdata_get_futures_hist_data_link_v1**](MarketDataApi.md#futuresdata_get_futures_hist_data_link_v1) | **GET** /sapi/v1/futures/histDataLink | Get Future TickLevel Orderbook Historical Data Download Link(USER_DATA)


# **futuresdata_get_futures_hist_data_link_v1**
> FuturesdataGetFuturesHistDataLinkV1Resp futuresdata_get_futures_hist_data_link_v1(symbol, data_type, start_time, end_time, timestamp, recv_window=recv_window)

Get Future TickLevel Orderbook Historical Data Download Link(USER_DATA)

Get Future TickLevel Orderbook Historical Data Download Link

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.futuresdata
from binance.derivatives.futuresdata.models.futuresdata_get_futures_hist_data_link_v1_resp import FuturesdataGetFuturesHistDataLinkV1Resp
from binance.derivatives.futuresdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.futuresdata.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.futuresdata.Configuration(
    auth=binance.derivatives.futuresdata.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.futuresdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.futuresdata.MarketDataApi(api_client)
    symbol = '' # str | symbol name, e.g. BTCUSDT or BTCUSD_PERP ｜ (default to '')
    data_type = '' # str | `T_DEPTH` for ticklevel orderbook data, `S_DEPTH` for orderbook snapshot data (default to '')
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Future TickLevel Orderbook Historical Data Download Link(USER_DATA)
        api_response = api_instance.futuresdata_get_futures_hist_data_link_v1(symbol, data_type, start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of MarketDataApi->futuresdata_get_futures_hist_data_link_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->futuresdata_get_futures_hist_data_link_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| symbol name, e.g. BTCUSDT or BTCUSD_PERP ｜ | [default to &#39;&#39;]
 **data_type** | **str**| &#x60;T_DEPTH&#x60; for ticklevel orderbook data, &#x60;S_DEPTH&#x60; for orderbook snapshot data | [default to &#39;&#39;]
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**FuturesdataGetFuturesHistDataLinkV1Resp**](FuturesdataGetFuturesHistDataLinkV1Resp.md)

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

