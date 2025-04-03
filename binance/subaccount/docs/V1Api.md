# binance.subaccount.V1Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_managed_subaccount_deposit_v1**](V1Api.md#subaccount_create_managed_subaccount_deposit_v1) | **POST** /sapi/v1/managed-subaccount/deposit | Deposit Assets Into The Managed Sub-account(For Investor Master Account)
[**subaccount_create_managed_subaccount_withdraw_v1**](V1Api.md#subaccount_create_managed_subaccount_withdraw_v1) | **POST** /sapi/v1/managed-subaccount/withdraw | Withdrawl Assets From The Managed Sub-account(For Investor Master Account)
[**subaccount_create_sub_account_blvt_enable_v1**](V1Api.md#subaccount_create_sub_account_blvt_enable_v1) | **POST** /sapi/v1/sub-account/blvt/enable | Enable Leverage Token for Sub-account(For Master Account)
[**subaccount_create_sub_account_eoptions_enable_v1**](V1Api.md#subaccount_create_sub_account_eoptions_enable_v1) | **POST** /sapi/v1/sub-account/eoptions/enable | Enable Options for Sub-account(For Master Account)(USER_DATA)
[**subaccount_create_sub_account_futures_enable_v1**](V1Api.md#subaccount_create_sub_account_futures_enable_v1) | **POST** /sapi/v1/sub-account/futures/enable | Enable Futures for Sub-account(For Master Account)
[**subaccount_create_sub_account_futures_internal_transfer_v1**](V1Api.md#subaccount_create_sub_account_futures_internal_transfer_v1) | **POST** /sapi/v1/sub-account/futures/internalTransfer | Sub-account Futures Asset Transfer(For Master Account)
[**subaccount_create_sub_account_futures_move_position_v1**](V1Api.md#subaccount_create_sub_account_futures_move_position_v1) | **POST** /sapi/v1/sub-account/futures/move-position | Move Position for Sub-account (For Master Account)
[**subaccount_create_sub_account_futures_transfer_v1**](V1Api.md#subaccount_create_sub_account_futures_transfer_v1) | **POST** /sapi/v1/sub-account/futures/transfer | Futures Transfer for Sub-account(For Master Account)
[**subaccount_create_sub_account_margin_enable_v1**](V1Api.md#subaccount_create_sub_account_margin_enable_v1) | **POST** /sapi/v1/sub-account/margin/enable | Enable Margin for Sub-account(For Master Account)
[**subaccount_create_sub_account_margin_transfer_v1**](V1Api.md#subaccount_create_sub_account_margin_transfer_v1) | **POST** /sapi/v1/sub-account/margin/transfer | Margin Transfer for Sub-account(For Master Account)
[**subaccount_create_sub_account_transfer_sub_to_master_v1**](V1Api.md#subaccount_create_sub_account_transfer_sub_to_master_v1) | **POST** /sapi/v1/sub-account/transfer/subToMaster | Transfer to Master(For Sub-account)
[**subaccount_create_sub_account_transfer_sub_to_sub_v1**](V1Api.md#subaccount_create_sub_account_transfer_sub_to_sub_v1) | **POST** /sapi/v1/sub-account/transfer/subToSub | Transfer to Sub-account of Same Master(For Sub-account)
[**subaccount_create_sub_account_universal_transfer_v1**](V1Api.md#subaccount_create_sub_account_universal_transfer_v1) | **POST** /sapi/v1/sub-account/universalTransfer | Universal Transfer(For Master Account)
[**subaccount_create_sub_account_virtual_sub_account_v1**](V1Api.md#subaccount_create_sub_account_virtual_sub_account_v1) | **POST** /sapi/v1/sub-account/virtualSubAccount | Create a Virtual Sub-account(For Master Account)
[**subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1**](V1Api.md#subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1) | **DELETE** /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList | Delete IP List For a Sub-account API Key(For Master Account)
[**subaccount_get_capital_deposit_sub_address_v1**](V1Api.md#subaccount_get_capital_deposit_sub_address_v1) | **GET** /sapi/v1/capital/deposit/subAddress | Get Sub-account Deposit Address(For Master Account)
[**subaccount_get_capital_deposit_sub_hisrec_v1**](V1Api.md#subaccount_get_capital_deposit_sub_hisrec_v1) | **GET** /sapi/v1/capital/deposit/subHisrec | Get Sub-account Deposit History(For Master Account)
[**subaccount_get_managed_subaccount_account_snapshot_v1**](V1Api.md#subaccount_get_managed_subaccount_account_snapshot_v1) | **GET** /sapi/v1/managed-subaccount/accountSnapshot | Query Managed Sub-account Snapshot(For Investor Master Account)
[**subaccount_get_managed_subaccount_asset_v1**](V1Api.md#subaccount_get_managed_subaccount_asset_v1) | **GET** /sapi/v1/managed-subaccount/asset | Query Managed Sub-account Asset Details(For Investor Master Account)
[**subaccount_get_managed_subaccount_deposit_address_v1**](V1Api.md#subaccount_get_managed_subaccount_deposit_address_v1) | **GET** /sapi/v1/managed-subaccount/deposit/address | Get Managed Sub-account Deposit Address (For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_fetch_future_asset_v1**](V1Api.md#subaccount_get_managed_subaccount_fetch_future_asset_v1) | **GET** /sapi/v1/managed-subaccount/fetch-future-asset | Query Managed Sub-account Futures Asset Details(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_info_v1**](V1Api.md#subaccount_get_managed_subaccount_info_v1) | **GET** /sapi/v1/managed-subaccount/info | Query Managed Sub-account List(For Investor)(USER_DATA)
[**subaccount_get_managed_subaccount_margin_asset_v1**](V1Api.md#subaccount_get_managed_subaccount_margin_asset_v1) | **GET** /sapi/v1/managed-subaccount/marginAsset | Query Managed Sub-account Margin Asset Details(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_for_investor_v1**](V1Api.md#subaccount_get_managed_subaccount_query_trans_log_for_investor_v1) | **GET** /sapi/v1/managed-subaccount/queryTransLogForInvestor | Query Managed Sub Account Transfer Log(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1**](V1Api.md#subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1) | **GET** /sapi/v1/managed-subaccount/queryTransLogForTradeParent | Query Managed Sub Account Transfer Log(For Trading Team Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_v1**](V1Api.md#subaccount_get_managed_subaccount_query_trans_log_v1) | **GET** /sapi/v1/managed-subaccount/query-trans-log | Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)
[**subaccount_get_sub_account_futures_account_summary_v1**](V1Api.md#subaccount_get_sub_account_futures_account_summary_v1) | **GET** /sapi/v1/sub-account/futures/accountSummary | Get Summary of Sub-account&#39;s Futures Account(For Master Account)
[**subaccount_get_sub_account_futures_account_v1**](V1Api.md#subaccount_get_sub_account_futures_account_v1) | **GET** /sapi/v1/sub-account/futures/account | Get Detail on Sub-account&#39;s Futures Account(For Master Account)
[**subaccount_get_sub_account_futures_internal_transfer_v1**](V1Api.md#subaccount_get_sub_account_futures_internal_transfer_v1) | **GET** /sapi/v1/sub-account/futures/internalTransfer | Query Sub-account Futures Asset Transfer History(For Master Account)
[**subaccount_get_sub_account_futures_move_position_v1**](V1Api.md#subaccount_get_sub_account_futures_move_position_v1) | **GET** /sapi/v1/sub-account/futures/move-position | Get Move Position History for Sub-account (For Master Account)
[**subaccount_get_sub_account_futures_position_risk_v1**](V1Api.md#subaccount_get_sub_account_futures_position_risk_v1) | **GET** /sapi/v1/sub-account/futures/positionRisk | Get Futures Position-Risk of Sub-account(For Master Account)
[**subaccount_get_sub_account_list_v1**](V1Api.md#subaccount_get_sub_account_list_v1) | **GET** /sapi/v1/sub-account/list | Query Sub-account List(For Master Account)
[**subaccount_get_sub_account_margin_account_summary_v1**](V1Api.md#subaccount_get_sub_account_margin_account_summary_v1) | **GET** /sapi/v1/sub-account/margin/accountSummary | Get Summary of Sub-account&#39;s Margin Account(For Master Account)
[**subaccount_get_sub_account_margin_account_v1**](V1Api.md#subaccount_get_sub_account_margin_account_v1) | **GET** /sapi/v1/sub-account/margin/account | Get Detail on Sub-account&#39;s Margin Account(For Master Account)
[**subaccount_get_sub_account_spot_summary_v1**](V1Api.md#subaccount_get_sub_account_spot_summary_v1) | **GET** /sapi/v1/sub-account/spotSummary | Query Sub-account Spot Assets Summary(For Master Account)
[**subaccount_get_sub_account_status_v1**](V1Api.md#subaccount_get_sub_account_status_v1) | **GET** /sapi/v1/sub-account/status | Get Sub-account&#39;s Status on Margin Or Futures(For Master Account)
[**subaccount_get_sub_account_sub_account_api_ip_restriction_v1**](V1Api.md#subaccount_get_sub_account_sub_account_api_ip_restriction_v1) | **GET** /sapi/v1/sub-account/subAccountApi/ipRestriction | Get IP Restriction for a Sub-account API Key(For Master Account)
[**subaccount_get_sub_account_sub_transfer_history_v1**](V1Api.md#subaccount_get_sub_account_sub_transfer_history_v1) | **GET** /sapi/v1/sub-account/sub/transfer/history | Query Sub-account Spot Asset Transfer History(For Master Account)
[**subaccount_get_sub_account_transaction_statistics_v1**](V1Api.md#subaccount_get_sub_account_transaction_statistics_v1) | **GET** /sapi/v1/sub-account/transaction-statistics | Query Sub-account Transaction Statistics(For Master Account)(USER_DATA)
[**subaccount_get_sub_account_transfer_sub_user_history_v1**](V1Api.md#subaccount_get_sub_account_transfer_sub_user_history_v1) | **GET** /sapi/v1/sub-account/transfer/subUserHistory | Sub-account Transfer History(For Sub-account)
[**subaccount_get_sub_account_universal_transfer_v1**](V1Api.md#subaccount_get_sub_account_universal_transfer_v1) | **GET** /sapi/v1/sub-account/universalTransfer | Query Universal Transfer History(For Master Account)


# **subaccount_create_managed_subaccount_deposit_v1**
> SubaccountCreateManagedSubaccountDepositV1Resp subaccount_create_managed_subaccount_deposit_v1(amount, asset, timestamp, to_email, recv_window=recv_window)

Deposit Assets Into The Managed Sub-account(For Investor Master Account)

Deposit Assets Into The Managed Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_managed_subaccount_deposit_v1_resp import SubaccountCreateManagedSubaccountDepositV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Deposit Assets Into The Managed Sub-account(For Investor Master Account)
        api_response = api_instance.subaccount_create_managed_subaccount_deposit_v1(amount, asset, timestamp, to_email, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_managed_subaccount_deposit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_managed_subaccount_deposit_v1: %s\n" % e)
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

[**SubaccountCreateManagedSubaccountDepositV1Resp**](SubaccountCreateManagedSubaccountDepositV1Resp.md)

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

# **subaccount_create_managed_subaccount_withdraw_v1**
> SubaccountCreateManagedSubaccountWithdrawV1Resp subaccount_create_managed_subaccount_withdraw_v1(amount, asset, from_email, timestamp, recv_window=recv_window, transfer_date=transfer_date)

Withdrawl Assets From The Managed Sub-account(For Investor Master Account)

Withdrawl Assets From The Managed Sub-account

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_create_managed_subaccount_withdraw_v1_resp import SubaccountCreateManagedSubaccountWithdrawV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    from_email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    transfer_date = 56 # int |  (optional)

    try:
        # Withdrawl Assets From The Managed Sub-account(For Investor Master Account)
        api_response = api_instance.subaccount_create_managed_subaccount_withdraw_v1(amount, asset, from_email, timestamp, recv_window=recv_window, transfer_date=transfer_date)
        print("The response of V1Api->subaccount_create_managed_subaccount_withdraw_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_managed_subaccount_withdraw_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **from_email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **transfer_date** | **int**|  | [optional] 

### Return type

[**SubaccountCreateManagedSubaccountWithdrawV1Resp**](SubaccountCreateManagedSubaccountWithdrawV1Resp.md)

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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    enable_blvt = True # bool | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Leverage Token for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_blvt_enable_v1(email, enable_blvt, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_blvt_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_blvt_enable_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Options for Sub-account(For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_create_sub_account_eoptions_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_eoptions_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_eoptions_enable_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Futures for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_futures_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_futures_enable_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_create_sub_account_futures_internal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_futures_internal_transfer_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    from_user_email = '' # str |  (default to '')
    order_args = None # List[object] | 
    product_type = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_user_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Move Position for Sub-account (For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_move_position_v1(from_user_email, order_args, product_type, timestamp, to_user_email, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_futures_move_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_futures_move_position_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Transfer for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_futures_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_futures_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_futures_transfer_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Margin for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_margin_enable_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_margin_enable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_margin_enable_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Transfer for Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_margin_transfer_v1(amount, asset, email, timestamp, type, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_margin_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_margin_transfer_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Transfer to Master(For Sub-account)
        api_response = api_instance.subaccount_create_sub_account_transfer_sub_to_master_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_transfer_sub_to_master_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_transfer_sub_to_master_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Transfer to Sub-account of Same Master(For Sub-account)
        api_response = api_instance.subaccount_create_sub_account_transfer_sub_to_sub_v1(amount, asset, timestamp, to_email, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_transfer_sub_to_sub_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_transfer_sub_to_sub_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_create_sub_account_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_universal_transfer_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    sub_account_string = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Create a Virtual Sub-account(For Master Account)
        api_response = api_instance.subaccount_create_sub_account_virtual_sub_account_v1(sub_account_string, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_create_sub_account_virtual_sub_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_create_sub_account_virtual_sub_account_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#email-address\">Sub-account email</a> (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str | Can be added in batches, separated by commas (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Delete IP List For a Sub-account API Key(For Master Account)
        api_response = api_instance.subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1(email, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of V1Api->subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Sub account email (default to '')
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub-account Deposit Address(For Master Account)
        api_response = api_instance.subaccount_get_capital_deposit_sub_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_capital_deposit_sub_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_capital_deposit_sub_address_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_capital_deposit_sub_hisrec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_capital_deposit_sub_hisrec_v1: %s\n" % e)
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

# **subaccount_get_managed_subaccount_account_snapshot_v1**
> SubaccountGetManagedSubaccountAccountSnapshotV1Resp subaccount_get_managed_subaccount_account_snapshot_v1(email, type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Managed Sub-account Snapshot(For Investor Master Account)

Query Managed Sub-account Snapshot

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp import SubaccountGetManagedSubaccountAccountSnapshotV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    type = '' # str | &#34;SPOT&#34;, &#34;MARGIN&#34;（cross）, &#34;FUTURES&#34;（UM） (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 7 # int | min 7, max 30, default 7 (optional) (default to 7)
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub-account Snapshot(For Investor Master Account)
        api_response = api_instance.subaccount_get_managed_subaccount_account_snapshot_v1(email, type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_managed_subaccount_account_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_account_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **type** | **str**| &amp;#34;SPOT&amp;#34;, &amp;#34;MARGIN&amp;#34;（cross）, &amp;#34;FUTURES&amp;#34;（UM） | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| min 7, max 30, default 7 | [optional] [default to 7]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetManagedSubaccountAccountSnapshotV1Resp**](SubaccountGetManagedSubaccountAccountSnapshotV1Resp.md)

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

# **subaccount_get_managed_subaccount_asset_v1**
> List[SubaccountGetManagedSubaccountAssetV1RespItem] subaccount_get_managed_subaccount_asset_v1(email, timestamp, recv_window=recv_window)

Query Managed Sub-account Asset Details(For Investor Master Account)

Query Managed Sub-account Asset Details

### Example


```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_asset_v1_resp_item import SubaccountGetManagedSubaccountAssetV1RespItem
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub-account Asset Details(For Investor Master Account)
        api_response = api_instance.subaccount_get_managed_subaccount_asset_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_managed_subaccount_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_asset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[SubaccountGetManagedSubaccountAssetV1RespItem]**](SubaccountGetManagedSubaccountAssetV1RespItem.md)

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

# **subaccount_get_managed_subaccount_deposit_address_v1**
> SubaccountGetManagedSubaccountDepositAddressV1Resp subaccount_get_managed_subaccount_deposit_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)

Get Managed Sub-account Deposit Address (For Investor Master Account)(USER_DATA)

Get investor's managed sub-account deposit address.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_deposit_address_v1_resp import SubaccountGetManagedSubaccountDepositAddressV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Sub user email (default to '')
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str | networks can be found in `GET /sapi/v1/capital/deposit/address` (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Managed Sub-account Deposit Address (For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_deposit_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_managed_subaccount_deposit_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_deposit_address_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub user email | [default to &#39;&#39;]
 **coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **network** | **str**| networks can be found in &#x60;GET /sapi/v1/capital/deposit/address&#x60; | [optional] [default to &#39;&#39;]
 **amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetManagedSubaccountDepositAddressV1Resp**](SubaccountGetManagedSubaccountDepositAddressV1Resp.md)

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

# **subaccount_get_managed_subaccount_fetch_future_asset_v1**
> SubaccountGetManagedSubaccountFetchFutureAssetV1Resp subaccount_get_managed_subaccount_fetch_future_asset_v1(email, account_type=account_type)

Query Managed Sub-account Futures Asset Details(For Investor Master Account)(USER_DATA)

Investor can use this api to query managed sub account futures asset details

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp import SubaccountGetManagedSubaccountFetchFutureAssetV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    account_type = '' # str | No input or input &#34;USDT_FUTURE&#34; to get UM Futures account details. Input &#34;COIN_FUTURE&#34; to get CM Futures account details. (optional) (default to '')

    try:
        # Query Managed Sub-account Futures Asset Details(For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_fetch_future_asset_v1(email, account_type=account_type)
        print("The response of V1Api->subaccount_get_managed_subaccount_fetch_future_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_fetch_future_asset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Managed Sub Account Email | [default to &#39;&#39;]
 **account_type** | **str**| No input or input &amp;#34;USDT_FUTURE&amp;#34; to get UM Futures account details. Input &amp;#34;COIN_FUTURE&amp;#34; to get CM Futures account details. | [optional] [default to &#39;&#39;]

### Return type

[**SubaccountGetManagedSubaccountFetchFutureAssetV1Resp**](SubaccountGetManagedSubaccountFetchFutureAssetV1Resp.md)

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

# **subaccount_get_managed_subaccount_info_v1**
> SubaccountGetManagedSubaccountInfoV1Resp subaccount_get_managed_subaccount_info_v1(timestamp, email=email, page=page, limit=limit, recv_window=recv_window)

Query Managed Sub-account List(For Investor)(USER_DATA)

Get investor's managed sub-account list.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_info_v1_resp import SubaccountGetManagedSubaccountInfoV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    email = '' # str | Managed sub-account email (optional) (default to '')
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 20, Max value: 20 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub-account List(For Investor)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_info_v1(timestamp, email=email, page=page, limit=limit, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_managed_subaccount_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **email** | **str**| Managed sub-account email | [optional] [default to &#39;&#39;]
 **page** | **int**| Default value: 1 | [optional] 
 **limit** | **int**| Default value: 20, Max value: 20 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetManagedSubaccountInfoV1Resp**](SubaccountGetManagedSubaccountInfoV1Resp.md)

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

# **subaccount_get_managed_subaccount_margin_asset_v1**
> SubaccountGetManagedSubaccountMarginAssetV1Resp subaccount_get_managed_subaccount_margin_asset_v1(email, account_type=account_type)

Query Managed Sub-account Margin Asset Details(For Investor Master Account)(USER_DATA)

Investor can use this api to query managed sub account margin asset details

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp import SubaccountGetManagedSubaccountMarginAssetV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    account_type = '' # str | No input or input &#34;MARGIN&#34; to get Cross Margin account details. Input &#34;ISOLATED_MARGIN&#34; to get Isolated Margin account details. (optional) (default to '')

    try:
        # Query Managed Sub-account Margin Asset Details(For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_margin_asset_v1(email, account_type=account_type)
        print("The response of V1Api->subaccount_get_managed_subaccount_margin_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_margin_asset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Managed Sub Account Email | [default to &#39;&#39;]
 **account_type** | **str**| No input or input &amp;#34;MARGIN&amp;#34; to get Cross Margin account details. Input &amp;#34;ISOLATED_MARGIN&amp;#34; to get Isolated Margin account details. | [optional] [default to &#39;&#39;]

### Return type

[**SubaccountGetManagedSubaccountMarginAssetV1Resp**](SubaccountGetManagedSubaccountMarginAssetV1Resp.md)

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

# **subaccount_get_managed_subaccount_query_trans_log_for_investor_v1**
> SubaccountGetManagedSubaccountQueryTransLogForInvestorV1Resp subaccount_get_managed_subaccount_query_trans_log_for_investor_v1(email, start_time, end_time, page, limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type)

Query Managed Sub Account Transfer Log(For Investor Master Account)(USER_DATA)

Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team.
Please refer to link

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_query_trans_log_for_investor_v1_resp import SubaccountGetManagedSubaccountQueryTransLogForInvestorV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    start_time = 56 # int | Start Time
    end_time = 56 # int | End Time (The start time and end time interval cannot exceed half a year)
    page = 56 # int | Page
    limit = 56 # int | Limit (Max: 500)
    transfers = '' # str | Transfer Direction (FROM/TO) (optional) (default to '')
    transfer_function_account_type = '' # str | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) (optional) (default to '')

    try:
        # Query Managed Sub Account Transfer Log(For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_query_trans_log_for_investor_v1(email, start_time, end_time, page, limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type)
        print("The response of V1Api->subaccount_get_managed_subaccount_query_trans_log_for_investor_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_query_trans_log_for_investor_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Managed Sub Account Email | [default to &#39;&#39;]
 **start_time** | **int**| Start Time | 
 **end_time** | **int**| End Time (The start time and end time interval cannot exceed half a year) | 
 **page** | **int**| Page | 
 **limit** | **int**| Limit (Max: 500) | 
 **transfers** | **str**| Transfer Direction (FROM/TO) | [optional] [default to &#39;&#39;]
 **transfer_function_account_type** | **str**| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) | [optional] [default to &#39;&#39;]

### Return type

[**SubaccountGetManagedSubaccountQueryTransLogForInvestorV1Resp**](SubaccountGetManagedSubaccountQueryTransLogForInvestorV1Resp.md)

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

# **subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1**
> SubaccountGetManagedSubaccountQueryTransLogForTradeParentV1Resp subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1(email, start_time, end_time, page, limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type)

Query Managed Sub Account Transfer Log(For Trading Team Master Account)(USER_DATA)

Trading team can use this api to query managed sub account transfer log. This endpoint is available for trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team.
Please refer to link

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1_resp import SubaccountGetManagedSubaccountQueryTransLogForTradeParentV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    start_time = 56 # int | Start Time
    end_time = 56 # int | End Time (The start time and end time interval cannot exceed half a year)
    page = 56 # int | Page
    limit = 56 # int | Limit (Max: 500)
    transfers = '' # str | Transfer Direction (FROM/TO) (optional) (default to '')
    transfer_function_account_type = '' # str | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) (optional) (default to '')

    try:
        # Query Managed Sub Account Transfer Log(For Trading Team Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1(email, start_time, end_time, page, limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type)
        print("The response of V1Api->subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Managed Sub Account Email | [default to &#39;&#39;]
 **start_time** | **int**| Start Time | 
 **end_time** | **int**| End Time (The start time and end time interval cannot exceed half a year) | 
 **page** | **int**| Page | 
 **limit** | **int**| Limit (Max: 500) | 
 **transfers** | **str**| Transfer Direction (FROM/TO) | [optional] [default to &#39;&#39;]
 **transfer_function_account_type** | **str**| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) | [optional] [default to &#39;&#39;]

### Return type

[**SubaccountGetManagedSubaccountQueryTransLogForTradeParentV1Resp**](SubaccountGetManagedSubaccountQueryTransLogForTradeParentV1Resp.md)

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

# **subaccount_get_managed_subaccount_query_trans_log_v1**
> SubaccountGetManagedSubaccountQueryTransLogV1Resp subaccount_get_managed_subaccount_query_trans_log_v1(start_time, end_time, page, limit, timestamp, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.subaccount
from binance.subaccount.models.subaccount_get_managed_subaccount_query_trans_log_v1_resp import SubaccountGetManagedSubaccountQueryTransLogV1Resp
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
    api_instance = binance.subaccount.V1Api(api_client)
    start_time = 56 # int | Start Time
    end_time = 56 # int | End Time (The start time and end time interval cannot exceed half a year)
    page = 56 # int | Page
    limit = 56 # int | Limit (Max: 500)
    timestamp = 56 # int | 
    transfers = '' # str | Transfer Direction (FROM/TO) (optional) (default to '')
    transfer_function_account_type = '' # str | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_query_trans_log_v1(start_time, end_time, page, limit, timestamp, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_managed_subaccount_query_trans_log_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_managed_subaccount_query_trans_log_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Start Time | 
 **end_time** | **int**| End Time (The start time and end time interval cannot exceed half a year) | 
 **page** | **int**| Page | 
 **limit** | **int**| Limit (Max: 500) | 
 **timestamp** | **int**|  | 
 **transfers** | **str**| Transfer Direction (FROM/TO) | [optional] [default to &#39;&#39;]
 **transfer_function_account_type** | **str**| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**SubaccountGetManagedSubaccountQueryTransLogV1Resp**](SubaccountGetManagedSubaccountQueryTransLogV1Resp.md)

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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Futures Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_summary_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_futures_account_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_futures_account_summary_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Futures Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_account_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_futures_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_futures_account_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_sub_account_futures_internal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_futures_internal_transfer_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_sub_account_futures_move_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_futures_move_position_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Position-Risk of Sub-account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_futures_position_risk_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_futures_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_futures_position_risk_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    email = '' # str | <a href=\"/docs/sub_account/account-management/Query-Sub-account-List#email-address\">Sub-account email</a> (optional) (default to '')
    is_freeze = '' # str | true or false (optional) (default to '')
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 1, Max value: 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account List(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_list_v1(timestamp, email=email, is_freeze=is_freeze, page=page, limit=limit, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_list_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Sub-account's Margin Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_margin_account_summary_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_margin_account_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_margin_account_summary_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#email-address\">Sub-account email</a> (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Detail on Sub-account's Margin Account(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_margin_account_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_margin_account_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    email = '' # str | Sub account email (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 20 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Spot Assets Summary(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_spot_summary_v1(timestamp, email=email, page=page, size=size, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_spot_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_spot_summary_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    timestamp = 56 # int | 
    email = '' # str | <a href=\"/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#email-address\">Sub-account email</a> (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub-account's Status on Margin Or Futures(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_status_v1(timestamp, email=email, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_status_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | <a href=\"/docs/sub_account/api-management#email-address\">Sub-account email</a> (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get IP Restriction for a Sub-account API Key(For Master Account)
        api_response = api_instance.subaccount_get_sub_account_sub_account_api_ip_restriction_v1(email, sub_account_api_key, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_sub_account_api_ip_restriction_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_sub_account_api_ip_restriction_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_sub_account_sub_transfer_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_sub_transfer_history_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
    email = '' # str | Sub user email (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub-account Transaction Statistics(For Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_sub_account_transaction_statistics_v1(email, timestamp, recv_window=recv_window)
        print("The response of V1Api->subaccount_get_sub_account_transaction_statistics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_transaction_statistics_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_sub_account_transfer_sub_user_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_transfer_sub_user_history_v1: %s\n" % e)
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
    api_instance = binance.subaccount.V1Api(api_client)
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
        print("The response of V1Api->subaccount_get_sub_account_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->subaccount_get_sub_account_universal_transfer_v1: %s\n" % e)
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

