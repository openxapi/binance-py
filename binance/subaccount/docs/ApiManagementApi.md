# binance.subaccount.ApiManagementApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_sub_account_sub_account_api_ip_restriction_v2**](ApiManagementApi.md#subaccount_create_sub_account_sub_account_api_ip_restriction_v2) | **POST** /sapi/v2/sub-account/subAccountApi/ipRestriction | Add IP Restriction for Sub-Account API key(For Master Account)
[**subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1**](ApiManagementApi.md#subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1) | **DELETE** /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList | Delete IP List For a Sub-account API Key(For Master Account)
[**subaccount_get_sub_account_sub_account_api_ip_restriction_v1**](ApiManagementApi.md#subaccount_get_sub_account_sub_account_api_ip_restriction_v1) | **GET** /sapi/v1/sub-account/subAccountApi/ipRestriction | Get IP Restriction for a Sub-account API Key(For Master Account)


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
    api_instance = binance.subaccount.ApiManagementApi(api_client)
    email = '' # str |  (default to '')
    status = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Add IP Restriction for Sub-Account API key(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_sub_account_api_ip_restriction_v2(email, status, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of ApiManagementApi->subaccount_create_sub_account_sub_account_api_ip_restriction_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiManagementApi->subaccount_create_sub_account_sub_account_api_ip_restriction_v2: %s\n" % e)
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

# **subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1**
> SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1(email, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)

Delete IP List For a Sub-account API Key(For Master Account)

Delete IP List For a Sub-account API Key

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1_resp import SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp
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
    api_instance = binance.subaccount.ApiManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#email-address\">Sub-account email</a> (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str | Can be added in batches, separated by commas (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Delete IP List For a Sub-account API Key(For Master Account)
        api_response = api_instance.subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1(email, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of ApiManagementApi->subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiManagementApi->subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **ip_address** | **str**| Can be added in batches, separated by commas | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp**](SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp.md)

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

# **subaccount_get_sub_account_sub_account_api_ip_restriction_v1**
> SubaccountGetSubAccountSubAccountApiIpRestrictionV1Resp subaccount_get_sub_account_sub_account_api_ip_restriction_v1(email, sub_account_api_key, timestamp, recv_window=recv_window)

Get IP Restriction for a Sub-account API Key(For Master Account)

Get IP Restriction for a Sub-account API Key

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_sub_account_api_ip_restriction_v1_resp import SubaccountGetSubAccountSubAccountApiIpRestrictionV1Resp
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
    api_instance = binance.subaccount.ApiManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/api-management#email-address\">Sub-account email</a> (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get IP Restriction for a Sub-account API Key(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_sub_account_api_ip_restriction_v1(email, sub_account_api_key, timestamp, recv_window=recv_window)
        print("The response of ApiManagementApi->subaccount_get_sub_account_sub_account_api_ip_restriction_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiManagementApi->subaccount_get_sub_account_sub_account_api_ip_restriction_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/api-management#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountSubAccountApiIpRestrictionV1Resp**](SubaccountGetSubAccountSubAccountApiIpRestrictionV1Resp.md)

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

