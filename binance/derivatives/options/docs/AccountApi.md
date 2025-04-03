# binance.derivatives.options.AccountApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_get_account_v1**](AccountApi.md#options_get_account_v1) | **GET** /eapi/v1/account | Option Account Information(TRADE)
[**options_get_bill_v1**](AccountApi.md#options_get_bill_v1) | **GET** /eapi/v1/bill | Account Funding Flow (USER_DATA)
[**options_get_income_asyn_id_v1**](AccountApi.md#options_get_income_asyn_id_v1) | **GET** /eapi/v1/income/asyn/id | Get Option Transaction History Download Link by Id (USER_DATA)
[**options_get_income_asyn_v1**](AccountApi.md#options_get_income_asyn_v1) | **GET** /eapi/v1/income/asyn | Get Download Id For Option Transaction History (USER_DATA)


# **options_get_account_v1**
> OptionsGetAccountV1Resp options_get_account_v1(timestamp, recv_window=recv_window)

Option Account Information(TRADE)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_account_v1_resp import OptionsGetAccountV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Option Account Information(TRADE)
        api_response = api_instance.options_get_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->options_get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->options_get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetAccountV1Resp**](OptionsGetAccountV1Resp.md)

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

# **options_get_bill_v1**
> List[OptionsGetBillV1RespItem] options_get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Account Funding Flow (USER_DATA)

Query account funding flows.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_bill_v1_resp_item import OptionsGetBillV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.AccountApi(api_client)
    currency = '' # str | Asset type, only support USDT  as of now (default to '')
    timestamp = 56 # int | 
    record_id = 56 # int | Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 (optional)
    start_time = 56 # int | Start Time, e.g 1593511200000 (optional)
    end_time = 56 # int | End Time, e.g 1593512200000 (optional)
    limit = 56 # int | Number of result sets returned Default:100 Max:1000 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Account Funding Flow (USER_DATA)
        api_response = api_instance.options_get_bill_v1(currency, timestamp, record_id=record_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->options_get_bill_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->options_get_bill_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Asset type, only support USDT  as of now | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **record_id** | **int**| Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 | [optional] 
 **start_time** | **int**| Start Time, e.g 1593511200000 | [optional] 
 **end_time** | **int**| End Time, e.g 1593512200000 | [optional] 
 **limit** | **int**| Number of result sets returned Default:100 Max:1000 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[OptionsGetBillV1RespItem]**](OptionsGetBillV1RespItem.md)

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

# **options_get_income_asyn_id_v1**
> OptionsGetIncomeAsynIdV1Resp options_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Option Transaction History Download Link by Id (USER_DATA)

Get option transaction history download Link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_income_asyn_id_v1_resp import OptionsGetIncomeAsynIdV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Option Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.options_get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->options_get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->options_get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**OptionsGetIncomeAsynIdV1Resp**](OptionsGetIncomeAsynIdV1Resp.md)

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

# **options_get_income_asyn_v1**
> OptionsGetIncomeAsynV1Resp options_get_income_asyn_v1()

Get Download Id For Option Transaction History (USER_DATA)

Get download id for option transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_income_asyn_v1_resp import OptionsGetIncomeAsynV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.options.Configuration(
    auth=binance.derivatives.options.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.AccountApi(api_client)

    try:
        # Get Download Id For Option Transaction History (USER_DATA)
        api_response = api_instance.options_get_income_asyn_v1()
        print("The response of AccountApi->options_get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->options_get_income_asyn_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetIncomeAsynV1Resp**](OptionsGetIncomeAsynV1Resp.md)

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

