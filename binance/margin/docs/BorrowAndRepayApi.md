# binance.margin.BorrowAndRepayApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_create_margin_borrow_repay_v1**](BorrowAndRepayApi.md#margin_create_margin_borrow_repay_v1) | **POST** /sapi/v1/margin/borrow-repay | Margin account borrow/repay(MARGIN)
[**margin_get_margin_borrow_repay_v1**](BorrowAndRepayApi.md#margin_get_margin_borrow_repay_v1) | **GET** /sapi/v1/margin/borrow-repay | Query borrow/repay records in Margin account(USER_DATA)
[**margin_get_margin_interest_history_v1**](BorrowAndRepayApi.md#margin_get_margin_interest_history_v1) | **GET** /sapi/v1/margin/interestHistory | Get Interest History (USER_DATA)
[**margin_get_margin_interest_rate_history_v1**](BorrowAndRepayApi.md#margin_get_margin_interest_rate_history_v1) | **GET** /sapi/v1/margin/interestRateHistory | Query Margin Interest Rate History (USER_DATA)
[**margin_get_margin_max_borrowable_v1**](BorrowAndRepayApi.md#margin_get_margin_max_borrowable_v1) | **GET** /sapi/v1/margin/maxBorrowable | Query Max Borrow (USER_DATA)
[**margin_get_margin_next_hourly_interest_rate_v1**](BorrowAndRepayApi.md#margin_get_margin_next_hourly_interest_rate_v1) | **GET** /sapi/v1/margin/next-hourly-interest-rate | Get future hourly interest rate (USER_DATA)


# **margin_create_margin_borrow_repay_v1**
> MarginCreateMarginBorrowRepayV1Resp margin_create_margin_borrow_repay_v1(amount, asset, is_isolated, symbol, timestamp, type, recv_window=recv_window)

Margin account borrow/repay(MARGIN)

Margin account borrow/repay(MARGIN)

### Example


```python
import binance.margin
from binance.margin.models.margin_create_margin_borrow_repay_v1_resp import MarginCreateMarginBorrowRepayV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    is_isolated = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Margin account borrow/repay(MARGIN)
        api_response = api_instance.margin_create_margin_borrow_repay_v1(amount, asset, is_isolated, symbol, timestamp, type, recv_window=recv_window)
        print("The response of BorrowAndRepayApi->margin_create_margin_borrow_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_create_margin_borrow_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **is_isolated** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**MarginCreateMarginBorrowRepayV1Resp**](MarginCreateMarginBorrowRepayV1Resp.md)

### Authorization

No authorization required

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

# **margin_get_margin_borrow_repay_v1**
> MarginGetMarginBorrowRepayV1Resp margin_get_margin_borrow_repay_v1(type, timestamp, asset=asset, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Query borrow/repay records in Margin account(USER_DATA)

Query borrow/repay records in Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_borrow_repay_v1_resp import MarginGetMarginBorrowRepayV1Resp
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
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    type = '' # str | `BORROW` or `REPAY` (default to '')
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    isolated_symbol = '' # str | Symbol in Isolated Margin (optional) (default to '')
    tx_id = 56 # int | `tranId` in `POST /sapi/v1/margin/loan` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query borrow/repay records in Margin account(USER_DATA)
        api_response = api_instance.margin_get_margin_borrow_repay_v1(type, timestamp, asset=asset, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of BorrowAndRepayApi->margin_get_margin_borrow_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_get_margin_borrow_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &#x60;BORROW&#x60; or &#x60;REPAY&#x60; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **isolated_symbol** | **str**| Symbol in Isolated Margin | [optional] [default to &#39;&#39;]
 **tx_id** | **int**| &#x60;tranId&#x60; in &#x60;POST /sapi/v1/margin/loan&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**MarginGetMarginBorrowRepayV1Resp**](MarginGetMarginBorrowRepayV1Resp.md)

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

# **margin_get_margin_interest_history_v1**
> MarginGetMarginInterestHistoryV1Resp margin_get_margin_interest_history_v1(timestamp, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Interest History (USER_DATA)

Get Interest History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_interest_history_v1_resp import MarginGetMarginInterestHistoryV1Resp
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
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Interest History (USER_DATA)
        api_response = api_instance.margin_get_margin_interest_history_v1(timestamp, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of BorrowAndRepayApi->margin_get_margin_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_get_margin_interest_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginInterestHistoryV1Resp**](MarginGetMarginInterestHistoryV1Resp.md)

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

# **margin_get_margin_interest_rate_history_v1**
> List[MarginGetMarginInterestRateHistoryV1RespItem] margin_get_margin_interest_rate_history_v1(asset, timestamp, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)

Query Margin Interest Rate History (USER_DATA)

Query Margin Interest Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_interest_rate_history_v1_resp_item import MarginGetMarginInterestRateHistoryV1RespItem
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
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    vip_level = 56 # int | Default: user&#39;s vip level (optional)
    start_time = 56 # int | Default: 7 days ago (optional)
    end_time = 56 # int | Default: present. Maximum range: 1 months. (optional)
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Margin Interest Rate History (USER_DATA)
        api_response = api_instance.margin_get_margin_interest_rate_history_v1(asset, timestamp, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of BorrowAndRepayApi->margin_get_margin_interest_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_get_margin_interest_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **vip_level** | **int**| Default: user&amp;#39;s vip level | [optional] 
 **start_time** | **int**| Default: 7 days ago | [optional] 
 **end_time** | **int**| Default: present. Maximum range: 1 months. | [optional] 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**List[MarginGetMarginInterestRateHistoryV1RespItem]**](MarginGetMarginInterestRateHistoryV1RespItem.md)

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

# **margin_get_margin_max_borrowable_v1**
> MarginGetMarginMaxBorrowableV1Resp margin_get_margin_max_borrowable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Borrow (USER_DATA)

Query Max Borrow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_max_borrowable_v1_resp import MarginGetMarginMaxBorrowableV1Resp
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
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Max Borrow (USER_DATA)
        api_response = api_instance.margin_get_margin_max_borrowable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of BorrowAndRepayApi->margin_get_margin_max_borrowable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_get_margin_max_borrowable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginMaxBorrowableV1Resp**](MarginGetMarginMaxBorrowableV1Resp.md)

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

# **margin_get_margin_next_hourly_interest_rate_v1**
> List[MarginGetMarginNextHourlyInterestRateV1RespItem] margin_get_margin_next_hourly_interest_rate_v1(assets, is_isolated)

Get future hourly interest rate (USER_DATA)

Get future hourly interest rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_next_hourly_interest_rate_v1_resp_item import MarginGetMarginNextHourlyInterestRateV1RespItem
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
    api_instance = binance.margin.BorrowAndRepayApi(api_client)
    assets = '' # str | List of assets, separated by commas, up to 20 (default to '')
    is_isolated = True # bool | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;

    try:
        # Get future hourly interest rate (USER_DATA)
        api_response = api_instance.margin_get_margin_next_hourly_interest_rate_v1(assets, is_isolated)
        print("The response of BorrowAndRepayApi->margin_get_margin_next_hourly_interest_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BorrowAndRepayApi->margin_get_margin_next_hourly_interest_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assets** | **str**| List of assets, separated by commas, up to 20 | [default to &#39;&#39;]
 **is_isolated** | **bool**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34; | 

### Return type

[**List[MarginGetMarginNextHourlyInterestRateV1RespItem]**](MarginGetMarginNextHourlyInterestRateV1RespItem.md)

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

