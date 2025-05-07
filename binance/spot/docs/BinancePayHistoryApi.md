# binance.spot.BinancePayHistoryApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pay_transactions_v1**](BinancePayHistoryApi.md#get_pay_transactions_v1) | **GET** /sapi/v1/pay/transactions | Get Pay Trade History


# **get_pay_transactions_v1**
> GetPayTransactionsV1Resp get_pay_transactions_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Pay Trade History

Get Pay Trade History

### Example


```python
import binance.spot
from binance.spot.models.get_pay_transactions_v1_resp import GetPayTransactionsV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.BinancePayHistoryApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 100 # int | default 100, max 100 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Pay Trade History
        api_response = api_instance.get_pay_transactions_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinancePayHistoryApi->get_pay_transactions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinancePayHistoryApi->get_pay_transactions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 100, max 100 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPayTransactionsV1Resp**](GetPayTransactionsV1Resp.md)

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

