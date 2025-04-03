# binance.wallet.AssetApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_create_asset_dust_btc_v1**](AssetApi.md#wallet_create_asset_dust_btc_v1) | **POST** /sapi/v1/asset/dust-btc | Get Assets That Can Be Converted Into BNB (USER_DATA)
[**wallet_create_asset_dust_v1**](AssetApi.md#wallet_create_asset_dust_v1) | **POST** /sapi/v1/asset/dust | Dust Transfer (USER_DATA)
[**wallet_create_asset_get_funding_asset_v1**](AssetApi.md#wallet_create_asset_get_funding_asset_v1) | **POST** /sapi/v1/asset/get-funding-asset | Funding Wallet (USER_DATA)
[**wallet_create_asset_get_user_asset_v3**](AssetApi.md#wallet_create_asset_get_user_asset_v3) | **POST** /sapi/v3/asset/getUserAsset | User Asset (USER_DATA)
[**wallet_create_asset_transfer_v1**](AssetApi.md#wallet_create_asset_transfer_v1) | **POST** /sapi/v1/asset/transfer | User Universal Transfer (USER_DATA)
[**wallet_create_bnb_burn_v1**](AssetApi.md#wallet_create_bnb_burn_v1) | **POST** /sapi/v1/bnbBurn | Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
[**wallet_get_asset_asset_detail_v1**](AssetApi.md#wallet_get_asset_asset_detail_v1) | **GET** /sapi/v1/asset/assetDetail | Asset Detail (USER_DATA)
[**wallet_get_asset_asset_dividend_v1**](AssetApi.md#wallet_get_asset_asset_dividend_v1) | **GET** /sapi/v1/asset/assetDividend | Asset Dividend Record (USER_DATA)
[**wallet_get_asset_custody_transfer_history_v1**](AssetApi.md#wallet_get_asset_custody_transfer_history_v1) | **GET** /sapi/v1/asset/custody/transfer-history | Query User Delegation History(For Master Account)(USER_DATA)
[**wallet_get_asset_dribblet_v1**](AssetApi.md#wallet_get_asset_dribblet_v1) | **GET** /sapi/v1/asset/dribblet | DustLog(USER_DATA)
[**wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1**](AssetApi.md#wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1) | **GET** /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage | Get Cloud-Mining payment and refund history (USER_DATA)
[**wallet_get_asset_trade_fee_v1**](AssetApi.md#wallet_get_asset_trade_fee_v1) | **GET** /sapi/v1/asset/tradeFee | Trade Fee (USER_DATA)
[**wallet_get_asset_transfer_v1**](AssetApi.md#wallet_get_asset_transfer_v1) | **GET** /sapi/v1/asset/transfer | Query User Universal Transfer History(USER_DATA)
[**wallet_get_asset_wallet_balance_v1**](AssetApi.md#wallet_get_asset_wallet_balance_v1) | **GET** /sapi/v1/asset/wallet/balance | Query User Wallet Balance (USER_DATA)
[**wallet_get_spot_delist_schedule_v1**](AssetApi.md#wallet_get_spot_delist_schedule_v1) | **GET** /sapi/v1/spot/delist-schedule | Get Spot Delist Schedule (MARKET_DATA)
[**wallet_get_spot_open_symbol_list_v1**](AssetApi.md#wallet_get_spot_open_symbol_list_v1) | **GET** /sapi/v1/spot/open-symbol-list | Get Open Symbol List (MARKET_DATA)


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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    account_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Assets That Can Be Converted Into BNB (USER_DATA)
        api_response = api_instance.wallet_create_asset_dust_btc_v1(timestamp, account_type=account_type, recv_window=recv_window)
        print("The response of AssetApi->wallet_create_asset_dust_btc_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_asset_dust_btc_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    asset = ['asset_example'] # List[str] | 
    timestamp = 56 # int | 
    account_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Dust Transfer (USER_DATA)
        api_response = api_instance.wallet_create_asset_dust_v1(asset, timestamp, account_type=account_type, recv_window=recv_window)
        print("The response of AssetApi->wallet_create_asset_dust_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_asset_dust_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    need_btc_valuation = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Funding Wallet (USER_DATA)
        api_response = api_instance.wallet_create_asset_get_funding_asset_v1(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
        print("The response of AssetApi->wallet_create_asset_get_funding_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_asset_get_funding_asset_v1: %s\n" % e)
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

# **wallet_create_asset_get_user_asset_v3**
> List[WalletCreateAssetGetUserAssetV3RespItem] wallet_create_asset_get_user_asset_v3(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)

User Asset (USER_DATA)

Get user assets, just for positive data.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_create_asset_get_user_asset_v3_resp_item import WalletCreateAssetGetUserAssetV3RespItem
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    need_btc_valuation = True # bool |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # User Asset (USER_DATA)
        api_response = api_instance.wallet_create_asset_get_user_asset_v3(timestamp, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
        print("The response of AssetApi->wallet_create_asset_get_user_asset_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_asset_get_user_asset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **need_btc_valuation** | **bool**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletCreateAssetGetUserAssetV3RespItem]**](WalletCreateAssetGetUserAssetV3RespItem.md)

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
    api_instance = binance.wallet.AssetApi(api_client)
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
        print("The response of AssetApi->wallet_create_asset_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_asset_transfer_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    interest_bnb_burn = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    spot_bnb_burn = '' # str |  (optional) (default to '')

    try:
        # Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
        api_response = api_instance.wallet_create_bnb_burn_v1(timestamp, interest_bnb_burn=interest_bnb_burn, recv_window=recv_window, spot_bnb_burn=spot_bnb_burn)
        print("The response of AssetApi->wallet_create_bnb_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_create_bnb_burn_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Asset Detail (USER_DATA)
        api_response = api_instance.wallet_get_asset_asset_detail_v1(timestamp, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_asset_asset_detail_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_asset_detail_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 20 # int | Default 20, max 500 (optional) (default to 20)
    recv_window = 56 # int |  (optional)

    try:
        # Asset Dividend Record (USER_DATA)
        api_response = api_instance.wallet_get_asset_asset_dividend_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_asset_asset_dividend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_asset_dividend_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
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
        print("The response of AssetApi->wallet_get_asset_custody_transfer_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_custody_transfer_history_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # DustLog(USER_DATA)
        api_response = api_instance.wallet_get_asset_dribblet_v1(timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_asset_dribblet_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_dribblet_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
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
        print("The response of AssetApi->wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_ledger_transfer_cloud_mining_query_by_page_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Trade Fee (USER_DATA)
        api_response = api_instance.wallet_get_asset_trade_fee_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_asset_trade_fee_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_trade_fee_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
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
        print("The response of AssetApi->wallet_get_asset_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_transfer_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    quote_asset = '' # str | `USDT`, `ETH`, `USDC`, `BNB`, etc. default `BTC` (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query User Wallet Balance (USER_DATA)
        api_response = api_instance.wallet_get_asset_wallet_balance_v1(timestamp, quote_asset=quote_asset, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_asset_wallet_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_asset_wallet_balance_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Spot Delist Schedule (MARKET_DATA)
        api_response = api_instance.wallet_get_spot_delist_schedule_v1(timestamp, recv_window=recv_window)
        print("The response of AssetApi->wallet_get_spot_delist_schedule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_spot_delist_schedule_v1: %s\n" % e)
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
    api_instance = binance.wallet.AssetApi(api_client)

    try:
        # Get Open Symbol List (MARKET_DATA)
        api_response = api_instance.wallet_get_spot_open_symbol_list_v1()
        print("The response of AssetApi->wallet_get_spot_open_symbol_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->wallet_get_spot_open_symbol_list_v1: %s\n" % e)
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

