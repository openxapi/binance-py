# binance.subaccount.V2Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_sub_account_sub_account_api_ip_restriction_v2**](V2Api.md#subaccount_create_sub_account_sub_account_api_ip_restriction_v2) | **POST** /sapi/v2/sub-account/subAccountApi/ipRestriction | Add IP Restriction for Sub-Account API key(For Master Account)
[**subaccount_get_sub_account_futures_account_summary_v2**](V2Api.md#subaccount_get_sub_account_futures_account_summary_v2) | **GET** /sapi/v2/sub-account/futures/accountSummary | Get Summary of Sub-account&#39;s Futures Account V2(For Master Account)
[**subaccount_get_sub_account_futures_account_v2**](V2Api.md#subaccount_get_sub_account_futures_account_v2) | **GET** /sapi/v2/sub-account/futures/account | Get Detail on Sub-account&#39;s Futures Account V2(For Master Account)
[**subaccount_get_sub_account_futures_position_risk_v2**](V2Api.md#subaccount_get_sub_account_futures_position_risk_v2) | **GET** /sapi/v2/sub-account/futures/positionRisk | Get Futures Position-Risk of Sub-account V2(For Master Account)


# **subaccount_create_sub_account_sub_account_api_ip_restriction_v2**
> SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp subaccount_create_sub_account_sub_account_api_ip_restriction_v2(email, status, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)

Add IP Restriction for Sub-Account API key(For Master Account)

Add IP Restriction for Sub-Account API key

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_sub_account_api_ip_restriction_v2_resp import SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp
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
    api_instance = binance.subaccount.V2Api(api_client)
    email = '' # str |  (default to '')
    status = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Add IP Restriction for Sub-Account API key(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_sub_account_api_ip_restriction_v2(email, status, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of V2Api->subaccount_create_sub_account_sub_account_api_ip_restriction_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->subaccount_create_sub_account_sub_account_api_ip_restriction_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **status** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **ip_address** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp**](SubaccountCreateSubAccountSubAccountApiIpRestrictionV2Resp.md)

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

# **subaccount_get_sub_account_futures_account_summary_v2**
> SubaccountGetSubAccountFuturesAccountSummaryV2Resp subaccount_get_sub_account_futures_account_summary_v2(futures_type, timestamp, page=page, limit=limit, recv_window=recv_window)

Get Summary of Sub-account's Futures Account V2(For Master Account)

Get Summary of Sub-account's Futures Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v2_resp import SubaccountGetSubAccountFuturesAccountSummaryV2Resp
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
    api_instance = binance.subaccount.V2Api(api_client)
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    page = 56 # int | default:1 (optional)
    limit = 56 # int | default:10, max:20 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Futures Account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_summary_v2(futures_type, timestamp, page=page, limit=limit, recv_window=recv_window)
        print("The response of V2Api->subaccount_get_sub_account_futures_account_summary_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->subaccount_get_sub_account_futures_account_summary_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures | 
 **timestamp** | **int**|  | 
 **page** | **int**| default:1 | [optional] 
 **limit** | **int**| default:10, max:20 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesAccountSummaryV2Resp**](SubaccountGetSubAccountFuturesAccountSummaryV2Resp.md)

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

# **subaccount_get_sub_account_futures_account_v2**
> SubaccountGetSubAccountFuturesAccountV2Resp subaccount_get_sub_account_futures_account_v2(email, futures_type, timestamp, recv_window=recv_window)

Get Detail on Sub-account's Futures Account V2(For Master Account)

Get Detail on Sub-account's Futures Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_account_v2_resp import SubaccountGetSubAccountFuturesAccountV2Resp
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
    api_instance = binance.subaccount.V2Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#email-address\">Sub-account email</a> (default to '')
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Futures Account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_v2(email, futures_type, timestamp, recv_window=recv_window)
        print("The response of V2Api->subaccount_get_sub_account_futures_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->subaccount_get_sub_account_futures_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **futures_type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesAccountV2Resp**](SubaccountGetSubAccountFuturesAccountV2Resp.md)

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
    api_instance = binance.subaccount.V2Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#email-address\">Sub-account email</a> (default to '')
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Position-Risk of Sub-account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_position_risk_v2(email, futures_type, timestamp, recv_window=recv_window)
        print("The response of V2Api->subaccount_get_sub_account_futures_position_risk_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->subaccount_get_sub_account_futures_position_risk_v2: %s\n" % e)
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

