# binance.subaccount.AccountManagementApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_sub_account_blvt_enable_v1**](AccountManagementApi.md#subaccount_create_sub_account_blvt_enable_v1) | **POST** /sapi/v1/sub-account/blvt/enable | Enable Leverage Token for Sub-account(For Master Account)
[**subaccount_create_sub_account_eoptions_enable_v1**](AccountManagementApi.md#subaccount_create_sub_account_eoptions_enable_v1) | **POST** /sapi/v1/sub-account/eoptions/enable | Enable Options for Sub-account(For Master Account)(USER_DATA)
[**subaccount_create_sub_account_futures_enable_v1**](AccountManagementApi.md#subaccount_create_sub_account_futures_enable_v1) | **POST** /sapi/v1/sub-account/futures/enable | Enable Futures for Sub-account(For Master Account)
[**subaccount_create_sub_account_margin_enable_v1**](AccountManagementApi.md#subaccount_create_sub_account_margin_enable_v1) | **POST** /sapi/v1/sub-account/margin/enable | Enable Margin for Sub-account(For Master Account)
[**subaccount_create_sub_account_virtual_sub_account_v1**](AccountManagementApi.md#subaccount_create_sub_account_virtual_sub_account_v1) | **POST** /sapi/v1/sub-account/virtualSubAccount | Create a Virtual Sub-account(For Master Account)
[**subaccount_get_sub_account_futures_position_risk_v1**](AccountManagementApi.md#subaccount_get_sub_account_futures_position_risk_v1) | **GET** /sapi/v1/sub-account/futures/positionRisk | Get Futures Position-Risk of Sub-account(For Master Account)
[**subaccount_get_sub_account_futures_position_risk_v2**](AccountManagementApi.md#subaccount_get_sub_account_futures_position_risk_v2) | **GET** /sapi/v2/sub-account/futures/positionRisk | Get Futures Position-Risk of Sub-account V2(For Master Account)
[**subaccount_get_sub_account_list_v1**](AccountManagementApi.md#subaccount_get_sub_account_list_v1) | **GET** /sapi/v1/sub-account/list | Query Sub-account List(For Master Account)
[**subaccount_get_sub_account_status_v1**](AccountManagementApi.md#subaccount_get_sub_account_status_v1) | **GET** /sapi/v1/sub-account/status | Get Sub-account&#39;s Status on Margin Or Futures(For Master Account)
[**subaccount_get_sub_account_transaction_statistics_v1**](AccountManagementApi.md#subaccount_get_sub_account_transaction_statistics_v1) | **GET** /sapi/v1/sub-account/transaction-statistics | Query Sub-account Transaction Statistics(For Master Account)(USER_DATA)


# **subaccount_create_sub_account_blvt_enable_v1**
> SubaccountCreateSubAccountBlvtEnableV1Resp subaccount_create_sub_account_blvt_enable_v1(email, enable_blvt, timestamp, recv_window=recv_window)

Enable Leverage Token for Sub-account(For Master Account)

Enable Leverage Token for Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_blvt_enable_v1_resp import SubaccountCreateSubAccountBlvtEnableV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str |  (default to '')
    enable_blvt = True # bool | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Leverage Token for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_blvt_enable_v1(email, enable_blvt, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_create_sub_account_blvt_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_create_sub_account_blvt_enable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **enable_blvt** | **bool**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountBlvtEnableV1Resp**](SubaccountCreateSubAccountBlvtEnableV1Resp.md)

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

# **subaccount_create_sub_account_eoptions_enable_v1**
> SubaccountCreateSubAccountEoptionsEnableV1Resp subaccount_create_sub_account_eoptions_enable_v1(email, timestamp, recv_window=recv_window)

Enable Options for Sub-account(For Master Account)(USER_DATA)

Enable Options for Sub-account (For Master Account).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_eoptions_enable_v1_resp import SubaccountCreateSubAccountEoptionsEnableV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.subaccount.Configuration(
    auth=binance.subaccount.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Options for Sub-account(For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_create_sub_account_eoptions_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_create_sub_account_eoptions_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_create_sub_account_eoptions_enable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountEoptionsEnableV1Resp**](SubaccountCreateSubAccountEoptionsEnableV1Resp.md)

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

# **subaccount_create_sub_account_futures_enable_v1**
> SubaccountCreateSubAccountFuturesEnableV1Resp subaccount_create_sub_account_futures_enable_v1(email, timestamp, recv_window=recv_window)

Enable Futures for Sub-account(For Master Account)

Enable Futures for Sub-account for Master Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_futures_enable_v1_resp import SubaccountCreateSubAccountFuturesEnableV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Futures for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_create_sub_account_futures_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_create_sub_account_futures_enable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountFuturesEnableV1Resp**](SubaccountCreateSubAccountFuturesEnableV1Resp.md)

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

# **subaccount_create_sub_account_margin_enable_v1**
> SubaccountCreateSubAccountMarginEnableV1Resp subaccount_create_sub_account_margin_enable_v1(email, timestamp, recv_window=recv_window)

Enable Margin for Sub-account(For Master Account)

Enable Margin for Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_margin_enable_v1_resp import SubaccountCreateSubAccountMarginEnableV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Margin for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_margin_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_create_sub_account_margin_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_create_sub_account_margin_enable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountMarginEnableV1Resp**](SubaccountCreateSubAccountMarginEnableV1Resp.md)

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

# **subaccount_create_sub_account_virtual_sub_account_v1**
> SubaccountCreateSubAccountVirtualSubAccountV1Resp subaccount_create_sub_account_virtual_sub_account_v1(sub_account_string, timestamp, recv_window=recv_window)

Create a Virtual Sub-account(For Master Account)

Create a Virtual Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_virtual_sub_account_v1_resp import SubaccountCreateSubAccountVirtualSubAccountV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    sub_account_string = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Create a Virtual Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_virtual_sub_account_v1(sub_account_string, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_create_sub_account_virtual_sub_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_create_sub_account_virtual_sub_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_string** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountVirtualSubAccountV1Resp**](SubaccountCreateSubAccountVirtualSubAccountV1Resp.md)

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

# **subaccount_get_sub_account_futures_position_risk_v1**
> List[SubaccountGetSubAccountFuturesPositionRiskV1RespItem] subaccount_get_sub_account_futures_position_risk_v1(email, timestamp, recv_window=recv_window)

Get Futures Position-Risk of Sub-account(For Master Account)

Get Futures Position-Risk of Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_position_risk_v1_resp_item import SubaccountGetSubAccountFuturesPositionRiskV1RespItem
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Position-Risk of Sub-account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_position_risk_v1(email, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_get_sub_account_futures_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_get_sub_account_futures_position_risk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[SubaccountGetSubAccountFuturesPositionRiskV1RespItem]**](SubaccountGetSubAccountFuturesPositionRiskV1RespItem.md)

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

# **subaccount_get_sub_account_futures_position_risk_v2**
> SubaccountGetSubAccountFuturesPositionRiskV2Resp subaccount_get_sub_account_futures_position_risk_v2(email, futures_type, timestamp, recv_window=recv_window)

Get Futures Position-Risk of Sub-account V2(For Master Account)

Get Futures Position-Risk of Sub-account V2

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_position_risk_v2_resp import SubaccountGetSubAccountFuturesPositionRiskV2Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#email-address\">Sub-account email</a> (default to '')
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Position-Risk of Sub-account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_position_risk_v2(email, futures_type, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_get_sub_account_futures_position_risk_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_get_sub_account_futures_position_risk_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **futures_type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesPositionRiskV2Resp**](SubaccountGetSubAccountFuturesPositionRiskV2Resp.md)

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

# **subaccount_get_sub_account_list_v1**
> SubaccountGetSubAccountListV1Resp subaccount_get_sub_account_list_v1(timestamp, email=email, is_freeze=is_freeze, page=page, limit=limit, recv_window=recv_window)

Query Sub-account List(For Master Account)

Query Sub-account List

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_list_v1_resp import SubaccountGetSubAccountListV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    timestamp = 56 # int | 
    email = '' # str | <a href=\"/docs/sub_account/account-management/Query-Sub-account-List#email-address\">Sub-account email</a> (optional) (default to '')
    is_freeze = '' # str | true or false (optional) (default to '')
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 1, Max value: 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account List(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_list_v1(timestamp, email=email, is_freeze=is_freeze, page=page, limit=limit, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_get_sub_account_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_get_sub_account_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/account-management/Query-Sub-account-List#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [optional] [default to &#39;&#39;]
 **is_freeze** | **str**| true or false | [optional] [default to &#39;&#39;]
 **page** | **int**| Default value: 1 | [optional] 
 **limit** | **int**| Default value: 1, Max value: 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountListV1Resp**](SubaccountGetSubAccountListV1Resp.md)

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

# **subaccount_get_sub_account_status_v1**
> List[SubaccountGetSubAccountStatusV1RespItem] subaccount_get_sub_account_status_v1(timestamp, email=email, recv_window=recv_window)

Get Sub-account's Status on Margin Or Futures(For Master Account)

Get Sub-account's Status on Margin Or Futures

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_status_v1_resp_item import SubaccountGetSubAccountStatusV1RespItem
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    timestamp = 56 # int | 
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#email-address\">Sub-account email</a> (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub-account's Status on Margin Or Futures(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_status_v1(timestamp, email=email, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_get_sub_account_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_get_sub_account_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[SubaccountGetSubAccountStatusV1RespItem]**](SubaccountGetSubAccountStatusV1RespItem.md)

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

# **subaccount_get_sub_account_transaction_statistics_v1**
> SubaccountGetSubAccountTransactionStatisticsV1Resp subaccount_get_sub_account_transaction_statistics_v1(email, timestamp, recv_window=recv_window)

Query Sub-account Transaction Statistics(For Master Account)(USER_DATA)

Query Sub-account Transaction statistics (For Master Account).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_transaction_statistics_v1_resp import SubaccountGetSubAccountTransactionStatisticsV1Resp
from binance.subaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.subaccount.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.subaccount.Configuration(
    auth=binance.subaccount.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.subaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.subaccount.AccountManagementApi(api_client)
    email = '' # str | Sub user email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Transaction Statistics(For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_sub_account_transaction_statistics_v1(email, timestamp, recv_window=recv_window)
        print("The response of AccountManagementApi->subaccount_get_sub_account_transaction_statistics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->subaccount_get_sub_account_transaction_statistics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub user email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountTransactionStatisticsV1Resp**](SubaccountGetSubAccountTransactionStatisticsV1Resp.md)

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

