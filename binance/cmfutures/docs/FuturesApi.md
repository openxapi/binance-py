# binance.cmfutures.FuturesApi

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_orders_v1**](FuturesApi.md#create_batch_orders_v1) | **POST** /dapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**create_countdown_cancel_all_v1**](FuturesApi.md#create_countdown_cancel_all_v1) | **POST** /dapi/v1/countdownCancelAll | Auto-Cancel All Open Orders (TRADE)
[**create_leverage_v1**](FuturesApi.md#create_leverage_v1) | **POST** /dapi/v1/leverage | Change Initial Leverage (TRADE)
[**create_listen_key_v1**](FuturesApi.md#create_listen_key_v1) | **POST** /dapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**create_margin_type_v1**](FuturesApi.md#create_margin_type_v1) | **POST** /dapi/v1/marginType | Change Margin Type (TRADE)
[**create_order_v1**](FuturesApi.md#create_order_v1) | **POST** /dapi/v1/order | New Order (TRADE)
[**create_position_margin_v1**](FuturesApi.md#create_position_margin_v1) | **POST** /dapi/v1/positionMargin | Modify Isolated Position Margin(TRADE)
[**create_position_side_dual_v1**](FuturesApi.md#create_position_side_dual_v1) | **POST** /dapi/v1/positionSide/dual | Change Position Mode(TRADE)
[**delete_all_open_orders_v1**](FuturesApi.md#delete_all_open_orders_v1) | **DELETE** /dapi/v1/allOpenOrders | Cancel All Open Orders(TRADE)
[**delete_batch_orders_v1**](FuturesApi.md#delete_batch_orders_v1) | **DELETE** /dapi/v1/batchOrders | Cancel Multiple Orders(TRADE)
[**delete_listen_key_v1**](FuturesApi.md#delete_listen_key_v1) | **DELETE** /dapi/v1/listenKey | Close User Data Stream(USER_STREAM)
[**delete_order_v1**](FuturesApi.md#delete_order_v1) | **DELETE** /dapi/v1/order | Cancel Order (TRADE)
[**get_account_v1**](FuturesApi.md#get_account_v1) | **GET** /dapi/v1/account | Account Information (USER_DATA)
[**get_adl_quantile_v1**](FuturesApi.md#get_adl_quantile_v1) | **GET** /dapi/v1/adlQuantile | Position ADL Quantile Estimation(USER_DATA)
[**get_agg_trades_v1**](FuturesApi.md#get_agg_trades_v1) | **GET** /dapi/v1/aggTrades | Compressed/Aggregate Trades List
[**get_all_orders_v1**](FuturesApi.md#get_all_orders_v1) | **GET** /dapi/v1/allOrders | All Orders (USER_DATA)
[**get_balance_v1**](FuturesApi.md#get_balance_v1) | **GET** /dapi/v1/balance | Futures Account Balance (USER_DATA)
[**get_commission_rate_v1**](FuturesApi.md#get_commission_rate_v1) | **GET** /dapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**get_constituents_v1**](FuturesApi.md#get_constituents_v1) | **GET** /dapi/v1/constituents | Query Index Price Constituents
[**get_continuous_klines_v1**](FuturesApi.md#get_continuous_klines_v1) | **GET** /dapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**get_depth_v1**](FuturesApi.md#get_depth_v1) | **GET** /dapi/v1/depth | Order Book
[**get_exchange_info_v1**](FuturesApi.md#get_exchange_info_v1) | **GET** /dapi/v1/exchangeInfo | Exchange Information
[**get_force_orders_v1**](FuturesApi.md#get_force_orders_v1) | **GET** /dapi/v1/forceOrders | User&#39;s Force Orders(USER_DATA)
[**get_funding_info_v1**](FuturesApi.md#get_funding_info_v1) | **GET** /dapi/v1/fundingInfo | Get Funding Rate Info
[**get_funding_rate_v1**](FuturesApi.md#get_funding_rate_v1) | **GET** /dapi/v1/fundingRate | Get Funding Rate History of Perpetual Futures
[**get_futures_data_basis**](FuturesApi.md#get_futures_data_basis) | **GET** /futures/data/basis | Basis
[**get_futures_data_global_long_short_account_ratio**](FuturesApi.md#get_futures_data_global_long_short_account_ratio) | **GET** /futures/data/globalLongShortAccountRatio | Long/Short Ratio
[**get_futures_data_open_interest_hist**](FuturesApi.md#get_futures_data_open_interest_hist) | **GET** /futures/data/openInterestHist | Open Interest Statistics
[**get_futures_data_taker_buy_sell_vol**](FuturesApi.md#get_futures_data_taker_buy_sell_vol) | **GET** /futures/data/takerBuySellVol | Taker Buy/Sell Volume
[**get_futures_data_top_long_short_account_ratio**](FuturesApi.md#get_futures_data_top_long_short_account_ratio) | **GET** /futures/data/topLongShortAccountRatio | Top Trader Long/Short Ratio (Accounts)
[**get_futures_data_top_long_short_position_ratio**](FuturesApi.md#get_futures_data_top_long_short_position_ratio) | **GET** /futures/data/topLongShortPositionRatio | Top Trader Long/Short Ratio (Positions)
[**get_historical_trades_v1**](FuturesApi.md#get_historical_trades_v1) | **GET** /dapi/v1/historicalTrades | Old Trades Lookup(MARKET_DATA)
[**get_income_asyn_id_v1**](FuturesApi.md#get_income_asyn_id_v1) | **GET** /dapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**get_income_asyn_v1**](FuturesApi.md#get_income_asyn_v1) | **GET** /dapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**get_income_v1**](FuturesApi.md#get_income_v1) | **GET** /dapi/v1/income | Get Income History(USER_DATA)
[**get_index_price_klines_v1**](FuturesApi.md#get_index_price_klines_v1) | **GET** /dapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**get_klines_v1**](FuturesApi.md#get_klines_v1) | **GET** /dapi/v1/klines | Kline/Candlestick Data
[**get_leverage_bracket_v1**](FuturesApi.md#get_leverage_bracket_v1) | **GET** /dapi/v1/leverageBracket | Notional Bracket for Pair(USER_DATA)
[**get_leverage_bracket_v2**](FuturesApi.md#get_leverage_bracket_v2) | **GET** /dapi/v2/leverageBracket | Notional Bracket for Symbol(USER_DATA)
[**get_mark_price_klines_v1**](FuturesApi.md#get_mark_price_klines_v1) | **GET** /dapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**get_open_interest_v1**](FuturesApi.md#get_open_interest_v1) | **GET** /dapi/v1/openInterest | Open Interest
[**get_open_order_v1**](FuturesApi.md#get_open_order_v1) | **GET** /dapi/v1/openOrder | Query Current Open Order(USER_DATA)
[**get_open_orders_v1**](FuturesApi.md#get_open_orders_v1) | **GET** /dapi/v1/openOrders | Current All Open Orders (USER_DATA)
[**get_order_amendment_v1**](FuturesApi.md#get_order_amendment_v1) | **GET** /dapi/v1/orderAmendment | Get Order Modify History (USER_DATA)
[**get_order_asyn_id_v1**](FuturesApi.md#get_order_asyn_id_v1) | **GET** /dapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**get_order_asyn_v1**](FuturesApi.md#get_order_asyn_v1) | **GET** /dapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**get_order_v1**](FuturesApi.md#get_order_v1) | **GET** /dapi/v1/order | Query Order (USER_DATA)
[**get_ping_v1**](FuturesApi.md#get_ping_v1) | **GET** /dapi/v1/ping | Test Connectivity
[**get_pm_account_info_v1**](FuturesApi.md#get_pm_account_info_v1) | **GET** /dapi/v1/pmAccountInfo | Classic Portfolio Margin Account Information (USER_DATA)
[**get_position_margin_history_v1**](FuturesApi.md#get_position_margin_history_v1) | **GET** /dapi/v1/positionMargin/history | Get Position Margin Change History(TRADE)
[**get_position_risk_v1**](FuturesApi.md#get_position_risk_v1) | **GET** /dapi/v1/positionRisk | Position Information(USER_DATA)
[**get_position_side_dual_v1**](FuturesApi.md#get_position_side_dual_v1) | **GET** /dapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**get_premium_index_klines_v1**](FuturesApi.md#get_premium_index_klines_v1) | **GET** /dapi/v1/premiumIndexKlines | Premium index Kline Data
[**get_premium_index_v1**](FuturesApi.md#get_premium_index_v1) | **GET** /dapi/v1/premiumIndex | Index Price and Mark Price
[**get_ticker24hr_v1**](FuturesApi.md#get_ticker24hr_v1) | **GET** /dapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**get_ticker_book_ticker_v1**](FuturesApi.md#get_ticker_book_ticker_v1) | **GET** /dapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**get_ticker_price_v1**](FuturesApi.md#get_ticker_price_v1) | **GET** /dapi/v1/ticker/price | Symbol Price Ticker
[**get_time_v1**](FuturesApi.md#get_time_v1) | **GET** /dapi/v1/time | Check Server time
[**get_trade_asyn_id_v1**](FuturesApi.md#get_trade_asyn_id_v1) | **GET** /dapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**get_trade_asyn_v1**](FuturesApi.md#get_trade_asyn_v1) | **GET** /dapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)
[**get_trades_v1**](FuturesApi.md#get_trades_v1) | **GET** /dapi/v1/trades | Recent Trades List
[**get_user_trades_v1**](FuturesApi.md#get_user_trades_v1) | **GET** /dapi/v1/userTrades | Account Trade List (USER_DATA)
[**update_batch_orders_v1**](FuturesApi.md#update_batch_orders_v1) | **PUT** /dapi/v1/batchOrders | Modify Multiple Orders(TRADE)
[**update_listen_key_v1**](FuturesApi.md#update_listen_key_v1) | **PUT** /dapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)
[**update_order_v1**](FuturesApi.md#update_order_v1) | **PUT** /dapi/v1/order | Modify Order (TRADE)


# **create_batch_orders_v1**
> List[CmfuturesCreateBatchOrdersV1RespInner] create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Place multiple orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_create_batch_order_v1_req_batch_orders_item import CmfuturesCreateBatchOrderV1ReqBatchOrdersItem
from binance.cmfutures.models.cmfutures_create_batch_orders_v1_resp_inner import CmfuturesCreateBatchOrdersV1RespInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    batch_orders = [binance.cmfutures.CmfuturesCreateBatchOrderV1ReqBatchOrdersItem()] # List[CmfuturesCreateBatchOrderV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[CmfuturesCreateBatchOrderV1ReqBatchOrdersItem]**](CmfuturesCreateBatchOrderV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesCreateBatchOrdersV1RespInner]**](CmfuturesCreateBatchOrdersV1RespInner.md)

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

# **create_countdown_cancel_all_v1**
> CreateCountdownCancelAllV1Resp create_countdown_cancel_all_v1(countdown_time, symbol, timestamp, recv_window=recv_window)

Auto-Cancel All Open Orders (TRADE)

Cancel all open orders of the specified symbol at the end of the specified countdown. This rest endpoint means to ensure your open orders are canceled in case of an outage. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and repalced by a new one. The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function. We do not recommend setting the countdown time to be too precise or too small.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_countdown_cancel_all_v1_resp import CreateCountdownCancelAllV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    countdown_time = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Auto-Cancel All Open Orders (TRADE)
        api_response = api_instance.create_countdown_cancel_all_v1(countdown_time, symbol, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_time** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateCountdownCancelAllV1Resp**](CreateCountdownCancelAllV1Resp.md)

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

# **create_leverage_v1**
> CreateLeverageV1Resp create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change Initial Leverage (TRADE)

Change user's initial leverage in the specific symbol market.
For Hedge Mode, LONG and SHORT positions of one symbol use the same initial leverage and share a total notional value.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_leverage_v1_resp import CreateLeverageV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Initial Leverage (TRADE)
        api_response = api_instance.create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->create_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLeverageV1Resp**](CreateLeverageV1Resp.md)

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

# **create_listen_key_v1**
> CreateListenKeyV1Resp create_listen_key_v1()

Start User Data Stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_listen_key_v1_resp import CreateListenKeyV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.create_listen_key_v1()
        print("The response of FuturesApi->create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateListenKeyV1Resp**](CreateListenKeyV1Resp.md)

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

# **create_margin_type_v1**
> CreateMarginTypeV1Resp create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)

Change Margin Type (TRADE)

Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.
With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_margin_type_v1_resp import CreateMarginTypeV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    margin_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Margin Type (TRADE)
        api_response = api_instance.create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->create_margin_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_margin_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMarginTypeV1Resp**](CreateMarginTypeV1Resp.md)

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

# **create_order_v1**
> CreateOrderV1Resp create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New Order (TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_order_v1_resp import CreateOrderV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    price_protect = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')
    working_type = '' # str |  (optional) (default to '')

    try:
        # New Order (TRADE)
        api_response = api_instance.create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of FuturesApi->create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **activation_price** | **str**|  | [optional] [default to &#39;&#39;]
 **callback_rate** | **str**|  | [optional] [default to &#39;&#39;]
 **close_position** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **price_protect** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **working_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateOrderV1Resp**](CreateOrderV1Resp.md)

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

# **create_position_margin_v1**
> CreatePositionMarginV1Resp create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)

Modify Isolated Position Margin(TRADE)

Modify Isolated Position Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_position_margin_v1_resp import CreatePositionMarginV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    amount = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Isolated Position Margin(TRADE)
        api_response = api_instance.create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)
        print("The response of FuturesApi->create_position_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_position_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**|  | 
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePositionMarginV1Resp**](CreatePositionMarginV1Resp.md)

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

# **create_position_side_dual_v1**
> CreatePositionSideDualV1Resp create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.create_position_side_dual_v1_resp import CreatePositionSideDualV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Position Mode(TRADE)
        api_response = api_instance.create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->create_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->create_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreatePositionSideDualV1Resp**](CreatePositionSideDualV1Resp.md)

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

# **delete_all_open_orders_v1**
> DeleteAllOpenOrdersV1Resp delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All Open Orders(TRADE)

Cancel All Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.delete_all_open_orders_v1_resp import DeleteAllOpenOrdersV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Open Orders(TRADE)
        api_response = api_instance.delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteAllOpenOrdersV1Resp**](DeleteAllOpenOrdersV1Resp.md)

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

# **delete_batch_orders_v1**
> List[CmfuturesDeleteBatchOrdersV1RespInner] delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)

Cancel Multiple Orders(TRADE)

Cancel Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_delete_batch_orders_v1_resp_inner import CmfuturesDeleteBatchOrdersV1RespInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id_list = [56] # List[int] | max length 10 <br/> e.g. [1234567,2345678] (optional)
    orig_client_order_id_list = ['orig_client_order_id_list_example'] # List[str] | max length 10<br/> e.g. [&#34;my_id_1&#34;,&#34;my_id_2&#34;], encode the double quotes. No space after comma. (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Orders(TRADE)
        api_response = api_instance.delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)
        print("The response of FuturesApi->delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->delete_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id_list** | [**List[int]**](int.md)| max length 10 &lt;br/&gt; e.g. [1234567,2345678] | [optional] 
 **orig_client_order_id_list** | [**List[str]**](str.md)| max length 10&lt;br/&gt; e.g. [&amp;#34;my_id_1&amp;#34;,&amp;#34;my_id_2&amp;#34;], encode the double quotes. No space after comma. | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesDeleteBatchOrdersV1RespInner]**](CmfuturesDeleteBatchOrdersV1RespInner.md)

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

# **delete_listen_key_v1**
> object delete_listen_key_v1()

Close User Data Stream(USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Close User Data Stream(USER_STREAM)
        api_response = api_instance.delete_listen_key_v1()
        print("The response of FuturesApi->delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->delete_listen_key_v1: %s\n" % e)
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

# **delete_order_v1**
> DeleteOrderV1Resp delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.delete_order_v1_resp import DeleteOrderV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Order (TRADE)
        api_response = api_instance.delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of FuturesApi->delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->delete_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteOrderV1Resp**](DeleteOrderV1Resp.md)

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

# **get_account_v1**
> GetAccountV1Resp get_account_v1(timestamp, recv_window=recv_window)

Account Information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_account_v1_resp import GetAccountV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information (USER_DATA)
        api_response = api_instance.get_account_v1(timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAccountV1Resp**](GetAccountV1Resp.md)

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

# **get_adl_quantile_v1**
> List[GetAdlQuantileV1RespItem] get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

Position ADL Quantile Estimation(USER_DATA)

Query position ADL quantile estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_adl_quantile_v1_resp_item import GetAdlQuantileV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of FuturesApi->get_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetAdlQuantileV1RespItem]**](GetAdlQuantileV1RespItem.md)

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

# **get_agg_trades_v1**
> List[GetAggTradesV1RespItem] get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_agg_trades_v1_resp_item import GetAggTradesV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_agg_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **from_id** | **int**| ID to get aggregate trades from INCLUSIVE. | [optional] 
 **start_time** | **int**| Timestamp in ms to get aggregate trades from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get aggregate trades until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[GetAggTradesV1RespItem]**](GetAggTradesV1RespItem.md)

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

# **get_all_orders_v1**
> List[GetAllOrdersV1RespItem] get_all_orders_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_all_orders_v1_resp_item import GetAllOrdersV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # All Orders (USER_DATA)
        api_response = api_instance.get_all_orders_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of FuturesApi->get_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetAllOrdersV1RespItem]**](GetAllOrdersV1RespItem.md)

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

# **get_balance_v1**
> List[GetBalanceV1RespItem] get_balance_v1(timestamp, recv_window=recv_window)

Futures Account Balance (USER_DATA)

Check futures account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_balance_v1_resp_item import GetBalanceV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance (USER_DATA)
        api_response = api_instance.get_balance_v1(timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBalanceV1RespItem]**](GetBalanceV1RespItem.md)

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

# **get_commission_rate_v1**
> GetCommissionRateV1Resp get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

User Commission Rate (USER_DATA)

Query user commission rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_commission_rate_v1_resp import GetCommissionRateV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetCommissionRateV1Resp**](GetCommissionRateV1Resp.md)

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

# **get_constituents_v1**
> GetConstituentsV1Resp get_constituents_v1(symbol)

Query Index Price Constituents

Query index price constituents

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_constituents_v1_resp import GetConstituentsV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.get_constituents_v1(symbol)
        print("The response of FuturesApi->get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_constituents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**GetConstituentsV1Resp**](GetConstituentsV1Resp.md)

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

# **get_continuous_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_continuous_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **contract_type** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_depth_v1**
> GetDepthV1Resp get_depth_v1(symbol, limit=limit)

Order Book

Query orderbook on specific symbol

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_depth_v1_resp import GetDepthV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.get_depth_v1(symbol, limit=limit)
        print("The response of FuturesApi->get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] | [optional] [default to 500]

### Return type

[**GetDepthV1Resp**](GetDepthV1Resp.md)

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

# **get_exchange_info_v1**
> CmfuturesGetExchangeInfoV1Resp get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_exchange_info_v1_resp import CmfuturesGetExchangeInfoV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.get_exchange_info_v1()
        print("The response of FuturesApi->get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesGetExchangeInfoV1Resp**](CmfuturesGetExchangeInfoV1Resp.md)

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

# **get_force_orders_v1**
> List[CmfuturesGetForceOrdersV1RespItem] get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, recv_window=recv_window, limit=limit, start_time=start_time, end_time=end_time)

User's Force Orders(USER_DATA)

User's Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_force_orders_v1_resp_item import CmfuturesGetForceOrdersV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # User's Force Orders(USER_DATA)
        api_response = api_instance.get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, recv_window=recv_window, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **auto_close_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetForceOrdersV1RespItem]**](CmfuturesGetForceOrdersV1RespItem.md)

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

# **get_funding_info_v1**
> List[GetFundingInfoV1RespItem] get_funding_info_v1()

Get Funding Rate Info

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_funding_info_v1_resp_item import GetFundingInfoV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.get_funding_info_v1()
        print("The response of FuturesApi->get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_funding_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFundingInfoV1RespItem]**](GetFundingInfoV1RespItem.md)

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

# **get_funding_rate_v1**
> List[GetFundingRateV1RespItem] get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History of Perpetual Futures

Get Funding Rate History of Perpetual Futures

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_funding_rate_v1_resp_item import GetFundingRateV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History of Perpetual Futures
        api_response = api_instance.get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding rate from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding rate  until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]

### Return type

[**List[GetFundingRateV1RespItem]**](GetFundingRateV1RespItem.md)

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

# **get_futures_data_basis**
> List[GetFuturesDataBasisRespItem] get_futures_data_basis(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Basis

Query basis

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_basis_resp_item import GetFuturesDataBasisRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Basis
        api_response = api_instance.get_futures_data_basis(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_basis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_basis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataBasisRespItem]**](GetFuturesDataBasisRespItem.md)

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

# **get_futures_data_global_long_short_account_ratio**
> List[GetFuturesDataGlobalLongShortAccountRatioRespItem] get_futures_data_global_long_short_account_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)

Long/Short Ratio

Query symbol Long/Short Ratio

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_global_long_short_account_ratio_resp_item import GetFuturesDataGlobalLongShortAccountRatioRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Long/Short Ratio
        api_response = api_instance.get_futures_data_global_long_short_account_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_global_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_global_long_short_account_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataGlobalLongShortAccountRatioRespItem]**](GetFuturesDataGlobalLongShortAccountRatioRespItem.md)

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

# **get_futures_data_open_interest_hist**
> List[GetFuturesDataOpenInterestHistRespItem] get_futures_data_open_interest_hist(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Open Interest Statistics

Query open interest stats

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_open_interest_hist_resp_item import GetFuturesDataOpenInterestHistRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Open Interest Statistics
        api_response = api_instance.get_futures_data_open_interest_hist(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_open_interest_hist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_open_interest_hist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataOpenInterestHistRespItem]**](GetFuturesDataOpenInterestHistRespItem.md)

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

# **get_futures_data_taker_buy_sell_vol**
> List[GetFuturesDataTakerBuySellVolRespItem] get_futures_data_taker_buy_sell_vol(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Taker Buy/Sell Volume

Taker Buy Volume: the total volume of buy orders filled by takers within the period.
Taker Sell Volume: the total volume of sell orders filled by takers within the period.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_taker_buy_sell_vol_resp_item import GetFuturesDataTakerBuySellVolRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Taker Buy/Sell Volume
        api_response = api_instance.get_futures_data_taker_buy_sell_vol(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_taker_buy_sell_vol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_taker_buy_sell_vol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataTakerBuySellVolRespItem]**](GetFuturesDataTakerBuySellVolRespItem.md)

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

# **get_futures_data_top_long_short_account_ratio**
> List[GetFuturesDataTopLongShortAccountRatioRespItem] get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Accounts)

The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only.
Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions
Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions
Long/Short Ratio (Accounts) = Long Account % / Short Account %

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_top_long_short_account_ratio_resp_item import GetFuturesDataTopLongShortAccountRatioRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Accounts)
        api_response = api_instance.get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_top_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_top_long_short_account_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataTopLongShortAccountRatioRespItem]**](GetFuturesDataTopLongShortAccountRatioRespItem.md)

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

# **get_futures_data_top_long_short_position_ratio**
> List[GetFuturesDataTopLongShortPositionRatioRespItem] get_futures_data_top_long_short_position_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Positions)

The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance.
Long Position % = Long positions of top traders / Total open positions of top traders
Short Position % = Short positions of top traders / Total open positions of top traders
Long/Short Ratio (Positions) = Long Position % / Short Position %

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_futures_data_top_long_short_position_ratio_resp_item import GetFuturesDataTopLongShortPositionRatioRespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Positions)
        api_response = api_instance.get_futures_data_top_long_short_position_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of FuturesApi->get_futures_data_top_long_short_position_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_futures_data_top_long_short_position_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[GetFuturesDataTopLongShortPositionRatioRespItem]**](GetFuturesDataTopLongShortPositionRatioRespItem.md)

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

# **get_historical_trades_v1**
> List[GetHistoricalTradesV1RespItem] get_historical_trades_v1(symbol, limit=limit, from_id=from_id)

Old Trades Lookup(MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_historical_trades_v1_resp_item import GetHistoricalTradesV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup(MARKET_DATA)
        api_response = api_instance.get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of FuturesApi->get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 500. | [optional] [default to 100]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[GetHistoricalTradesV1RespItem]**](GetHistoricalTradesV1RespItem.md)

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

# **get_income_asyn_id_v1**
> GetIncomeAsynIdV1Resp get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Transaction History Download Link by Id (USER_DATA)

Get futures transaction history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_income_asyn_id_v1_resp import GetIncomeAsynIdV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetIncomeAsynIdV1Resp**](GetIncomeAsynIdV1Resp.md)

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

# **get_income_asyn_v1**
> GetIncomeAsynV1Resp get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Transaction History(USER_DATA)

Get download id for futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_income_asyn_v1_resp import GetIncomeAsynV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetIncomeAsynV1Resp**](GetIncomeAsynV1Resp.md)

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

# **get_income_v1**
> List[GetIncomeV1RespItem] get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get Income History(USER_DATA)

Get income history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_income_v1_resp_item import GetIncomeV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | &#34;TRANSFER&#34;,&#34;WELCOME_BONUS&#34;, &#34;FUNDING_FEE&#34;, &#34;REALIZED_PNL&#34;, &#34;COMMISSION&#34;, &#34;INSURANCE_CLEAR&#34;, and &#34;DELIVERED_SETTELMENT&#34; (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    page = 56 # int |  (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History(USER_DATA)
        api_response = api_instance.get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of FuturesApi->get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_income_v1: %s\n" % e)
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

[**List[GetIncomeV1RespItem]**](GetIncomeV1RespItem.md)

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

# **get_index_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_index_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_leverage_bracket_v1**
> List[GetLeverageBracketV1RespItem] get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)

Notional Bracket for Pair(USER_DATA)

Not recommended to continue using this v1 endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_leverage_bracket_v1_resp_item import GetLeverageBracketV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Pair(USER_DATA)
        api_response = api_instance.get_leverage_bracket_v1(timestamp, pair=pair, recv_window=recv_window)
        print("The response of FuturesApi->get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetLeverageBracketV1RespItem]**](GetLeverageBracketV1RespItem.md)

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

# **get_leverage_bracket_v2**
> List[GetLeverageBracketV2RespItem] get_leverage_bracket_v2(timestamp, symbol=symbol, recv_window=recv_window)

Notional Bracket for Symbol(USER_DATA)

Get the symbol's notional bracket list.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_leverage_bracket_v2_resp_item import GetLeverageBracketV2RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional Bracket for Symbol(USER_DATA)
        api_response = api_instance.get_leverage_bracket_v2(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of FuturesApi->get_leverage_bracket_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_leverage_bracket_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetLeverageBracketV2RespItem]**](GetLeverageBracketV2RespItem.md)

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

# **get_mark_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_mark_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_open_interest_v1**
> GetOpenInterestV1Resp get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_open_interest_v1_resp import GetOpenInterestV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.get_open_interest_v1(symbol)
        print("The response of FuturesApi->get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**GetOpenInterestV1Resp**](GetOpenInterestV1Resp.md)

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

# **get_open_order_v1**
> GetOpenOrderV1Resp get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current Open Order(USER_DATA)

Query Current Open Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_open_order_v1_resp import GetOpenOrderV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Order(USER_DATA)
        api_response = api_instance.get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of FuturesApi->get_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_open_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetOpenOrderV1Resp**](GetOpenOrderV1Resp.md)

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

# **get_open_orders_v1**
> List[GetOpenOrdersV1RespItem] get_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)

Current All Open Orders (USER_DATA)

Get all open orders on a symbol. Careful when accessing this with no symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_open_orders_v1_resp_item import GetOpenOrdersV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Current All Open Orders (USER_DATA)
        api_response = api_instance.get_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)
        print("The response of FuturesApi->get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetOpenOrdersV1RespItem]**](GetOpenOrdersV1RespItem.md)

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

# **get_order_amendment_v1**
> List[GetOrderAmendmentV1RespItem] get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Order Modify History (USER_DATA)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_order_amendment_v1_resp_item import GetOrderAmendmentV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get modification history from INCLUSIVE (optional)
    end_time = 56 # int | Timestamp in ms to get modification history until INCLUSIVE (optional)
    limit = 50 # int | Default 50; max 100 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Get Order Modify History (USER_DATA)
        api_response = api_instance.get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of FuturesApi->get_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_order_amendment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get modification history from INCLUSIVE | [optional] 
 **end_time** | **int**| Timestamp in ms to get modification history until INCLUSIVE | [optional] 
 **limit** | **int**| Default 50; max 100 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetOrderAmendmentV1RespItem]**](GetOrderAmendmentV1RespItem.md)

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

# **get_order_asyn_id_v1**
> GetOrderAsynIdV1Resp get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Order History Download Link by Id (USER_DATA)

Get futures order history download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_order_asyn_id_v1_resp import GetOrderAsynIdV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetOrderAsynIdV1Resp**](GetOrderAsynIdV1Resp.md)

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

# **get_order_asyn_v1**
> GetOrderAsynV1Resp get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_order_asyn_v1_resp import GetOrderAsynV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetOrderAsynV1Resp**](GetOrderAsynV1Resp.md)

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

# **get_order_v1**
> GetOrderV1Resp get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_order_v1_resp import GetOrderV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Order (USER_DATA)
        api_response = api_instance.get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of FuturesApi->get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetOrderV1Resp**](GetOrderV1Resp.md)

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

# **get_ping_v1**
> object get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.cmfutures
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.get_ping_v1()
        print("The response of FuturesApi->get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_ping_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **get_pm_account_info_v1**
> GetPmAccountInfoV1Resp get_pm_account_info_v1(asset, recv_window=recv_window)

Classic Portfolio Margin Account Information (USER_DATA)

Get Classic Portfolio Margin current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_pm_account_info_v1_resp import GetPmAccountInfoV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    asset = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Classic Portfolio Margin Account Information (USER_DATA)
        api_response = api_instance.get_pm_account_info_v1(asset, recv_window=recv_window)
        print("The response of FuturesApi->get_pm_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_pm_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPmAccountInfoV1Resp**](GetPmAccountInfoV1Resp.md)

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

# **get_position_margin_history_v1**
> List[GetPositionMarginHistoryV1RespItem] get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Position Margin Change History(TRADE)

Get position margin change history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_position_margin_history_v1_resp_item import GetPositionMarginHistoryV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1: Add position margin,2: Reduce position margin (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default: 50 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Get Position Margin Change History(TRADE)
        api_response = api_instance.get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of FuturesApi->get_position_margin_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_position_margin_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1: Add position margin,2: Reduce position margin | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default: 50 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPositionMarginHistoryV1RespItem]**](GetPositionMarginHistoryV1RespItem.md)

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

# **get_position_risk_v1**
> List[GetPositionRiskV1RespItem] get_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)

Position Information(USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_position_risk_v1_resp_item import GetPositionRiskV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    margin_asset = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information(USER_DATA)
        api_response = api_instance.get_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)
        print("The response of FuturesApi->get_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_position_risk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **margin_asset** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPositionRiskV1RespItem]**](GetPositionRiskV1RespItem.md)

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

# **get_position_side_dual_v1**
> GetPositionSideDualV1Resp get_position_side_dual_v1(timestamp, recv_window=recv_window)

Get Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_position_side_dual_v1_resp import GetPositionSideDualV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetPositionSideDualV1Resp**](GetPositionSideDualV1Resp.md)

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

# **get_premium_index_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of FuturesApi->get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_premium_index_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_premium_index_v1**
> List[GetPremiumIndexV1RespItem] get_premium_index_v1(symbol=symbol, pair=pair)

Index Price and Mark Price

Query index price and mark price

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_premium_index_v1_resp_item import GetPremiumIndexV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Index Price and Mark Price
        api_response = api_instance.get_premium_index_v1(symbol=symbol, pair=pair)
        print("The response of FuturesApi->get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetPremiumIndexV1RespItem]**](GetPremiumIndexV1RespItem.md)

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

# **get_ticker24hr_v1**
> List[GetTicker24hrV1RespItem] get_ticker24hr_v1(symbol=symbol, pair=pair)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_ticker24hr_v1_resp_item import GetTicker24hrV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.get_ticker24hr_v1(symbol=symbol, pair=pair)
        print("The response of FuturesApi->get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetTicker24hrV1RespItem]**](GetTicker24hrV1RespItem.md)

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

# **get_ticker_book_ticker_v1**
> List[GetTickerBookTickerV1RespItem] get_ticker_book_ticker_v1(symbol=symbol, pair=pair)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_ticker_book_ticker_v1_resp_item import GetTickerBookTickerV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.get_ticker_book_ticker_v1(symbol=symbol, pair=pair)
        print("The response of FuturesApi->get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetTickerBookTickerV1RespItem]**](GetTickerBookTickerV1RespItem.md)

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

# **get_ticker_price_v1**
> List[GetTickerPriceV1RespItem] get_ticker_price_v1(symbol=symbol, pair=pair)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_ticker_price_v1_resp_item import GetTickerPriceV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.get_ticker_price_v1(symbol=symbol, pair=pair)
        print("The response of FuturesApi->get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetTickerPriceV1RespItem]**](GetTickerPriceV1RespItem.md)

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

# **get_time_v1**
> GetTimeV1Resp get_time_v1()

Check Server time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_time_v1_resp import GetTimeV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Check Server time
        api_response = api_instance.get_time_v1()
        print("The response of FuturesApi->get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTimeV1Resp**](GetTimeV1Resp.md)

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

# **get_trade_asyn_id_v1**
> GetTradeAsynIdV1Resp get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get Futures Trade Download Link by Id(USER_DATA)

Get futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_trade_asyn_id_v1_resp import GetTradeAsynIdV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetTradeAsynIdV1Resp**](GetTradeAsynIdV1Resp.md)

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

# **get_trade_asyn_v1**
> GetTradeAsynV1Resp get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Trade History (USER_DATA)

Get download id for futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_trade_asyn_v1_resp import GetTradeAsynV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetTradeAsynV1Resp**](GetTradeAsynV1Resp.md)

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

# **get_trades_v1**
> List[GetTradesV1RespItem] get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.cmfutures
from binance.cmfutures.models.get_trades_v1_resp_item import GetTradesV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.get_trades_v1(symbol, limit=limit)
        print("The response of FuturesApi->get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[GetTradesV1RespItem]**](GetTradesV1RespItem.md)

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

# **get_user_trades_v1**
> List[GetUserTradesV1RespItem] get_user_trades_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.get_user_trades_v1_resp_item import GetUserTradesV1RespItem
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 50 # int | Default 50; max 1000 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.get_user_trades_v1(timestamp, symbol=symbol, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of FuturesApi->get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->get_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 50; max 1000 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetUserTradesV1RespItem]**](GetUserTradesV1RespItem.md)

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

# **update_batch_orders_v1**
> List[CmfuturesUpdateBatchOrdersV1RespInner] update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Modify Multiple Orders(TRADE)

Modify Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.cmfutures_update_batch_orders_v1_req_batch_orders_item import CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
from binance.cmfutures.models.cmfutures_update_batch_orders_v1_resp_inner import CmfuturesUpdateBatchOrdersV1RespInner
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    batch_orders = [binance.cmfutures.CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem()] # List[CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Modify Multiple Orders(TRADE)
        api_response = api_instance.update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of FuturesApi->update_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->update_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem]**](CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[CmfuturesUpdateBatchOrdersV1RespInner]**](CmfuturesUpdateBatchOrdersV1RespInner.md)

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

# **update_listen_key_v1**
> object update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.update_listen_key_v1()
        print("The response of FuturesApi->update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->update_listen_key_v1: %s\n" % e)
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

# **update_order_v1**
> UpdateOrderV1Resp update_order_v1(side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window)

Modify Order (TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.cmfutures
from binance.cmfutures.models.update_order_v1_resp import UpdateOrderV1Resp
from binance.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.cmfutures.Configuration(
    auth=binance.cmfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.cmfutures.FuturesApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Order (TRADE)
        api_response = api_instance.update_order_v1(side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window)
        print("The response of FuturesApi->update_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesApi->update_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UpdateOrderV1Resp**](UpdateOrderV1Resp.md)

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

