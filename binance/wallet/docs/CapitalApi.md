# binance.wallet.CapitalApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_capital_deposit_credit_apply_v1**](CapitalApi.md#wallet_create_capital_deposit_credit_apply_v1) | **POST** /sapi/v1/capital/deposit/credit-apply | One click arrival deposit apply (for expired address deposit) (USER_DATA)
[**wallet_create_capital_withdraw_apply_v1**](CapitalApi.md#wallet_create_capital_withdraw_apply_v1) | **POST** /sapi/v1/capital/withdraw/apply | Withdraw(USER_DATA)
[**wallet_get_capital_config_getall_v1**](CapitalApi.md#wallet_get_capital_config_getall_v1) | **GET** /sapi/v1/capital/config/getall | All Coins&#39; Information (USER_DATA)
[**wallet_get_capital_deposit_address_list_v1**](CapitalApi.md#wallet_get_capital_deposit_address_list_v1) | **GET** /sapi/v1/capital/deposit/address/list | Fetch deposit address list with network(USER_DATA)
[**wallet_get_capital_deposit_address_v1**](CapitalApi.md#wallet_get_capital_deposit_address_v1) | **GET** /sapi/v1/capital/deposit/address | Deposit Address(supporting network) (USER_DATA)
[**wallet_get_capital_deposit_hisrec_v1**](CapitalApi.md#wallet_get_capital_deposit_hisrec_v1) | **GET** /sapi/v1/capital/deposit/hisrec | Deposit History (supporting network) (USER_DATA)
[**wallet_get_capital_withdraw_address_list_v1**](CapitalApi.md#wallet_get_capital_withdraw_address_list_v1) | **GET** /sapi/v1/capital/withdraw/address/list | Fetch withdraw address list (USER_DATA)
[**wallet_get_capital_withdraw_history_v1**](CapitalApi.md#wallet_get_capital_withdraw_history_v1) | **GET** /sapi/v1/capital/withdraw/history | Withdraw History (supporting network) (USER_DATA)


# **wallet_create_capital_deposit_credit_apply_v1**
> WalletCreateCapitalDepositCreditApplyV1Resp wallet_create_capital_deposit_credit_apply_v1(deposit_id=deposit_id, sub_account_id=sub_account_id, sub_user_id=sub_user_id, tx_id=tx_id)

One click arrival deposit apply (for expired address deposit) (USER_DATA)

Apply deposit credit for expired address (One click arrival)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_capital_deposit_credit_apply_v1_resp import WalletCreateCapitalDepositCreditApplyV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    deposit_id = 56 # int |  (optional)
    sub_account_id = 56 # int |  (optional)
    sub_user_id = 56 # int |  (optional)
    tx_id = '' # str |  (optional) (default to '')

    try:
        # One click arrival deposit apply (for expired address deposit) (USER_DATA)
        api_response = api_instance.wallet_create_capital_deposit_credit_apply_v1(deposit_id=deposit_id, sub_account_id=sub_account_id, sub_user_id=sub_user_id, tx_id=tx_id)
        print("The response of CapitalApi->wallet_create_capital_deposit_credit_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_create_capital_deposit_credit_apply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_id** | **int**|  | [optional] 
 **sub_account_id** | **int**|  | [optional] 
 **sub_user_id** | **int**|  | [optional] 
 **tx_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletCreateCapitalDepositCreditApplyV1Resp**](WalletCreateCapitalDepositCreditApplyV1Resp.md)

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

# **wallet_create_capital_withdraw_apply_v1**
> WalletCreateCapitalWithdrawApplyV1Resp wallet_create_capital_withdraw_apply_v1(address, amount, coin, timestamp, address_tag=address_tag, name=name, network=network, recv_window=recv_window, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type, withdraw_order_id=withdraw_order_id)

Withdraw(USER_DATA)

Submit a withdraw request.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_capital_withdraw_apply_v1_resp import WalletCreateCapitalWithdrawApplyV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    address = '' # str |  (default to '')
    amount = '' # str |  (default to '')
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    address_tag = '' # str |  (optional) (default to '')
    name = '' # str |  (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    transaction_fee_flag = False # bool |  (optional) (default to False)
    wallet_type = 56 # int |  (optional)
    withdraw_order_id = '' # str |  (optional) (default to '')

    try:
        # Withdraw(USER_DATA)
        api_response = api_instance.wallet_create_capital_withdraw_apply_v1(address, amount, coin, timestamp, address_tag=address_tag, name=name, network=network, recv_window=recv_window, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type, withdraw_order_id=withdraw_order_id)
        print("The response of CapitalApi->wallet_create_capital_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_create_capital_withdraw_apply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | [default to &#39;&#39;]
 **amount** | **str**|  | [default to &#39;&#39;]
 **coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **address_tag** | **str**|  | [optional] [default to &#39;&#39;]
 **name** | **str**|  | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **transaction_fee_flag** | **bool**|  | [optional] [default to False]
 **wallet_type** | **int**|  | [optional] 
 **withdraw_order_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletCreateCapitalWithdrawApplyV1Resp**](WalletCreateCapitalWithdrawApplyV1Resp.md)

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

# **wallet_get_capital_config_getall_v1**
> List[WalletGetCapitalConfigGetallV1RespItem] wallet_get_capital_config_getall_v1(timestamp, recv_window=recv_window)

All Coins' Information (USER_DATA)

Get information of coins (available for deposit and withdraw) for user.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_config_getall_v1_resp_item import WalletGetCapitalConfigGetallV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # All Coins' Information (USER_DATA)
        api_response = api_instance.wallet_get_capital_config_getall_v1(timestamp, recv_window=recv_window)
        print("The response of CapitalApi->wallet_get_capital_config_getall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_config_getall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetCapitalConfigGetallV1RespItem]**](WalletGetCapitalConfigGetallV1RespItem.md)

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

# **wallet_get_capital_deposit_address_list_v1**
> List[WalletGetCapitalDepositAddressListV1RespItem] wallet_get_capital_deposit_address_list_v1(coin, timestamp, network=network)

Fetch deposit address list with network(USER_DATA)

Fetch deposit address list with network.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_deposit_address_list_v1_resp_item import WalletGetCapitalDepositAddressListV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    coin = '' # str | `coin` refers to the parent network address format that the address is using (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')

    try:
        # Fetch deposit address list with network(USER_DATA)
        api_response = api_instance.wallet_get_capital_deposit_address_list_v1(coin, timestamp, network=network)
        print("The response of CapitalApi->wallet_get_capital_deposit_address_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_deposit_address_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| &#x60;coin&#x60; refers to the parent network address format that the address is using | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **network** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[WalletGetCapitalDepositAddressListV1RespItem]**](WalletGetCapitalDepositAddressListV1RespItem.md)

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

# **wallet_get_capital_deposit_address_v1**
> WalletGetCapitalDepositAddressV1Resp wallet_get_capital_deposit_address_v1(coin, timestamp, network=network, amount=amount, recv_window=recv_window)

Deposit Address(supporting network) (USER_DATA)

Fetch deposit address with network.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_deposit_address_v1_resp import WalletGetCapitalDepositAddressV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Deposit Address(supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_capital_deposit_address_v1(coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of CapitalApi->wallet_get_capital_deposit_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_deposit_address_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetCapitalDepositAddressV1Resp**](WalletGetCapitalDepositAddressV1Resp.md)

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

# **wallet_get_capital_deposit_hisrec_v1**
> List[WalletGetCapitalDepositHisrecV1RespItem] wallet_get_capital_deposit_hisrec_v1(timestamp, include_source=include_source, coin=coin, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window, tx_id=tx_id)

Deposit History (supporting network) (USER_DATA)

Fetch deposit history.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_deposit_hisrec_v1_resp_item import WalletGetCapitalDepositHisrecV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    timestamp = 56 # int | 
    include_source = False # bool | Default: `false`, return `sourceAddress`field when set to `true` (optional) (default to False)
    coin = '' # str |  (optional) (default to '')
    status = 56 # int | 0(0:pending, 6:credited but cannot withdraw, 7:Wrong Deposit, 8:Waiting User confirm, 1:success, 2:rejected) (optional)
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    offset = 56 # int | Default:0 (optional)
    limit = 56 # int | Default:1000, Max:1000 (optional)
    recv_window = 56 # int |  (optional)
    tx_id = '' # str |  (optional) (default to '')

    try:
        # Deposit History (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_capital_deposit_hisrec_v1(timestamp, include_source=include_source, coin=coin, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window, tx_id=tx_id)
        print("The response of CapitalApi->wallet_get_capital_deposit_hisrec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_deposit_hisrec_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **include_source** | **bool**| Default: &#x60;false&#x60;, return &#x60;sourceAddress&#x60;field when set to &#x60;true&#x60; | [optional] [default to False]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **int**| 0(0:pending, 6:credited but cannot withdraw, 7:Wrong Deposit, 8:Waiting User confirm, 1:success, 2:rejected) | [optional] 
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **offset** | **int**| Default:0 | [optional] 
 **limit** | **int**| Default:1000, Max:1000 | [optional] 
 **recv_window** | **int**|  | [optional] 
 **tx_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[WalletGetCapitalDepositHisrecV1RespItem]**](WalletGetCapitalDepositHisrecV1RespItem.md)

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

# **wallet_get_capital_withdraw_address_list_v1**
> List[WalletGetCapitalWithdrawAddressListV1RespItem] wallet_get_capital_withdraw_address_list_v1()

Fetch withdraw address list (USER_DATA)

Fetch withdraw address list

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_withdraw_address_list_v1_resp_item import WalletGetCapitalWithdrawAddressListV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)

    try:
        # Fetch withdraw address list (USER_DATA)
        api_response = api_instance.wallet_get_capital_withdraw_address_list_v1()
        print("The response of CapitalApi->wallet_get_capital_withdraw_address_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_withdraw_address_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WalletGetCapitalWithdrawAddressListV1RespItem]**](WalletGetCapitalWithdrawAddressListV1RespItem.md)

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

# **wallet_get_capital_withdraw_history_v1**
> List[WalletGetCapitalWithdrawHistoryV1RespItem] wallet_get_capital_withdraw_history_v1(timestamp, coin=coin, withdraw_order_id=withdraw_order_id, status=status, offset=offset, limit=limit, id_list=id_list, start_time=start_time, end_time=end_time, recv_window=recv_window)

Withdraw History (supporting network) (USER_DATA)

Fetch withdraw history.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_capital_withdraw_history_v1_resp_item import WalletGetCapitalWithdrawHistoryV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.CapitalApi(api_client)
    timestamp = 56 # int | 
    coin = '' # str |  (optional) (default to '')
    withdraw_order_id = '' # str |  (optional) (default to '')
    status = 56 # int | 0(0:Email Sent, 2:Awaiting Approval 3:Rejected 4:Processing 6:Completed) (optional)
    offset = 56 # int |  (optional)
    limit = 1000 # int | Default: 1000, Max: 1000 (optional) (default to 1000)
    id_list = '' # str | id list returned in the response of POST `/sapi/v1/capital/withdraw/apply`, separated by `,` (optional) (default to '')
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Withdraw History (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_capital_withdraw_history_v1(timestamp, coin=coin, withdraw_order_id=withdraw_order_id, status=status, offset=offset, limit=limit, id_list=id_list, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of CapitalApi->wallet_get_capital_withdraw_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapitalApi->wallet_get_capital_withdraw_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **withdraw_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **int**| 0(0:Email Sent, 2:Awaiting Approval 3:Rejected 4:Processing 6:Completed) | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**| Default: 1000, Max: 1000 | [optional] [default to 1000]
 **id_list** | **str**| id list returned in the response of POST &#x60;/sapi/v1/capital/withdraw/apply&#x60;, separated by &#x60;,&#x60; | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetCapitalWithdrawHistoryV1RespItem]**](WalletGetCapitalWithdrawHistoryV1RespItem.md)

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

