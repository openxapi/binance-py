# binance.umfutures.UsdsMarginedFuturesApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_orders_v1**](UsdsMarginedFuturesApi.md#create_batch_orders_v1) | **POST** /fapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**create_convert_accept_quote_v1**](UsdsMarginedFuturesApi.md#create_convert_accept_quote_v1) | **POST** /fapi/v1/convert/acceptQuote | Accept the offered quote (USER_DATA)
[**create_convert_get_quote_v1**](UsdsMarginedFuturesApi.md#create_convert_get_quote_v1) | **POST** /fapi/v1/convert/getQuote | Send Quote Request(USER_DATA)
[**create_countdown_cancel_all_v1**](UsdsMarginedFuturesApi.md#create_countdown_cancel_all_v1) | **POST** /fapi/v1/countdownCancelAll | Auto-Cancel All Open Orders (TRADE)
[**create_fee_burn_v1**](UsdsMarginedFuturesApi.md#create_fee_burn_v1) | **POST** /fapi/v1/feeBurn | Toggle BNB Burn On Futures Trade (TRADE)
[**create_leverage_v1**](UsdsMarginedFuturesApi.md#create_leverage_v1) | **POST** /fapi/v1/leverage | Change Initial Leverage(TRADE)
[**create_listen_key_v1**](UsdsMarginedFuturesApi.md#create_listen_key_v1) | **POST** /fapi/v1/listenKey | Start User Data Stream (USER_STREAM)
[**create_margin_type_v1**](UsdsMarginedFuturesApi.md#create_margin_type_v1) | **POST** /fapi/v1/marginType | Change Margin Type(TRADE)
[**create_multi_assets_margin_v1**](UsdsMarginedFuturesApi.md#create_multi_assets_margin_v1) | **POST** /fapi/v1/multiAssetsMargin | Change Multi-Assets Mode (TRADE)
[**create_order_test_v1**](UsdsMarginedFuturesApi.md#create_order_test_v1) | **POST** /fapi/v1/order/test | Test Order(TRADE)
[**create_order_v1**](UsdsMarginedFuturesApi.md#create_order_v1) | **POST** /fapi/v1/order | New Order(TRADE)
[**create_position_margin_v1**](UsdsMarginedFuturesApi.md#create_position_margin_v1) | **POST** /fapi/v1/positionMargin | Modify Isolated Position Margin(TRADE)
[**create_position_side_dual_v1**](UsdsMarginedFuturesApi.md#create_position_side_dual_v1) | **POST** /fapi/v1/positionSide/dual | Change Position Mode(TRADE)
[**delete_all_open_orders_v1**](UsdsMarginedFuturesApi.md#delete_all_open_orders_v1) | **DELETE** /fapi/v1/allOpenOrders | Cancel All Open Orders (TRADE)
[**delete_batch_orders_v1**](UsdsMarginedFuturesApi.md#delete_batch_orders_v1) | **DELETE** /fapi/v1/batchOrders | Cancel Multiple Orders (TRADE)
[**delete_listen_key_v1**](UsdsMarginedFuturesApi.md#delete_listen_key_v1) | **DELETE** /fapi/v1/listenKey | Close User Data Stream (USER_STREAM)
[**delete_order_v1**](UsdsMarginedFuturesApi.md#delete_order_v1) | **DELETE** /fapi/v1/order | Cancel Order (TRADE)
[**get_account_config_v1**](UsdsMarginedFuturesApi.md#get_account_config_v1) | **GET** /fapi/v1/accountConfig | Futures Account Configuration(USER_DATA)
[**get_account_v2**](UsdsMarginedFuturesApi.md#get_account_v2) | **GET** /fapi/v2/account | Account Information V2(USER_DATA)
[**get_account_v3**](UsdsMarginedFuturesApi.md#get_account_v3) | **GET** /fapi/v3/account | Account Information V3(USER_DATA)
[**get_adl_quantile_v1**](UsdsMarginedFuturesApi.md#get_adl_quantile_v1) | **GET** /fapi/v1/adlQuantile | Position ADL Quantile Estimation(USER_DATA)
[**get_agg_trades_v1**](UsdsMarginedFuturesApi.md#get_agg_trades_v1) | **GET** /fapi/v1/aggTrades | Compressed/Aggregate Trades List
[**get_all_orders_v1**](UsdsMarginedFuturesApi.md#get_all_orders_v1) | **GET** /fapi/v1/allOrders | All Orders (USER_DATA)
[**get_api_trading_status_v1**](UsdsMarginedFuturesApi.md#get_api_trading_status_v1) | **GET** /fapi/v1/apiTradingStatus | Futures Trading Quantitative Rules Indicators (USER_DATA)
[**get_asset_index_v1**](UsdsMarginedFuturesApi.md#get_asset_index_v1) | **GET** /fapi/v1/assetIndex | Multi-Assets Mode Asset Index
[**get_balance_v2**](UsdsMarginedFuturesApi.md#get_balance_v2) | **GET** /fapi/v2/balance | Futures Account Balance V2 (USER_DATA)
[**get_balance_v3**](UsdsMarginedFuturesApi.md#get_balance_v3) | **GET** /fapi/v3/balance | Futures Account Balance V3 (USER_DATA)
[**get_commission_rate_v1**](UsdsMarginedFuturesApi.md#get_commission_rate_v1) | **GET** /fapi/v1/commissionRate | User Commission Rate (USER_DATA)
[**get_constituents_v1**](UsdsMarginedFuturesApi.md#get_constituents_v1) | **GET** /fapi/v1/constituents | Query Index Price Constituents
[**get_continuous_klines_v1**](UsdsMarginedFuturesApi.md#get_continuous_klines_v1) | **GET** /fapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**get_convert_exchange_info_v1**](UsdsMarginedFuturesApi.md#get_convert_exchange_info_v1) | **GET** /fapi/v1/convert/exchangeInfo | List All Convert Pairs
[**get_convert_order_status_v1**](UsdsMarginedFuturesApi.md#get_convert_order_status_v1) | **GET** /fapi/v1/convert/orderStatus | Order status(USER_DATA)
[**get_depth_v1**](UsdsMarginedFuturesApi.md#get_depth_v1) | **GET** /fapi/v1/depth | Order Book
[**get_exchange_info_v1**](UsdsMarginedFuturesApi.md#get_exchange_info_v1) | **GET** /fapi/v1/exchangeInfo | Exchange Information
[**get_fee_burn_v1**](UsdsMarginedFuturesApi.md#get_fee_burn_v1) | **GET** /fapi/v1/feeBurn | Get BNB Burn Status (USER_DATA)
[**get_force_orders_v1**](UsdsMarginedFuturesApi.md#get_force_orders_v1) | **GET** /fapi/v1/forceOrders | User&#39;s Force Orders (USER_DATA)
[**get_funding_info_v1**](UsdsMarginedFuturesApi.md#get_funding_info_v1) | **GET** /fapi/v1/fundingInfo | Get Funding Rate Info
[**get_funding_rate_v1**](UsdsMarginedFuturesApi.md#get_funding_rate_v1) | **GET** /fapi/v1/fundingRate | Get Funding Rate History
[**get_futures_data_basis**](UsdsMarginedFuturesApi.md#get_futures_data_basis) | **GET** /futures/data/basis | Basis
[**get_futures_data_delivery_price**](UsdsMarginedFuturesApi.md#get_futures_data_delivery_price) | **GET** /futures/data/delivery-price | Quarterly Contract Settlement Price
[**get_futures_data_global_long_short_account_ratio**](UsdsMarginedFuturesApi.md#get_futures_data_global_long_short_account_ratio) | **GET** /futures/data/globalLongShortAccountRatio | Long/Short Ratio
[**get_futures_data_open_interest_hist**](UsdsMarginedFuturesApi.md#get_futures_data_open_interest_hist) | **GET** /futures/data/openInterestHist | Open Interest Statistics
[**get_futures_data_takerlongshort_ratio**](UsdsMarginedFuturesApi.md#get_futures_data_takerlongshort_ratio) | **GET** /futures/data/takerlongshortRatio | Taker Buy/Sell Volume
[**get_futures_data_top_long_short_account_ratio**](UsdsMarginedFuturesApi.md#get_futures_data_top_long_short_account_ratio) | **GET** /futures/data/topLongShortAccountRatio | Top Trader Long/Short Ratio (Accounts)
[**get_futures_data_top_long_short_position_ratio**](UsdsMarginedFuturesApi.md#get_futures_data_top_long_short_position_ratio) | **GET** /futures/data/topLongShortPositionRatio | Top Trader Long/Short Ratio (Positions)
[**get_historical_trades_v1**](UsdsMarginedFuturesApi.md#get_historical_trades_v1) | **GET** /fapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**get_income_asyn_id_v1**](UsdsMarginedFuturesApi.md#get_income_asyn_id_v1) | **GET** /fapi/v1/income/asyn/id | Get Futures Transaction History Download Link by Id (USER_DATA)
[**get_income_asyn_v1**](UsdsMarginedFuturesApi.md#get_income_asyn_v1) | **GET** /fapi/v1/income/asyn | Get Download Id For Futures Transaction History(USER_DATA)
[**get_index_info_v1**](UsdsMarginedFuturesApi.md#get_index_info_v1) | **GET** /fapi/v1/indexInfo | Composite Index Symbol Information
[**get_index_price_klines_v1**](UsdsMarginedFuturesApi.md#get_index_price_klines_v1) | **GET** /fapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**get_klines_v1**](UsdsMarginedFuturesApi.md#get_klines_v1) | **GET** /fapi/v1/klines | Kline/Candlestick Data
[**get_leverage_bracket_v1**](UsdsMarginedFuturesApi.md#get_leverage_bracket_v1) | **GET** /fapi/v1/leverageBracket | Notional and Leverage Brackets (USER_DATA)
[**get_mark_price_klines_v1**](UsdsMarginedFuturesApi.md#get_mark_price_klines_v1) | **GET** /fapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**get_multi_assets_margin_v1**](UsdsMarginedFuturesApi.md#get_multi_assets_margin_v1) | **GET** /fapi/v1/multiAssetsMargin | Get Current Multi-Assets Mode (USER_DATA)
[**get_open_interest_v1**](UsdsMarginedFuturesApi.md#get_open_interest_v1) | **GET** /fapi/v1/openInterest | Open Interest
[**get_open_order_v1**](UsdsMarginedFuturesApi.md#get_open_order_v1) | **GET** /fapi/v1/openOrder | Query Current Open Order (USER_DATA)
[**get_open_orders_v1**](UsdsMarginedFuturesApi.md#get_open_orders_v1) | **GET** /fapi/v1/openOrders | Current All Open Orders (USER_DATA)
[**get_order_amendment_v1**](UsdsMarginedFuturesApi.md#get_order_amendment_v1) | **GET** /fapi/v1/orderAmendment | Get Order Modify History (USER_DATA)
[**get_order_asyn_id_v1**](UsdsMarginedFuturesApi.md#get_order_asyn_id_v1) | **GET** /fapi/v1/order/asyn/id | Get Futures Order History Download Link by Id (USER_DATA)
[**get_order_asyn_v1**](UsdsMarginedFuturesApi.md#get_order_asyn_v1) | **GET** /fapi/v1/order/asyn | Get Download Id For Futures Order History (USER_DATA)
[**get_order_v1**](UsdsMarginedFuturesApi.md#get_order_v1) | **GET** /fapi/v1/order | Query Order (USER_DATA)
[**get_ping_v1**](UsdsMarginedFuturesApi.md#get_ping_v1) | **GET** /fapi/v1/ping | Test Connectivity
[**get_pm_account_info_v1**](UsdsMarginedFuturesApi.md#get_pm_account_info_v1) | **GET** /fapi/v1/pmAccountInfo | Classic Portfolio Margin Account Information (USER_DATA)
[**get_position_margin_history_v1**](UsdsMarginedFuturesApi.md#get_position_margin_history_v1) | **GET** /fapi/v1/positionMargin/history | Get Position Margin Change History (TRADE)
[**get_position_risk_v2**](UsdsMarginedFuturesApi.md#get_position_risk_v2) | **GET** /fapi/v2/positionRisk | Position Information V2 (USER_DATA)
[**get_position_risk_v3**](UsdsMarginedFuturesApi.md#get_position_risk_v3) | **GET** /fapi/v3/positionRisk | Position Information V3 (USER_DATA)
[**get_position_side_dual_v1**](UsdsMarginedFuturesApi.md#get_position_side_dual_v1) | **GET** /fapi/v1/positionSide/dual | Get Current Position Mode(USER_DATA)
[**get_premium_index_klines_v1**](UsdsMarginedFuturesApi.md#get_premium_index_klines_v1) | **GET** /fapi/v1/premiumIndexKlines | Premium index Kline Data
[**get_premium_index_v1**](UsdsMarginedFuturesApi.md#get_premium_index_v1) | **GET** /fapi/v1/premiumIndex | Mark Price
[**get_rate_limit_order_v1**](UsdsMarginedFuturesApi.md#get_rate_limit_order_v1) | **GET** /fapi/v1/rateLimit/order | Query User Rate Limit (USER_DATA)
[**get_symbol_config_v1**](UsdsMarginedFuturesApi.md#get_symbol_config_v1) | **GET** /fapi/v1/symbolConfig | Symbol Configuration(USER_DATA)
[**get_ticker24hr_v1**](UsdsMarginedFuturesApi.md#get_ticker24hr_v1) | **GET** /fapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**get_ticker_book_ticker_v1**](UsdsMarginedFuturesApi.md#get_ticker_book_ticker_v1) | **GET** /fapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**get_ticker_price_v1**](UsdsMarginedFuturesApi.md#get_ticker_price_v1) | **GET** /fapi/v1/ticker/price | Symbol Price Ticker
[**get_ticker_price_v2**](UsdsMarginedFuturesApi.md#get_ticker_price_v2) | **GET** /fapi/v2/ticker/price | Symbol Price Ticker V2
[**get_time_v1**](UsdsMarginedFuturesApi.md#get_time_v1) | **GET** /fapi/v1/time | Check Server Time
[**get_trade_asyn_id_v1**](UsdsMarginedFuturesApi.md#get_trade_asyn_id_v1) | **GET** /fapi/v1/trade/asyn/id | Get Futures Trade Download Link by Id(USER_DATA)
[**get_trade_asyn_v1**](UsdsMarginedFuturesApi.md#get_trade_asyn_v1) | **GET** /fapi/v1/trade/asyn | Get Download Id For Futures Trade History (USER_DATA)
[**get_trades_v1**](UsdsMarginedFuturesApi.md#get_trades_v1) | **GET** /fapi/v1/trades | Recent Trades List
[**get_user_trades_v1**](UsdsMarginedFuturesApi.md#get_user_trades_v1) | **GET** /fapi/v1/userTrades | Account Trade List (USER_DATA)
[**update_batch_orders_v1**](UsdsMarginedFuturesApi.md#update_batch_orders_v1) | **PUT** /fapi/v1/batchOrders | Modify Multiple Orders(TRADE)
[**update_listen_key_v1**](UsdsMarginedFuturesApi.md#update_listen_key_v1) | **PUT** /fapi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)
[**update_order_v1**](UsdsMarginedFuturesApi.md#update_order_v1) | **PUT** /fapi/v1/order | Modify Order (TRADE)


# **create_batch_orders_v1**
> List[UmfuturesCreateBatchOrdersV1RespInner] create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Place Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_create_batch_orders_v1_req_batch_orders_item import UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem
from binance.umfutures.models.umfutures_create_batch_orders_v1_resp_inner import UmfuturesCreateBatchOrdersV1RespInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    batch_orders = [binance.umfutures.UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem]**](UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesCreateBatchOrdersV1RespInner]**](UmfuturesCreateBatchOrdersV1RespInner.md)

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

# **create_convert_accept_quote_v1**
> CreateConvertAcceptQuoteV1Resp create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)

Accept the offered quote (USER_DATA)

Accept the offered quote by quote ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_convert_accept_quote_v1_resp import CreateConvertAcceptQuoteV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    quote_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Accept the offered quote (USER_DATA)
        api_response = api_instance.create_convert_accept_quote_v1(quote_id, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_convert_accept_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_convert_accept_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateConvertAcceptQuoteV1Resp**](CreateConvertAcceptQuoteV1Resp.md)

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

# **create_convert_get_quote_v1**
> CreateConvertGetQuoteV1Resp create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time)

Send Quote Request(USER_DATA)

Request a quote for the requested token pairs

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_convert_get_quote_v1_resp import CreateConvertGetQuoteV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    from_asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_asset = '' # str |  (default to '')
    from_amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_amount = '' # str |  (optional) (default to '')
    valid_time = '10' # str |  (optional) (default to '10')

    try:
        # Send Quote Request(USER_DATA)
        api_response = api_instance.create_convert_get_quote_v1(from_asset, timestamp, to_asset, from_amount=from_amount, recv_window=recv_window, to_amount=to_amount, valid_time=valid_time)
        print("The response of UsdsMarginedFuturesApi->create_convert_get_quote_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_convert_get_quote_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_asset** | **str**|  | [default to &#39;&#39;]
 **from_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **valid_time** | **str**|  | [optional] [default to &#39;10&#39;]

### Return type

[**CreateConvertGetQuoteV1Resp**](CreateConvertGetQuoteV1Resp.md)

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
> UmfuturesCreateCountdownCancelAllV1Resp create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)

Auto-Cancel All Open Orders (TRADE)

Cancel all open orders of the specified symbol at the end of the specified countdown.
The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req
from binance.umfutures.models.umfutures_create_countdown_cancel_all_v1_resp import UmfuturesCreateCountdownCancelAllV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    umfutures_create_countdown_cancel_all_v1_req = binance.umfutures.UmfuturesCreateCountdownCancelAllV1Req() # UmfuturesCreateCountdownCancelAllV1Req |  (optional)

    try:
        # Auto-Cancel All Open Orders (TRADE)
        api_response = api_instance.create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)
        print("The response of UsdsMarginedFuturesApi->create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_countdown_cancel_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **umfutures_create_countdown_cancel_all_v1_req** | [**UmfuturesCreateCountdownCancelAllV1Req**](UmfuturesCreateCountdownCancelAllV1Req.md)|  | [optional] 

### Return type

[**UmfuturesCreateCountdownCancelAllV1Resp**](UmfuturesCreateCountdownCancelAllV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fee_burn_v1**
> CreateFeeBurnV1Resp create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)

Toggle BNB Burn On Futures Trade (TRADE)

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_fee_burn_v1_resp import CreateFeeBurnV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    fee_burn = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Toggle BNB Burn On Futures Trade (TRADE)
        api_response = api_instance.create_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_burn** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateFeeBurnV1Resp**](CreateFeeBurnV1Resp.md)

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

Change Initial Leverage(TRADE)

Change user's initial leverage of specific symbol market.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_leverage_v1_resp import CreateLeverageV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Initial Leverage(TRADE)
        api_response = api_instance.create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_leverage_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.create_listen_key_v1_resp import CreateListenKeyV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Start User Data Stream (USER_STREAM)
        api_response = api_instance.create_listen_key_v1()
        print("The response of UsdsMarginedFuturesApi->create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_listen_key_v1: %s\n" % e)
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

Change Margin Type(TRADE)

Change symbol level margin type

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_margin_type_v1_resp import CreateMarginTypeV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    margin_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Margin Type(TRADE)
        api_response = api_instance.create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_margin_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_margin_type_v1: %s\n" % e)
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

# **create_multi_assets_margin_v1**
> CreateMultiAssetsMarginV1Resp create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)

Change Multi-Assets Mode (TRADE)

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_multi_assets_margin_v1_resp import CreateMultiAssetsMarginV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    multi_assets_margin = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Multi-Assets Mode (TRADE)
        api_response = api_instance.create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_assets_margin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMultiAssetsMarginV1Resp**](CreateMultiAssetsMarginV1Resp.md)

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

# **create_order_test_v1**
> CreateOrderTestV1Resp create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

Test Order(TRADE)

Testing order request, this order will not be submitted to matching engine

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_order_test_v1_resp import CreateOrderTestV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
    good_till_date = 56 # int |  (optional)
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
        # Test Order(TRADE)
        api_response = api_instance.create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of UsdsMarginedFuturesApi->create_order_test_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_order_test_v1: %s\n" % e)
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
 **good_till_date** | **int**|  | [optional] 
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

[**CreateOrderTestV1Resp**](CreateOrderTestV1Resp.md)

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
> CreateOrderV1Resp create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New Order(TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_order_v1_resp import CreateOrderV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    close_position = '' # str |  (optional) (default to '')
    good_till_date = 56 # int |  (optional)
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
        # New Order(TRADE)
        api_response = api_instance.create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of UsdsMarginedFuturesApi->create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_order_v1: %s\n" % e)
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
 **good_till_date** | **int**|  | [optional] 
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
import binance.umfutures
from binance.umfutures.models.create_position_margin_v1_resp import CreatePositionMarginV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    amount = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Isolated Position Margin(TRADE)
        api_response = api_instance.create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_position_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_position_margin_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.create_position_side_dual_v1_resp import CreatePositionSideDualV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Position Mode(TRADE)
        api_response = api_instance.create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->create_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->create_position_side_dual_v1: %s\n" % e)
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

Cancel All Open Orders (TRADE)

Cancel All Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.delete_all_open_orders_v1_resp import DeleteAllOpenOrdersV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Open Orders (TRADE)
        api_response = api_instance.delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->delete_all_open_orders_v1: %s\n" % e)
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
> List[UmfuturesDeleteBatchOrdersV1RespInner] delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)

Cancel Multiple Orders (TRADE)

Cancel Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_delete_batch_orders_v1_resp_inner import UmfuturesDeleteBatchOrdersV1RespInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id_list = [56] # List[int] | max length 10 <br/> e.g. [1234567,2345678] (optional)
    orig_client_order_id_list = ['orig_client_order_id_list_example'] # List[str] | max length 10<br/> e.g. [&#34;my_id_1&#34;,&#34;my_id_2&#34;], encode the double quotes. No space after comma. (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Orders (TRADE)
        api_response = api_instance.delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->delete_batch_orders_v1: %s\n" % e)
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

[**List[UmfuturesDeleteBatchOrdersV1RespInner]**](UmfuturesDeleteBatchOrdersV1RespInner.md)

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

Close User Data Stream (USER_STREAM)

Close out a user data stream.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Close User Data Stream (USER_STREAM)
        api_response = api_instance.delete_listen_key_v1()
        print("The response of UsdsMarginedFuturesApi->delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->delete_listen_key_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.delete_order_v1_resp import DeleteOrderV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Order (TRADE)
        api_response = api_instance.delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->delete_order_v1: %s\n" % e)
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

# **get_account_config_v1**
> GetAccountConfigV1Resp get_account_config_v1(timestamp, recv_window=recv_window)

Futures Account Configuration(USER_DATA)

Query account configuration

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_account_config_v1_resp import GetAccountConfigV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Configuration(USER_DATA)
        api_response = api_instance.get_account_config_v1(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_account_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_account_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAccountConfigV1Resp**](GetAccountConfigV1Resp.md)

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

# **get_account_v2**
> GetAccountV2Resp get_account_v2(timestamp, recv_window=recv_window)

Account Information V2(USER_DATA)

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_account_v2_resp import GetAccountV2Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information V2(USER_DATA)
        api_response = api_instance.get_account_v2(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAccountV2Resp**](GetAccountV2Resp.md)

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

# **get_account_v3**
> GetAccountV3Resp get_account_v3(timestamp, recv_window=recv_window)

Account Information V3(USER_DATA)

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_account_v3_resp import GetAccountV3Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information V3(USER_DATA)
        api_response = api_instance.get_account_v3(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_account_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_account_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetAccountV3Resp**](GetAccountV3Resp.md)

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

Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_adl_quantile_v1_resp_item import GetAdlQuantileV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_adl_quantile_v1: %s\n" % e)
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
> List[UmfuturesGetAggTradesV1RespItem] get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate market trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_agg_trades_v1_resp_item import UmfuturesGetAggTradesV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_agg_trades_v1: %s\n" % e)
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

[**List[UmfuturesGetAggTradesV1RespItem]**](UmfuturesGetAggTradesV1RespItem.md)

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
> List[GetAllOrdersV1RespItem] get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_all_orders_v1_resp_item import GetAllOrdersV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # All Orders (USER_DATA)
        api_response = api_instance.get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
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

# **get_api_trading_status_v1**
> UmfuturesGetApiTradingStatusV1Resp get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)

Futures Trading Quantitative Rules Indicators (USER_DATA)

Futures trading quantitative rules indicators, for more information on this, please refer to the Futures Trading Quantitative Rules

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_api_trading_status_v1_resp import UmfuturesGetApiTradingStatusV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Futures Trading Quantitative Rules Indicators (USER_DATA)
        api_response = api_instance.get_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetApiTradingStatusV1Resp**](UmfuturesGetApiTradingStatusV1Resp.md)

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

# **get_asset_index_v1**
> UmfuturesGetAssetIndexV1Resp get_asset_index_v1(symbol=symbol)

Multi-Assets Mode Asset Index

asset index for Multi-Assets mode

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_asset_index_v1_resp import UmfuturesGetAssetIndexV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str | Asset pair (optional) (default to '')

    try:
        # Multi-Assets Mode Asset Index
        api_response = api_instance.get_asset_index_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_asset_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_asset_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Asset pair | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetAssetIndexV1Resp**](UmfuturesGetAssetIndexV1Resp.md)

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

# **get_balance_v2**
> List[GetBalanceV2RespItem] get_balance_v2(timestamp, recv_window=recv_window)

Futures Account Balance V2 (USER_DATA)

Query account balance info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_balance_v2_resp_item import GetBalanceV2RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance V2 (USER_DATA)
        api_response = api_instance.get_balance_v2(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_balance_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_balance_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBalanceV2RespItem]**](GetBalanceV2RespItem.md)

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

# **get_balance_v3**
> List[GetBalanceV3RespItem] get_balance_v3(timestamp, recv_window=recv_window)

Futures Account Balance V3 (USER_DATA)

Query account balance info

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_balance_v3_resp_item import GetBalanceV3RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Futures Account Balance V3 (USER_DATA)
        api_response = api_instance.get_balance_v3(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_balance_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_balance_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBalanceV3RespItem]**](GetBalanceV3RespItem.md)

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

Get User Commission Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_commission_rate_v1_resp import GetCommissionRateV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # User Commission Rate (USER_DATA)
        api_response = api_instance.get_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_commission_rate_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_constituents_v1_resp import GetConstituentsV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.get_constituents_v1(symbol)
        print("The response of UsdsMarginedFuturesApi->get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_constituents_v1: %s\n" % e)
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
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_continuous_klines_v1: %s\n" % e)
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

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_convert_exchange_info_v1**
> List[GetConvertExchangeInfoV1RespItem] get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)

List All Convert Pairs

Query for all convertible token pairs and the tokens’ respective upper/lower limits

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_convert_exchange_info_v1_resp_item import GetConvertExchangeInfoV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    from_asset = '' # str | User spends coin (optional) (default to '')
    to_asset = '' # str | User receives coin (optional) (default to '')

    try:
        # List All Convert Pairs
        api_response = api_instance.get_convert_exchange_info_v1(from_asset=from_asset, to_asset=to_asset)
        print("The response of UsdsMarginedFuturesApi->get_convert_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_convert_exchange_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**| User spends coin | [optional] [default to &#39;&#39;]
 **to_asset** | **str**| User receives coin | [optional] [default to &#39;&#39;]

### Return type

[**List[GetConvertExchangeInfoV1RespItem]**](GetConvertExchangeInfoV1RespItem.md)

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

# **get_convert_order_status_v1**
> GetConvertOrderStatusV1Resp get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)

Order status(USER_DATA)

Query order status by order ID.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_convert_order_status_v1_resp import GetConvertOrderStatusV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    order_id = '' # str | Either orderId or quoteId is required (optional) (default to '')
    quote_id = '' # str | Either orderId or quoteId is required (optional) (default to '')

    try:
        # Order status(USER_DATA)
        api_response = api_instance.get_convert_order_status_v1(order_id=order_id, quote_id=quote_id)
        print("The response of UsdsMarginedFuturesApi->get_convert_order_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_convert_order_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]
 **quote_id** | **str**| Either orderId or quoteId is required | [optional] [default to &#39;&#39;]

### Return type

[**GetConvertOrderStatusV1Resp**](GetConvertOrderStatusV1Resp.md)

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

# **get_depth_v1**
> GetDepthV1Resp get_depth_v1(symbol, limit=limit)

Order Book

Query symbol orderbook

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_depth_v1_resp import GetDepthV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.get_depth_v1(symbol, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_depth_v1: %s\n" % e)
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
> UmfuturesGetExchangeInfoV1Resp get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_exchange_info_v1_resp import UmfuturesGetExchangeInfoV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.get_exchange_info_v1()
        print("The response of UsdsMarginedFuturesApi->get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesGetExchangeInfoV1Resp**](UmfuturesGetExchangeInfoV1Resp.md)

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

# **get_fee_burn_v1**
> GetFeeBurnV1Resp get_fee_burn_v1(timestamp, recv_window=recv_window)

Get BNB Burn Status (USER_DATA)

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_fee_burn_v1_resp import GetFeeBurnV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get BNB Burn Status (USER_DATA)
        api_response = api_instance.get_fee_burn_v1(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetFeeBurnV1Resp**](GetFeeBurnV1Resp.md)

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

# **get_force_orders_v1**
> List[GetForceOrdersV1RespItem] get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

User's Force Orders (USER_DATA)

Query user's Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_force_orders_v1_resp_item import GetForceOrdersV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | &#34;LIQUIDATION&#34; for liquidation orders, &#34;ADL&#34; for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # User's Force Orders (USER_DATA)
        api_response = api_instance.get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **auto_close_type** | **str**| &amp;#34;LIQUIDATION&amp;#34; for liquidation orders, &amp;#34;ADL&amp;#34; for ADL orders. | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetForceOrdersV1RespItem]**](GetForceOrdersV1RespItem.md)

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
import binance.umfutures
from binance.umfutures.models.get_funding_info_v1_resp_item import GetFundingInfoV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.get_funding_info_v1()
        print("The response of UsdsMarginedFuturesApi->get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_funding_info_v1: %s\n" % e)
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
> List[GetFundingRateV1RespItem] get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History

Get Funding Rate History

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_funding_rate_v1_resp_item import GetFundingRateV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History
        api_response = api_instance.get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
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
> List[GetFuturesDataBasisRespItem] get_futures_data_basis(pair, contract_type, period, limit, start_time=start_time, end_time=end_time)

Basis

Query future basis

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_futures_data_basis_resp_item import GetFuturesDataBasisRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    pair = '' # str | BTCUSDT (default to '')
    contract_type = '' # str | CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Basis
        api_response = api_instance.get_futures_data_basis(pair, contract_type, period, limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_basis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_basis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSDT | [default to &#39;&#39;]
 **contract_type** | **str**| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [default to 30]
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

# **get_futures_data_delivery_price**
> List[UmfuturesGetFuturesDataDeliveryPriceRespItem] get_futures_data_delivery_price(pair)

Quarterly Contract Settlement Price

Latest price for a symbol or symbols.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_futures_data_delivery_price_resp_item import UmfuturesGetFuturesDataDeliveryPriceRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    pair = '' # str | e.g BTCUSDT (default to '')

    try:
        # Quarterly Contract Settlement Price
        api_response = api_instance.get_futures_data_delivery_price(pair)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_delivery_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_delivery_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| e.g BTCUSDT | [default to &#39;&#39;]

### Return type

[**List[UmfuturesGetFuturesDataDeliveryPriceRespItem]**](UmfuturesGetFuturesDataDeliveryPriceRespItem.md)

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
> List[GetFuturesDataGlobalLongShortAccountRatioRespItem] get_futures_data_global_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Long/Short Ratio

Query symbol Long/Short Ratio

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_futures_data_global_long_short_account_ratio_resp_item import GetFuturesDataGlobalLongShortAccountRatioRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Long/Short Ratio
        api_response = api_instance.get_futures_data_global_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_global_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_global_long_short_account_ratio: %s\n" % e)
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
> List[GetFuturesDataOpenInterestHistRespItem] get_futures_data_open_interest_hist(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Open Interest Statistics

Open Interest Statistics

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_futures_data_open_interest_hist_resp_item import GetFuturesDataOpenInterestHistRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Open Interest Statistics
        api_response = api_instance.get_futures_data_open_interest_hist(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_open_interest_hist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_open_interest_hist: %s\n" % e)
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

# **get_futures_data_takerlongshort_ratio**
> List[GetFuturesDataTakerlongshortRatioRespItem] get_futures_data_takerlongshort_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Taker Buy/Sell Volume

Taker Buy/Sell Volume

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_futures_data_takerlongshort_ratio_resp_item import GetFuturesDataTakerlongshortRatioRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Taker Buy/Sell Volume
        api_response = api_instance.get_futures_data_takerlongshort_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_takerlongshort_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_takerlongshort_ratio: %s\n" % e)
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

[**List[GetFuturesDataTakerlongshortRatioRespItem]**](GetFuturesDataTakerlongshortRatioRespItem.md)

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
import binance.umfutures
from binance.umfutures.models.get_futures_data_top_long_short_account_ratio_resp_item import GetFuturesDataTopLongShortAccountRatioRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Accounts)
        api_response = api_instance.get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_top_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_top_long_short_account_ratio: %s\n" % e)
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
> List[GetFuturesDataTopLongShortPositionRatioRespItem] get_futures_data_top_long_short_position_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Positions)

The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance.
Long Position % = Long positions of top traders / Total open positions of top traders
Short Position % = Short positions of top traders / Total open positions of top traders
Long/Short Ratio (Positions) = Long Position % / Short Position %

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_futures_data_top_long_short_position_ratio_resp_item import GetFuturesDataTopLongShortPositionRatioRespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Positions)
        api_response = api_instance.get_futures_data_top_long_short_position_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of UsdsMarginedFuturesApi->get_futures_data_top_long_short_position_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_futures_data_top_long_short_position_ratio: %s\n" % e)
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

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_historical_trades_v1_resp_item import GetHistoricalTradesV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of UsdsMarginedFuturesApi->get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_historical_trades_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_income_asyn_id_v1_resp import GetIncomeAsynIdV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Transaction History Download Link by Id (USER_DATA)
        api_response = api_instance.get_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_income_asyn_id_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_income_asyn_v1_resp import GetIncomeAsynV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Transaction History(USER_DATA)
        api_response = api_instance.get_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_income_asyn_v1: %s\n" % e)
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

# **get_index_info_v1**
> List[GetIndexInfoV1RespItem] get_index_info_v1(symbol=symbol)

Composite Index Symbol Information

Query composite index symbol information

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_index_info_v1_resp_item import GetIndexInfoV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Composite Index Symbol Information
        api_response = api_instance.get_index_info_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_index_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_index_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetIndexInfoV1RespItem]**](GetIndexInfoV1RespItem.md)

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

# **get_index_price_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair.
Klines are uniquely identified by their open time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_index_price_klines_v1: %s\n" % e)
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

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_klines_v1: %s\n" % e)
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

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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
> UmfuturesGetLeverageBracketV1Resp get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

Notional and Leverage Brackets (USER_DATA)

Query user notional and leverage bracket on speicfic symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Notional and Leverage Brackets (USER_DATA)
        api_response = api_instance.get_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetLeverageBracketV1Resp**](UmfuturesGetLeverageBracketV1Resp.md)

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
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_mark_price_klines_v1: %s\n" % e)
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

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **get_multi_assets_margin_v1**
> GetMultiAssetsMarginV1Resp get_multi_assets_margin_v1(timestamp, recv_window=recv_window)

Get Current Multi-Assets Mode (USER_DATA)

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_multi_assets_margin_v1_resp import GetMultiAssetsMarginV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Multi-Assets Mode (USER_DATA)
        api_response = api_instance.get_multi_assets_margin_v1(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMultiAssetsMarginV1Resp**](GetMultiAssetsMarginV1Resp.md)

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

# **get_open_interest_v1**
> GetOpenInterestV1Resp get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_open_interest_v1_resp import GetOpenInterestV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.get_open_interest_v1(symbol)
        print("The response of UsdsMarginedFuturesApi->get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_open_interest_v1: %s\n" % e)
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

Query Current Open Order (USER_DATA)

Query open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_open_order_v1_resp import GetOpenOrderV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Order (USER_DATA)
        api_response = api_instance.get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_open_order_v1: %s\n" % e)
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
> List[GetOpenOrdersV1RespItem] get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Current All Open Orders (USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_open_orders_v1_resp_item import GetOpenOrdersV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Current All Open Orders (USER_DATA)
        api_response = api_instance.get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
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
import binance.umfutures
from binance.umfutures.models.get_order_amendment_v1_resp_item import GetOrderAmendmentV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
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
        print("The response of UsdsMarginedFuturesApi->get_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_order_amendment_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_order_asyn_id_v1_resp import GetOrderAsynIdV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Order History Download Link by Id (USER_DATA)
        api_response = api_instance.get_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_order_asyn_id_v1: %s\n" % e)
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
> UmfuturesGetOrderAsynV1Resp get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For Futures Order History (USER_DATA)

Get Download Id For Futures Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_order_asyn_v1_resp import UmfuturesGetOrderAsynV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Order History (USER_DATA)
        api_response = api_instance.get_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesGetOrderAsynV1Resp**](UmfuturesGetOrderAsynV1Resp.md)

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
import binance.umfutures
from binance.umfutures.models.get_order_v1_resp import GetOrderV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Order (USER_DATA)
        api_response = api_instance.get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_order_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.get_ping_v1()
        print("The response of UsdsMarginedFuturesApi->get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_ping_v1: %s\n" % e)
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
> GetPmAccountInfoV1Resp get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)

Classic Portfolio Margin Account Information (USER_DATA)

Get Classic Portfolio Margin current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_pm_account_info_v1_resp import GetPmAccountInfoV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Classic Portfolio Margin Account Information (USER_DATA)
        api_response = api_instance.get_pm_account_info_v1(asset, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_pm_account_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_pm_account_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
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

Get Position Margin Change History (TRADE)

Get Position Margin Change History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_position_margin_history_v1_resp_item import GetPositionMarginHistoryV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1: Add position margin，2: Reduce position margin (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int | Default current time if not pass (optional)
    limit = 500 # int | Default: 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Position Margin Change History (TRADE)
        api_response = api_instance.get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_position_margin_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_position_margin_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1: Add position margin，2: Reduce position margin | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**| Default current time if not pass | [optional] 
 **limit** | **int**| Default: 500 | [optional] [default to 500]
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

# **get_position_risk_v2**
> List[GetPositionRiskV2RespItem] get_position_risk_v2(timestamp, symbol=symbol, recv_window=recv_window)

Position Information V2 (USER_DATA)

Get current position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_position_risk_v2_resp_item import GetPositionRiskV2RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information V2 (USER_DATA)
        api_response = api_instance.get_position_risk_v2(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_position_risk_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_position_risk_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPositionRiskV2RespItem]**](GetPositionRiskV2RespItem.md)

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

# **get_position_risk_v3**
> List[GetPositionRiskV3RespItem] get_position_risk_v3(timestamp, symbol=symbol, recv_window=recv_window)

Position Information V3 (USER_DATA)

Get current position information(only symbol that has position or open orders will be returned).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_position_risk_v3_resp_item import GetPositionRiskV3RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information V3 (USER_DATA)
        api_response = api_instance.get_position_risk_v3(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_position_risk_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_position_risk_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetPositionRiskV3RespItem]**](GetPositionRiskV3RespItem.md)

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
import binance.umfutures
from binance.umfutures.models.get_position_side_dual_v1_resp import GetPositionSideDualV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Current Position Mode(USER_DATA)
        api_response = api_instance.get_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_position_side_dual_v1: %s\n" % e)
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
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_premium_index_klines_v1: %s\n" % e)
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

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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
> UmfuturesGetPremiumIndexV1Resp get_premium_index_v1(symbol=symbol)

Mark Price

Mark Price and Funding Rate

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_premium_index_v1_resp import UmfuturesGetPremiumIndexV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Mark Price
        api_response = api_instance.get_premium_index_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetPremiumIndexV1Resp**](UmfuturesGetPremiumIndexV1Resp.md)

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

# **get_rate_limit_order_v1**
> List[GetRateLimitOrderV1RespItem] get_rate_limit_order_v1(timestamp, recv_window=recv_window)

Query User Rate Limit (USER_DATA)

Query User Rate Limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_rate_limit_order_v1_resp_item import GetRateLimitOrderV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query User Rate Limit (USER_DATA)
        api_response = api_instance.get_rate_limit_order_v1(timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetRateLimitOrderV1RespItem]**](GetRateLimitOrderV1RespItem.md)

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

# **get_symbol_config_v1**
> List[GetSymbolConfigV1RespItem] get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)

Symbol Configuration(USER_DATA)

Get current account symbol configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_symbol_config_v1_resp_item import GetSymbolConfigV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Symbol Configuration(USER_DATA)
        api_response = api_instance.get_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_symbol_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_symbol_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetSymbolConfigV1RespItem]**](GetSymbolConfigV1RespItem.md)

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

# **get_ticker24hr_v1**
> UmfuturesGetTicker24hrV1Resp get_ticker24hr_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.
Careful when accessing this with no symbol.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_ticker24hr_v1_resp import UmfuturesGetTicker24hrV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.get_ticker24hr_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTicker24hrV1Resp**](UmfuturesGetTicker24hrV1Resp.md)

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
> UmfuturesGetTickerBookTickerV1Resp get_ticker_book_ticker_v1(symbol=symbol)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp import UmfuturesGetTickerBookTickerV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.get_ticker_book_ticker_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerBookTickerV1Resp**](UmfuturesGetTickerBookTickerV1Resp.md)

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
> UmfuturesGetTickerPriceV1Resp get_ticker_price_v1(symbol=symbol)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_ticker_price_v1_resp import UmfuturesGetTickerPriceV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.get_ticker_price_v1(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerPriceV1Resp**](UmfuturesGetTickerPriceV1Resp.md)

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

# **get_ticker_price_v2**
> UmfuturesGetTickerPriceV2Resp get_ticker_price_v2(symbol=symbol)

Symbol Price Ticker V2

Latest price for a symbol or symbols.

### Example


```python
import binance.umfutures
from binance.umfutures.models.umfutures_get_ticker_price_v2_resp import UmfuturesGetTickerPriceV2Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker V2
        api_response = api_instance.get_ticker_price_v2(symbol=symbol)
        print("The response of UsdsMarginedFuturesApi->get_ticker_price_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_ticker_price_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerPriceV2Resp**](UmfuturesGetTickerPriceV2Resp.md)

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

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.umfutures
from binance.umfutures.models.get_time_v1_resp import GetTimeV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Check Server Time
        api_response = api_instance.get_time_v1()
        print("The response of UsdsMarginedFuturesApi->get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_time_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_trade_asyn_id_v1_resp import GetTradeAsynIdV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.get_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_trade_asyn_id_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_trade_asyn_v1_resp import GetTradeAsynV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For Futures Trade History (USER_DATA)
        api_response = api_instance.get_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_trade_asyn_v1: %s\n" % e)
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
import binance.umfutures
from binance.umfutures.models.get_trades_v1_resp_item import GetTradesV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.get_trades_v1(symbol, limit=limit)
        print("The response of UsdsMarginedFuturesApi->get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_trades_v1: %s\n" % e)
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
> List[GetUserTradesV1RespItem] get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_user_trades_v1_resp_item import GetUserTradesV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | This can only be used in combination with `symbol` (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Account Trade List (USER_DATA)
        api_response = api_instance.get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->get_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| This can only be used in combination with &#x60;symbol&#x60; | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
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
> List[UmfuturesUpdateBatchOrdersV1RespItem] update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Modify Multiple Orders(TRADE)

Modify Multiple Orders (TRADE)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.umfutures_update_batch_orders_v1_req_batch_orders_item import UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
from binance.umfutures.models.umfutures_update_batch_orders_v1_resp_item import UmfuturesUpdateBatchOrdersV1RespItem
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    batch_orders = [binance.umfutures.UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Modify Multiple Orders(TRADE)
        api_response = api_instance.update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->update_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->update_batch_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_orders** | [**List[UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem]**](UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem.md)|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesUpdateBatchOrdersV1RespItem]**](UmfuturesUpdateBatchOrdersV1RespItem.md)

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
> UpdateListenKeyV1Resp update_listen_key_v1()

Keepalive User Data Stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.update_listen_key_v1_resp import UpdateListenKeyV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.update_listen_key_v1()
        print("The response of UsdsMarginedFuturesApi->update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->update_listen_key_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UpdateListenKeyV1Resp**](UpdateListenKeyV1Resp.md)

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
> UpdateOrderV1Resp update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify Order (TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.update_order_v1_resp import UpdateOrderV1Resp
from binance.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.umfutures.Configuration(
    auth=binance.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.umfutures.UsdsMarginedFuturesApi(api_client)
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Order (TRADE)
        api_response = api_instance.update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of UsdsMarginedFuturesApi->update_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsdsMarginedFuturesApi->update_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | **str**|  | [default to &#39;&#39;]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
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

