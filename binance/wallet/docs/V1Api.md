# binance.wallet.V1Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_account_disable_fast_withdraw_switch_v1**](V1Api.md#wallet_create_account_disable_fast_withdraw_switch_v1) | **POST** /sapi/v1/account/disableFastWithdrawSwitch | Disable Fast Withdraw Switch (USER_DATA)
[**wallet_create_account_enable_fast_withdraw_switch_v1**](V1Api.md#wallet_create_account_enable_fast_withdraw_switch_v1) | **POST** /sapi/v1/account/enableFastWithdrawSwitch | Enable Fast Withdraw Switch (USER_DATA)
[**wallet_create_asset_dust_btc_v1**](V1Api.md#wallet_create_asset_dust_btc_v1) | **POST** /sapi/v1/asset/dust-btc | Get Assets That Can Be Converted Into BNB (USER_DATA)
[**wallet_create_asset_dust_v1**](V1Api.md#wallet_create_asset_dust_v1) | **POST** /sapi/v1/asset/dust | Dust Transfer (USER_DATA)
[**wallet_create_asset_get_funding_asset_v1**](V1Api.md#wallet_create_asset_get_funding_asset_v1) | **POST** /sapi/v1/asset/get-funding-asset | Funding Wallet (USER_DATA)
[**wallet_create_asset_transfer_v1**](V1Api.md#wallet_create_asset_transfer_v1) | **POST** /sapi/v1/asset/transfer | User Universal Transfer (USER_DATA)
[**wallet_create_bnb_burn_v1**](V1Api.md#wallet_create_bnb_burn_v1) | **POST** /sapi/v1/bnbBurn | Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
[**wallet_create_capital_deposit_credit_apply_v1**](V1Api.md#wallet_create_capital_deposit_credit_apply_v1) | **POST** /sapi/v1/capital/deposit/credit-apply | One click arrival deposit apply (for expired address deposit) (USER_DATA)
[**wallet_create_capital_withdraw_apply_v1**](V1Api.md#wallet_create_capital_withdraw_apply_v1) | **POST** /sapi/v1/capital/withdraw/apply | Withdraw(USER_DATA)
[**wallet_create_localentity_broker_withdraw_apply_v1**](V1Api.md#wallet_create_localentity_broker_withdraw_apply_v1) | **POST** /sapi/v1/localentity/broker/withdraw/apply | Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)
[**wallet_create_localentity_withdraw_apply_v1**](V1Api.md#wallet_create_localentity_withdraw_apply_v1) | **POST** /sapi/v1/localentity/withdraw/apply | Withdraw (for local entities that require travel rule) (USER_DATA)
[**wallet_get_account_api_restrictions_v1**](V1Api.md#wallet_get_account_api_restrictions_v1) | **GET** /sapi/v1/account/apiRestrictions | Get API Key Permission (USER_DATA)
[**wallet_get_account_api_trading_status_v1**](V1Api.md#wallet_get_account_api_trading_status_v1) | **GET** /sapi/v1/account/apiTradingStatus | Account API Trading Status (USER_DATA)
[**wallet_get_account_info_v1**](V1Api.md#wallet_get_account_info_v1) | **GET** /sapi/v1/account/info | Account info (USER_DATA)
[**wallet_get_account_snapshot_v1**](V1Api.md#wallet_get_account_snapshot_v1) | **GET** /sapi/v1/accountSnapshot | Daily Account Snapshot (USER_DATA)
[**wallet_get_account_status_v1**](V1Api.md#wallet_get_account_status_v1) | **GET** /sapi/v1/account/status | Account Status (USER_DATA)
[**wallet_get_asset_asset_detail_v1**](V1Api.md#wallet_get_asset_asset_detail_v1) | **GET** /sapi/v1/asset/assetDetail | Asset Detail (USER_DATA)
[**wallet_get_asset_asset_dividend_v1**](V1Api.md#wallet_get_asset_asset_dividend_v1) | **GET** /sapi/v1/asset/assetDividend | Asset Dividend Record (USER_DATA)
[**wallet_get_asset_custody_transfer_history_v1**](V1Api.md#wallet_get_asset_custody_transfer_history_v1) | **GET** /sapi/v1/asset/custody/transfer-history | Query User Delegation History(For Master Account)(USER_DATA)
[**wallet_get_asset_dribblet_v1**](V1Api.md#wallet_get_asset_dribblet_v1) | **GET** /sapi/v1/asset/dribblet | DustLog(USER_DATA)
[**wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1**](V1Api.md#wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1) | **GET** /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage | Get Cloud-Mining payment and refund history (USER_DATA)
[**wallet_get_asset_trade_fee_v1**](V1Api.md#wallet_get_asset_trade_fee_v1) | **GET** /sapi/v1/asset/tradeFee | Trade Fee (USER_DATA)
[**wallet_get_asset_transfer_v1**](V1Api.md#wallet_get_asset_transfer_v1) | **GET** /sapi/v1/asset/transfer | Query User Universal Transfer History(USER_DATA)
[**wallet_get_asset_wallet_balance_v1**](V1Api.md#wallet_get_asset_wallet_balance_v1) | **GET** /sapi/v1/asset/wallet/balance | Query User Wallet Balance (USER_DATA)
[**wallet_get_capital_config_getall_v1**](V1Api.md#wallet_get_capital_config_getall_v1) | **GET** /sapi/v1/capital/config/getall | All Coins&#39; Information (USER_DATA)
[**wallet_get_capital_deposit_address_list_v1**](V1Api.md#wallet_get_capital_deposit_address_list_v1) | **GET** /sapi/v1/capital/deposit/address/list | Fetch deposit address list with network(USER_DATA)
[**wallet_get_capital_deposit_address_v1**](V1Api.md#wallet_get_capital_deposit_address_v1) | **GET** /sapi/v1/capital/deposit/address | Deposit Address(supporting network) (USER_DATA)
[**wallet_get_capital_deposit_hisrec_v1**](V1Api.md#wallet_get_capital_deposit_hisrec_v1) | **GET** /sapi/v1/capital/deposit/hisrec | Deposit History (supporting network) (USER_DATA)
[**wallet_get_capital_withdraw_address_list_v1**](V1Api.md#wallet_get_capital_withdraw_address_list_v1) | **GET** /sapi/v1/capital/withdraw/address/list | Fetch withdraw address list (USER_DATA)
[**wallet_get_capital_withdraw_history_v1**](V1Api.md#wallet_get_capital_withdraw_history_v1) | **GET** /sapi/v1/capital/withdraw/history | Withdraw History (supporting network) (USER_DATA)
[**wallet_get_localentity_deposit_history_v1**](V1Api.md#wallet_get_localentity_deposit_history_v1) | **GET** /sapi/v1/localentity/deposit/history | Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)
[**wallet_get_localentity_vasp_v1**](V1Api.md#wallet_get_localentity_vasp_v1) | **GET** /sapi/v1/localentity/vasp | Onboarded VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_get_localentity_withdraw_history_v1**](V1Api.md#wallet_get_localentity_withdraw_history_v1) | **GET** /sapi/v1/localentity/withdraw/history | Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_get_spot_delist_schedule_v1**](V1Api.md#wallet_get_spot_delist_schedule_v1) | **GET** /sapi/v1/spot/delist-schedule | Get Spot Delist Schedule (MARKET_DATA)
[**wallet_get_spot_open_symbol_list_v1**](V1Api.md#wallet_get_spot_open_symbol_list_v1) | **GET** /sapi/v1/spot/open-symbol-list | Get Open Symbol List (MARKET_DATA)
[**wallet_get_system_status_v1**](V1Api.md#wallet_get_system_status_v1) | **GET** /sapi/v1/system/status | System Status (System)
[**wallet_update_localentity_broker_deposit_provide_info_v1**](V1Api.md#wallet_update_localentity_broker_deposit_provide_info_v1) | **PUT** /sapi/v1/localentity/broker/deposit/provide-info | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
[**wallet_update_localentity_deposit_provide_info_v1**](V1Api.md#wallet_update_localentity_deposit_provide_info_v1) | **PUT** /sapi/v1/localentity/deposit/provide-info | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)


# **wallet_create_account_disable_fast_withdraw_switch_v1**
> object wallet_create_account_disable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)

Disable Fast Withdraw Switch (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Disable Fast Withdraw Switch (USER_DATA)
        api_response = api_instance.wallet_create_account_disable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_create_account_disable_fast_withdraw_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_account_disable_fast_withdraw_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

**object**

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

# **wallet_create_account_enable_fast_withdraw_switch_v1**
> object wallet_create_account_enable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)

Enable Fast Withdraw Switch (USER_DATA)

Enable Fast Withdraw Switch (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Fast Withdraw Switch (USER_DATA)
        api_response = api_instance.wallet_create_account_enable_fast_withdraw_switch_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_create_account_enable_fast_withdraw_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_account_enable_fast_withdraw_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

**object**

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

# **wallet_create_asset_dust_btc_v1**
> WalletCreateAssetDustBtcV1Resp wallet_create_asset_dust_btc_v1(timestamp, account_type=account_type, recv_window=recv_window)

Get Assets That Can Be Converted Into BNB (USER_DATA)

Get Assets That Can Be Converted Into BNB

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_dust_btc_v1_resp import WalletCreateAssetDustBtcV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    account_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Assets That Can Be Converted Into BNB (USER_DATA)
        api_response = api_instance.wallet_create_asset_dust_btc_v1(timestamp, account_type=account_type, recv_window=recv_window)
        print("The response of V1Api->wallet_create_asset_dust_btc_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_asset_dust_btc_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **account_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletCreateAssetDustBtcV1Resp**](WalletCreateAssetDustBtcV1Resp.md)

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

# **wallet_create_asset_dust_v1**
> WalletCreateAssetDustV1Resp wallet_create_asset_dust_v1(asset, timestamp, account_type=account_type, recv_window=recv_window)

Dust Transfer (USER_DATA)

Convert dust assets to BNB.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_dust_v1_resp import WalletCreateAssetDustV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    asset = ['asset_example'] # List[str] | 
    timestamp = 56 # int | 
    account_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Dust Transfer (USER_DATA)
        api_response = api_instance.wallet_create_asset_dust_v1(asset, timestamp, account_type=account_type, recv_window=recv_window)
        print("The response of V1Api->wallet_create_asset_dust_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_asset_dust_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**List[str]**](str.md)|  | 
 **timestamp** | **int**|  | 
 **account_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletCreateAssetDustV1Resp**](WalletCreateAssetDustV1Resp.md)

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

# **wallet_create_asset_get_funding_asset_v1**
> List[WalletCreateAssetGetFundingAssetV1RespItem] wallet_create_asset_get_funding_asset_v1(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)

Funding Wallet (USER_DATA)

Query Funding Wallet

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_get_funding_asset_v1_resp_item import WalletCreateAssetGetFundingAssetV1RespItem
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    need_btc_valuation = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Funding Wallet (USER_DATA)
        api_response = api_instance.wallet_create_asset_get_funding_asset_v1(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
        print("The response of V1Api->wallet_create_asset_get_funding_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_asset_get_funding_asset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **need_btc_valuation** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletCreateAssetGetFundingAssetV1RespItem]**](WalletCreateAssetGetFundingAssetV1RespItem.md)

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

# **wallet_create_asset_transfer_v1**
> WalletCreateAssetTransferV1Resp wallet_create_asset_transfer_v1(amount, asset, timestamp, type, from_symbol=from_symbol, recv_window=recv_window, to_symbol=to_symbol)

User Universal Transfer (USER_DATA)

user universal transfer

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_transfer_v1_resp import WalletCreateAssetTransferV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    from_symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_symbol = '' # str |  (optional) (default to '')

    try:
        # User Universal Transfer (USER_DATA)
        api_response = api_instance.wallet_create_asset_transfer_v1(amount, asset, timestamp, type, from_symbol=from_symbol, recv_window=recv_window, to_symbol=to_symbol)
        print("The response of V1Api->wallet_create_asset_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_asset_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **from_symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletCreateAssetTransferV1Resp**](WalletCreateAssetTransferV1Resp.md)

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

# **wallet_create_bnb_burn_v1**
> WalletCreateBnbBurnV1Resp wallet_create_bnb_burn_v1(timestamp, interest_bnb_burn=interest_bnb_burn, recv_window=recv_window, spot_bnb_burn=spot_bnb_burn)

Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)

Toggle BNB Burn On Spot Trade And Margin Interest

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_bnb_burn_v1_resp import WalletCreateBnbBurnV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    interest_bnb_burn = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    spot_bnb_burn = '' # str |  (optional) (default to '')

    try:
        # Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
        api_response = api_instance.wallet_create_bnb_burn_v1(timestamp, interest_bnb_burn=interest_bnb_burn, recv_window=recv_window, spot_bnb_burn=spot_bnb_burn)
        print("The response of V1Api->wallet_create_bnb_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_bnb_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **interest_bnb_burn** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **spot_bnb_burn** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**WalletCreateBnbBurnV1Resp**](WalletCreateBnbBurnV1Resp.md)

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
    api_instance = binance.wallet.V1Api(api_client)
    deposit_id = 56 # int |  (optional)
    sub_account_id = 56 # int |  (optional)
    sub_user_id = 56 # int |  (optional)
    tx_id = '' # str |  (optional) (default to '')

    try:
        # One click arrival deposit apply (for expired address deposit) (USER_DATA)
        api_response = api_instance.wallet_create_capital_deposit_credit_apply_v1(deposit_id=deposit_id, sub_account_id=sub_account_id, sub_user_id=sub_user_id, tx_id=tx_id)
        print("The response of V1Api->wallet_create_capital_deposit_credit_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_capital_deposit_credit_apply_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_create_capital_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_capital_withdraw_apply_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_create_localentity_broker_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_localentity_broker_withdraw_apply_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_create_localentity_withdraw_apply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_create_localentity_withdraw_apply_v1: %s\n" % e)
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

# **wallet_get_account_api_restrictions_v1**
> WalletGetAccountApiRestrictionsV1Resp wallet_get_account_api_restrictions_v1(timestamp, recv_window=recv_window)

Get API Key Permission (USER_DATA)

Get API Key Permission

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_api_restrictions_v1_resp import WalletGetAccountApiRestrictionsV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get API Key Permission (USER_DATA)
        api_response = api_instance.wallet_get_account_api_restrictions_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_account_api_restrictions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_account_api_restrictions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountApiRestrictionsV1Resp**](WalletGetAccountApiRestrictionsV1Resp.md)

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

# **wallet_get_account_api_trading_status_v1**
> WalletGetAccountApiTradingStatusV1Resp wallet_get_account_api_trading_status_v1(timestamp, recv_window=recv_window)

Account API Trading Status (USER_DATA)

Fetch account api trading status detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_api_trading_status_v1_resp import WalletGetAccountApiTradingStatusV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account API Trading Status (USER_DATA)
        api_response = api_instance.wallet_get_account_api_trading_status_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_account_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_account_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountApiTradingStatusV1Resp**](WalletGetAccountApiTradingStatusV1Resp.md)

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

# **wallet_get_account_info_v1**
> WalletGetAccountInfoV1Resp wallet_get_account_info_v1(timestamp, recv_window=recv_window)

Account info (USER_DATA)

Fetch account info detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_info_v1_resp import WalletGetAccountInfoV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account info (USER_DATA)
        api_response = api_instance.wallet_get_account_info_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountInfoV1Resp**](WalletGetAccountInfoV1Resp.md)

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

# **wallet_get_account_snapshot_v1**
> WalletGetAccountSnapshotV1Resp wallet_get_account_snapshot_v1(type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Daily Account Snapshot (USER_DATA)

Daily account snapshot

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_snapshot_v1_resp import WalletGetAccountSnapshotV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    type = '' # str | &#34;SPOT&#34;, &#34;MARGIN&#34;, &#34;FUTURES&#34; (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 7 # int | min 7, max 30, default 7 (optional) (default to 7)
    recv_window = 56 # int |  (optional)

    try:
        # Daily Account Snapshot (USER_DATA)
        api_response = api_instance.wallet_get_account_snapshot_v1(type, timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->wallet_get_account_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_account_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &amp;#34;SPOT&amp;#34;, &amp;#34;MARGIN&amp;#34;, &amp;#34;FUTURES&amp;#34; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| min 7, max 30, default 7 | [optional] [default to 7]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountSnapshotV1Resp**](WalletGetAccountSnapshotV1Resp.md)

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

# **wallet_get_account_status_v1**
> WalletGetAccountStatusV1Resp wallet_get_account_status_v1(timestamp, recv_window=recv_window)

Account Status (USER_DATA)

Fetch account status detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_account_status_v1_resp import WalletGetAccountStatusV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Status (USER_DATA)
        api_response = api_instance.wallet_get_account_status_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_account_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_account_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAccountStatusV1Resp**](WalletGetAccountStatusV1Resp.md)

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

# **wallet_get_asset_asset_detail_v1**
> Dict[str, WalletGetAssetAssetDetailV1RespValue] wallet_get_asset_asset_detail_v1(timestamp, recv_window=recv_window)

Asset Detail (USER_DATA)

Fetch details of assets supported on Binance.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_asset_detail_v1_resp_value import WalletGetAssetAssetDetailV1RespValue
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Asset Detail (USER_DATA)
        api_response = api_instance.wallet_get_asset_asset_detail_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_asset_detail_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_asset_detail_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**Dict[str, WalletGetAssetAssetDetailV1RespValue]**](WalletGetAssetAssetDetailV1RespValue.md)

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

# **wallet_get_asset_asset_dividend_v1**
> WalletGetAssetAssetDividendV1Resp wallet_get_asset_asset_dividend_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Asset Dividend Record (USER_DATA)

Query asset dividend record.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_asset_dividend_v1_resp import WalletGetAssetAssetDividendV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 20 # int | Default 20, max 500 (optional) (default to 20)
    recv_window = 56 # int |  (optional)

    try:
        # Asset Dividend Record (USER_DATA)
        api_response = api_instance.wallet_get_asset_asset_dividend_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_asset_dividend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_asset_dividend_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 20, max 500 | [optional] [default to 20]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAssetAssetDividendV1Resp**](WalletGetAssetAssetDividendV1Resp.md)

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

# **wallet_get_asset_custody_transfer_history_v1**
> WalletGetAssetCustodyTransferHistoryV1Resp wallet_get_asset_custody_transfer_history_v1(email, start_time, end_time, timestamp, type=type, asset=asset, current=current, size=size, recv_window=recv_window)

Query User Delegation History(For Master Account)(USER_DATA)

Query User Delegation History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_custody_transfer_history_v1_resp import WalletGetAssetCustodyTransferHistoryV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    email = '' # str |  (default to '')
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    type = '' # str | Delegate/Undelegate (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    current = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query User Delegation History(For Master Account)(USER_DATA)
        api_response = api_instance.wallet_get_asset_custody_transfer_history_v1(email, start_time, end_time, timestamp, type=type, asset=asset, current=current, size=size, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_custody_transfer_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_custody_transfer_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **type** | **str**| Delegate/Undelegate | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAssetCustodyTransferHistoryV1Resp**](WalletGetAssetCustodyTransferHistoryV1Resp.md)

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

# **wallet_get_asset_dribblet_v1**
> WalletGetAssetDribbletV1Resp wallet_get_asset_dribblet_v1(timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)

DustLog(USER_DATA)

Dustlog

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_dribblet_v1_resp import WalletGetAssetDribbletV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # DustLog(USER_DATA)
        api_response = api_instance.wallet_get_asset_dribblet_v1(timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_dribblet_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_dribblet_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAssetDribbletV1Resp**](WalletGetAssetDribbletV1Resp.md)

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

# **wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1**
> WalletGetAssetLedgerTransferCloudMiningQueryByPageV1Resp wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1(start_time, end_time, tran_id=tran_id, client_tran_id=client_tran_id, asset=asset, current=current, size=size)

Get Cloud-Mining payment and refund history (USER_DATA)

The query of Cloud-Mining payment and refund history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp import WalletGetAssetLedgerTransferCloudMiningQueryByPageV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    start_time = 56 # int | inclusive, unit: ms
    end_time = 56 # int | exclusive, unit: ms
    tran_id = 56 # int | The transaction id (optional)
    client_tran_id = '' # str | The unique flag (optional) (default to '')
    asset = '' # str | If it is blank, we will query all assets (optional) (default to '')
    current = 1 # int | current page, default 1, the min value is 1 (optional) (default to 1)
    size = 10 # int | page size, default 10, the max value is 100 (optional) (default to 10)

    try:
        # Get Cloud-Mining payment and refund history (USER_DATA)
        api_response = api_instance.wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1(start_time, end_time, tran_id=tran_id, client_tran_id=client_tran_id, asset=asset, current=current, size=size)
        print("The response of V1Api->wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| inclusive, unit: ms | 
 **end_time** | **int**| exclusive, unit: ms | 
 **tran_id** | **int**| The transaction id | [optional] 
 **client_tran_id** | **str**| The unique flag | [optional] [default to &#39;&#39;]
 **asset** | **str**| If it is blank, we will query all assets | [optional] [default to &#39;&#39;]
 **current** | **int**| current page, default 1, the min value is 1 | [optional] [default to 1]
 **size** | **int**| page size, default 10, the max value is 100 | [optional] [default to 10]

### Return type

[**WalletGetAssetLedgerTransferCloudMiningQueryByPageV1Resp**](WalletGetAssetLedgerTransferCloudMiningQueryByPageV1Resp.md)

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

# **wallet_get_asset_trade_fee_v1**
> List[WalletGetAssetTradeFeeV1RespItem] wallet_get_asset_trade_fee_v1(timestamp, symbol=symbol, recv_window=recv_window)

Trade Fee (USER_DATA)

Fetch trade fee

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_trade_fee_v1_resp_item import WalletGetAssetTradeFeeV1RespItem
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Trade Fee (USER_DATA)
        api_response = api_instance.wallet_get_asset_trade_fee_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_trade_fee_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_trade_fee_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetAssetTradeFeeV1RespItem]**](WalletGetAssetTradeFeeV1RespItem.md)

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

# **wallet_get_asset_transfer_v1**
> WalletGetAssetTransferV1Resp wallet_get_asset_transfer_v1(type, timestamp, start_time=start_time, end_time=end_time, current=current, size=size, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)

Query User Universal Transfer History(USER_DATA)

Query User Universal Transfer History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_transfer_v1_resp import WalletGetAssetTransferV1Resp
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
    api_instance = binance.wallet.V1Api(api_client)
    type = '' # str |  (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Default 1 (optional) (default to 1)
    size = 10 # int | Default 10, Max 100 (optional) (default to 10)
    from_symbol = '' # str |  (optional) (default to '')
    to_symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query User Universal Transfer History(USER_DATA)
        api_response = api_instance.wallet_get_asset_transfer_v1(type, timestamp, start_time=start_time, end_time=end_time, current=current, size=size, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Default 1 | [optional] [default to 1]
 **size** | **int**| Default 10, Max 100 | [optional] [default to 10]
 **from_symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **to_symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**WalletGetAssetTransferV1Resp**](WalletGetAssetTransferV1Resp.md)

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

# **wallet_get_asset_wallet_balance_v1**
> List[WalletGetAssetWalletBalanceV1RespItem] wallet_get_asset_wallet_balance_v1(timestamp, quote_asset=quote_asset, recv_window=recv_window)

Query User Wallet Balance (USER_DATA)

Query User Wallet Balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_asset_wallet_balance_v1_resp_item import WalletGetAssetWalletBalanceV1RespItem
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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    quote_asset = '' # str | `USDT`, `ETH`, `USDC`, `BNB`, etc. default `BTC` (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query User Wallet Balance (USER_DATA)
        api_response = api_instance.wallet_get_asset_wallet_balance_v1(timestamp, quote_asset=quote_asset, recv_window=recv_window)
        print("The response of V1Api->wallet_get_asset_wallet_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_asset_wallet_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **quote_asset** | **str**| &#x60;USDT&#x60;, &#x60;ETH&#x60;, &#x60;USDC&#x60;, &#x60;BNB&#x60;, etc. default &#x60;BTC&#x60; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetAssetWalletBalanceV1RespItem]**](WalletGetAssetWalletBalanceV1RespItem.md)

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
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # All Coins' Information (USER_DATA)
        api_response = api_instance.wallet_get_capital_config_getall_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_capital_config_getall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_config_getall_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
    coin = '' # str | `coin` refers to the parent network address format that the address is using (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')

    try:
        # Fetch deposit address list with network(USER_DATA)
        api_response = api_instance.wallet_get_capital_deposit_address_list_v1(coin, timestamp, network=network)
        print("The response of V1Api->wallet_get_capital_deposit_address_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_deposit_address_list_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
    coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    network = '' # str |  (optional) (default to '')
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Deposit Address(supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_capital_deposit_address_v1(coin, timestamp, network=network, amount=amount, recv_window=recv_window)
        print("The response of V1Api->wallet_get_capital_deposit_address_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_deposit_address_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_get_capital_deposit_hisrec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_deposit_hisrec_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)

    try:
        # Fetch withdraw address list (USER_DATA)
        api_response = api_instance.wallet_get_capital_withdraw_address_list_v1()
        print("The response of V1Api->wallet_get_capital_withdraw_address_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_withdraw_address_list_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_get_capital_withdraw_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_capital_withdraw_history_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_get_localentity_deposit_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_localentity_deposit_history_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)

    try:
        # Onboarded VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_vasp_v1()
        print("The response of V1Api->wallet_get_localentity_vasp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_localentity_vasp_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_get_localentity_withdraw_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_localentity_withdraw_history_v1: %s\n" % e)
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

# **wallet_get_spot_delist_schedule_v1**
> List[WalletGetSpotDelistScheduleV1RespItem] wallet_get_spot_delist_schedule_v1(timestamp, recv_window=recv_window)

Get Spot Delist Schedule (MARKET_DATA)

Get symbols delist schedule for spot

### Example


```python
import binance.wallet
from binance.wallet.models.wallet_get_spot_delist_schedule_v1_resp_item import WalletGetSpotDelistScheduleV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.V1Api(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Spot Delist Schedule (MARKET_DATA)
        api_response = api_instance.wallet_get_spot_delist_schedule_v1(timestamp, recv_window=recv_window)
        print("The response of V1Api->wallet_get_spot_delist_schedule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_spot_delist_schedule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetSpotDelistScheduleV1RespItem]**](WalletGetSpotDelistScheduleV1RespItem.md)

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

# **wallet_get_spot_open_symbol_list_v1**
> List[WalletGetSpotOpenSymbolListV1RespItem] wallet_get_spot_open_symbol_list_v1()

Get Open Symbol List (MARKET_DATA)

Get the list of symbols that are scheduled to be opened for trading in the market.

### Example


```python
import binance.wallet
from binance.wallet.models.wallet_get_spot_open_symbol_list_v1_resp_item import WalletGetSpotOpenSymbolListV1RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.V1Api(api_client)

    try:
        # Get Open Symbol List (MARKET_DATA)
        api_response = api_instance.wallet_get_spot_open_symbol_list_v1()
        print("The response of V1Api->wallet_get_spot_open_symbol_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_spot_open_symbol_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WalletGetSpotOpenSymbolListV1RespItem]**](WalletGetSpotOpenSymbolListV1RespItem.md)

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

# **wallet_get_system_status_v1**
> WalletGetSystemStatusV1Resp wallet_get_system_status_v1()

System Status (System)

Fetch system status.

### Example


```python
import binance.wallet
from binance.wallet.models.wallet_get_system_status_v1_resp import WalletGetSystemStatusV1Resp
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.V1Api(api_client)

    try:
        # System Status (System)
        api_response = api_instance.wallet_get_system_status_v1()
        print("The response of V1Api->wallet_get_system_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_get_system_status_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletGetSystemStatusV1Resp**](WalletGetSystemStatusV1Resp.md)

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
    api_instance = binance.wallet.V1Api(api_client)
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
        print("The response of V1Api->wallet_update_localentity_broker_deposit_provide_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_update_localentity_broker_deposit_provide_info_v1: %s\n" % e)
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
    api_instance = binance.wallet.V1Api(api_client)
    questionnaire = '' # str |  (default to '')
    timestamp = 56 # int | 
    tran_id = 56 # int | 

    try:
        # Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_update_localentity_deposit_provide_info_v1(questionnaire, timestamp, tran_id)
        print("The response of V1Api->wallet_update_localentity_deposit_provide_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->wallet_update_localentity_deposit_provide_info_v1: %s\n" % e)
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

