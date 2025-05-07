# binance.spot.C2cApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_c2c_order_match_list_user_order_history_v1**](C2cApi.md#get_c2c_order_match_list_user_order_history_v1) | **GET** /sapi/v1/c2c/orderMatch/listUserOrderHistory | Get C2C Trade History (USER_DATA)


# **get_c2c_order_match_list_user_order_history_v1**
> GetC2cOrderMatchListUserOrderHistoryV1Resp get_c2c_order_match_list_user_order_history_v1(timestamp, start_time=start_time, end_time=end_time, page=page, recv_window=recv_window)

Get C2C Trade History (USER_DATA)

Get C2C Trade History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_c2c_order_match_list_user_order_history_v1_resp import GetC2cOrderMatchListUserOrderHistoryV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.C2cApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 1 # int | Default 1 (optional) (default to 1)
    recv_window = 56 # int |  (optional)

    try:
        # Get C2C Trade History (USER_DATA)
        api_response = api_instance.get_c2c_order_match_list_user_order_history_v1(timestamp, start_time=start_time, end_time=end_time, page=page, recv_window=recv_window)
        print("The response of C2cApi->get_c2c_order_match_list_user_order_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling C2cApi->get_c2c_order_match_list_user_order_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| Default 1 | [optional] [default to 1]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetC2cOrderMatchListUserOrderHistoryV1Resp**](GetC2cOrderMatchListUserOrderHistoryV1Resp.md)

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

