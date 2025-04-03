# binance.subaccount.AssetManagementApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_sub_account_futures_internal_transfer_v1**](AssetManagementApi.md#subaccount_create_sub_account_futures_internal_transfer_v1) | **POST** /sapi/v1/sub-account/futures/internalTransfer | Sub-account Futures Asset Transfer(For Master Account)
[**subaccount_create_sub_account_futures_move_position_v1**](AssetManagementApi.md#subaccount_create_sub_account_futures_move_position_v1) | **POST** /sapi/v1/sub-account/futures/move-position | Move Position for Sub-account (For Master Account)
[**subaccount_create_sub_account_futures_transfer_v1**](AssetManagementApi.md#subaccount_create_sub_account_futures_transfer_v1) | **POST** /sapi/v1/sub-account/futures/transfer | Futures Transfer for Sub-account(For Master Account)
[**subaccount_create_sub_account_margin_transfer_v1**](AssetManagementApi.md#subaccount_create_sub_account_margin_transfer_v1) | **POST** /sapi/v1/sub-account/margin/transfer | Margin Transfer for Sub-account(For Master Account)
[**subaccount_create_sub_account_transfer_sub_to_master_v1**](AssetManagementApi.md#subaccount_create_sub_account_transfer_sub_to_master_v1) | **POST** /sapi/v1/sub-account/transfer/subToMaster | Transfer to Master(For Sub-account)
[**subaccount_create_sub_account_transfer_sub_to_sub_v1**](AssetManagementApi.md#subaccount_create_sub_account_transfer_sub_to_sub_v1) | **POST** /sapi/v1/sub-account/transfer/subToSub | Transfer to Sub-account of Same Master(For Sub-account)
[**subaccount_create_sub_account_universal_transfer_v1**](AssetManagementApi.md#subaccount_create_sub_account_universal_transfer_v1) | **POST** /sapi/v1/sub-account/universalTransfer | Universal Transfer(For Master Account)
[**subaccount_get_capital_deposit_sub_address_v1**](AssetManagementApi.md#subaccount_get_capital_deposit_sub_address_v1) | **GET** /sapi/v1/capital/deposit/subAddress | Get Sub-account Deposit Address(For Master Account)
[**subaccount_get_capital_deposit_sub_hisrec_v1**](AssetManagementApi.md#subaccount_get_capital_deposit_sub_hisrec_v1) | **GET** /sapi/v1/capital/deposit/subHisrec | Get Sub-account Deposit History(For Master Account)
[**subaccount_get_sub_account_assets_v3**](AssetManagementApi.md#subaccount_get_sub_account_assets_v3) | **GET** /sapi/v3/sub-account/assets | Query Sub-account Assets(For Master Account)
[**subaccount_get_sub_account_assets_v4**](AssetManagementApi.md#subaccount_get_sub_account_assets_v4) | **GET** /sapi/v4/sub-account/assets | Query Sub-account Assets (For Master Account)(USER_DATA)
[**subaccount_get_sub_account_futures_account_summary_v1**](AssetManagementApi.md#subaccount_get_sub_account_futures_account_summary_v1) | **GET** /sapi/v1/sub-account/futures/accountSummary | Get Summary of Sub-account&#39;s Futures Account(For Master Account)
[**subaccount_get_sub_account_futures_account_summary_v2**](AssetManagementApi.md#subaccount_get_sub_account_futures_account_summary_v2) | **GET** /sapi/v2/sub-account/futures/accountSummary | Get Summary of Sub-account&#39;s Futures Account V2(For Master Account)
[**subaccount_get_sub_account_futures_account_v1**](AssetManagementApi.md#subaccount_get_sub_account_futures_account_v1) | **GET** /sapi/v1/sub-account/futures/account | Get Detail on Sub-account&#39;s Futures Account(For Master Account)
[**subaccount_get_sub_account_futures_account_v2**](AssetManagementApi.md#subaccount_get_sub_account_futures_account_v2) | **GET** /sapi/v2/sub-account/futures/account | Get Detail on Sub-account&#39;s Futures Account V2(For Master Account)
[**subaccount_get_sub_account_futures_internal_transfer_v1**](AssetManagementApi.md#subaccount_get_sub_account_futures_internal_transfer_v1) | **GET** /sapi/v1/sub-account/futures/internalTransfer | Query Sub-account Futures Asset Transfer History(For Master Account)
[**subaccount_get_sub_account_futures_move_position_v1**](AssetManagementApi.md#subaccount_get_sub_account_futures_move_position_v1) | **GET** /sapi/v1/sub-account/futures/move-position | Get Move Position History for Sub-account (For Master Account)
[**subaccount_get_sub_account_margin_account_summary_v1**](AssetManagementApi.md#subaccount_get_sub_account_margin_account_summary_v1) | **GET** /sapi/v1/sub-account/margin/accountSummary | Get Summary of Sub-account&#39;s Margin Account(For Master Account)
[**subaccount_get_sub_account_margin_account_v1**](AssetManagementApi.md#subaccount_get_sub_account_margin_account_v1) | **GET** /sapi/v1/sub-account/margin/account | Get Detail on Sub-account&#39;s Margin Account(For Master Account)
[**subaccount_get_sub_account_spot_summary_v1**](AssetManagementApi.md#subaccount_get_sub_account_spot_summary_v1) | **GET** /sapi/v1/sub-account/spotSummary | Query Sub-account Spot Assets Summary(For Master Account)
[**subaccount_get_sub_account_sub_transfer_history_v1**](AssetManagementApi.md#subaccount_get_sub_account_sub_transfer_history_v1) | **GET** /sapi/v1/sub-account/sub/transfer/history | Query Sub-account Spot Asset Transfer History(For Master Account)
[**subaccount_get_sub_account_transfer_sub_user_history_v1**](AssetManagementApi.md#subaccount_get_sub_account_transfer_sub_user_history_v1) | **GET** /sapi/v1/sub-account/transfer/subUserHistory | Sub-account Transfer History(For Sub-account)
[**subaccount_get_sub_account_universal_transfer_v1**](AssetManagementApi.md#subaccount_get_sub_account_universal_transfer_v1) | **GET** /sapi/v1/sub-account/universalTransfer | Query Universal Transfer History(For Master Account)


# **subaccount_create_sub_account_futures_internal_transfer_v1**
> SubaccountCreateSubAccountFuturesInternalTransferV1Resp subaccount_create_sub_account_futures_internal_transfer_v1(amount, asset, from_email, futures_type, timestamp, to_email, recv_window=recv_window)

Sub-account Futures Asset Transfer(For Master Account)

Sub-account Futures Asset Transfer

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_futures_internal_transfer_v1_resp import SubaccountCreateSubAccountFuturesInternalTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    from_email = '' # str |  (default to '')
    futures_type = 56 # int | 
    timestamp = 56 # int | 
    to_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Sub-account Futures Asset Transfer(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_internal_transfer_v1(amount, asset, from_email, futures_type, timestamp, to_email, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_futures_internal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_futures_internal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **from_email** | **str**|  | [default to &#39;&#39;]
 **futures_type** | **int**|  | 
 **timestamp** | **int**|  | 
 **to_email** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountFuturesInternalTransferV1Resp**](SubaccountCreateSubAccountFuturesInternalTransferV1Resp.md)

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

# **subaccount_create_sub_account_futures_move_position_v1**
> SubaccountCreateSubAccountFuturesMovePositionV1Resp subaccount_create_sub_account_futures_move_position_v1(from_user_email, order_args, product_type, timestamp, to_user_email, recv_window=recv_window)

Move Position for Sub-account (For Master Account)

Move position between sub-master, master-sub, or sub-sub accounts when necessary

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_futures_move_position_v1_resp import SubaccountCreateSubAccountFuturesMovePositionV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    from_user_email = '' # str |  (default to '')
    order_args = None # List[object] | 
    product_type = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_user_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Move Position for Sub-account (For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_move_position_v1(from_user_email, order_args, product_type, timestamp, to_user_email, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_futures_move_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_futures_move_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_user_email** | **str**|  | [default to &#39;&#39;]
 **order_args** | [**List[object]**](object.md)|  | 
 **product_type** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_user_email** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountFuturesMovePositionV1Resp**](SubaccountCreateSubAccountFuturesMovePositionV1Resp.md)

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

# **subaccount_create_sub_account_futures_transfer_v1**
> SubaccountCreateSubAccountFuturesTransferV1Resp subaccount_create_sub_account_futures_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)

Futures Transfer for Sub-account(For Master Account)

Futures Transfer for Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_futures_transfer_v1_resp import SubaccountCreateSubAccountFuturesTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Transfer for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_futures_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_futures_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountFuturesTransferV1Resp**](SubaccountCreateSubAccountFuturesTransferV1Resp.md)

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

# **subaccount_create_sub_account_margin_transfer_v1**
> SubaccountCreateSubAccountMarginTransferV1Resp subaccount_create_sub_account_margin_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)

Margin Transfer for Sub-account(For Master Account)

Margin Transfer for Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_margin_transfer_v1_resp import SubaccountCreateSubAccountMarginTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Transfer for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_margin_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_margin_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_margin_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountMarginTransferV1Resp**](SubaccountCreateSubAccountMarginTransferV1Resp.md)

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

# **subaccount_create_sub_account_transfer_sub_to_master_v1**
> SubaccountCreateSubAccountTransferSubToMasterV1Resp subaccount_create_sub_account_transfer_sub_to_master_v1(amount, asset, timestamp, recv_window=recv_window)

Transfer to Master(For Sub-account)

Transfer to Master

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_transfer_sub_to_master_v1_resp import SubaccountCreateSubAccountTransferSubToMasterV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Transfer to Master(For Sub-account)
        api_response = api_instance.subaccount_create_sub_account_transfer_sub_to_master_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_transfer_sub_to_master_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_transfer_sub_to_master_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountTransferSubToMasterV1Resp**](SubaccountCreateSubAccountTransferSubToMasterV1Resp.md)

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

# **subaccount_create_sub_account_transfer_sub_to_sub_v1**
> SubaccountCreateSubAccountTransferSubToSubV1Resp subaccount_create_sub_account_transfer_sub_to_sub_v1(amount, asset, timestamp, to_email, recv_window=recv_window)

Transfer to Sub-account of Same Master(For Sub-account)

Transfer to Sub-account of Same Master

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_transfer_sub_to_sub_v1_resp import SubaccountCreateSubAccountTransferSubToSubV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Transfer to Sub-account of Same Master(For Sub-account)
        api_response = api_instance.subaccount_create_sub_account_transfer_sub_to_sub_v1(amount, asset, timestamp, to_email, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_create_sub_account_transfer_sub_to_sub_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_transfer_sub_to_sub_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_email** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountCreateSubAccountTransferSubToSubV1Resp**](SubaccountCreateSubAccountTransferSubToSubV1Resp.md)

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

# **subaccount_create_sub_account_universal_transfer_v1**
> SubaccountCreateSubAccountUniversalTransferV1Resp subaccount_create_sub_account_universal_transfer_v1(amount, asset, from_account_type, timestamp, to_account_type, client_tran_id=client_tran_id, from_email=from_email, recv_window=recv_window, symbol=symbol, to_email=to_email)

Universal Transfer(For Master Account)

Universal Transfer

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_sub_account_universal_transfer_v1_resp import SubaccountCreateSubAccountUniversalTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    from_account_type = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_account_type = '' # str |  (default to '')
    client_tran_id = '' # str |  (optional) (default to '')
    from_email = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')
    to_email = '' # str |  (optional) (default to '')

    try:
        # Universal Transfer(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_universal_transfer_v1(amount, asset, from_account_type, timestamp, to_account_type, client_tran_id=client_tran_id, from_email=from_email, recv_window=recv_window, symbol=symbol, to_email=to_email)
        print("The response of AssetManagementApi->subaccount_create_sub_account_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_create_sub_account_universal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **from_account_type** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_account_type** | **str**|  | [default to &#39;&#39;]
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **from_email** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **to_email** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**SubaccountCreateSubAccountUniversalTransferV1Resp**](SubaccountCreateSubAccountUniversalTransferV1Resp.md)

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

# **subaccount_get_capital_deposit_sub_address_v1**
> SubaccountGetCapitalDepositSubAddressV1Resp subaccount_get_capital_deposit_sub_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)

Get Sub-account Deposit Address(For Master Account)

Fetch sub-account deposit address

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_capital_deposit_sub_address_v1_resp import SubaccountGetCapitalDepositSubAddressV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | Sub account email (default to '')
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub-account Deposit Address(For Master Account)
        api_response = api_instance.subaccount_get_capital_deposit_sub_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_capital_deposit_sub_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_capital_deposit_sub_address_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub account email | [default to &#39;&#39;]
 **coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetCapitalDepositSubAddressV1Resp**](SubaccountGetCapitalDepositSubAddressV1Resp.md)

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

# **subaccount_get_capital_deposit_sub_hisrec_v1**
> List[SubaccountGetCapitalDepositSubHisrecV1RespItem] subaccount_get_capital_deposit_sub_hisrec_v1(email, timestamp, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window, tx_id=tx_id)

Get Sub-account Deposit History(For Master Account)

Fetch sub-account deposit history

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_capital_deposit_sub_hisrec_v1_resp_item import SubaccountGetCapitalDepositSubHisrecV1RespItem
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | Sub account email (default to '')
    timestamp = 56 # int | 
    coin = '' # str |  (optional) (default to '')
    status = 56 # int | 0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success) (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int | default:0 (optional)
    recv_window = 56 # int |  (optional)
    tx_id = '' # str |  (optional) (default to '')

    try:
        # Get Sub-account Deposit History(For Master Account)
        api_response = api_instance.subaccount_get_capital_deposit_sub_hisrec_v1(email, timestamp, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window, tx_id=tx_id)
        print("The response of AssetManagementApi->subaccount_get_capital_deposit_sub_hisrec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_capital_deposit_sub_hisrec_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub account email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **int**| 0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success) | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**| default:0 | [optional] 
 **recv_window** | **int**|  | [optional] 
 **tx_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[SubaccountGetCapitalDepositSubHisrecV1RespItem]**](SubaccountGetCapitalDepositSubHisrecV1RespItem.md)

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

# **subaccount_get_sub_account_assets_v3**
> SubaccountGetSubAccountAssetsV3Resp subaccount_get_sub_account_assets_v3(email, timestamp, recv_window=recv_window)

Query Sub-account Assets(For Master Account)

Fetch sub-account assets

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_assets_v3_resp import SubaccountGetSubAccountAssetsV3Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | Sub account email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Assets(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_assets_v3(email, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_assets_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_assets_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub account email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountAssetsV3Resp**](SubaccountGetSubAccountAssetsV3Resp.md)

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

# **subaccount_get_sub_account_assets_v4**
> SubaccountGetSubAccountAssetsV4Resp subaccount_get_sub_account_assets_v4(email, timestamp, recv_window=recv_window)

Query Sub-account Assets (For Master Account)(USER_DATA)

Fetch sub-account assets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_assets_v4_resp import SubaccountGetSubAccountAssetsV4Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | Sub Account Email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Assets (For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_sub_account_assets_v4(email, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_assets_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_assets_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub Account Email | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountAssetsV4Resp**](SubaccountGetSubAccountAssetsV4Resp.md)

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

# **subaccount_get_sub_account_futures_account_summary_v1**
> SubaccountGetSubAccountFuturesAccountSummaryV1Resp subaccount_get_sub_account_futures_account_summary_v1(timestamp, recv_window=recv_window)

Get Summary of Sub-account's Futures Account(For Master Account)

Get Summary of Sub-account's Futures Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v1_resp import SubaccountGetSubAccountFuturesAccountSummaryV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Futures Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_summary_v1(timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_account_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_account_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesAccountSummaryV1Resp**](SubaccountGetSubAccountFuturesAccountSummaryV1Resp.md)

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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    page = 56 # int | default:1 (optional)
    limit = 56 # int | default:10, max:20 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Futures Account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_summary_v2(futures_type, timestamp, page=page, limit=limit, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_account_summary_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_account_summary_v2: %s\n" % e)
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

# **subaccount_get_sub_account_futures_account_v1**
> SubaccountGetSubAccountFuturesAccountV1Resp subaccount_get_sub_account_futures_account_v1(email, timestamp, recv_window=recv_window)

Get Detail on Sub-account's Futures Account(For Master Account)

Get Detail on Sub-account's Futures Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_account_v1_resp import SubaccountGetSubAccountFuturesAccountV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Futures Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_v1(email, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesAccountV1Resp**](SubaccountGetSubAccountFuturesAccountV1Resp.md)

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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#email-address\">Sub-account email</a> (default to '')
    futures_type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Futures Account V2(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_v2(email, futures_type, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_account_v2: %s\n" % e)
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

# **subaccount_get_sub_account_futures_internal_transfer_v1**
> SubaccountGetSubAccountFuturesInternalTransferV1Resp subaccount_get_sub_account_futures_internal_transfer_v1(email, futures_type, timestamp, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Sub-account Futures Asset Transfer History(For Master Account)

Query Sub-account Futures Asset Transfer History

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_internal_transfer_v1_resp import SubaccountGetSubAccountFuturesInternalTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#email-address\">Sub-account email</a> (default to '')
    futures_type = 56 # int | 1:USDT-margined Futures，2: Coin-margined Futures
    timestamp = 56 # int | 
    start_time = 56 # int | Cannot be earlier than 1 month ago (optional)
    end_time = 56 # int |  (optional)
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 50, Max value: 500 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Futures Asset Transfer History(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_internal_transfer_v1(email, futures_type, timestamp, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_internal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_internal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **futures_type** | **int**| 1:USDT-margined Futures，2: Coin-margined Futures | 
 **timestamp** | **int**|  | 
 **start_time** | **int**| Cannot be earlier than 1 month ago | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| Default value: 1 | [optional] 
 **limit** | **int**| Default value: 50, Max value: 500 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesInternalTransferV1Resp**](SubaccountGetSubAccountFuturesInternalTransferV1Resp.md)

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

# **subaccount_get_sub_account_futures_move_position_v1**
> SubaccountGetSubAccountFuturesMovePositionV1Resp subaccount_get_sub_account_futures_move_position_v1(symbol, page, row, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)

Get Move Position History for Sub-account (For Master Account)

Query move position history

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_futures_move_position_v1_resp import SubaccountGetSubAccountFuturesMovePositionV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    symbol = '' # str |  (default to '')
    page = 56 # int | 
    row = 56 # int | 
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Move Position History for Sub-account (For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_move_position_v1(symbol, page, row, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_futures_move_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_futures_move_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **page** | **int**|  | 
 **row** | **int**|  | 
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountFuturesMovePositionV1Resp**](SubaccountGetSubAccountFuturesMovePositionV1Resp.md)

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

# **subaccount_get_sub_account_margin_account_summary_v1**
> SubaccountGetSubAccountMarginAccountSummaryV1Resp subaccount_get_sub_account_margin_account_summary_v1(timestamp, recv_window=recv_window)

Get Summary of Sub-account's Margin Account(For Master Account)

Get Summary of Sub-account's Margin Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_margin_account_summary_v1_resp import SubaccountGetSubAccountMarginAccountSummaryV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Margin Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_margin_account_summary_v1(timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_margin_account_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_margin_account_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountMarginAccountSummaryV1Resp**](SubaccountGetSubAccountMarginAccountSummaryV1Resp.md)

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

# **subaccount_get_sub_account_margin_account_v1**
> SubaccountGetSubAccountMarginAccountV1Resp subaccount_get_sub_account_margin_account_v1(email, timestamp, recv_window=recv_window)

Get Detail on Sub-account's Margin Account(For Master Account)

Get Detail on Sub-account's Margin Account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_margin_account_v1_resp import SubaccountGetSubAccountMarginAccountV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Margin Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_margin_account_v1(email, timestamp, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;a href&#x3D;\&quot;/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#email-address\&quot;&gt;Sub-account email&lt;/a&gt; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountMarginAccountV1Resp**](SubaccountGetSubAccountMarginAccountV1Resp.md)

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

# **subaccount_get_sub_account_spot_summary_v1**
> SubaccountGetSubAccountSpotSummaryV1Resp subaccount_get_sub_account_spot_summary_v1(timestamp, email=email, page=page, size=size, recv_window=recv_window)

Query Sub-account Spot Assets Summary(For Master Account)

Get BTC valued asset summary of subaccounts.

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_spot_summary_v1_resp import SubaccountGetSubAccountSpotSummaryV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    email = '' # str | Sub account email (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 20 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Spot Assets Summary(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_spot_summary_v1(timestamp, email=email, page=page, size=size, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_spot_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_spot_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **email** | **str**| Sub account email | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 20 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountSpotSummaryV1Resp**](SubaccountGetSubAccountSpotSummaryV1Resp.md)

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

# **subaccount_get_sub_account_sub_transfer_history_v1**
> List[SubaccountGetSubAccountSubTransferHistoryV1RespItem] subaccount_get_sub_account_sub_transfer_history_v1(timestamp, from_email=from_email, to_email=to_email, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Sub-account Spot Asset Transfer History(For Master Account)

Query Sub-account Spot Asset Transfer History

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_sub_transfer_history_v1_resp_item import SubaccountGetSubAccountSubTransferHistoryV1RespItem
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    from_email = '' # str |  (optional) (default to '')
    to_email = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 500 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Spot Asset Transfer History(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_sub_transfer_history_v1(timestamp, from_email=from_email, to_email=to_email, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_sub_transfer_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_sub_transfer_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_email** | **str**|  | [optional] [default to &#39;&#39;]
 **to_email** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| Default value: 1 | [optional] 
 **limit** | **int**| Default value: 500 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[SubaccountGetSubAccountSubTransferHistoryV1RespItem]**](SubaccountGetSubAccountSubTransferHistoryV1RespItem.md)

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

# **subaccount_get_sub_account_transfer_sub_user_history_v1**
> List[SubaccountGetSubAccountTransferSubUserHistoryV1RespItem] subaccount_get_sub_account_transfer_sub_user_history_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, return_fail_history=return_fail_history, recv_window=recv_window)

Sub-account Transfer History(For Sub-account)

Sub-account Transfer History

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_transfer_sub_user_history_v1_resp_item import SubaccountGetSubAccountTransferSubUserHistoryV1RespItem
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str | If not sent, result of all assets will be returned (optional) (default to '')
    type = 56 # int | 1: transfer in, 2: transfer out (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500 (optional) (default to 500)
    return_fail_history = True # bool | Default `False`, return PROCESS and SUCCESS status history; If `True`,return PROCESS and SUCCESS and FAILURE status history (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Sub-account Transfer History(For Sub-account)
        api_response = api_instance.subaccount_get_sub_account_transfer_sub_user_history_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, return_fail_history=return_fail_history, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_transfer_sub_user_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_transfer_sub_user_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**| If not sent, result of all assets will be returned | [optional] [default to &#39;&#39;]
 **type** | **int**| 1: transfer in, 2: transfer out | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500 | [optional] [default to 500]
 **return_fail_history** | **bool**| Default &#x60;False&#x60;, return PROCESS and SUCCESS status history; If &#x60;True&#x60;,return PROCESS and SUCCESS and FAILURE status history | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[SubaccountGetSubAccountTransferSubUserHistoryV1RespItem]**](SubaccountGetSubAccountTransferSubUserHistoryV1RespItem.md)

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

# **subaccount_get_sub_account_universal_transfer_v1**
> SubaccountGetSubAccountUniversalTransferV1Resp subaccount_get_sub_account_universal_transfer_v1(timestamp, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Universal Transfer History(For Master Account)

Query Universal Transfer History

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_sub_account_universal_transfer_v1_resp import SubaccountGetSubAccountUniversalTransferV1Resp
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
    api_instance = binance.subaccount.AssetManagementApi(api_client)
    timestamp = 56 # int | 
    from_email = '' # str |  (optional) (default to '')
    to_email = '' # str |  (optional) (default to '')
    client_tran_id = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 1 # int | Default 1 (optional) (default to 1)
    limit = 500 # int | Default 500, Max 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Universal Transfer History(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_universal_transfer_v1(timestamp, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AssetManagementApi->subaccount_get_sub_account_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetManagementApi->subaccount_get_sub_account_universal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_email** | **str**|  | [optional] [default to &#39;&#39;]
 **to_email** | **str**|  | [optional] [default to &#39;&#39;]
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| Default 1 | [optional] [default to 1]
 **limit** | **int**| Default 500, Max 500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetSubAccountUniversalTransferV1Resp**](SubaccountGetSubAccountUniversalTransferV1Resp.md)

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

