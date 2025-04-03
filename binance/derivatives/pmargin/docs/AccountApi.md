# binance.derivatives.pmargin.AccountApi

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmargin_create_asset_collection_v1**](AccountApi.md#pmargin_create_asset_collection_v1) | **POST** /papi/v1/asset-collection | Fund Collection by Asset(TRADE)
[**pmargin_create_auto_collection_v1**](AccountApi.md#pmargin_create_auto_collection_v1) | **POST** /papi/v1/auto-collection | Fund Auto-collection(TRADE)
[**pmargin_create_bnb_transfer_v1**](AccountApi.md#pmargin_create_bnb_transfer_v1) | **POST** /papi/v1/bnb-transfer | BNB transfer (TRADE)
[**pmargin_create_cm_leverage_v1**](AccountApi.md#pmargin_create_cm_leverage_v1) | **POST** /papi/v1/cm/leverage | Change CM Initial Leverage (TRADE)
[**pmargin_create_cm_position_side_dual_v1**](AccountApi.md#pmargin_create_cm_position_side_dual_v1) | **POST** /papi/v1/cm/positionSide/dual | Change CM Position Mode(TRADE)
[**pmargin_create_repay_futures_negative_balance_v1**](AccountApi.md#pmargin_create_repay_futures_negative_balance_v1) | **POST** /papi/v1/repay-futures-negative-balance | Repay futures Negative Balance(USER_DATA)
[**pmargin_create_repay_futures_switch_v1**](AccountApi.md#pmargin_create_repay_futures_switch_v1) | **POST** /papi/v1/repay-futures-switch | Change Auto-repay-futures Status(TRADE)
[**pmargin_create_um_leverage_v1**](AccountApi.md#pmargin_create_um_leverage_v1) | **POST** /papi/v1/um/leverage | Change UM Initial Leverage(TRADE)
[**pmargin_create_um_position_side_dual_v1**](AccountApi.md#pmargin_create_um_position_side_dual_v1) | **POST** /papi/v1/um/positionSide/dual | Change UM Position Mode(TRADE)
[**pmargin_get_account_v1**](AccountApi.md#pmargin_get_account_v1) | **GET** /papi/v1/account | Account Information(USER_DATA)
[**pmargin_get_balance_v1**](AccountApi.md#pmargin_get_balance_v1) | **GET** /papi/v1/balance | Account Balance(USER_DATA)
[**pmargin_get_cm_account_v1**](AccountApi.md#pmargin_get_cm_account_v1) | **GET** /papi/v1/cm/account | Get CM Account Detail(USER_DATA)
[**pmargin_get_cm_commission_rate_v1**](AccountApi.md#pmargin_get_cm_commission_rate_v1) | **GET** /papi/v1/cm/commissionRate | Get User Commission Rate for CM(USER_DATA)
[**pmargin_get_cm_income_v1**](AccountApi.md#pmargin_get_cm_income_v1) | **GET** /papi/v1/cm/income | Get CM Income History(USER_DATA)
[**pmargin_get_cm_leverage_bracket_v1**](AccountApi.md#pmargin_get_cm_leverage_bracket_v1) | **GET** /papi/v1/cm/leverageBracket | CM Notional and Leverage Brackets(USER_DATA)
[**pmargin_get_cm_position_risk_v1**](AccountApi.md#pmargin_get_cm_position_risk_v1) | **GET** /papi/v1/cm/positionRisk | Query CM Position Information(USER_DATA)
[**pmargin_get_cm_position_side_dual_v1**](AccountApi.md#pmargin_get_cm_position_side_dual_v1) | **GET** /papi/v1/cm/positionSide/dual | Get CM Current Position Mode(USER_DATA)
[**pmargin_get_margin_margin_interest_history_v1**](AccountApi.md#pmargin_get_margin_margin_interest_history_v1) | **GET** /papi/v1/margin/marginInterestHistory | Get Margin Borrow/Loan Interest History(USER_DATA)
[**pmargin_get_margin_margin_loan_v1**](AccountApi.md#pmargin_get_margin_margin_loan_v1) | **GET** /papi/v1/margin/marginLoan | Query Margin Loan Record(USER_DATA)
[**pmargin_get_margin_max_borrowable_v1**](AccountApi.md#pmargin_get_margin_max_borrowable_v1) | **GET** /papi/v1/margin/maxBorrowable | Margin Max Borrow(USER_DATA)
[**pmargin_get_margin_max_withdraw_v1**](AccountApi.md#pmargin_get_margin_max_withdraw_v1) | **GET** /papi/v1/margin/maxWithdraw | Query Margin Max Withdraw(USER_DATA)
[**pmargin_get_margin_repay_loan_v1**](AccountApi.md#pmargin_get_margin_repay_loan_v1) | **GET** /papi/v1/margin/repayLoan | Query Margin repay Record(USER_DATA)
[**pmargin_get_portfolio_interest_history_v1**](AccountApi.md#pmargin_get_portfolio_interest_history_v1) | **GET** /papi/v1/portfolio/interest-history | Query Portfolio Margin Negative Balance Interest History(USER_DATA)
[**pmargin_get_portfolio_negative_balance_exchange_record_v1**](AccountApi.md#pmargin_get_portfolio_negative_balance_exchange_record_v1) | **GET** /papi/v1/portfolio/negative-balance-exchange-record | Query User Negative Balance Auto Exchange Record (USER_DATA)
[**pmargin_get_rate_limit_order_v1**](AccountApi.md#pmargin_get_rate_limit_order_v1) | **GET** /papi/v1/rateLimit/order | Query User Rate Limit (USER_DATA)
[**pmargin_get_repay_futures_switch_v1**](AccountApi.md#pmargin_get_repay_futures_switch_v1) | **GET** /papi/v1/repay-futures-switch | Get Auto-repay-futures Status(USER_DATA)
[**pmargin_get_um_account_config_v1**](AccountApi.md#pmargin_get_um_account_config_v1) | **GET** /papi/v1/um/accountConfig | UM Futures Account Configuration(USER_DATA)
[**pmargin_get_um_account_v1**](AccountApi.md#pmargin_get_um_account_v1) | **GET** /papi/v1/um/account | Get UM Account Detail(USER_DATA)
[**pmargin_get_um_account_v2**](AccountApi.md#pmargin_get_um_account_v2) | **GET** /papi/v2/um/account | Get UM Account Detail V2(USER_DATA)
[**pmargin_get_um_api_trading_status_v1**](AccountApi.md#pmargin_get_um_api_trading_status_v1) | **GET** /papi/v1/um/apiTradingStatus | Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)
[**pmargin_get_um_commission_rate_v1**](AccountApi.md#pmargin_get_um_commission_rate_v1) | **GET** /papi/v1/um/commissionRate | Get User Commission Rate for UM(USER_DATA)
[**pmargin_get_um_income_asyn_id_v1**](AccountApi.md#pmargin_get_um_income_asyn_id_v1) | **GET** /papi/v1/um/income/asyn/id | Get UM Futures Transaction Download Link by Id(USER_DATA)
[**pmargin_get_um_income_asyn_v1**](AccountApi.md#pmargin_get_um_income_asyn_v1) | **GET** /papi/v1/um/income/asyn | Get Download Id For UM Futures Transaction History (USER_DATA)
[**pmargin_get_um_income_v1**](AccountApi.md#pmargin_get_um_income_v1) | **GET** /papi/v1/um/income | Get UM Income History(USER_DATA)
[**pmargin_get_um_leverage_bracket_v1**](AccountApi.md#pmargin_get_um_leverage_bracket_v1) | **GET** /papi/v1/um/leverageBracket | UM Notional and Leverage Brackets (USER_DATA)
[**pmargin_get_um_order_asyn_id_v1**](AccountApi.md#pmargin_get_um_order_asyn_id_v1) | **GET** /papi/v1/um/order/asyn/id | Get UM Futures Order Download Link by Id(USER_DATA)
[**pmargin_get_um_order_asyn_v1**](AccountApi.md#pmargin_get_um_order_asyn_v1) | **GET** /papi/v1/um/order/asyn | Get Download Id For UM Futures Order History (USER_DATA)
[**pmargin_get_um_position_risk_v1**](AccountApi.md#pmargin_get_um_position_risk_v1) | **GET** /papi/v1/um/positionRisk | Query UM Position Information(USER_DATA)
[**pmargin_get_um_position_side_dual_v1**](AccountApi.md#pmargin_get_um_position_side_dual_v1) | **GET** /papi/v1/um/positionSide/dual | Get UM Current Position Mode(USER_DATA)
[**pmargin_get_um_symbol_config_v1**](AccountApi.md#pmargin_get_um_symbol_config_v1) | **GET** /papi/v1/um/symbolConfig | UM Futures Symbol Configuration(USER_DATA)
[**pmargin_get_um_trade_asyn_id_v1**](AccountApi.md#pmargin_get_um_trade_asyn_id_v1) | **GET** /papi/v1/um/trade/asyn/id | Get UM Futures Trade Download Link by Id(USER_DATA)
[**pmargin_get_um_trade_asyn_v1**](AccountApi.md#pmargin_get_um_trade_asyn_v1) | **GET** /papi/v1/um/trade/asyn | Get Download Id For UM Futures Trade History (USER_DATA)


# **pmargin_create_asset_collection_v1**
> PmarginCreateAssetCollectionV1Resp pmargin_create_asset_collection_v1(asset, timestamp, recv_window=recv_window)

Fund Collection by Asset(TRADE)

Transfers specific asset from Futures Account to Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_asset_collection_v1_resp import PmarginCreateAssetCollectionV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Collection by Asset(TRADE)
        api_response = api_instance.pmargin_create_asset_collection_v1(asset, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_asset_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_asset_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateAssetCollectionV1Resp**](PmarginCreateAssetCollectionV1Resp.md)

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

# **pmargin_create_auto_collection_v1**
> PmarginCreateAutoCollectionV1Resp pmargin_create_auto_collection_v1(timestamp, recv_window=recv_window)

Fund Auto-collection(TRADE)

Fund collection for Portfolio Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_auto_collection_v1_resp import PmarginCreateAutoCollectionV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Auto-collection(TRADE)
        api_response = api_instance.pmargin_create_auto_collection_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_auto_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_auto_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateAutoCollectionV1Resp**](PmarginCreateAutoCollectionV1Resp.md)

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

# **pmargin_create_bnb_transfer_v1**
> PmarginCreateBnbTransferV1Resp pmargin_create_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)

BNB transfer (TRADE)

Transfer BNB in and out of UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_bnb_transfer_v1_resp import PmarginCreateBnbTransferV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    transfer_side = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # BNB transfer (TRADE)
        api_response = api_instance.pmargin_create_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_bnb_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_bnb_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **transfer_side** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateBnbTransferV1Resp**](PmarginCreateBnbTransferV1Resp.md)

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

# **pmargin_create_cm_leverage_v1**
> PmarginCreateCmLeverageV1Resp pmargin_create_cm_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change CM Initial Leverage (TRADE)

Change user's initial leverage of specific symbol in CM.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_cm_leverage_v1_resp import PmarginCreateCmLeverageV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change CM Initial Leverage (TRADE)
        api_response = api_instance.pmargin_create_cm_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_cm_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_cm_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateCmLeverageV1Resp**](PmarginCreateCmLeverageV1Resp.md)

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

# **pmargin_create_cm_position_side_dual_v1**
> PmarginCreateCmPositionSideDualV1Resp pmargin_create_cm_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change CM Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_cm_position_side_dual_v1_resp import PmarginCreateCmPositionSideDualV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change CM Position Mode(TRADE)
        api_response = api_instance.pmargin_create_cm_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_cm_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_cm_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateCmPositionSideDualV1Resp**](PmarginCreateCmPositionSideDualV1Resp.md)

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

# **pmargin_create_repay_futures_negative_balance_v1**
> PmarginCreateRepayFuturesNegativeBalanceV1Resp pmargin_create_repay_futures_negative_balance_v1(timestamp, recv_window=recv_window)

Repay futures Negative Balance(USER_DATA)

Repay futures Negative Balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_repay_futures_negative_balance_v1_resp import PmarginCreateRepayFuturesNegativeBalanceV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Repay futures Negative Balance(USER_DATA)
        api_response = api_instance.pmargin_create_repay_futures_negative_balance_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_repay_futures_negative_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_repay_futures_negative_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateRepayFuturesNegativeBalanceV1Resp**](PmarginCreateRepayFuturesNegativeBalanceV1Resp.md)

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

# **pmargin_create_repay_futures_switch_v1**
> PmarginCreateRepayFuturesSwitchV1Resp pmargin_create_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)

Change Auto-repay-futures Status(TRADE)

Change Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_repay_futures_switch_v1_resp import PmarginCreateRepayFuturesSwitchV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    auto_repay = 'true' # str |  (default to 'true')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Auto-repay-futures Status(TRADE)
        api_response = api_instance.pmargin_create_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_repay** | **str**|  | [default to &#39;true&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateRepayFuturesSwitchV1Resp**](PmarginCreateRepayFuturesSwitchV1Resp.md)

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

# **pmargin_create_um_leverage_v1**
> PmarginCreateUmLeverageV1Resp pmargin_create_um_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change UM Initial Leverage(TRADE)

Change user's initial leverage of specific symbol in UM.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_um_leverage_v1_resp import PmarginCreateUmLeverageV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change UM Initial Leverage(TRADE)
        api_response = api_instance.pmargin_create_um_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_um_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_um_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateUmLeverageV1Resp**](PmarginCreateUmLeverageV1Resp.md)

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

# **pmargin_create_um_position_side_dual_v1**
> PmarginCreateUmPositionSideDualV1Resp pmargin_create_um_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change UM Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_um_position_side_dual_v1_resp import PmarginCreateUmPositionSideDualV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change UM Position Mode(TRADE)
        api_response = api_instance.pmargin_create_um_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_create_um_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_create_um_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateUmPositionSideDualV1Resp**](PmarginCreateUmPositionSideDualV1Resp.md)

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

# **pmargin_get_account_v1**
> PmarginGetAccountV1Resp pmargin_get_account_v1(timestamp, recv_window=recv_window)

Account Information(USER_DATA)

Query account information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_account_v1_resp import PmarginGetAccountV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information(USER_DATA)
        api_response = api_instance.pmargin_get_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetAccountV1Resp**](PmarginGetAccountV1Resp.md)

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

# **pmargin_get_balance_v1**
> PmarginGetBalanceV1Resp pmargin_get_balance_v1(timestamp, asset=asset, recv_window=recv_window)

Account Balance(USER_DATA)

Query account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_balance_v1_resp import PmarginGetBalanceV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Account Balance(USER_DATA)
        api_response = api_instance.pmargin_get_balance_v1(timestamp, asset=asset, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetBalanceV1Resp**](PmarginGetBalanceV1Resp.md)

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

# **pmargin_get_cm_account_v1**
> PmarginGetCmAccountV1Resp pmargin_get_cm_account_v1(timestamp, recv_window=recv_window)

Get CM Account Detail(USER_DATA)

Get current CM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp import PmarginGetCmAccountV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get CM Account Detail(USER_DATA)
        api_response = api_instance.pmargin_get_cm_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetCmAccountV1Resp**](PmarginGetCmAccountV1Resp.md)

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

# **pmargin_get_cm_commission_rate_v1**
> PmarginGetCmCommissionRateV1Resp pmargin_get_cm_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

Get User Commission Rate for CM(USER_DATA)

Get User Commission Rate for CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_commission_rate_v1_resp import PmarginGetCmCommissionRateV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User Commission Rate for CM(USER_DATA)
        api_response = api_instance.pmargin_get_cm_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetCmCommissionRateV1Resp**](PmarginGetCmCommissionRateV1Resp.md)

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

# **pmargin_get_cm_income_v1**
> List[PmarginGetCmIncomeV1RespItem] pmargin_get_cm_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get CM Income History(USER_DATA)

Get CM Income History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_income_v1_resp_item import PmarginGetCmIncomeV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | &#34;TRANSFER&#34;,&#34;WELCOME_BONUS&#34;, &#34;FUNDING_FEE&#34;, &#34;REALIZED_PNL&#34;, &#34;COMMISSION&#34;, &#34;INSURANCE_CLEAR&#34;, and &#34;DELIVERED_SETTELMENT&#34; (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get CM Income History(USER_DATA)
        api_response = api_instance.pmargin_get_cm_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| &amp;#34;TRANSFER&amp;#34;,&amp;#34;WELCOME_BONUS&amp;#34;, &amp;#34;FUNDING_FEE&amp;#34;, &amp;#34;REALIZED_PNL&amp;#34;, &amp;#34;COMMISSION&amp;#34;, &amp;#34;INSURANCE_CLEAR&amp;#34;, and &amp;#34;DELIVERED_SETTELMENT&amp;#34; | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmIncomeV1RespItem]**](PmarginGetCmIncomeV1RespItem.md)

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

# **pmargin_get_cm_leverage_bracket_v1**
> List[PmarginGetCmLeverageBracketV1RespItem] pmargin_get_cm_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

CM Notional and Leverage Brackets(USER_DATA)

Query CM notional and leverage brackets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_leverage_bracket_v1_resp_item import PmarginGetCmLeverageBracketV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # CM Notional and Leverage Brackets(USER_DATA)
        api_response = api_instance.pmargin_get_cm_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmLeverageBracketV1RespItem]**](PmarginGetCmLeverageBracketV1RespItem.md)

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

# **pmargin_get_cm_position_risk_v1**
> List[PmarginGetCmPositionRiskV1RespItem] pmargin_get_cm_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)

Query CM Position Information(USER_DATA)

Get current CM position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_position_risk_v1_resp_item import PmarginGetCmPositionRiskV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    margin_asset = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Position Information(USER_DATA)
        api_response = api_instance.pmargin_get_cm_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_position_risk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **margin_asset** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmPositionRiskV1RespItem]**](PmarginGetCmPositionRiskV1RespItem.md)

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

# **pmargin_get_cm_position_side_dual_v1**
> PmarginGetCmPositionSideDualV1Resp pmargin_get_cm_position_side_dual_v1(timestamp, recv_window=recv_window)

Get CM Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_position_side_dual_v1_resp import PmarginGetCmPositionSideDualV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get CM Current Position Mode(USER_DATA)
        api_response = api_instance.pmargin_get_cm_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_cm_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_cm_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetCmPositionSideDualV1Resp**](PmarginGetCmPositionSideDualV1Resp.md)

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

# **pmargin_get_margin_margin_interest_history_v1**
> PmarginGetMarginMarginInterestHistoryV1Resp pmargin_get_margin_margin_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Get Margin Borrow/Loan Interest History(USER_DATA)

Get Margin Borrow/Loan Interest History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_margin_interest_history_v1_resp import PmarginGetMarginMarginInterestHistoryV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    archived = '' # str | Default: `false`. Set to `true` for archived data from 6 months ago (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Margin Borrow/Loan Interest History(USER_DATA)
        api_response = api_instance.pmargin_get_margin_margin_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_margin_margin_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_margin_margin_interest_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: &#x60;false&#x60;. Set to &#x60;true&#x60; for archived data from 6 months ago | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**PmarginGetMarginMarginInterestHistoryV1Resp**](PmarginGetMarginMarginInterestHistoryV1Resp.md)

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

# **pmargin_get_margin_margin_loan_v1**
> PmarginGetMarginMarginLoanV1Resp pmargin_get_margin_margin_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Margin Loan Record(USER_DATA)

Query margin loan record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_margin_loan_v1_resp import PmarginGetMarginMarginLoanV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    tx_id = 56 # int | the `tranId` in `POST/papi/v1/marginLoan` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    archived = '' # str | Default: `false`. Set to `true` for archived data from 6 months ago (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Loan Record(USER_DATA)
        api_response = api_instance.pmargin_get_margin_margin_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_margin_margin_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_margin_margin_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **tx_id** | **int**| the &#x60;tranId&#x60; in &#x60;POST/papi/v1/marginLoan&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: &#x60;false&#x60;. Set to &#x60;true&#x60; for archived data from 6 months ago | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetMarginMarginLoanV1Resp**](PmarginGetMarginMarginLoanV1Resp.md)

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

# **pmargin_get_margin_max_borrowable_v1**
> PmarginGetMarginMaxBorrowableV1Resp pmargin_get_margin_max_borrowable_v1(asset, timestamp, recv_window=recv_window)

Margin Max Borrow(USER_DATA)

Query margin max borrow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_max_borrowable_v1_resp import PmarginGetMarginMaxBorrowableV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Max Borrow(USER_DATA)
        api_response = api_instance.pmargin_get_margin_max_borrowable_v1(asset, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_margin_max_borrowable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_margin_max_borrowable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**PmarginGetMarginMaxBorrowableV1Resp**](PmarginGetMarginMaxBorrowableV1Resp.md)

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

# **pmargin_get_margin_max_withdraw_v1**
> PmarginGetMarginMaxWithdrawV1Resp pmargin_get_margin_max_withdraw_v1(asset, timestamp, recv_window=recv_window)

Query Margin Max Withdraw(USER_DATA)

Query Margin Max Withdraw

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_max_withdraw_v1_resp import PmarginGetMarginMaxWithdrawV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Max Withdraw(USER_DATA)
        api_response = api_instance.pmargin_get_margin_max_withdraw_v1(asset, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_margin_max_withdraw_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_margin_max_withdraw_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**PmarginGetMarginMaxWithdrawV1Resp**](PmarginGetMarginMaxWithdrawV1Resp.md)

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

# **pmargin_get_margin_repay_loan_v1**
> PmarginGetMarginRepayLoanV1Resp pmargin_get_margin_repay_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Margin repay Record(USER_DATA)

Query margin repay record.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_repay_loan_v1_resp import PmarginGetMarginRepayLoanV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    tx_id = 56 # int | the tranId in `POST/papi/v1/repayLoan` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    archived = '' # str | Default: `false`. Set to `true` for archived data from 6 months ago (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin repay Record(USER_DATA)
        api_response = api_instance.pmargin_get_margin_repay_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_margin_repay_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_margin_repay_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **tx_id** | **int**| the tranId in &#x60;POST/papi/v1/repayLoan&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: &#x60;false&#x60;. Set to &#x60;true&#x60; for archived data from 6 months ago | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetMarginRepayLoanV1Resp**](PmarginGetMarginRepayLoanV1Resp.md)

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

# **pmargin_get_portfolio_interest_history_v1**
> List[PmarginGetPortfolioInterestHistoryV1RespItem] pmargin_get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)

Query Portfolio Margin Negative Balance Interest History(USER_DATA)

Query interest history of negative balance for portfolio margin.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_portfolio_interest_history_v1_resp_item import PmarginGetPortfolioInterestHistoryV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Portfolio Margin Negative Balance Interest History(USER_DATA)
        api_response = api_instance.pmargin_get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_portfolio_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_portfolio_interest_history_v1: %s\n" % e)
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

[**List[PmarginGetPortfolioInterestHistoryV1RespItem]**](PmarginGetPortfolioInterestHistoryV1RespItem.md)

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

# **pmargin_get_portfolio_negative_balance_exchange_record_v1**
> PmarginGetPortfolioNegativeBalanceExchangeRecordV1Resp pmargin_get_portfolio_negative_balance_exchange_record_v1(start_time, end_time, timestamp, recv_window=recv_window)

Query User Negative Balance Auto Exchange Record (USER_DATA)

Query user negative balance auto exchange record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_portfolio_negative_balance_exchange_record_v1_resp import PmarginGetPortfolioNegativeBalanceExchangeRecordV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User Negative Balance Auto Exchange Record (USER_DATA)
        api_response = api_instance.pmargin_get_portfolio_negative_balance_exchange_record_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_portfolio_negative_balance_exchange_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_portfolio_negative_balance_exchange_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetPortfolioNegativeBalanceExchangeRecordV1Resp**](PmarginGetPortfolioNegativeBalanceExchangeRecordV1Resp.md)

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

# **pmargin_get_rate_limit_order_v1**
> List[PmarginGetRateLimitOrderV1RespItem] pmargin_get_rate_limit_order_v1(timestamp, recv_window=recv_window)

Query User Rate Limit (USER_DATA)

Query User Rate Limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_rate_limit_order_v1_resp_item import PmarginGetRateLimitOrderV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query User Rate Limit (USER_DATA)
        api_response = api_instance.pmargin_get_rate_limit_order_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetRateLimitOrderV1RespItem]**](PmarginGetRateLimitOrderV1RespItem.md)

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

# **pmargin_get_repay_futures_switch_v1**
> PmarginGetRepayFuturesSwitchV1Resp pmargin_get_repay_futures_switch_v1(timestamp, recv_window=recv_window)

Get Auto-repay-futures Status(USER_DATA)

Query Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_repay_futures_switch_v1_resp import PmarginGetRepayFuturesSwitchV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-repay-futures Status(USER_DATA)
        api_response = api_instance.pmargin_get_repay_futures_switch_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetRepayFuturesSwitchV1Resp**](PmarginGetRepayFuturesSwitchV1Resp.md)

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

# **pmargin_get_um_account_config_v1**
> PmarginGetUmAccountConfigV1Resp pmargin_get_um_account_config_v1(timestamp, recv_window=recv_window)

UM Futures Account Configuration(USER_DATA)

Query UM Futures account configuration

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_account_config_v1_resp import PmarginGetUmAccountConfigV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # UM Futures Account Configuration(USER_DATA)
        api_response = api_instance.pmargin_get_um_account_config_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_account_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_account_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmAccountConfigV1Resp**](PmarginGetUmAccountConfigV1Resp.md)

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

# **pmargin_get_um_account_v1**
> PmarginGetUmAccountV1Resp pmargin_get_um_account_v1(timestamp, recv_window=recv_window)

Get UM Account Detail(USER_DATA)

Get current UM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_account_v1_resp import PmarginGetUmAccountV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Account Detail(USER_DATA)
        api_response = api_instance.pmargin_get_um_account_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmAccountV1Resp**](PmarginGetUmAccountV1Resp.md)

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

# **pmargin_get_um_account_v2**
> PmarginGetUmAccountV2Resp pmargin_get_um_account_v2(timestamp, recv_window=recv_window)

Get UM Account Detail V2(USER_DATA)

Get current UM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp import PmarginGetUmAccountV2Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Account Detail V2(USER_DATA)
        api_response = api_instance.pmargin_get_um_account_v2(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmAccountV2Resp**](PmarginGetUmAccountV2Resp.md)

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

# **pmargin_get_um_api_trading_status_v1**
> PmarginGetUmApiTradingStatusV1Resp pmargin_get_um_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)

Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)

Portfolio Margin UM Trading Quantitative Rules Indicators

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp import PmarginGetUmApiTradingStatusV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)
        api_response = api_instance.pmargin_get_um_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmApiTradingStatusV1Resp**](PmarginGetUmApiTradingStatusV1Resp.md)

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

# **pmargin_get_um_commission_rate_v1**
> PmarginGetUmCommissionRateV1Resp pmargin_get_um_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

Get User Commission Rate for UM(USER_DATA)

Get User Commission Rate for UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_commission_rate_v1_resp import PmarginGetUmCommissionRateV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User Commission Rate for UM(USER_DATA)
        api_response = api_instance.pmargin_get_um_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmCommissionRateV1Resp**](PmarginGetUmCommissionRateV1Resp.md)

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

# **pmargin_get_um_income_asyn_id_v1**
> PmarginGetUmIncomeAsynIdV1Resp pmargin_get_um_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Transaction Download Link by Id(USER_DATA)

Get UM futures Transaction download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_income_asyn_id_v1_resp import PmarginGetUmIncomeAsynIdV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Transaction Download Link by Id(USER_DATA)
        api_response = api_instance.pmargin_get_um_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmIncomeAsynIdV1Resp**](PmarginGetUmIncomeAsynIdV1Resp.md)

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

# **pmargin_get_um_income_asyn_v1**
> PmarginGetUmIncomeAsynV1Resp pmargin_get_um_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Transaction History (USER_DATA)

Get download id for UM futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_income_asyn_v1_resp import PmarginGetUmIncomeAsynV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Transaction History (USER_DATA)
        api_response = api_instance.pmargin_get_um_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmIncomeAsynV1Resp**](PmarginGetUmIncomeAsynV1Resp.md)

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

# **pmargin_get_um_income_v1**
> List[PmarginGetUmIncomeV1RespItem] pmargin_get_um_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get UM Income History(USER_DATA)

Get UM Income History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_income_v1_resp_item import PmarginGetUmIncomeV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Income History(USER_DATA)
        api_response = api_instance.pmargin_get_um_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmIncomeV1RespItem]**](PmarginGetUmIncomeV1RespItem.md)

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

# **pmargin_get_um_leverage_bracket_v1**
> List[PmarginGetUmLeverageBracketV1RespItem] pmargin_get_um_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Notional and Leverage Brackets (USER_DATA)

Query UM notional and leverage brackets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_leverage_bracket_v1_resp_item import PmarginGetUmLeverageBracketV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Notional and Leverage Brackets (USER_DATA)
        api_response = api_instance.pmargin_get_um_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmLeverageBracketV1RespItem]**](PmarginGetUmLeverageBracketV1RespItem.md)

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

# **pmargin_get_um_order_asyn_id_v1**
> PmarginGetUmOrderAsynIdV1Resp pmargin_get_um_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Order Download Link by Id(USER_DATA)

Get UM futures order download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_order_asyn_id_v1_resp import PmarginGetUmOrderAsynIdV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Order Download Link by Id(USER_DATA)
        api_response = api_instance.pmargin_get_um_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmOrderAsynIdV1Resp**](PmarginGetUmOrderAsynIdV1Resp.md)

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

# **pmargin_get_um_order_asyn_v1**
> PmarginGetUmOrderAsynV1Resp pmargin_get_um_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Order History (USER_DATA)

Get download id for UM futures order history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_order_asyn_v1_resp import PmarginGetUmOrderAsynV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Order History (USER_DATA)
        api_response = api_instance.pmargin_get_um_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmOrderAsynV1Resp**](PmarginGetUmOrderAsynV1Resp.md)

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

# **pmargin_get_um_position_risk_v1**
> List[PmarginGetUmPositionRiskV1RespItem] pmargin_get_um_position_risk_v1()

Query UM Position Information(USER_DATA)

Get current UM position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_position_risk_v1_resp_item import PmarginGetUmPositionRiskV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)

    try:
        # Query UM Position Information(USER_DATA)
        api_response = api_instance.pmargin_get_um_position_risk_v1()
        print("The response of AccountApi->pmargin_get_um_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_position_risk_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PmarginGetUmPositionRiskV1RespItem]**](PmarginGetUmPositionRiskV1RespItem.md)

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

# **pmargin_get_um_position_side_dual_v1**
> PmarginGetUmPositionSideDualV1Resp pmargin_get_um_position_side_dual_v1(timestamp, recv_window=recv_window)

Get UM Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_position_side_dual_v1_resp import PmarginGetUmPositionSideDualV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Current Position Mode(USER_DATA)
        api_response = api_instance.pmargin_get_um_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmPositionSideDualV1Resp**](PmarginGetUmPositionSideDualV1Resp.md)

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

# **pmargin_get_um_symbol_config_v1**
> List[PmarginGetUmSymbolConfigV1RespItem] pmargin_get_um_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Futures Symbol Configuration(USER_DATA)

Get current UM account symbol configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_symbol_config_v1_resp_item import PmarginGetUmSymbolConfigV1RespItem
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Futures Symbol Configuration(USER_DATA)
        api_response = api_instance.pmargin_get_um_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_symbol_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_symbol_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmSymbolConfigV1RespItem]**](PmarginGetUmSymbolConfigV1RespItem.md)

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

# **pmargin_get_um_trade_asyn_id_v1**
> PmarginGetUmTradeAsynIdV1Resp pmargin_get_um_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Trade Download Link by Id(USER_DATA)

Get UM futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_trade_asyn_id_v1_resp import PmarginGetUmTradeAsynIdV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.pmargin_get_um_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmTradeAsynIdV1Resp**](PmarginGetUmTradeAsynIdV1Resp.md)

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

# **pmargin_get_um_trade_asyn_v1**
> PmarginGetUmTradeAsynV1Resp pmargin_get_um_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Trade History (USER_DATA)

Get download id for UM futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_trade_asyn_v1_resp import PmarginGetUmTradeAsynV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmargin.Configuration(
    auth=binance.derivatives.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.AccountApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Trade History (USER_DATA)
        api_response = api_instance.pmargin_get_um_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of AccountApi->pmargin_get_um_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pmargin_get_um_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmTradeAsynV1Resp**](PmarginGetUmTradeAsynV1Resp.md)

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

