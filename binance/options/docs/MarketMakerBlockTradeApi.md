# binance.options.MarketMakerBlockTradeApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_block_order_create_v1**](MarketMakerBlockTradeApi.md#create_block_order_create_v1) | **POST** /eapi/v1/block/order/create | New Block Trade Order (TRADE)
[**delete_block_order_create_v1**](MarketMakerBlockTradeApi.md#delete_block_order_create_v1) | **DELETE** /eapi/v1/block/order/create | Cancel Block Trade Order (TRADE)


# **create_block_order_create_v1**
> OptionsCreateBlockOrderCreateV1Resp create_block_order_create_v1(legs, liquidity, price, quantity, side, symbol, timestamp, recv_window=recv_window)

New Block Trade Order (TRADE)

Send in a new block trade order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.models.options_create_block_order_create_v1_resp import OptionsCreateBlockOrderCreateV1Resp
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.MarketMakerBlockTradeApi(api_client)
    legs = ['legs_example'] # List[str] | 
    liquidity = '' # str |  (default to '')
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # New Block Trade Order (TRADE)
        api_response = api_instance.create_block_order_create_v1(legs, liquidity, price, quantity, side, symbol, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->create_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->create_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legs** | [**List[str]**](str.md)|  | 
 **liquidity** | **str**|  | [default to &#39;&#39;]
 **price** | **str**|  | [default to &#39;&#39;]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsCreateBlockOrderCreateV1Resp**](OptionsCreateBlockOrderCreateV1Resp.md)

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

# **delete_block_order_create_v1**
> object delete_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)

Cancel Block Trade Order (TRADE)

Cancel a block trade order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.options
from binance.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.options.Configuration(
    auth=binance.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.options.MarketMakerBlockTradeApi(api_client)
    block_order_matching_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Block Trade Order (TRADE)
        api_response = api_instance.delete_block_order_create_v1(block_order_matching_key, timestamp, recv_window=recv_window)
        print("The response of MarketMakerBlockTradeApi->delete_block_order_create_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMakerBlockTradeApi->delete_block_order_create_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_order_matching_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**object**

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

