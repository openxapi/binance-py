# binance.spot.MarginTradingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_margin_api_key_v1**](MarginTradingApi.md#create_margin_api_key_v1) | **POST** /sapi/v1/margin/apiKey | Create Special Key(Low-Latency Trading)(TRADE)
[**create_margin_borrow_repay_v1**](MarginTradingApi.md#create_margin_borrow_repay_v1) | **POST** /sapi/v1/margin/borrow-repay | Margin account borrow/repay(MARGIN)
[**create_margin_exchange_small_liability_v1**](MarginTradingApi.md#create_margin_exchange_small_liability_v1) | **POST** /sapi/v1/margin/exchange-small-liability | Small Liability Exchange (MARGIN)
[**create_margin_isolated_account_v1**](MarginTradingApi.md#create_margin_isolated_account_v1) | **POST** /sapi/v1/margin/isolated/account | Enable Isolated Margin Account (TRADE)
[**create_margin_listen_key_v1**](MarginTradingApi.md#create_margin_listen_key_v1) | **POST** /sapi/v1/margin/listen-key | Start User Data Stream (USER_STREAM)
[**create_margin_manual_liquidation_v1**](MarginTradingApi.md#create_margin_manual_liquidation_v1) | **POST** /sapi/v1/margin/manual-liquidation | Margin Manual Liquidation(MARGIN)
[**create_margin_max_leverage_v1**](MarginTradingApi.md#create_margin_max_leverage_v1) | **POST** /sapi/v1/margin/max-leverage | Adjust cross margin max leverage (USER_DATA)
[**create_margin_order_oco_v1**](MarginTradingApi.md#create_margin_order_oco_v1) | **POST** /sapi/v1/margin/order/oco | Margin Account New OCO (TRADE)
[**create_margin_order_oto_v1**](MarginTradingApi.md#create_margin_order_oto_v1) | **POST** /sapi/v1/margin/order/oto | Margin Account New OTO (TRADE)
[**create_margin_order_otoco_v1**](MarginTradingApi.md#create_margin_order_otoco_v1) | **POST** /sapi/v1/margin/order/otoco | Margin Account New OTOCO (TRADE)
[**create_margin_order_v1**](MarginTradingApi.md#create_margin_order_v1) | **POST** /sapi/v1/margin/order | Margin Account New Order (TRADE)
[**create_user_data_stream_isolated_v1**](MarginTradingApi.md#create_user_data_stream_isolated_v1) | **POST** /sapi/v1/userDataStream/isolated | Start Isolated Margin User Data Stream (USER_STREAM)
[**create_user_data_stream_v1**](MarginTradingApi.md#create_user_data_stream_v1) | **POST** /sapi/v1/userDataStream | Start Margin User Data Stream (USER_STREAM)
[**delete_margin_api_key_v1**](MarginTradingApi.md#delete_margin_api_key_v1) | **DELETE** /sapi/v1/margin/apiKey | Delete Special Key(Low-Latency Trading)(TRADE)
[**delete_margin_isolated_account_v1**](MarginTradingApi.md#delete_margin_isolated_account_v1) | **DELETE** /sapi/v1/margin/isolated/account | Disable Isolated Margin Account (TRADE)
[**delete_margin_listen_key_v1**](MarginTradingApi.md#delete_margin_listen_key_v1) | **DELETE** /sapi/v1/margin/listen-key | Close User Data Stream (USER_STREAM)
[**delete_margin_open_orders_v1**](MarginTradingApi.md#delete_margin_open_orders_v1) | **DELETE** /sapi/v1/margin/openOrders | Margin Account Cancel all Open Orders on a Symbol (TRADE)
[**delete_margin_order_list_v1**](MarginTradingApi.md#delete_margin_order_list_v1) | **DELETE** /sapi/v1/margin/orderList | Margin Account Cancel OCO (TRADE)
[**delete_margin_order_v1**](MarginTradingApi.md#delete_margin_order_v1) | **DELETE** /sapi/v1/margin/order | Margin Account Cancel Order (TRADE)
[**delete_user_data_stream_isolated_v1**](MarginTradingApi.md#delete_user_data_stream_isolated_v1) | **DELETE** /sapi/v1/userDataStream/isolated | Close Isolated Margin User Data Stream (USER_STREAM)
[**delete_user_data_stream_v1**](MarginTradingApi.md#delete_user_data_stream_v1) | **DELETE** /sapi/v1/userDataStream | Close Margin User Data Stream (USER_STREAM)
[**get_bnb_burn_v1**](MarginTradingApi.md#get_bnb_burn_v1) | **GET** /sapi/v1/bnbBurn | Get BNB Burn Status (USER_DATA)
[**get_margin_account_v1**](MarginTradingApi.md#get_margin_account_v1) | **GET** /sapi/v1/margin/account | Query Cross Margin Account Details (USER_DATA)
[**get_margin_all_assets_v1**](MarginTradingApi.md#get_margin_all_assets_v1) | **GET** /sapi/v1/margin/allAssets | Get All Margin Assets (MARKET_DATA)
[**get_margin_all_order_list_v1**](MarginTradingApi.md#get_margin_all_order_list_v1) | **GET** /sapi/v1/margin/allOrderList | Query Margin Account&#39;s all OCO (USER_DATA)
[**get_margin_all_orders_v1**](MarginTradingApi.md#get_margin_all_orders_v1) | **GET** /sapi/v1/margin/allOrders | Query Margin Account&#39;s All Orders (USER_DATA)
[**get_margin_all_pairs_v1**](MarginTradingApi.md#get_margin_all_pairs_v1) | **GET** /sapi/v1/margin/allPairs | Get All Cross Margin Pairs (MARKET_DATA)
[**get_margin_api_key_list_v1**](MarginTradingApi.md#get_margin_api_key_list_v1) | **GET** /sapi/v1/margin/api-key-list | Query Special key List(Low Latency Trading)(TRADE)
[**get_margin_api_key_v1**](MarginTradingApi.md#get_margin_api_key_v1) | **GET** /sapi/v1/margin/apiKey | Query Special key(Low Latency Trading)(TRADE)
[**get_margin_available_inventory_v1**](MarginTradingApi.md#get_margin_available_inventory_v1) | **GET** /sapi/v1/margin/available-inventory | Query Margin Available Inventory(USER_DATA)
[**get_margin_borrow_repay_v1**](MarginTradingApi.md#get_margin_borrow_repay_v1) | **GET** /sapi/v1/margin/borrow-repay | Query borrow/repay records in Margin account(USER_DATA)
[**get_margin_capital_flow_v1**](MarginTradingApi.md#get_margin_capital_flow_v1) | **GET** /sapi/v1/margin/capital-flow | Query Cross Isolated Margin Capital Flow (USER_DATA)
[**get_margin_cross_margin_collateral_ratio_v1**](MarginTradingApi.md#get_margin_cross_margin_collateral_ratio_v1) | **GET** /sapi/v1/margin/crossMarginCollateralRatio | Cross margin collateral ratio (MARKET_DATA)
[**get_margin_cross_margin_data_v1**](MarginTradingApi.md#get_margin_cross_margin_data_v1) | **GET** /sapi/v1/margin/crossMarginData | Query Cross Margin Fee Data (USER_DATA)
[**get_margin_delist_schedule_v1**](MarginTradingApi.md#get_margin_delist_schedule_v1) | **GET** /sapi/v1/margin/delist-schedule | Get Delist Schedule (MARKET_DATA)
[**get_margin_exchange_small_liability_history_v1**](MarginTradingApi.md#get_margin_exchange_small_liability_history_v1) | **GET** /sapi/v1/margin/exchange-small-liability-history | Get Small Liability Exchange History (USER_DATA)
[**get_margin_exchange_small_liability_v1**](MarginTradingApi.md#get_margin_exchange_small_liability_v1) | **GET** /sapi/v1/margin/exchange-small-liability | Get Small Liability Exchange Coin List (USER_DATA)
[**get_margin_force_liquidation_rec_v1**](MarginTradingApi.md#get_margin_force_liquidation_rec_v1) | **GET** /sapi/v1/margin/forceLiquidationRec | Get Force Liquidation Record (USER_DATA)
[**get_margin_interest_history_v1**](MarginTradingApi.md#get_margin_interest_history_v1) | **GET** /sapi/v1/margin/interestHistory | Get Interest History (USER_DATA)
[**get_margin_interest_rate_history_v1**](MarginTradingApi.md#get_margin_interest_rate_history_v1) | **GET** /sapi/v1/margin/interestRateHistory | Query Margin Interest Rate History (USER_DATA)
[**get_margin_isolated_account_limit_v1**](MarginTradingApi.md#get_margin_isolated_account_limit_v1) | **GET** /sapi/v1/margin/isolated/accountLimit | Query Enabled Isolated Margin Account Limit (USER_DATA)
[**get_margin_isolated_account_v1**](MarginTradingApi.md#get_margin_isolated_account_v1) | **GET** /sapi/v1/margin/isolated/account | Query Isolated Margin Account Info (USER_DATA)
[**get_margin_isolated_all_pairs_v1**](MarginTradingApi.md#get_margin_isolated_all_pairs_v1) | **GET** /sapi/v1/margin/isolated/allPairs | Get All Isolated Margin Symbol(MARKET_DATA)
[**get_margin_isolated_margin_data_v1**](MarginTradingApi.md#get_margin_isolated_margin_data_v1) | **GET** /sapi/v1/margin/isolatedMarginData | Query Isolated Margin Fee Data (USER_DATA)
[**get_margin_isolated_margin_tier_v1**](MarginTradingApi.md#get_margin_isolated_margin_tier_v1) | **GET** /sapi/v1/margin/isolatedMarginTier | Query Isolated Margin Tier Data (USER_DATA)
[**get_margin_leverage_bracket_v1**](MarginTradingApi.md#get_margin_leverage_bracket_v1) | **GET** /sapi/v1/margin/leverageBracket | Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
[**get_margin_max_borrowable_v1**](MarginTradingApi.md#get_margin_max_borrowable_v1) | **GET** /sapi/v1/margin/maxBorrowable | Query Max Borrow (USER_DATA)
[**get_margin_max_transferable_v1**](MarginTradingApi.md#get_margin_max_transferable_v1) | **GET** /sapi/v1/margin/maxTransferable | Query Max Transfer-Out Amount (USER_DATA)
[**get_margin_my_trades_v1**](MarginTradingApi.md#get_margin_my_trades_v1) | **GET** /sapi/v1/margin/myTrades | Query Margin Account&#39;s Trade List (USER_DATA)
[**get_margin_next_hourly_interest_rate_v1**](MarginTradingApi.md#get_margin_next_hourly_interest_rate_v1) | **GET** /sapi/v1/margin/next-hourly-interest-rate | Get future hourly interest rate (USER_DATA)
[**get_margin_open_order_list_v1**](MarginTradingApi.md#get_margin_open_order_list_v1) | **GET** /sapi/v1/margin/openOrderList | Query Margin Account&#39;s Open OCO (USER_DATA)
[**get_margin_open_orders_v1**](MarginTradingApi.md#get_margin_open_orders_v1) | **GET** /sapi/v1/margin/openOrders | Query Margin Account&#39;s Open Orders (USER_DATA)
[**get_margin_order_list_v1**](MarginTradingApi.md#get_margin_order_list_v1) | **GET** /sapi/v1/margin/orderList | Query Margin Account&#39;s OCO (USER_DATA)
[**get_margin_order_v1**](MarginTradingApi.md#get_margin_order_v1) | **GET** /sapi/v1/margin/order | Query Margin Account&#39;s Order (USER_DATA)
[**get_margin_price_index_v1**](MarginTradingApi.md#get_margin_price_index_v1) | **GET** /sapi/v1/margin/priceIndex | Query Margin PriceIndex (MARKET_DATA)
[**get_margin_rate_limit_order_v1**](MarginTradingApi.md#get_margin_rate_limit_order_v1) | **GET** /sapi/v1/margin/rateLimit/order | Query Current Margin Order Count Usage (TRADE)
[**get_margin_trade_coeff_v1**](MarginTradingApi.md#get_margin_trade_coeff_v1) | **GET** /sapi/v1/margin/tradeCoeff | Get Summary of Margin account (USER_DATA)
[**get_margin_transfer_v1**](MarginTradingApi.md#get_margin_transfer_v1) | **GET** /sapi/v1/margin/transfer | Get Cross Margin Transfer History (USER_DATA)
[**update_margin_api_key_ip_v1**](MarginTradingApi.md#update_margin_api_key_ip_v1) | **PUT** /sapi/v1/margin/apiKey/ip | Edit ip for Special Key(Low-Latency Trading)(TRADE)
[**update_margin_listen_key_v1**](MarginTradingApi.md#update_margin_listen_key_v1) | **PUT** /sapi/v1/margin/listen-key | Keepalive User Data Stream (USER_STREAM)
[**update_user_data_stream_isolated_v1**](MarginTradingApi.md#update_user_data_stream_isolated_v1) | **PUT** /sapi/v1/userDataStream/isolated | Keepalive Isolated Margin User Data Stream (USER_STREAM)
[**update_user_data_stream_v1**](MarginTradingApi.md#update_user_data_stream_v1) | **PUT** /sapi/v1/userDataStream | Keepalive Margin User Data Stream (USER_STREAM)


# **create_margin_api_key_v1**
> CreateMarginApiKeyV1Resp create_margin_api_key_v1(api_name, timestamp, ip=ip, permission_mode=permission_mode, public_key=public_key, recv_window=recv_window, symbol=symbol)

Create Special Key(Low-Latency Trading)(TRADE)

**Binance Margin offers low-latency trading through a special key, available exclusively to users with VIP level 4 or higher. **

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_api_key_v1_resp import CreateMarginApiKeyV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    api_name = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip = '' # str |  (optional) (default to '')
    permission_mode = '' # str |  (optional) (default to '')
    public_key = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Create Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.create_margin_api_key_v1(api_name, timestamp, ip=ip, permission_mode=permission_mode, public_key=public_key, recv_window=recv_window, symbol=symbol)
        print("The response of MarginTradingApi->create_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_name** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **ip** | **str**|  | [optional] [default to &#39;&#39;]
 **permission_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **public_key** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMarginApiKeyV1Resp**](CreateMarginApiKeyV1Resp.md)

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

# **create_margin_borrow_repay_v1**
> CreateMarginBorrowRepayV1Resp create_margin_borrow_repay_v1(amount, asset, is_isolated, symbol, timestamp, type, recv_window=recv_window)

Margin account borrow/repay(MARGIN)

Margin account borrow/repay(MARGIN)

### Example


```python
import binance.spot
from binance.spot.models.create_margin_borrow_repay_v1_resp import CreateMarginBorrowRepayV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    is_isolated = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Margin account borrow/repay(MARGIN)
        api_response = api_instance.create_margin_borrow_repay_v1(amount, asset, is_isolated, symbol, timestamp, type, recv_window=recv_window)
        print("The response of MarginTradingApi->create_margin_borrow_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_borrow_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **is_isolated** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMarginBorrowRepayV1Resp**](CreateMarginBorrowRepayV1Resp.md)

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

# **create_margin_exchange_small_liability_v1**
> MarginCreateMarginExchangeSmallLiabilityV1Resp create_margin_exchange_small_liability_v1(asset_names, timestamp, recv_window=recv_window)

Small Liability Exchange (MARGIN)

Small Liability Exchange

### Example


```python
import binance.spot
from binance.spot.models.margin_create_margin_exchange_small_liability_v1_resp import MarginCreateMarginExchangeSmallLiabilityV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    asset_names = ['asset_names_example'] # List[str] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Small Liability Exchange (MARGIN)
        api_response = api_instance.create_margin_exchange_small_liability_v1(asset_names, timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->create_margin_exchange_small_liability_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_exchange_small_liability_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_names** | [**List[str]**](str.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**MarginCreateMarginExchangeSmallLiabilityV1Resp**](MarginCreateMarginExchangeSmallLiabilityV1Resp.md)

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

# **create_margin_isolated_account_v1**
> CreateMarginIsolatedAccountV1Resp create_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)

Enable Isolated Margin Account (TRADE)

Enable isolated margin account for a specific symbol(Only supports activation of previously disabled accounts).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_isolated_account_v1_resp import CreateMarginIsolatedAccountV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Isolated Margin Account (TRADE)
        api_response = api_instance.create_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->create_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMarginIsolatedAccountV1Resp**](CreateMarginIsolatedAccountV1Resp.md)

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

# **create_margin_listen_key_v1**
> CreateMarginListenKeyV1Resp create_margin_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_listen_key_v1_resp import CreateMarginListenKeyV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.create_margin_listen_key_v1()
        print("The response of MarginTradingApi->create_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateMarginListenKeyV1Resp**](CreateMarginListenKeyV1Resp.md)

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

# **create_margin_manual_liquidation_v1**
> CreateMarginManualLiquidationV1Resp create_margin_manual_liquidation_v1(timestamp, type, recv_window=recv_window, symbol=symbol)

Margin Manual Liquidation(MARGIN)

Margin Manual Liquidation

### Example


```python
import binance.spot
from binance.spot.models.create_margin_manual_liquidation_v1_resp import CreateMarginManualLiquidationV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Margin Manual Liquidation(MARGIN)
        api_response = api_instance.create_margin_manual_liquidation_v1(timestamp, type, recv_window=recv_window, symbol=symbol)
        print("The response of MarginTradingApi->create_margin_manual_liquidation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_manual_liquidation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMarginManualLiquidationV1Resp**](CreateMarginManualLiquidationV1Resp.md)

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

# **create_margin_max_leverage_v1**
> CreateMarginMaxLeverageV1Resp create_margin_max_leverage_v1(max_leverage)

Adjust cross margin max leverage (USER_DATA)

Adjust cross margin max leverage

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_max_leverage_v1_resp import CreateMarginMaxLeverageV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    max_leverage = 56 # int | 

    try:
        # Adjust cross margin max leverage (USER_DATA)
        api_response = api_instance.create_margin_max_leverage_v1(max_leverage)
        print("The response of MarginTradingApi->create_margin_max_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_max_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_leverage** | **int**|  | 

### Return type

[**CreateMarginMaxLeverageV1Resp**](CreateMarginMaxLeverageV1Resp.md)

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

# **create_margin_order_oco_v1**
> CreateMarginOrderOcoV1Resp create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)

Margin Account New OCO (TRADE)

Send in a new OCO for a margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_order_oco_v1_resp import CreateMarginOrderOcoV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    stop_price = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    auto_repay_at_cancel = True # bool |  (optional)
    is_isolated = '' # str |  (optional) (default to '')
    limit_client_order_id = '' # str |  (optional) (default to '')
    limit_iceberg_qty = '' # str |  (optional) (default to '')
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    side_effect_type = '' # str |  (optional) (default to '')
    stop_client_order_id = '' # str |  (optional) (default to '')
    stop_iceberg_qty = '' # str |  (optional) (default to '')
    stop_limit_price = '' # str |  (optional) (default to '')
    stop_limit_time_in_force = '' # str |  (optional) (default to '')

    try:
        # Margin Account New OCO (TRADE)
        api_response = api_instance.create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)
        print("The response of MarginTradingApi->create_margin_order_oco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_order_oco_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | **str**|  | [default to &#39;&#39;]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **stop_price** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **auto_repay_at_cancel** | **bool**|  | [optional] 
 **is_isolated** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **side_effect_type** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_price** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMarginOrderOcoV1Resp**](CreateMarginOrderOcoV1Resp.md)

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

# **create_margin_order_oto_v1**
> CreateMarginOrderOtoV1Resp create_margin_order_oto_v1(pending_quantity, pending_side, pending_type, symbol, working_iceberg_qty, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_time_in_force=working_time_in_force)

Margin Account New OTO (TRADE)

Post a new OTO order for margin account:

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_order_oto_v1_resp import CreateMarginOrderOtoV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    pending_quantity = '' # str |  (default to '')
    pending_side = '' # str |  (default to '')
    pending_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    working_iceberg_qty = '' # str |  (default to '')
    working_price = '' # str |  (default to '')
    working_quantity = '' # str |  (default to '')
    working_side = '' # str |  (default to '')
    working_type =  # str |  (default to )
    auto_repay_at_cancel = True # bool |  (optional)
    is_isolated = '' # str |  (optional) (default to '')
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    pending_client_order_id = '' # str |  (optional) (default to '')
    pending_iceberg_qty = '' # str |  (optional) (default to '')
    pending_price = '' # str |  (optional) (default to '')
    pending_stop_price = '' # str |  (optional) (default to '')
    pending_time_in_force = '' # str |  (optional) (default to '')
    pending_trailing_delta = '' # str |  (optional) (default to '')
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    side_effect_type = '' # str |  (optional) (default to '')
    working_client_order_id = '' # str |  (optional) (default to '')
    working_time_in_force = '' # str |  (optional) (default to '')

    try:
        # Margin Account New OTO (TRADE)
        api_response = api_instance.create_margin_order_oto_v1(pending_quantity, pending_side, pending_type, symbol, working_iceberg_qty, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_time_in_force=working_time_in_force)
        print("The response of MarginTradingApi->create_margin_order_oto_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_order_oto_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_quantity** | **str**|  | [default to &#39;&#39;]
 **pending_side** | **str**|  | [default to &#39;&#39;]
 **pending_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **working_iceberg_qty** | **str**|  | [default to &#39;&#39;]
 **working_price** | **str**|  | [default to &#39;&#39;]
 **working_quantity** | **str**|  | [default to &#39;&#39;]
 **working_side** | **str**|  | [default to &#39;&#39;]
 **working_type** | **str**|  | [default to ]
 **auto_repay_at_cancel** | **bool**|  | [optional] 
 **is_isolated** | **str**|  | [optional] [default to &#39;&#39;]
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **side_effect_type** | **str**|  | [optional] [default to &#39;&#39;]
 **working_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **working_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMarginOrderOtoV1Resp**](CreateMarginOrderOtoV1Resp.md)

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

# **create_margin_order_otoco_v1**
> CreateMarginOrderOtocoV1Resp create_margin_order_otoco_v1(pending_above_type, pending_quantity, pending_side, symbol, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_time_in_force=working_time_in_force)

Margin Account New OTOCO (TRADE)

Post a new OTOCO order for margin account：

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_margin_order_otoco_v1_resp import CreateMarginOrderOtocoV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    pending_above_type =  # str |  (default to )
    pending_quantity = '' # str |  (default to '')
    pending_side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    working_price = '' # str |  (default to '')
    working_quantity = '' # str |  (default to '')
    working_side = '' # str |  (default to '')
    working_type =  # str |  (default to )
    auto_repay_at_cancel = True # bool |  (optional)
    is_isolated = '' # str |  (optional) (default to '')
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    pending_above_client_order_id = '' # str |  (optional) (default to '')
    pending_above_iceberg_qty = '' # str |  (optional) (default to '')
    pending_above_price = '' # str |  (optional) (default to '')
    pending_above_stop_price = '' # str |  (optional) (default to '')
    pending_above_time_in_force = '' # str |  (optional) (default to '')
    pending_above_trailing_delta = '' # str |  (optional) (default to '')
    pending_below_client_order_id = '' # str |  (optional) (default to '')
    pending_below_iceberg_qty = '' # str |  (optional) (default to '')
    pending_below_price = '' # str |  (optional) (default to '')
    pending_below_stop_price = '' # str |  (optional) (default to '')
    pending_below_time_in_force = '' # str |  (optional) (default to '')
    pending_below_trailing_delta = '' # str |  (optional) (default to '')
    pending_below_type =  # str |  (optional) (default to )
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    side_effect_type = '' # str |  (optional) (default to '')
    working_client_order_id = '' # str |  (optional) (default to '')
    working_iceberg_qty = '' # str |  (optional) (default to '')
    working_time_in_force = '' # str |  (optional) (default to '')

    try:
        # Margin Account New OTOCO (TRADE)
        api_response = api_instance.create_margin_order_otoco_v1(pending_above_type, pending_quantity, pending_side, symbol, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_time_in_force=working_time_in_force)
        print("The response of MarginTradingApi->create_margin_order_otoco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_order_otoco_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_above_type** | **str**|  | [default to ]
 **pending_quantity** | **str**|  | [default to &#39;&#39;]
 **pending_side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **working_price** | **str**|  | [default to &#39;&#39;]
 **working_quantity** | **str**|  | [default to &#39;&#39;]
 **working_side** | **str**|  | [default to &#39;&#39;]
 **working_type** | **str**|  | [default to ]
 **auto_repay_at_cancel** | **bool**|  | [optional] 
 **is_isolated** | **str**|  | [optional] [default to &#39;&#39;]
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_type** | **str**|  | [optional] [default to ]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **side_effect_type** | **str**|  | [optional] [default to &#39;&#39;]
 **working_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **working_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **working_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateMarginOrderOtocoV1Resp**](CreateMarginOrderOtocoV1Resp.md)

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

# **create_margin_order_v1**
> MarginCreateMarginOrderV1Resp create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, is_isolated=is_isolated, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)

Margin Account New Order (TRADE)

Post a new order for margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.margin_create_margin_order_v1_resp import MarginCreateMarginOrderV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    auto_repay_at_cancel = True # bool |  (optional)
    iceberg_qty = '' # str |  (optional) (default to '')
    is_isolated = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    quote_order_qty = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    side_effect_type = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # Margin Account New Order (TRADE)
        api_response = api_instance.create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, is_isolated=is_isolated, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)
        print("The response of MarginTradingApi->create_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_margin_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **auto_repay_at_cancel** | **bool**|  | [optional] 
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **is_isolated** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **quote_order_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **side_effect_type** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**MarginCreateMarginOrderV1Resp**](MarginCreateMarginOrderV1Resp.md)

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

# **create_user_data_stream_isolated_v1**
> CreateUserDataStreamIsolatedV1Resp create_user_data_stream_isolated_v1(symbol)

Start Isolated Margin User Data Stream (USER_STREAM)

Start a new isolated margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_user_data_stream_isolated_v1_resp import CreateUserDataStreamIsolatedV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Start Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.create_user_data_stream_isolated_v1(symbol)
        print("The response of MarginTradingApi->create_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**CreateUserDataStreamIsolatedV1Resp**](CreateUserDataStreamIsolatedV1Resp.md)

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

# **create_user_data_stream_v1**
> CreateUserDataStreamV1Resp create_user_data_stream_v1()

Start Margin User Data Stream (USER_STREAM)

Start a new margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_user_data_stream_v1_resp import CreateUserDataStreamV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)

    try:
        # Start Margin User Data Stream (USER_STREAM)
        api_response = api_instance.create_user_data_stream_v1()
        print("The response of MarginTradingApi->create_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->create_user_data_stream_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateUserDataStreamV1Resp**](CreateUserDataStreamV1Resp.md)

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

# **delete_margin_api_key_v1**
> object delete_margin_api_key_v1(timestamp, api_key=api_key, api_name=api_name, symbol=symbol, recv_window=recv_window)

Delete Special Key(Low-Latency Trading)(TRADE)

This only applies to Special Key for Low Latency Trading.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    api_key = '' # str |  (optional) (default to '')
    api_name = '' # str |  (optional) (default to '')
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Delete Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.delete_margin_api_key_v1(timestamp, api_key=api_key, api_name=api_name, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->delete_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **api_key** | **str**|  | [optional] [default to &#39;&#39;]
 **api_name** | **str**|  | [optional] [default to &#39;&#39;]
 **symbol** | **str**| isolated margin pair | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

**object**

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

# **delete_margin_isolated_account_v1**
> DeleteMarginIsolatedAccountV1Resp delete_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)

Disable Isolated Margin Account (TRADE)

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24
hours.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_margin_isolated_account_v1_resp import DeleteMarginIsolatedAccountV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Disable Isolated Margin Account (TRADE)
        api_response = api_instance.delete_margin_isolated_account_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->delete_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**DeleteMarginIsolatedAccountV1Resp**](DeleteMarginIsolatedAccountV1Resp.md)

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

# **delete_margin_listen_key_v1**
> object delete_margin_listen_key_v1()

Close User Data Stream (USER_STREAM)

Close out a user data stream.

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
    api_instance = binance.spot.MarginTradingApi(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.delete_margin_listen_key_v1()
        print("The response of MarginTradingApi->delete_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **delete_margin_open_orders_v1**
> List[DeleteMarginOpenOrdersV1RespItem] delete_margin_open_orders_v1(symbol, timestamp, is_isolated=is_isolated, recv_window=recv_window)

Margin Account Cancel all Open Orders on a Symbol (TRADE)

Cancels all active orders on a symbol for margin account.
This includes OCO orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_margin_open_orders_v1_resp_item import DeleteMarginOpenOrdersV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel all Open Orders on a Symbol (TRADE)
        api_response = api_instance.delete_margin_open_orders_v1(symbol, timestamp, is_isolated=is_isolated, recv_window=recv_window)
        print("The response of MarginTradingApi->delete_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[DeleteMarginOpenOrdersV1RespItem]**](DeleteMarginOpenOrdersV1RespItem.md)

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

# **delete_margin_order_list_v1**
> DeleteMarginOrderListV1Resp delete_margin_order_list_v1(symbol, timestamp, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel OCO (TRADE)

Cancel an entire Order List for a margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_margin_order_list_v1_resp import DeleteMarginOrderListV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel OCO (TRADE)
        api_response = api_instance.delete_margin_order_list_v1(symbol, timestamp, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of MarginTradingApi->delete_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] 
 **list_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**DeleteMarginOrderListV1Resp**](DeleteMarginOrderListV1Resp.md)

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

# **delete_margin_order_v1**
> DeleteMarginOrderV1Resp delete_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel Order (TRADE)

Cancel an active order for margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_margin_order_v1_resp import DeleteMarginOrderV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel Order (TRADE)
        api_response = api_instance.delete_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of MarginTradingApi->delete_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_margin_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default. | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**DeleteMarginOrderV1Resp**](DeleteMarginOrderV1Resp.md)

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

# **delete_user_data_stream_isolated_v1**
> object delete_user_data_stream_isolated_v1(symbol, listenkey)

Close Isolated Margin User Data Stream (USER_STREAM)

Close out a isolated margin user data stream.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    listenkey = '' # str |  (default to '')

    try:
        # Close Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.delete_user_data_stream_isolated_v1(symbol, listenkey)
        print("The response of MarginTradingApi->delete_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **listenkey** | **str**|  | [default to &#39;&#39;]

### Return type

**object**

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

# **delete_user_data_stream_v1**
> object delete_user_data_stream_v1(listenkey)

Close Margin User Data Stream (USER_STREAM)

Close out a Margin user data stream.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    listenkey = '' # str |  (default to '')

    try:
        # Close Margin User Data Stream (USER_STREAM)
        api_response = api_instance.delete_user_data_stream_v1(listenkey)
        print("The response of MarginTradingApi->delete_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->delete_user_data_stream_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenkey** | **str**|  | [default to &#39;&#39;]

### Return type

**object**

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

# **get_bnb_burn_v1**
> GetBnbBurnV1Resp get_bnb_burn_v1(timestamp, recv_window=recv_window)

Get BNB Burn Status (USER_DATA)

Get BNB Burn Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_bnb_burn_v1_resp import GetBnbBurnV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Get BNB Burn Status (USER_DATA)
        api_response = api_instance.get_bnb_burn_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_bnb_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_bnb_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**GetBnbBurnV1Resp**](GetBnbBurnV1Resp.md)

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

# **get_margin_account_v1**
> GetMarginAccountV1Resp get_margin_account_v1(timestamp, recv_window=recv_window)

Query Cross Margin Account Details (USER_DATA)

Query Cross Margin Account Details

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_account_v1_resp import GetMarginAccountV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Cross Margin Account Details (USER_DATA)
        api_response = api_instance.get_margin_account_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginAccountV1Resp**](GetMarginAccountV1Resp.md)

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

# **get_margin_all_assets_v1**
> List[GetMarginAllAssetsV1RespItem] get_margin_all_assets_v1(asset=asset)

Get All Margin Assets (MARKET_DATA)

Get All Margin Assets.

### Example


```python
import binance.spot
from binance.spot.models.get_margin_all_assets_v1_resp_item import GetMarginAllAssetsV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    asset = '' # str |  (optional) (default to '')

    try:
        # Get All Margin Assets (MARKET_DATA)
        api_response = api_instance.get_margin_all_assets_v1(asset=asset)
        print("The response of MarginTradingApi->get_margin_all_assets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_all_assets_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetMarginAllAssetsV1RespItem]**](GetMarginAllAssetsV1RespItem.md)

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

# **get_margin_all_order_list_v1**
> List[GetMarginAllOrderListV1RespItem] get_margin_all_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's all OCO (USER_DATA)

Retrieves all OCO for a specific margin account based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_all_order_list_v1_resp_item import GetMarginAllOrderListV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | mandatory for isolated margin, not supported for cross margin (optional) (default to '')
    from_id = 56 # int | If supplied, neither `startTime` or `endTime` can be provided (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 56 # int | Default Value: 500; Max Value: 1000 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's all OCO (USER_DATA)
        api_response = api_instance.get_margin_all_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_all_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_all_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| mandatory for isolated margin, not supported for cross margin | [optional] [default to &#39;&#39;]
 **from_id** | **int**| If supplied, neither &#x60;startTime&#x60; or &#x60;endTime&#x60; can be provided | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default Value: 500; Max Value: 1000 | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginAllOrderListV1RespItem]**](GetMarginAllOrderListV1RespItem.md)

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

# **get_margin_all_orders_v1**
> List[GetMarginAllOrdersV1RespItem] get_margin_all_orders_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's All Orders (USER_DATA)

Query Margin Account's All Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_all_orders_v1_resp_item import GetMarginAllOrdersV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 500. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's All Orders (USER_DATA)
        api_response = api_instance.get_margin_all_orders_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 500. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginAllOrdersV1RespItem]**](GetMarginAllOrdersV1RespItem.md)

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

# **get_margin_all_pairs_v1**
> List[GetMarginAllPairsV1RespItem] get_margin_all_pairs_v1(symbol=symbol)

Get All Cross Margin Pairs (MARKET_DATA)

Get All Cross Margin Pairs

### Example


```python
import binance.spot
from binance.spot.models.get_margin_all_pairs_v1_resp_item import GetMarginAllPairsV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Get All Cross Margin Pairs (MARKET_DATA)
        api_response = api_instance.get_margin_all_pairs_v1(symbol=symbol)
        print("The response of MarginTradingApi->get_margin_all_pairs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_all_pairs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetMarginAllPairsV1RespItem]**](GetMarginAllPairsV1RespItem.md)

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

# **get_margin_api_key_list_v1**
> List[GetMarginApiKeyListV1RespItem] get_margin_api_key_list_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query Special key List(Low Latency Trading)(TRADE)

This only applies to Special Key for Low Latency Trading.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_api_key_list_v1_resp_item import GetMarginApiKeyListV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Special key List(Low Latency Trading)(TRADE)
        api_response = api_instance.get_margin_api_key_list_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_api_key_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_api_key_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| isolated margin pair | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginApiKeyListV1RespItem]**](GetMarginApiKeyListV1RespItem.md)

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

# **get_margin_api_key_v1**
> GetMarginApiKeyV1Resp get_margin_api_key_v1(api_key, timestamp, symbol=symbol, recv_window=recv_window)

Query Special key(Low Latency Trading)(TRADE)

Query Special Key Information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_api_key_v1_resp import GetMarginApiKeyV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Special key(Low Latency Trading)(TRADE)
        api_response = api_instance.get_margin_api_key_v1(api_key, timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **symbol** | **str**| isolated margin pair | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginApiKeyV1Resp**](GetMarginApiKeyV1Resp.md)

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

# **get_margin_available_inventory_v1**
> MarginGetMarginAvailableInventoryV1Resp get_margin_available_inventory_v1(type)

Query Margin Available Inventory(USER_DATA)

Margin available Inventory query

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.margin_get_margin_available_inventory_v1_resp import MarginGetMarginAvailableInventoryV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    type = '' # str | MARGIN,ISOLATED (default to '')

    try:
        # Query Margin Available Inventory(USER_DATA)
        api_response = api_instance.get_margin_available_inventory_v1(type)
        print("The response of MarginTradingApi->get_margin_available_inventory_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_available_inventory_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| MARGIN,ISOLATED | [default to &#39;&#39;]

### Return type

[**MarginGetMarginAvailableInventoryV1Resp**](MarginGetMarginAvailableInventoryV1Resp.md)

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

# **get_margin_borrow_repay_v1**
> GetMarginBorrowRepayV1Resp get_margin_borrow_repay_v1(type, timestamp, asset=asset, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Query borrow/repay records in Margin account(USER_DATA)

Query borrow/repay records in Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_borrow_repay_v1_resp import GetMarginBorrowRepayV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    type = '' # str | `BORROW` or `REPAY` (default to '')
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    isolated_symbol = '' # str | Symbol in Isolated Margin (optional) (default to '')
    tx_id = 56 # int | `tranId` in `POST /sapi/v1/margin/loan` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query borrow/repay records in Margin account(USER_DATA)
        api_response = api_instance.get_margin_borrow_repay_v1(type, timestamp, asset=asset, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_borrow_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_borrow_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &#x60;BORROW&#x60; or &#x60;REPAY&#x60; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **isolated_symbol** | **str**| Symbol in Isolated Margin | [optional] [default to &#39;&#39;]
 **tx_id** | **int**| &#x60;tranId&#x60; in &#x60;POST /sapi/v1/margin/loan&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetMarginBorrowRepayV1Resp**](GetMarginBorrowRepayV1Resp.md)

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

# **get_margin_capital_flow_v1**
> List[GetMarginCapitalFlowV1RespItem] get_margin_capital_flow_v1(timestamp, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Query Cross Isolated Margin Capital Flow (USER_DATA)

Query Cross Isolated Margin Capital Flow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_capital_flow_v1_resp_item import GetMarginCapitalFlowV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    symbol = '' # str | 查询逐仓数据时必填 (optional) (default to '')
    type = '' # str |  (optional) (default to '')
    start_time = 56 # int | 只支持查询最近90天的数据 (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | 如设置fromId, 将返回id &gt; fromId的数据。否则将返回最新数据 (optional)
    limit = 56 # int | 每次返回的数据条数限制。默认 500; 最大 1000. (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Cross Isolated Margin Capital Flow (USER_DATA)
        api_response = api_instance.get_margin_capital_flow_v1(timestamp, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_capital_flow_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_capital_flow_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **symbol** | **str**| 查询逐仓数据时必填 | [optional] [default to &#39;&#39;]
 **type** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| 只支持查询最近90天的数据 | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| 如设置fromId, 将返回id &amp;gt; fromId的数据。否则将返回最新数据 | [optional] 
 **limit** | **int**| 每次返回的数据条数限制。默认 500; 最大 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginCapitalFlowV1RespItem]**](GetMarginCapitalFlowV1RespItem.md)

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

# **get_margin_cross_margin_collateral_ratio_v1**
> List[GetMarginCrossMarginCollateralRatioV1RespItem] get_margin_cross_margin_collateral_ratio_v1()

Cross margin collateral ratio (MARKET_DATA)

Cross margin collateral ratio

### Example


```python
import binance.spot
from binance.spot.models.get_margin_cross_margin_collateral_ratio_v1_resp_item import GetMarginCrossMarginCollateralRatioV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)

    try:
        # Cross margin collateral ratio (MARKET_DATA)
        api_response = api_instance.get_margin_cross_margin_collateral_ratio_v1()
        print("The response of MarginTradingApi->get_margin_cross_margin_collateral_ratio_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_cross_margin_collateral_ratio_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetMarginCrossMarginCollateralRatioV1RespItem]**](GetMarginCrossMarginCollateralRatioV1RespItem.md)

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

# **get_margin_cross_margin_data_v1**
> List[GetMarginCrossMarginDataV1RespItem] get_margin_cross_margin_data_v1(timestamp, vip_level=vip_level, coin=coin, recv_window=recv_window)

Query Cross Margin Fee Data (USER_DATA)

Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_cross_margin_data_v1_resp_item import GetMarginCrossMarginDataV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    vip_level = 56 # int | User&#39;s current specific margin data will be returned if vipLevel is omitted (optional)
    coin = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Cross Margin Fee Data (USER_DATA)
        api_response = api_instance.get_margin_cross_margin_data_v1(timestamp, vip_level=vip_level, coin=coin, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_cross_margin_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_cross_margin_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **vip_level** | **int**| User&amp;#39;s current specific margin data will be returned if vipLevel is omitted | [optional] 
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginCrossMarginDataV1RespItem]**](GetMarginCrossMarginDataV1RespItem.md)

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

# **get_margin_delist_schedule_v1**
> List[GetMarginDelistScheduleV1RespItem] get_margin_delist_schedule_v1(timestamp, recv_window=recv_window)

Get Delist Schedule (MARKET_DATA)

Get tokens or symbols delist schedule for cross margin and isolated margin

### Example


```python
import binance.spot
from binance.spot.models.get_margin_delist_schedule_v1_resp_item import GetMarginDelistScheduleV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Delist Schedule (MARKET_DATA)
        api_response = api_instance.get_margin_delist_schedule_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_delist_schedule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_delist_schedule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetMarginDelistScheduleV1RespItem]**](GetMarginDelistScheduleV1RespItem.md)

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

# **get_margin_exchange_small_liability_history_v1**
> GetMarginExchangeSmallLiabilityHistoryV1Resp get_margin_exchange_small_liability_history_v1(current, size, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)

Get Small Liability Exchange History (USER_DATA)

Get Small liability Exchange History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_exchange_small_liability_history_v1_resp import GetMarginExchangeSmallLiabilityHistoryV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    current = 56 # int | Currently querying page. Start from 1. Default:1
    size = 56 # int | Default:10, Max:100
    timestamp = 56 # int | 
    start_time = 56 # int | Default: 30 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Small Liability Exchange History (USER_DATA)
        api_response = api_instance.get_margin_exchange_small_liability_history_v1(current, size, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_exchange_small_liability_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_exchange_small_liability_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current** | **int**| Currently querying page. Start from 1. Default:1 | 
 **size** | **int**| Default:10, Max:100 | 
 **timestamp** | **int**|  | 
 **start_time** | **int**| Default: 30 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMarginExchangeSmallLiabilityHistoryV1Resp**](GetMarginExchangeSmallLiabilityHistoryV1Resp.md)

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

# **get_margin_exchange_small_liability_v1**
> List[GetMarginExchangeSmallLiabilityV1RespItem] get_margin_exchange_small_liability_v1(timestamp, recv_window=recv_window)

Get Small Liability Exchange Coin List (USER_DATA)

Query the coins which can be small liability exchange

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_exchange_small_liability_v1_resp_item import GetMarginExchangeSmallLiabilityV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Small Liability Exchange Coin List (USER_DATA)
        api_response = api_instance.get_margin_exchange_small_liability_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_exchange_small_liability_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_exchange_small_liability_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetMarginExchangeSmallLiabilityV1RespItem]**](GetMarginExchangeSmallLiabilityV1RespItem.md)

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

# **get_margin_force_liquidation_rec_v1**
> GetMarginForceLiquidationRecV1Resp get_margin_force_liquidation_rec_v1(timestamp, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)

Get Force Liquidation Record (USER_DATA)

Get Force Liquidation Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_force_liquidation_rec_v1_resp import GetMarginForceLiquidationRecV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    isolated_symbol = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Force Liquidation Record (USER_DATA)
        api_response = api_instance.get_margin_force_liquidation_rec_v1(timestamp, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_force_liquidation_rec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_force_liquidation_rec_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **isolated_symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginForceLiquidationRecV1Resp**](GetMarginForceLiquidationRecV1Resp.md)

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

# **get_margin_interest_history_v1**
> GetMarginInterestHistoryV1Resp get_margin_interest_history_v1(timestamp, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Interest History (USER_DATA)

Get Interest History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_interest_history_v1_resp import GetMarginInterestHistoryV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Interest History (USER_DATA)
        api_response = api_instance.get_margin_interest_history_v1(timestamp, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_interest_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginInterestHistoryV1Resp**](GetMarginInterestHistoryV1Resp.md)

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

# **get_margin_interest_rate_history_v1**
> List[GetMarginInterestRateHistoryV1RespItem] get_margin_interest_rate_history_v1(asset, timestamp, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)

Query Margin Interest Rate History (USER_DATA)

Query Margin Interest Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_interest_rate_history_v1_resp_item import GetMarginInterestRateHistoryV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    vip_level = 56 # int | Default: user&#39;s vip level (optional)
    start_time = 56 # int | Default: 7 days ago (optional)
    end_time = 56 # int | Default: present. Maximum range: 1 months. (optional)
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Margin Interest Rate History (USER_DATA)
        api_response = api_instance.get_margin_interest_rate_history_v1(asset, timestamp, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_interest_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_interest_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **vip_level** | **int**| Default: user&amp;#39;s vip level | [optional] 
 **start_time** | **int**| Default: 7 days ago | [optional] 
 **end_time** | **int**| Default: present. Maximum range: 1 months. | [optional] 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**List[GetMarginInterestRateHistoryV1RespItem]**](GetMarginInterestRateHistoryV1RespItem.md)

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

# **get_margin_isolated_account_limit_v1**
> GetMarginIsolatedAccountLimitV1Resp get_margin_isolated_account_limit_v1(timestamp, recv_window=recv_window)

Query Enabled Isolated Margin Account Limit (USER_DATA)

Query enabled isolated margin account limit.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_isolated_account_limit_v1_resp import GetMarginIsolatedAccountLimitV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Enabled Isolated Margin Account Limit (USER_DATA)
        api_response = api_instance.get_margin_isolated_account_limit_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_isolated_account_limit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_isolated_account_limit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**GetMarginIsolatedAccountLimitV1Resp**](GetMarginIsolatedAccountLimitV1Resp.md)

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

# **get_margin_isolated_account_v1**
> GetMarginIsolatedAccountV1Resp get_margin_isolated_account_v1(timestamp, symbols=symbols, recv_window=recv_window)

Query Isolated Margin Account Info (USER_DATA)

Query Isolated Margin Account Info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_isolated_account_v1_resp import GetMarginIsolatedAccountV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    symbols = '' # str | Max 5 symbols can be sent; separated by &#34;,&#34;. e.g. &#34;BTCUSDT,BNBUSDT,ADAUSDT&#34; (optional) (default to '')
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Query Isolated Margin Account Info (USER_DATA)
        api_response = api_instance.get_margin_isolated_account_v1(timestamp, symbols=symbols, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_isolated_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_isolated_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbols** | **str**| Max 5 symbols can be sent; separated by &amp;#34;,&amp;#34;. e.g. &amp;#34;BTCUSDT,BNBUSDT,ADAUSDT&amp;#34; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**GetMarginIsolatedAccountV1Resp**](GetMarginIsolatedAccountV1Resp.md)

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

# **get_margin_isolated_all_pairs_v1**
> List[GetMarginIsolatedAllPairsV1RespItem] get_margin_isolated_all_pairs_v1(timestamp, symbol=symbol, recv_window=recv_window)

Get All Isolated Margin Symbol(MARKET_DATA)

Get All Isolated Margin Symbol

### Example


```python
import binance.spot
from binance.spot.models.get_margin_isolated_all_pairs_v1_resp_item import GetMarginIsolatedAllPairsV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Get All Isolated Margin Symbol(MARKET_DATA)
        api_response = api_instance.get_margin_isolated_all_pairs_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_isolated_all_pairs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_isolated_all_pairs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**List[GetMarginIsolatedAllPairsV1RespItem]**](GetMarginIsolatedAllPairsV1RespItem.md)

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

# **get_margin_isolated_margin_data_v1**
> List[GetMarginIsolatedMarginDataV1RespItem] get_margin_isolated_margin_data_v1(timestamp, vip_level=vip_level, symbol=symbol, recv_window=recv_window)

Query Isolated Margin Fee Data (USER_DATA)

Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_isolated_margin_data_v1_resp_item import GetMarginIsolatedMarginDataV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    vip_level = 56 # int | User&#39;s current specific margin data will be returned if vipLevel is omitted (optional)
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Isolated Margin Fee Data (USER_DATA)
        api_response = api_instance.get_margin_isolated_margin_data_v1(timestamp, vip_level=vip_level, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_isolated_margin_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_isolated_margin_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **vip_level** | **int**| User&amp;#39;s current specific margin data will be returned if vipLevel is omitted | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginIsolatedMarginDataV1RespItem]**](GetMarginIsolatedMarginDataV1RespItem.md)

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

# **get_margin_isolated_margin_tier_v1**
> List[GetMarginIsolatedMarginTierV1RespItem] get_margin_isolated_margin_tier_v1(symbol, timestamp, tier=tier, recv_window=recv_window)

Query Isolated Margin Tier Data (USER_DATA)

Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_isolated_margin_tier_v1_resp_item import GetMarginIsolatedMarginTierV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    tier = 56 # int | All margin tier data will be returned if tier is omitted (optional)
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Isolated Margin Tier Data (USER_DATA)
        api_response = api_instance.get_margin_isolated_margin_tier_v1(symbol, timestamp, tier=tier, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_isolated_margin_tier_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_isolated_margin_tier_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **tier** | **int**| All margin tier data will be returned if tier is omitted | [optional] 
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginIsolatedMarginTierV1RespItem]**](GetMarginIsolatedMarginTierV1RespItem.md)

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

# **get_margin_leverage_bracket_v1**
> List[GetMarginLeverageBracketV1RespItem] get_margin_leverage_bracket_v1()

Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)

Liability Coin Leverage Bracket in Cross Margin Pro Mode

### Example


```python
import binance.spot
from binance.spot.models.get_margin_leverage_bracket_v1_resp_item import GetMarginLeverageBracketV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)

    try:
        # Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
        api_response = api_instance.get_margin_leverage_bracket_v1()
        print("The response of MarginTradingApi->get_margin_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_leverage_bracket_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetMarginLeverageBracketV1RespItem]**](GetMarginLeverageBracketV1RespItem.md)

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

# **get_margin_max_borrowable_v1**
> GetMarginMaxBorrowableV1Resp get_margin_max_borrowable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Borrow (USER_DATA)

Query Max Borrow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_max_borrowable_v1_resp import GetMarginMaxBorrowableV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Max Borrow (USER_DATA)
        api_response = api_instance.get_margin_max_borrowable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_max_borrowable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_max_borrowable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginMaxBorrowableV1Resp**](GetMarginMaxBorrowableV1Resp.md)

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

# **get_margin_max_transferable_v1**
> GetMarginMaxTransferableV1Resp get_margin_max_transferable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Transfer-Out Amount (USER_DATA)

Query Max Transfer-Out Amount

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_max_transferable_v1_resp import GetMarginMaxTransferableV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    isolated_symbol = '' # str | isolated symbol (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Max Transfer-Out Amount (USER_DATA)
        api_response = api_instance.get_margin_max_transferable_v1(asset, timestamp, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_max_transferable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_max_transferable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **isolated_symbol** | **str**| isolated symbol | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginMaxTransferableV1Resp**](GetMarginMaxTransferableV1Resp.md)

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

# **get_margin_my_trades_v1**
> List[GetMarginMyTradesV1RespItem] get_margin_my_trades_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Query Margin Account's Trade List (USER_DATA)

Query Margin Account's Trade List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_my_trades_v1_resp_item import GetMarginMyTradesV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Trade List (USER_DATA)
        api_response = api_instance.get_margin_my_trades_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_my_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_my_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginMyTradesV1RespItem]**](GetMarginMyTradesV1RespItem.md)

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

# **get_margin_next_hourly_interest_rate_v1**
> List[GetMarginNextHourlyInterestRateV1RespItem] get_margin_next_hourly_interest_rate_v1(assets, is_isolated)

Get future hourly interest rate (USER_DATA)

Get future hourly interest rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_next_hourly_interest_rate_v1_resp_item import GetMarginNextHourlyInterestRateV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    assets = '' # str | List of assets, separated by commas, up to 20 (default to '')
    is_isolated = True # bool | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;

    try:
        # Get future hourly interest rate (USER_DATA)
        api_response = api_instance.get_margin_next_hourly_interest_rate_v1(assets, is_isolated)
        print("The response of MarginTradingApi->get_margin_next_hourly_interest_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_next_hourly_interest_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assets** | **str**| List of assets, separated by commas, up to 20 | [default to &#39;&#39;]
 **is_isolated** | **bool**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34; | 

### Return type

[**List[GetMarginNextHourlyInterestRateV1RespItem]**](GetMarginNextHourlyInterestRateV1RespItem.md)

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

# **get_margin_open_order_list_v1**
> List[GetMarginOpenOrderListV1RespItem] get_margin_open_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Margin Account's Open OCO (USER_DATA)

Query Margin Account's Open OCO

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_open_order_list_v1_resp_item import GetMarginOpenOrderListV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | mandatory for isolated margin, not supported for cross margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Open OCO (USER_DATA)
        api_response = api_instance.get_margin_open_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_open_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_open_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| mandatory for isolated margin, not supported for cross margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginOpenOrderListV1RespItem]**](GetMarginOpenOrderListV1RespItem.md)

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

# **get_margin_open_orders_v1**
> List[MarginGetMarginOpenOrdersV1RespItem] get_margin_open_orders_v1(timestamp, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)

Query Margin Account's Open Orders (USER_DATA)

Query Margin Account's Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.margin_get_margin_open_orders_v1_resp_item import MarginGetMarginOpenOrdersV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Open Orders (USER_DATA)
        api_response = api_instance.get_margin_open_orders_v1(timestamp, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginOpenOrdersV1RespItem]**](MarginGetMarginOpenOrdersV1RespItem.md)

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

# **get_margin_order_list_v1**
> GetMarginOrderListV1Resp get_margin_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_order_list_v1_resp import GetMarginOrderListV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | mandatory for isolated margin, not supported for cross margin (optional) (default to '')
    order_list_id = 56 # int | Either `orderListId` or `origClientOrderId` must be provided (optional)
    orig_client_order_id = '' # str | Either `orderListId` or `origClientOrderId` must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's OCO (USER_DATA)
        api_response = api_instance.get_margin_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| mandatory for isolated margin, not supported for cross margin | [optional] [default to &#39;&#39;]
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;origClientOrderId&#x60; must be provided | [optional] 
 **orig_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;origClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginOrderListV1Resp**](GetMarginOrderListV1Resp.md)

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

# **get_margin_order_v1**
> GetMarginOrderV1Resp get_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's Order (USER_DATA)

Query Margin Account's Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_order_v1_resp import GetMarginOrderV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Order (USER_DATA)
        api_response = api_instance.get_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginOrderV1Resp**](GetMarginOrderV1Resp.md)

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

# **get_margin_price_index_v1**
> GetMarginPriceIndexV1Resp get_margin_price_index_v1(symbol)

Query Margin PriceIndex (MARKET_DATA)

Query Margin PriceIndex

### Example


```python
import binance.spot
from binance.spot.models.get_margin_price_index_v1_resp import GetMarginPriceIndexV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Margin PriceIndex (MARKET_DATA)
        api_response = api_instance.get_margin_price_index_v1(symbol)
        print("The response of MarginTradingApi->get_margin_price_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_price_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**GetMarginPriceIndexV1Resp**](GetMarginPriceIndexV1Resp.md)

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

# **get_margin_rate_limit_order_v1**
> List[GetMarginRateLimitOrderV1RespItem] get_margin_rate_limit_order_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Current Margin Order Count Usage (TRADE)

Displays the user's current margin order count usage for all intervals.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_rate_limit_order_v1_resp_item import GetMarginRateLimitOrderV1RespItem
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | isolated symbol, mandatory for isolated margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Current Margin Order Count Usage (TRADE)
        api_response = api_instance.get_margin_rate_limit_order_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| isolated symbol, mandatory for isolated margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMarginRateLimitOrderV1RespItem]**](GetMarginRateLimitOrderV1RespItem.md)

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

# **get_margin_trade_coeff_v1**
> GetMarginTradeCoeffV1Resp get_margin_trade_coeff_v1(timestamp, recv_window=recv_window)

Get Summary of Margin account (USER_DATA)

Get personal margin level information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_trade_coeff_v1_resp import GetMarginTradeCoeffV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Summary of Margin account (USER_DATA)
        api_response = api_instance.get_margin_trade_coeff_v1(timestamp, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_trade_coeff_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_trade_coeff_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMarginTradeCoeffV1Resp**](GetMarginTradeCoeffV1Resp.md)

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

# **get_margin_transfer_v1**
> GetMarginTransferV1Resp get_margin_transfer_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, isolated_symbol=isolated_symbol, recv_window=recv_window)

Get Cross Margin Transfer History (USER_DATA)

Get Cross Margin Transfer History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_margin_transfer_v1_resp import GetMarginTransferV1Resp
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
    api_instance = binance.spot.MarginTradingApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    type = '' # str | Transfer Type: ROLL_IN, ROLL_OUT (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    isolated_symbol = '' # str | Symbol in Isolated Margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Cross Margin Transfer History (USER_DATA)
        api_response = api_instance.get_margin_transfer_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, isolated_symbol=isolated_symbol, recv_window=recv_window)
        print("The response of MarginTradingApi->get_margin_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->get_margin_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **type** | **str**| Transfer Type: ROLL_IN, ROLL_OUT | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **isolated_symbol** | **str**| Symbol in Isolated Margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginTransferV1Resp**](GetMarginTransferV1Resp.md)

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

# **update_margin_api_key_ip_v1**
> object update_margin_api_key_ip_v1(api_key, ip, timestamp, recv_window=recv_window, symbol=symbol)

Edit ip for Special Key(Low-Latency Trading)(TRADE)

Edit ip restriction. This only applies to Special Key for Low Latency Trading.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    api_key = '' # str |  (default to '')
    ip = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Edit ip for Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.update_margin_api_key_ip_v1(api_key, ip, timestamp, recv_window=recv_window, symbol=symbol)
        print("The response of MarginTradingApi->update_margin_api_key_ip_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->update_margin_api_key_ip_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [default to &#39;&#39;]
 **ip** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

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

# **update_margin_listen_key_v1**
> object update_margin_listen_key_v1(listen_key)

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.update_margin_listen_key_v1(listen_key)
        print("The response of MarginTradingApi->update_margin_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->update_margin_listen_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**|  | [default to &#39;&#39;]

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

# **update_user_data_stream_isolated_v1**
> object update_user_data_stream_isolated_v1(listen_key, symbol)

Keepalive Isolated Margin User Data Stream (USER_STREAM)

Keepalive an isolated margin user data stream to prevent a time out.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    listen_key = '' # str |  (default to '')
    symbol = '' # str |  (default to '')

    try:
        # Keepalive Isolated Margin User Data Stream (USER_STREAM)
        api_response = api_instance.update_user_data_stream_isolated_v1(listen_key, symbol)
        print("The response of MarginTradingApi->update_user_data_stream_isolated_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->update_user_data_stream_isolated_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]

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

# **update_user_data_stream_v1**
> object update_user_data_stream_v1(listen_key)

Keepalive Margin User Data Stream (USER_STREAM)

Keepalive a margin user data stream to prevent a time out.

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
    api_instance = binance.spot.MarginTradingApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive Margin User Data Stream (USER_STREAM)
        api_response = api_instance.update_user_data_stream_v1(listen_key)
        print("The response of MarginTradingApi->update_user_data_stream_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginTradingApi->update_user_data_stream_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**|  | [default to &#39;&#39;]

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

