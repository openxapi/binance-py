# binance.spot.DualInvestmentApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dci_product_auto_compound_edit_status_v1**](DualInvestmentApi.md#create_dci_product_auto_compound_edit_status_v1) | **POST** /sapi/v1/dci/product/auto_compound/edit-status | Change Auto-Compound status(USER_DATA)
[**create_dci_product_subscribe_v1**](DualInvestmentApi.md#create_dci_product_subscribe_v1) | **POST** /sapi/v1/dci/product/subscribe | Subscribe Dual Investment products(USER_DATA)
[**get_dci_product_accounts_v1**](DualInvestmentApi.md#get_dci_product_accounts_v1) | **GET** /sapi/v1/dci/product/accounts | Check Dual Investment accounts(USER_DATA)
[**get_dci_product_list_v1**](DualInvestmentApi.md#get_dci_product_list_v1) | **GET** /sapi/v1/dci/product/list | Get Dual Investment product list
[**get_dci_product_positions_v1**](DualInvestmentApi.md#get_dci_product_positions_v1) | **GET** /sapi/v1/dci/product/positions | Get Dual Investment positions(USER_DATA)


# **create_dci_product_auto_compound_edit_status_v1**
> CreateDciProductAutoCompoundEditStatusV1Resp create_dci_product_auto_compound_edit_status_v1(position_id, timestamp, auto_compound_plan=auto_compound_plan, recv_window=recv_window)

Change Auto-Compound status(USER_DATA)

Change Auto-Compound status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_dci_product_auto_compound_edit_status_v1_resp import CreateDciProductAutoCompoundEditStatusV1Resp
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
    api_instance = binance.spot.DualInvestmentApi(api_client)
    position_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    auto_compound_plan = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Change Auto-Compound status(USER_DATA)
        api_response = api_instance.create_dci_product_auto_compound_edit_status_v1(position_id, timestamp, auto_compound_plan=auto_compound_plan, recv_window=recv_window)
        print("The response of DualInvestmentApi->create_dci_product_auto_compound_edit_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DualInvestmentApi->create_dci_product_auto_compound_edit_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **auto_compound_plan** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateDciProductAutoCompoundEditStatusV1Resp**](CreateDciProductAutoCompoundEditStatusV1Resp.md)

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

# **create_dci_product_subscribe_v1**
> CreateDciProductSubscribeV1Resp create_dci_product_subscribe_v1(auto_compound_plan, deposit_amount, id, order_id, timestamp, recv_window=recv_window)

Subscribe Dual Investment products(USER_DATA)

Subscribe Dual Investment products

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_dci_product_subscribe_v1_resp import CreateDciProductSubscribeV1Resp
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
    api_instance = binance.spot.DualInvestmentApi(api_client)
    auto_compound_plan = '' # str |  (default to '')
    deposit_amount = '' # str |  (default to '')
    id = '' # str |  (default to '')
    order_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Subscribe Dual Investment products(USER_DATA)
        api_response = api_instance.create_dci_product_subscribe_v1(auto_compound_plan, deposit_amount, id, order_id, timestamp, recv_window=recv_window)
        print("The response of DualInvestmentApi->create_dci_product_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DualInvestmentApi->create_dci_product_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_compound_plan** | **str**|  | [default to &#39;&#39;]
 **deposit_amount** | **str**|  | [default to &#39;&#39;]
 **id** | **str**|  | [default to &#39;&#39;]
 **order_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateDciProductSubscribeV1Resp**](CreateDciProductSubscribeV1Resp.md)

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

# **get_dci_product_accounts_v1**
> GetDciProductAccountsV1Resp get_dci_product_accounts_v1(timestamp, recv_window=recv_window)

Check Dual Investment accounts(USER_DATA)

Check Dual Investment accounts

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_dci_product_accounts_v1_resp import GetDciProductAccountsV1Resp
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
    api_instance = binance.spot.DualInvestmentApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Check Dual Investment accounts(USER_DATA)
        api_response = api_instance.get_dci_product_accounts_v1(timestamp, recv_window=recv_window)
        print("The response of DualInvestmentApi->get_dci_product_accounts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DualInvestmentApi->get_dci_product_accounts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetDciProductAccountsV1Resp**](GetDciProductAccountsV1Resp.md)

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

# **get_dci_product_list_v1**
> GetDciProductListV1Resp get_dci_product_list_v1(option_type, exercised_coin, invest_coin, timestamp, page_size=page_size, page_index=page_index, recv_window=recv_window)

Get Dual Investment product list

Get Dual Investment product list

### Example


```python
import binance.spot
from binance.spot.models.get_dci_product_list_v1_resp import GetDciProductListV1Resp
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
    api_instance = binance.spot.DualInvestmentApi(api_client)
    option_type = '' # str | Input CALL or PUT (default to '')
    exercised_coin = '' # str | Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you should input: `optionType`:CALL,`exercisedCoin`:USDT,`investCoin`:BNB; if you subscribe to a low buy product (put option), you should input: `optionType`:PUT,`exercisedCoin`:BNB,`investCoin`:USDT (default to '')
    invest_coin = '' # str | Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you should input: `optionType`:CALL,`exercisedCoin`:USDT,`investCoin`:BNB; if you subscribe to a low buy product (put option), you should input: `optionType`:PUT,`exercisedCoin`:BNB,`investCoin`:USDT (default to '')
    timestamp = 56 # int | 
    page_size = 10 # int | Default: 10, Maximum: 100 (optional) (default to 10)
    page_index = 1 # int | Default: 1 (optional) (default to 1)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get Dual Investment product list
        api_response = api_instance.get_dci_product_list_v1(option_type, exercised_coin, invest_coin, timestamp, page_size=page_size, page_index=page_index, recv_window=recv_window)
        print("The response of DualInvestmentApi->get_dci_product_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DualInvestmentApi->get_dci_product_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_type** | **str**| Input CALL or PUT | [default to &#39;&#39;]
 **exercised_coin** | **str**| Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you should input: &#x60;optionType&#x60;:CALL,&#x60;exercisedCoin&#x60;:USDT,&#x60;investCoin&#x60;:BNB; if you subscribe to a low buy product (put option), you should input: &#x60;optionType&#x60;:PUT,&#x60;exercisedCoin&#x60;:BNB,&#x60;investCoin&#x60;:USDT | [default to &#39;&#39;]
 **invest_coin** | **str**| Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you should input: &#x60;optionType&#x60;:CALL,&#x60;exercisedCoin&#x60;:USDT,&#x60;investCoin&#x60;:BNB; if you subscribe to a low buy product (put option), you should input: &#x60;optionType&#x60;:PUT,&#x60;exercisedCoin&#x60;:BNB,&#x60;investCoin&#x60;:USDT | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **page_size** | **int**| Default: 10, Maximum: 100 | [optional] [default to 10]
 **page_index** | **int**| Default: 1 | [optional] [default to 1]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetDciProductListV1Resp**](GetDciProductListV1Resp.md)

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

# **get_dci_product_positions_v1**
> GetDciProductPositionsV1Resp get_dci_product_positions_v1(timestamp, status=status, page_size=page_size, page_index=page_index, recv_window=recv_window)

Get Dual Investment positions(USER_DATA)

Get Dual Investment positions (batch)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_dci_product_positions_v1_resp import GetDciProductPositionsV1Resp
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
    api_instance = binance.spot.DualInvestmentApi(api_client)
    timestamp = 56 # int | 
    status = '' # str | `PENDING`:Products are purchasing, will give results later;`PURCHASE_SUCCESS`:purchase successfully;`SETTLED`: Products are finish settling;`PURCHASE_FAIL`:fail to purchase;`REFUNDING`:refund ongoing;`REFUND_SUCCESS`:refund to spot account successfully; `SETTLING`:Products are settling. If don&#39;t fill this field, will response all the position status. (optional) (default to '')
    page_size = 10 # int | Default: 10, Max:100 (optional) (default to 10)
    page_index = 56 # int | Default:1 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get Dual Investment positions(USER_DATA)
        api_response = api_instance.get_dci_product_positions_v1(timestamp, status=status, page_size=page_size, page_index=page_index, recv_window=recv_window)
        print("The response of DualInvestmentApi->get_dci_product_positions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DualInvestmentApi->get_dci_product_positions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **status** | **str**| &#x60;PENDING&#x60;:Products are purchasing, will give results later;&#x60;PURCHASE_SUCCESS&#x60;:purchase successfully;&#x60;SETTLED&#x60;: Products are finish settling;&#x60;PURCHASE_FAIL&#x60;:fail to purchase;&#x60;REFUNDING&#x60;:refund ongoing;&#x60;REFUND_SUCCESS&#x60;:refund to spot account successfully; &#x60;SETTLING&#x60;:Products are settling. If don&amp;#39;t fill this field, will response all the position status. | [optional] [default to &#39;&#39;]
 **page_size** | **int**| Default: 10, Max:100 | [optional] [default to 10]
 **page_index** | **int**| Default:1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetDciProductPositionsV1Resp**](GetDciProductPositionsV1Resp.md)

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

