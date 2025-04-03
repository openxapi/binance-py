# binance.subaccount.ManagedSubAccountApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccount_create_managed_subaccount_deposit_v1**](ManagedSubAccountApi.md#subaccount_create_managed_subaccount_deposit_v1) | **POST** /sapi/v1/managed-subaccount/deposit | Deposit Assets Into The Managed Sub-account(For Investor Master Account)
[**subaccount_create_managed_subaccount_withdraw_v1**](ManagedSubAccountApi.md#subaccount_create_managed_subaccount_withdraw_v1) | **POST** /sapi/v1/managed-subaccount/withdraw | Withdrawl Assets From The Managed Sub-account(For Investor Master Account)
[**subaccount_get_managed_subaccount_account_snapshot_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_account_snapshot_v1) | **GET** /sapi/v1/managed-subaccount/accountSnapshot | Query Managed Sub-account Snapshot(For Investor Master Account)
[**subaccount_get_managed_subaccount_asset_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_asset_v1) | **GET** /sapi/v1/managed-subaccount/asset | Query Managed Sub-account Asset Details(For Investor Master Account)
[**subaccount_get_managed_subaccount_deposit_address_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_deposit_address_v1) | **GET** /sapi/v1/managed-subaccount/deposit/address | Get Managed Sub-account Deposit Address (For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_fetch_future_asset_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_fetch_future_asset_v1) | **GET** /sapi/v1/managed-subaccount/fetch-future-asset | Query Managed Sub-account Futures Asset Details(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_info_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_info_v1) | **GET** /sapi/v1/managed-subaccount/info | Query Managed Sub-account List(For Investor)(USER_DATA)
[**subaccount_get_managed_subaccount_margin_asset_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_margin_asset_v1) | **GET** /sapi/v1/managed-subaccount/marginAsset | Query Managed Sub-account Margin Asset Details(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_for_investor_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_query_trans_log_for_investor_v1) | **GET** /sapi/v1/managed-subaccount/queryTransLogForInvestor | Query Managed Sub Account Transfer Log(For Investor Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1) | **GET** /sapi/v1/managed-subaccount/queryTransLogForTradeParent | Query Managed Sub Account Transfer Log(For Trading Team Master Account)(USER_DATA)
[**subaccount_get_managed_subaccount_query_trans_log_v1**](ManagedSubAccountApi.md#subaccount_get_managed_subaccount_query_trans_log_v1) | **GET** /sapi/v1/managed-subaccount/query-trans-log | Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)


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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_email = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Deposit Assets Into The Managed Sub-account(For Investor Master Account)
        api_response = api_instance.subaccount_create_managed_subaccount_deposit_v1(amount, asset, timestamp, to_email, recv_window=recv_window)
        print("The response of ManagedSubAccountApi->subaccount_create_managed_subaccount_deposit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_create_managed_subaccount_deposit_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    from_email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    transfer_date = 56 # int |  (optional)

    try:
        # Withdrawl Assets From The Managed Sub-account(For Investor Master Account)
        api_response = api_instance.subaccount_create_managed_subaccount_withdraw_v1(amount, asset, from_email, timestamp, recv_window=recv_window, transfer_date=transfer_date)
        print("The response of ManagedSubAccountApi->subaccount_create_managed_subaccount_withdraw_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_create_managed_subaccount_withdraw_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
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
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_account_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_account_snapshot_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub-account Asset Details(For Investor Master Account)
        api_response = api_instance.subaccount_get_managed_subaccount_asset_v1(email, timestamp, recv_window=recv_window)
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_asset_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    email = '' # str | Sub user email (default to '')
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str | networks can be found in `GET /sapi/v1/capital/deposit/address` (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Managed Sub-account Deposit Address (For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_deposit_address_v1(email, coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_deposit_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_deposit_address_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    account_type = '' # str | No input or input &#34;USDT_FUTURE&#34; to get UM Futures account details. Input &#34;COIN_FUTURE&#34; to get CM Futures account details. (optional) (default to '')

    try:
        # Query Managed Sub-account Futures Asset Details(For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_fetch_future_asset_v1(email, account_type=account_type)
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_fetch_future_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_fetch_future_asset_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    timestamp = 56 # int | 
    email = '' # str | Managed sub-account email (optional) (default to '')
    page = 56 # int | Default value: 1 (optional)
    limit = 56 # int | Default value: 20, Max value: 20 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Managed Sub-account List(For Investor)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_info_v1(timestamp, email=email, page=page, limit=limit, recv_window=recv_window)
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_info_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
    email = '' # str | Managed Sub Account Email (default to '')
    account_type = '' # str | No input or input &#34;MARGIN&#34; to get Cross Margin account details. Input &#34;ISOLATED_MARGIN&#34; to get Isolated Margin account details. (optional) (default to '')

    try:
        # Query Managed Sub-account Margin Asset Details(For Investor Master Account)(USER_DATA)
        api_response = api_instance.subaccount_get_managed_subaccount_margin_asset_v1(email, account_type=account_type)
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_margin_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_margin_asset_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
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
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_for_investor_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_for_investor_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
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
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_for_trade_parent_v1: %s\n" % e)
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
    api_instance = binance.subaccount.ManagedSubAccountApi(api_client)
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
        print("The response of ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedSubAccountApi->subaccount_get_managed_subaccount_query_trans_log_v1: %s\n" % e)
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

