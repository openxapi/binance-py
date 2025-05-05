# binance.spot.PortfolioMarginProApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_portfolio_asset_collection_v1**](PortfolioMarginProApi.md#create_portfolio_asset_collection_v1) | **POST** /sapi/v1/portfolio/asset-collection | Fund Collection by Asset(USER_DATA)
[**create_portfolio_auto_collection_v1**](PortfolioMarginProApi.md#create_portfolio_auto_collection_v1) | **POST** /sapi/v1/portfolio/auto-collection | Fund Auto-collection(USER_DATA)
[**create_portfolio_bnb_transfer_v1**](PortfolioMarginProApi.md#create_portfolio_bnb_transfer_v1) | **POST** /sapi/v1/portfolio/bnb-transfer | BNB transfer(USER_DATA)
[**create_portfolio_mint_v1**](PortfolioMarginProApi.md#create_portfolio_mint_v1) | **POST** /sapi/v1/portfolio/mint | Mint BFUSD for Portfolio Margin(TRADE)
[**create_portfolio_redeem_v1**](PortfolioMarginProApi.md#create_portfolio_redeem_v1) | **POST** /sapi/v1/portfolio/redeem | Redeem BFUSD for Portfolio Margin(TRADE)
[**create_portfolio_repay_futures_negative_balance_v1**](PortfolioMarginProApi.md#create_portfolio_repay_futures_negative_balance_v1) | **POST** /sapi/v1/portfolio/repay-futures-negative-balance | Repay futures Negative Balance(USER_DATA)
[**create_portfolio_repay_futures_switch_v1**](PortfolioMarginProApi.md#create_portfolio_repay_futures_switch_v1) | **POST** /sapi/v1/portfolio/repay-futures-switch | Change Auto-repay-futures Status(TRADE)
[**create_portfolio_repay_v1**](PortfolioMarginProApi.md#create_portfolio_repay_v1) | **POST** /sapi/v1/portfolio/repay | Portfolio Margin Pro Bankruptcy Loan Repay
[**get_portfolio_account_v1**](PortfolioMarginProApi.md#get_portfolio_account_v1) | **GET** /sapi/v1/portfolio/account | Get Portfolio Margin Pro Account Info(USER_DATA)
[**get_portfolio_account_v2**](PortfolioMarginProApi.md#get_portfolio_account_v2) | **GET** /sapi/v2/portfolio/account | Get Portfolio Margin Pro SPAN Account Info(USER_DATA)
[**get_portfolio_asset_index_price_v1**](PortfolioMarginProApi.md#get_portfolio_asset_index_price_v1) | **GET** /sapi/v1/portfolio/asset-index-price | Query Portfolio Margin Asset Index Price (MARKET_DATA)
[**get_portfolio_balance_v1**](PortfolioMarginProApi.md#get_portfolio_balance_v1) | **GET** /sapi/v1/portfolio/balance | Get Portfolio Margin Pro Account Balance(USER_DATA)
[**get_portfolio_collateral_rate_v1**](PortfolioMarginProApi.md#get_portfolio_collateral_rate_v1) | **GET** /sapi/v1/portfolio/collateralRate | Portfolio Margin Collateral Rate(MARKET_DATA)
[**get_portfolio_collateral_rate_v2**](PortfolioMarginProApi.md#get_portfolio_collateral_rate_v2) | **GET** /sapi/v2/portfolio/collateralRate | Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)
[**get_portfolio_interest_history_v1**](PortfolioMarginProApi.md#get_portfolio_interest_history_v1) | **GET** /sapi/v1/portfolio/interest-history | Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)
[**get_portfolio_margin_asset_leverage_v1**](PortfolioMarginProApi.md#get_portfolio_margin_asset_leverage_v1) | **GET** /sapi/v1/portfolio/margin-asset-leverage | Get Portfolio Margin Asset Leverage(USER_DATA)
[**get_portfolio_pm_loan_history_v1**](PortfolioMarginProApi.md#get_portfolio_pm_loan_history_v1) | **GET** /sapi/v1/portfolio/pmLoan-history | Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)
[**get_portfolio_pm_loan_v1**](PortfolioMarginProApi.md#get_portfolio_pm_loan_v1) | **GET** /sapi/v1/portfolio/pmLoan | Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)
[**get_portfolio_repay_futures_switch_v1**](PortfolioMarginProApi.md#get_portfolio_repay_futures_switch_v1) | **GET** /sapi/v1/portfolio/repay-futures-switch | Get Auto-repay-futures Status(USER_DATA)


# **create_portfolio_asset_collection_v1**
> CreatePortfolioAssetCollectionV1Resp create_portfolio_asset_collection_v1(asset, timestamp, recv_window=recv_window)

Fund Collection by Asset(USER_DATA)

Transfers specific asset from Futures Account to Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_asset_collection_v1_resp import CreatePortfolioAssetCollectionV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Collection by Asset(USER_DATA)
        api_response = api_instance.create_portfolio_asset_collection_v1(asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_asset_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_asset_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioAssetCollectionV1Resp**](CreatePortfolioAssetCollectionV1Resp.md)

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

# **create_portfolio_auto_collection_v1**
> CreatePortfolioAutoCollectionV1Resp create_portfolio_auto_collection_v1(timestamp, recv_window=recv_window)

Fund Auto-collection(USER_DATA)

Transfers all assets from Futures Account to Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_auto_collection_v1_resp import CreatePortfolioAutoCollectionV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Auto-collection(USER_DATA)
        api_response = api_instance.create_portfolio_auto_collection_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_auto_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_auto_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioAutoCollectionV1Resp**](CreatePortfolioAutoCollectionV1Resp.md)

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

# **create_portfolio_bnb_transfer_v1**
> CreatePortfolioBnbTransferV1Resp create_portfolio_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)

BNB transfer(USER_DATA)

BNB transfer can be between Margin Account and USDM Account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_bnb_transfer_v1_resp import CreatePortfolioBnbTransferV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    transfer_side = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # BNB transfer(USER_DATA)
        api_response = api_instance.create_portfolio_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_bnb_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_bnb_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **transfer_side** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioBnbTransferV1Resp**](CreatePortfolioBnbTransferV1Resp.md)

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

# **create_portfolio_mint_v1**
> CreatePortfolioMintV1Resp create_portfolio_mint_v1(amount, from_asset, target_asset, timestamp, recv_window=recv_window)

Mint BFUSD for Portfolio Margin(TRADE)

Mint BFUSD for all types of Portfolio Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_mint_v1_resp import CreatePortfolioMintV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    amount = '' # str |  (default to '')
    from_asset = '' # str |  (default to '')
    target_asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Mint BFUSD for Portfolio Margin(TRADE)
        api_response = api_instance.create_portfolio_mint_v1(amount, from_asset, target_asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_mint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_mint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **from_asset** | **str**|  | [default to &#39;&#39;]
 **target_asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioMintV1Resp**](CreatePortfolioMintV1Resp.md)

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

# **create_portfolio_redeem_v1**
> CreatePortfolioRedeemV1Resp create_portfolio_redeem_v1(amount, from_asset, target_asset, timestamp, recv_window=recv_window)

Redeem BFUSD for Portfolio Margin(TRADE)

Redeem BFUSD for all types of Portfolio Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_redeem_v1_resp import CreatePortfolioRedeemV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    amount = '' # str |  (default to '')
    from_asset = '' # str |  (default to '')
    target_asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Redeem BFUSD for Portfolio Margin(TRADE)
        api_response = api_instance.create_portfolio_redeem_v1(amount, from_asset, target_asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_redeem_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_redeem_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **from_asset** | **str**|  | [default to &#39;&#39;]
 **target_asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioRedeemV1Resp**](CreatePortfolioRedeemV1Resp.md)

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

# **create_portfolio_repay_futures_negative_balance_v1**
> CreatePortfolioRepayFuturesNegativeBalanceV1Resp create_portfolio_repay_futures_negative_balance_v1(timestamp, var_from=var_from, recv_window=recv_window)

Repay futures Negative Balance(USER_DATA)

Repay futures Negative Balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_repay_futures_negative_balance_v1_resp import CreatePortfolioRepayFuturesNegativeBalanceV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    var_from = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Repay futures Negative Balance(USER_DATA)
        api_response = api_instance.create_portfolio_repay_futures_negative_balance_v1(timestamp, var_from=var_from, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_repay_futures_negative_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_repay_futures_negative_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **var_from** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioRepayFuturesNegativeBalanceV1Resp**](CreatePortfolioRepayFuturesNegativeBalanceV1Resp.md)

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

# **create_portfolio_repay_futures_switch_v1**
> CreatePortfolioRepayFuturesSwitchV1Resp create_portfolio_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)

Change Auto-repay-futures Status(TRADE)

Change Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_portfolio_repay_futures_switch_v1_resp import CreatePortfolioRepayFuturesSwitchV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    auto_repay = 'true' # str |  (default to 'true')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Auto-repay-futures Status(TRADE)
        api_response = api_instance.create_portfolio_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_repay** | **str**|  | [default to &#39;true&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioRepayFuturesSwitchV1Resp**](CreatePortfolioRepayFuturesSwitchV1Resp.md)

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

# **create_portfolio_repay_v1**
> CreatePortfolioRepayV1Resp create_portfolio_repay_v1(timestamp, var_from=var_from, recv_window=recv_window)

Portfolio Margin Pro Bankruptcy Loan Repay

Repay Portfolio Margin Pro Bankruptcy Loan

### Example


```python
import binance.spot
from binance.spot.models.create_portfolio_repay_v1_resp import CreatePortfolioRepayV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    var_from = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Portfolio Margin Pro Bankruptcy Loan Repay
        api_response = api_instance.create_portfolio_repay_v1(timestamp, var_from=var_from, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->create_portfolio_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->create_portfolio_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **var_from** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePortfolioRepayV1Resp**](CreatePortfolioRepayV1Resp.md)

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

# **get_portfolio_account_v1**
> GetPortfolioAccountV1Resp get_portfolio_account_v1(timestamp, recv_window=recv_window)

Get Portfolio Margin Pro Account Info(USER_DATA)

Get Portfolio Margin Pro Account Info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_account_v1_resp import GetPortfolioAccountV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Portfolio Margin Pro Account Info(USER_DATA)
        api_response = api_instance.get_portfolio_account_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPortfolioAccountV1Resp**](GetPortfolioAccountV1Resp.md)

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

# **get_portfolio_account_v2**
> get_portfolio_account_v2(timestamp, recv_window=recv_window)

Get Portfolio Margin Pro SPAN Account Info(USER_DATA)

Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Portfolio Margin Pro SPAN Account Info(USER_DATA)
        api_instance.get_portfolio_account_v2(timestamp, recv_window=recv_window)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_asset_index_price_v1**
> List[GetPortfolioAssetIndexPriceV1RespItem] get_portfolio_asset_index_price_v1(asset=asset)

Query Portfolio Margin Asset Index Price (MARKET_DATA)

Query Portfolio Margin Asset Index Price

### Example


```python
import binance.spot
from binance.spot.models.get_portfolio_asset_index_price_v1_resp_item import GetPortfolioAssetIndexPriceV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    asset = '' # str |  (optional) (default to '')

    try:
        # Query Portfolio Margin Asset Index Price (MARKET_DATA)
        api_response = api_instance.get_portfolio_asset_index_price_v1(asset=asset)
        print("The response of PortfolioMarginProApi->get_portfolio_asset_index_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_asset_index_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetPortfolioAssetIndexPriceV1RespItem]**](GetPortfolioAssetIndexPriceV1RespItem.md)

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

# **get_portfolio_balance_v1**
> List[GetPortfolioBalanceV1RespItem] get_portfolio_balance_v1(timestamp, asset=asset, recv_window=recv_window)

Get Portfolio Margin Pro Account Balance(USER_DATA)

Query Portfolio Margin Pro account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_balance_v1_resp_item import GetPortfolioBalanceV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Portfolio Margin Pro Account Balance(USER_DATA)
        api_response = api_instance.get_portfolio_balance_v1(timestamp, asset=asset, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPortfolioBalanceV1RespItem]**](GetPortfolioBalanceV1RespItem.md)

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

# **get_portfolio_collateral_rate_v1**
> List[GetPortfolioCollateralRateV1RespItem] get_portfolio_collateral_rate_v1()

Portfolio Margin Collateral Rate(MARKET_DATA)

Portfolio Margin Collateral Rate

### Example


```python
import binance.spot
from binance.spot.models.get_portfolio_collateral_rate_v1_resp_item import GetPortfolioCollateralRateV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)

    try:
        # Portfolio Margin Collateral Rate(MARKET_DATA)
        api_response = api_instance.get_portfolio_collateral_rate_v1()
        print("The response of PortfolioMarginProApi->get_portfolio_collateral_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_collateral_rate_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPortfolioCollateralRateV1RespItem]**](GetPortfolioCollateralRateV1RespItem.md)

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

# **get_portfolio_collateral_rate_v2**
> List[GetPortfolioCollateralRateV2RespItem] get_portfolio_collateral_rate_v2(timestamp, recv_window=recv_window)

Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)

Portfolio Margin PRO Tiered Collateral Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_collateral_rate_v2_resp_item import GetPortfolioCollateralRateV2RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)
        api_response = api_instance.get_portfolio_collateral_rate_v2(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_collateral_rate_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_collateral_rate_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPortfolioCollateralRateV2RespItem]**](GetPortfolioCollateralRateV2RespItem.md)

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

# **get_portfolio_interest_history_v1**
> List[GetPortfolioInterestHistoryV1RespItem] get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)

Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)

Query interest history of negative balance for portfolio margin.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_interest_history_v1_resp_item import GetPortfolioInterestHistoryV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)
        api_response = api_instance.get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_interest_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPortfolioInterestHistoryV1RespItem]**](GetPortfolioInterestHistoryV1RespItem.md)

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

# **get_portfolio_margin_asset_leverage_v1**
> List[GetPortfolioMarginAssetLeverageV1RespItem] get_portfolio_margin_asset_leverage_v1()

Get Portfolio Margin Asset Leverage(USER_DATA)

Get Portfolio Margin Asset Leverage

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_margin_asset_leverage_v1_resp_item import GetPortfolioMarginAssetLeverageV1RespItem
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)

    try:
        # Get Portfolio Margin Asset Leverage(USER_DATA)
        api_response = api_instance.get_portfolio_margin_asset_leverage_v1()
        print("The response of PortfolioMarginProApi->get_portfolio_margin_asset_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_margin_asset_leverage_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPortfolioMarginAssetLeverageV1RespItem]**](GetPortfolioMarginAssetLeverageV1RespItem.md)

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

# **get_portfolio_pm_loan_history_v1**
> GetPortfolioPmLoanHistoryV1Resp get_portfolio_pm_loan_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)

Query repay history of pmloan for portfolio margin pro.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_pm_loan_history_v1_resp import GetPortfolioPmLoanHistoryV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)
        api_response = api_instance.get_portfolio_pm_loan_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_pm_loan_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_pm_loan_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPortfolioPmLoanHistoryV1Resp**](GetPortfolioPmLoanHistoryV1Resp.md)

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

# **get_portfolio_pm_loan_v1**
> GetPortfolioPmLoanV1Resp get_portfolio_pm_loan_v1(timestamp, recv_window=recv_window)

Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)

Query Portfolio Margin Pro Bankruptcy Loan Amount

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_pm_loan_v1_resp import GetPortfolioPmLoanV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)
        api_response = api_instance.get_portfolio_pm_loan_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_pm_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_pm_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPortfolioPmLoanV1Resp**](GetPortfolioPmLoanV1Resp.md)

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

# **get_portfolio_repay_futures_switch_v1**
> GetPortfolioRepayFuturesSwitchV1Resp get_portfolio_repay_futures_switch_v1(timestamp, recv_window=recv_window)

Get Auto-repay-futures Status(USER_DATA)

Query Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_portfolio_repay_futures_switch_v1_resp import GetPortfolioRepayFuturesSwitchV1Resp
from binance.spot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.spot.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.spot.Configuration(
    auth=binance.spot.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.spot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.spot.PortfolioMarginProApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-repay-futures Status(USER_DATA)
        api_response = api_instance.get_portfolio_repay_futures_switch_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginProApi->get_portfolio_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginProApi->get_portfolio_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPortfolioRepayFuturesSwitchV1Resp**](GetPortfolioRepayFuturesSwitchV1Resp.md)

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

