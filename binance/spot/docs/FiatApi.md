# binance.spot.FiatApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fiat_orders_v1**](FiatApi.md#get_fiat_orders_v1) | **GET** /sapi/v1/fiat/orders | Get Fiat Deposit/Withdraw History (USER_DATA)
[**get_fiat_payments_v1**](FiatApi.md#get_fiat_payments_v1) | **GET** /sapi/v1/fiat/payments | Get Fiat Payments History (USER_DATA)


# **get_fiat_orders_v1**
> GetFiatOrdersV1Resp get_fiat_orders_v1(transaction_type, timestamp, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)

Get Fiat Deposit/Withdraw History (USER_DATA)

Get Fiat Deposit/Withdraw History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_fiat_orders_v1_resp import GetFiatOrdersV1Resp
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
    api_instance = binance.spot.FiatApi(api_client)
    transaction_type = '' # str | 0-deposit,1-withdraw (default to '')
    timestamp = 56 # int | 
    begin_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 1 # int | default 1 (optional) (default to 1)
    rows = 100 # int | default 100, max 500 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Fiat Deposit/Withdraw History (USER_DATA)
        api_response = api_instance.get_fiat_orders_v1(transaction_type, timestamp, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)
        print("The response of FiatApi->get_fiat_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatApi->get_fiat_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **str**| 0-deposit,1-withdraw | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **begin_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| default 1 | [optional] [default to 1]
 **rows** | **int**| default 100, max 500 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetFiatOrdersV1Resp**](GetFiatOrdersV1Resp.md)

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

# **get_fiat_payments_v1**
> GetFiatPaymentsV1Resp get_fiat_payments_v1(transaction_type, timestamp, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)

Get Fiat Payments History (USER_DATA)

Get Fiat Deposit/Withdraw History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_fiat_payments_v1_resp import GetFiatPaymentsV1Resp
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
    api_instance = binance.spot.FiatApi(api_client)
    transaction_type = '' # str | 0-buy,1-sell (default to '')
    timestamp = 56 # int | 
    begin_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 1 # int | default 1 (optional) (default to 1)
    rows = 100 # int | default 100, max 500 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Fiat Payments History (USER_DATA)
        api_response = api_instance.get_fiat_payments_v1(transaction_type, timestamp, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)
        print("The response of FiatApi->get_fiat_payments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatApi->get_fiat_payments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **str**| 0-buy,1-sell | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **begin_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| default 1 | [optional] [default to 1]
 **rows** | **int**| default 100, max 500 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetFiatPaymentsV1Resp**](GetFiatPaymentsV1Resp.md)

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

