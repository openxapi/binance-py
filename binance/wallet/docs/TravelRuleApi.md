# binance.wallet.TravelRuleApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_localentity_broker_withdraw_apply_v1**](TravelRuleApi.md#wallet_create_localentity_broker_withdraw_apply_v1) | **POST** /sapi/v1/localentity/broker/withdraw/apply | Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)
[**wallet_create_localentity_withdraw_apply_v1**](TravelRuleApi.md#wallet_create_localentity_withdraw_apply_v1) | **POST** /sapi/v1/localentity/withdraw/apply | Withdraw (for local entities that require travel rule) (USER_DATA)
[**wallet_get_localentity_deposit_history_v1**](TravelRuleApi.md#wallet_get_localentity_deposit_history_v1) | **GET** /sapi/v1/localentity/deposit/history | Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)
[**wallet_get_localentity_vasp_v1**](TravelRuleApi.md#wallet_get_localentity_vasp_v1) | **GET** /sapi/v1/localentity/vasp | Onboarded VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_get_localentity_withdraw_history_v1**](TravelRuleApi.md#wallet_get_localentity_withdraw_history_v1) | **GET** /sapi/v1/localentity/withdraw/history | Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_get_localentity_withdraw_history_v2**](TravelRuleApi.md#wallet_get_localentity_withdraw_history_v2) | **GET** /sapi/v2/localentity/withdraw/history | Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_update_localentity_broker_deposit_provide_info_v1**](TravelRuleApi.md#wallet_update_localentity_broker_deposit_provide_info_v1) | **PUT** /sapi/v1/localentity/broker/deposit/provide-info | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_update_localentity_deposit_provide_info_v1**](TravelRuleApi.md#wallet_update_localentity_deposit_provide_info_v1) | **PUT** /sapi/v1/localentity/deposit/provide-info | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)


# **wallet_create_localentity_broker_withdraw_apply_v1**
> WalletCreateLocalentityBrokerWithdrawApplyV1Resp wallet_create_localentity_broker_withdraw_apply_v1(address, amount, coin, originator_pii, questionnaire, signature, sub_account_id, timestamp, withdraw_order_id, address_name=address_name, address_tag=address_tag, network=network, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type)

Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)

Submit a withdrawal request for brokers of local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_localentity_broker_withdraw_apply_v1_resp import WalletCreateLocalentityBrokerWithdrawApplyV1Resp
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    address = '' # str |  (default to '')
    amount = None # object | 
    coin = '' # str |  (default to '')
    originator_pii = '' # str |  (default to '')
    questionnaire = '' # str |  (default to '')
    signature = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    withdraw_order_id = '' # str |  (default to '')
    address_name = '' # str |  (optional) (default to '')
    address_tag = '' # str |  (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    transaction_fee_flag = False # bool |  (optional) (default to False)
    wallet_type = 56 # int |  (optional)

    try:
        # Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)
        api_response = api_instance.wallet_create_localentity_broker_withdraw_apply_v1(address, amount, coin, originator_pii, questionnaire, signature, sub_account_id, timestamp, withdraw_order_id, address_name=address_name, address_tag=address_tag, network=network, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type)
        print("The response of TravelRuleApi->wallet_create_localentity_broker_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_create_localentity_broker_withdraw_apply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | [default to &#39;&#39;]
 **amount** | [**object**](object.md)|  | 
 **coin** | **str**|  | [default to &#39;&#39;]
 **originator_pii** | **str**|  | [default to &#39;&#39;]
 **questionnaire** | **str**|  | [default to &#39;&#39;]
 **signature** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **withdraw_order_id** | **str**|  | [default to &#39;&#39;]
 **address_name** | **str**|  | [optional] [default to &#39;&#39;]
 **address_tag** | **str**|  | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **transaction_fee_flag** | **bool**|  | [optional] [default to False]
 **wallet_type** | **int**|  | [optional] 

### Return type

[**WalletCreateLocalentityBrokerWithdrawApplyV1Resp**](WalletCreateLocalentityBrokerWithdrawApplyV1Resp.md)

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

# **wallet_create_localentity_withdraw_apply_v1**
> WalletCreateLocalentityWithdrawApplyV1Resp wallet_create_localentity_withdraw_apply_v1(address, amount, coin, questionnaire, timestamp, address_tag=address_tag, name=name, network=network, recv_window=recv_window, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type, withdraw_order_id=withdraw_order_id)

Withdraw (for local entities that require travel rule) (USER_DATA)

Submit a withdrawal request for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_localentity_withdraw_apply_v1_resp import WalletCreateLocalentityWithdrawApplyV1Resp
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    address = '' # str |  (default to '')
    amount = '' # str |  (default to '')
    coin = '' # str |  (default to '')
    questionnaire = '' # str |  (default to '')
    timestamp = 56 # int | 
    address_tag = '' # str |  (optional) (default to '')
    name = '' # str |  (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    transaction_fee_flag = False # bool |  (optional) (default to False)
    wallet_type = 56 # int |  (optional)
    withdraw_order_id = '' # str |  (optional) (default to '')

    try:
        # Withdraw (for local entities that require travel rule) (USER_DATA)
        api_response = api_instance.wallet_create_localentity_withdraw_apply_v1(address, amount, coin, questionnaire, timestamp, address_tag=address_tag, name=name, network=network, recv_window=recv_window, transaction_fee_flag=transaction_fee_flag, wallet_type=wallet_type, withdraw_order_id=withdraw_order_id)
        print("The response of TravelRuleApi->wallet_create_localentity_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_create_localentity_withdraw_apply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | [default to &#39;&#39;]
 **amount** | **str**|  | [default to &#39;&#39;]
 **coin** | **str**|  | [default to &#39;&#39;]
 **questionnaire** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **address_tag** | **str**|  | [optional] [default to &#39;&#39;]
 **name** | **str**|  | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **transaction_fee_flag** | **bool**|  | [optional] [default to False]
 **wallet_type** | **int**|  | [optional] 
 **withdraw_order_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletCreateLocalentityWithdrawApplyV1Resp**](WalletCreateLocalentityWithdrawApplyV1Resp.md)

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

# **wallet_get_localentity_deposit_history_v1**
> List[WalletGetLocalentityDepositHistoryV1RespItem] wallet_get_localentity_deposit_history_v1(timestamp, tr_id=tr_id, tx_id=tx_id, tran_id=tran_id, network=network, coin=coin, travel_rule_status=travel_rule_status, pending_questionnaire=pending_questionnaire, start_time=start_time, end_time=end_time, offset=offset, limit=limit)

Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)

Fetch deposit history for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_localentity_deposit_history_v1_resp_item import WalletGetLocalentityDepositHistoryV1RespItem
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    timestamp = 56 # int | 
    tr_id = '' # str | Comma(,) separated list of travel rule record Ids. (optional) (default to '')
    tx_id = '' # str | Comma(,) separated list of transaction Ids. (optional) (default to '')
    tran_id = '' # str | Comma(,) separated list of wallet tran Ids. (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    coin = '' # str |  (optional) (default to '')
    travel_rule_status = 56 # int | 0:Completed,1:Pending,2:Failed (optional)
    pending_questionnaire = True # bool | true: Only return records that pending deposit questionnaire. false/not provided: return all records. (optional)
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    offset = 56 # int | Default:0 (optional)
    limit = 56 # int | Default:1000, Max:1000 (optional)

    try:
        # Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_deposit_history_v1(timestamp, tr_id=tr_id, tx_id=tx_id, tran_id=tran_id, network=network, coin=coin, travel_rule_status=travel_rule_status, pending_questionnaire=pending_questionnaire, start_time=start_time, end_time=end_time, offset=offset, limit=limit)
        print("The response of TravelRuleApi->wallet_get_localentity_deposit_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_get_localentity_deposit_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **tr_id** | **str**| Comma(,) separated list of travel rule record Ids. | [optional] [default to &#39;&#39;]
 **tx_id** | **str**| Comma(,) separated list of transaction Ids. | [optional] [default to &#39;&#39;]
 **tran_id** | **str**| Comma(,) separated list of wallet tran Ids. | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **travel_rule_status** | **int**| 0:Completed,1:Pending,2:Failed | [optional] 
 **pending_questionnaire** | **bool**| true: Only return records that pending deposit questionnaire. false/not provided: return all records. | [optional] 
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **offset** | **int**| Default:0 | [optional] 
 **limit** | **int**| Default:1000, Max:1000 | [optional] 

### Return type

[**List[WalletGetLocalentityDepositHistoryV1RespItem]**](WalletGetLocalentityDepositHistoryV1RespItem.md)

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

# **wallet_get_localentity_vasp_v1**
> List[WalletGetLocalentityVaspV1RespItem] wallet_get_localentity_vasp_v1()

Onboarded VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)

Fetch the onboarded VASP list for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_localentity_vasp_v1_resp_item import WalletGetLocalentityVaspV1RespItem
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
    api_instance = binance.wallet.TravelRuleApi(api_client)

    try:
        # Onboarded VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_vasp_v1()
        print("The response of TravelRuleApi->wallet_get_localentity_vasp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_get_localentity_vasp_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WalletGetLocalentityVaspV1RespItem]**](WalletGetLocalentityVaspV1RespItem.md)

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

# **wallet_get_localentity_withdraw_history_v1**
> List[WalletGetLocalentityWithdrawHistoryV1RespItem] wallet_get_localentity_withdraw_history_v1(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)

Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA)

Fetch withdraw history for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_localentity_withdraw_history_v1_resp_item import WalletGetLocalentityWithdrawHistoryV1RespItem
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    timestamp = 56 # int | 
    tr_id = '' # str | Comma(,) separated list of travel rule record Ids. (optional) (default to '')
    tx_id = '' # str | Comma(,) separated list of transaction Ids. (optional) (default to '')
    withdraw_order_id = '' # str | Comma(,) separated list of withdrawID defined by the client (i.e. client&#39;s internal withdrawID). (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    coin = '' # str |  (optional) (default to '')
    travel_rule_status = 56 # int | 0:Completed,1:Pending,2:Failed (optional)
    offset = 0 # int | Default: 0 (optional) (default to 0)
    limit = 1000 # int | Default: 1000, Max: 1000 (optional) (default to 1000)
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_withdraw_history_v1(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of TravelRuleApi->wallet_get_localentity_withdraw_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_get_localentity_withdraw_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **tr_id** | **str**| Comma(,) separated list of travel rule record Ids. | [optional] [default to &#39;&#39;]
 **tx_id** | **str**| Comma(,) separated list of transaction Ids. | [optional] [default to &#39;&#39;]
 **withdraw_order_id** | **str**| Comma(,) separated list of withdrawID defined by the client (i.e. client&amp;#39;s internal withdrawID). | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **travel_rule_status** | **int**| 0:Completed,1:Pending,2:Failed | [optional] 
 **offset** | **int**| Default: 0 | [optional] [default to 0]
 **limit** | **int**| Default: 1000, Max: 1000 | [optional] [default to 1000]
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetLocalentityWithdrawHistoryV1RespItem]**](WalletGetLocalentityWithdrawHistoryV1RespItem.md)

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

# **wallet_get_localentity_withdraw_history_v2**
> List[WalletGetLocalentityWithdrawHistoryV2RespItem] wallet_get_localentity_withdraw_history_v2(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)

Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)

Fetch withdraw history for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_localentity_withdraw_history_v2_resp_item import WalletGetLocalentityWithdrawHistoryV2RespItem
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    timestamp = 56 # int | 
    tr_id = '' # str | Comma(,) separated list of travel rule record Ids. (optional) (default to '')
    tx_id = '' # str | Comma(,) separated list of transaction Ids. (optional) (default to '')
    withdraw_order_id = '' # str | Withdraw ID defined by the client (i.e. client&#39;s internal withdrawID). (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    coin = '' # str |  (optional) (default to '')
    travel_rule_status = 56 # int | 0:Completed,1:Pending,2:Failed (optional)
    offset = 0 # int | Default: 0 (optional) (default to 0)
    limit = 1000 # int | Default: 1000, Max: 1000 (optional) (default to 1000)
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_withdraw_history_v2(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of TravelRuleApi->wallet_get_localentity_withdraw_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_get_localentity_withdraw_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **tr_id** | **str**| Comma(,) separated list of travel rule record Ids. | [optional] [default to &#39;&#39;]
 **tx_id** | **str**| Comma(,) separated list of transaction Ids. | [optional] [default to &#39;&#39;]
 **withdraw_order_id** | **str**| Withdraw ID defined by the client (i.e. client&amp;#39;s internal withdrawID). | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **travel_rule_status** | **int**| 0:Completed,1:Pending,2:Failed | [optional] 
 **offset** | **int**| Default: 0 | [optional] [default to 0]
 **limit** | **int**| Default: 1000, Max: 1000 | [optional] [default to 1000]
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetLocalentityWithdrawHistoryV2RespItem]**](WalletGetLocalentityWithdrawHistoryV2RespItem.md)

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

# **wallet_update_localentity_broker_deposit_provide_info_v1**
> WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp wallet_update_localentity_broker_deposit_provide_info_v1(beneficiary_pii, deposit_id, questionnaire, signature, sub_account_id, timestamp, address=address, address_tag=address_tag, amount=amount, coin=coin, network=network)

Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

Submit questionnaire for brokers of local entities that require travel rule.
The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not
yet onboarded with GTR.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_update_localentity_broker_deposit_provide_info_v1_resp import WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    beneficiary_pii = '' # str |  (default to '')
    deposit_id = '' # str |  (default to '')
    questionnaire = '' # str |  (default to '')
    signature = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    address = '' # str |  (optional) (default to '')
    address_tag = '' # str |  (optional) (default to '')
    amount = None # object |  (optional)
    coin = '' # str |  (optional) (default to '')
    network = '' # str |  (optional) (default to '')

    try:
        # Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_update_localentity_broker_deposit_provide_info_v1(beneficiary_pii, deposit_id, questionnaire, signature, sub_account_id, timestamp, address=address, address_tag=address_tag, amount=amount, coin=coin, network=network)
        print("The response of TravelRuleApi->wallet_update_localentity_broker_deposit_provide_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_update_localentity_broker_deposit_provide_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_pii** | **str**|  | [default to &#39;&#39;]
 **deposit_id** | **str**|  | [default to &#39;&#39;]
 **questionnaire** | **str**|  | [default to &#39;&#39;]
 **signature** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **address** | **str**|  | [optional] [default to &#39;&#39;]
 **address_tag** | **str**|  | [optional] [default to &#39;&#39;]
 **amount** | [**object**](object.md)|  | [optional] 
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp**](WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp.md)

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

# **wallet_update_localentity_deposit_provide_info_v1**
> WalletUpdateLocalentityDepositProvideInfoV1Resp wallet_update_localentity_deposit_provide_info_v1(questionnaire, timestamp, tran_id)

Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

Submit questionnaire for local entities that require travel rule.
The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not
yet onboarded with GTR.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_update_localentity_deposit_provide_info_v1_resp import WalletUpdateLocalentityDepositProvideInfoV1Resp
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
    api_instance = binance.wallet.TravelRuleApi(api_client)
    questionnaire = '' # str |  (default to '')
    timestamp = 56 # int | 
    tran_id = 56 # int | 

    try:
        # Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_update_localentity_deposit_provide_info_v1(questionnaire, timestamp, tran_id)
        print("The response of TravelRuleApi->wallet_update_localentity_deposit_provide_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->wallet_update_localentity_deposit_provide_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **tran_id** | **int**|  | 

### Return type

[**WalletUpdateLocalentityDepositProvideInfoV1Resp**](WalletUpdateLocalentityDepositProvideInfoV1Resp.md)

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

