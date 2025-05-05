# binance.spot.SpotTradingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_cancel_replace_v3**](SpotTradingApi.md#create_order_cancel_replace_v3) | **POST** /api/v3/order/cancelReplace | Cancel an Existing Order and Send a New Order (TRADE)
[**create_order_list_oco_v3**](SpotTradingApi.md#create_order_list_oco_v3) | **POST** /api/v3/orderList/oco | New Order list - OCO (TRADE)
[**create_order_list_oto_v3**](SpotTradingApi.md#create_order_list_oto_v3) | **POST** /api/v3/orderList/oto | New Order list - OTO (TRADE)
[**create_order_list_otoco_v3**](SpotTradingApi.md#create_order_list_otoco_v3) | **POST** /api/v3/orderList/otoco | New Order list - OTOCO (TRADE)
[**create_order_oco_v3**](SpotTradingApi.md#create_order_oco_v3) | **POST** /api/v3/order/oco | New OCO - Deprecated (TRADE)
[**create_order_test_v3**](SpotTradingApi.md#create_order_test_v3) | **POST** /api/v3/order/test | Test new order (TRADE)
[**create_order_v3**](SpotTradingApi.md#create_order_v3) | **POST** /api/v3/order | New order (TRADE)
[**create_sor_order_test_v3**](SpotTradingApi.md#create_sor_order_test_v3) | **POST** /api/v3/sor/order/test | Test new order using SOR (TRADE)
[**create_sor_order_v3**](SpotTradingApi.md#create_sor_order_v3) | **POST** /api/v3/sor/order | New order using SOR (TRADE)
[**create_user_data_stream_v3**](SpotTradingApi.md#create_user_data_stream_v3) | **POST** /api/v3/userDataStream | Start user data stream (USER_STREAM)
[**delete_open_orders_v3**](SpotTradingApi.md#delete_open_orders_v3) | **DELETE** /api/v3/openOrders | Cancel All Open Orders on a Symbol (TRADE)
[**delete_order_list_v3**](SpotTradingApi.md#delete_order_list_v3) | **DELETE** /api/v3/orderList | Cancel Order list (TRADE)
[**delete_order_v3**](SpotTradingApi.md#delete_order_v3) | **DELETE** /api/v3/order | Cancel order (TRADE)
[**delete_user_data_stream_v3**](SpotTradingApi.md#delete_user_data_stream_v3) | **DELETE** /api/v3/userDataStream | Close user data stream (USER_STREAM)
[**get_account_commission_v3**](SpotTradingApi.md#get_account_commission_v3) | **GET** /api/v3/account/commission | Query Commission Rates (USER_DATA)
[**get_account_v3**](SpotTradingApi.md#get_account_v3) | **GET** /api/v3/account | Account information (USER_DATA)
[**get_agg_trades_v3**](SpotTradingApi.md#get_agg_trades_v3) | **GET** /api/v3/aggTrades | Compressed/Aggregate trades list
[**get_all_order_list_v3**](SpotTradingApi.md#get_all_order_list_v3) | **GET** /api/v3/allOrderList | Query all Order lists (USER_DATA)
[**get_all_orders_v3**](SpotTradingApi.md#get_all_orders_v3) | **GET** /api/v3/allOrders | All orders (USER_DATA)
[**get_avg_price_v3**](SpotTradingApi.md#get_avg_price_v3) | **GET** /api/v3/avgPrice | Current average price
[**get_depth_v3**](SpotTradingApi.md#get_depth_v3) | **GET** /api/v3/depth | Order book
[**get_exchange_info_v3**](SpotTradingApi.md#get_exchange_info_v3) | **GET** /api/v3/exchangeInfo | Exchange information
[**get_historical_trades_v3**](SpotTradingApi.md#get_historical_trades_v3) | **GET** /api/v3/historicalTrades | Old trade lookup
[**get_klines_v3**](SpotTradingApi.md#get_klines_v3) | **GET** /api/v3/klines | Kline/Candlestick data
[**get_my_allocations_v3**](SpotTradingApi.md#get_my_allocations_v3) | **GET** /api/v3/myAllocations | Query Allocations (USER_DATA)
[**get_my_prevented_matches_v3**](SpotTradingApi.md#get_my_prevented_matches_v3) | **GET** /api/v3/myPreventedMatches | Query Prevented Matches (USER_DATA)
[**get_my_trades_v3**](SpotTradingApi.md#get_my_trades_v3) | **GET** /api/v3/myTrades | Account trade list (USER_DATA)
[**get_open_order_list_v3**](SpotTradingApi.md#get_open_order_list_v3) | **GET** /api/v3/openOrderList | Query Open Order lists (USER_DATA)
[**get_open_orders_v3**](SpotTradingApi.md#get_open_orders_v3) | **GET** /api/v3/openOrders | Current open orders (USER_DATA)
[**get_order_list_v3**](SpotTradingApi.md#get_order_list_v3) | **GET** /api/v3/orderList | Query Order list (USER_DATA)
[**get_order_v3**](SpotTradingApi.md#get_order_v3) | **GET** /api/v3/order | Query order (USER_DATA)
[**get_ping_v3**](SpotTradingApi.md#get_ping_v3) | **GET** /api/v3/ping | Test connectivity
[**get_rate_limit_order_v3**](SpotTradingApi.md#get_rate_limit_order_v3) | **GET** /api/v3/rateLimit/order | Query Unfilled Order Count (USER_DATA)
[**get_ticker24hr_v3**](SpotTradingApi.md#get_ticker24hr_v3) | **GET** /api/v3/ticker/24hr | 24hr ticker price change statistics
[**get_ticker_book_ticker_v3**](SpotTradingApi.md#get_ticker_book_ticker_v3) | **GET** /api/v3/ticker/bookTicker | Symbol order book ticker
[**get_ticker_price_v3**](SpotTradingApi.md#get_ticker_price_v3) | **GET** /api/v3/ticker/price | Symbol price ticker
[**get_ticker_trading_day_v3**](SpotTradingApi.md#get_ticker_trading_day_v3) | **GET** /api/v3/ticker/tradingDay | Trading Day Ticker
[**get_ticker_v3**](SpotTradingApi.md#get_ticker_v3) | **GET** /api/v3/ticker | Rolling window price change statistics
[**get_time_v3**](SpotTradingApi.md#get_time_v3) | **GET** /api/v3/time | Check server time
[**get_trades_v3**](SpotTradingApi.md#get_trades_v3) | **GET** /api/v3/trades | Recent trades list
[**get_ui_klines_v3**](SpotTradingApi.md#get_ui_klines_v3) | **GET** /api/v3/uiKlines | UIKlines
[**update_user_data_stream_v3**](SpotTradingApi.md#update_user_data_stream_v3) | **PUT** /api/v3/userDataStream | Keepalive user data stream (USER_STREAM)


# **create_order_cancel_replace_v3**
> SpotCreateOrderCancelReplaceV3Resp create_order_cancel_replace_v3(cancel_replace_mode, side, symbol, timestamp, type, cancel_new_client_order_id=cancel_new_client_order_id, cancel_order_id=cancel_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_restrictions=cancel_restrictions, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

Cancel an Existing Order and Send a New Order (TRADE)

Cancels an existing order and places a new order on the same symbol.
Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.
A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED ), will still increase the order count by 1.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_order_cancel_replace_v3_resp import SpotCreateOrderCancelReplaceV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    cancel_replace_mode = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    cancel_new_client_order_id = '' # str |  (optional) (default to '')
    cancel_order_id = 56 # int |  (optional)
    cancel_orig_client_order_id = '' # str |  (optional) (default to '')
    cancel_restrictions = '' # str |  (optional) (default to '')
    iceberg_qty = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    order_rate_limit_exceeded_mode = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    quote_order_qty = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    strategy_type = 56 # int |  (optional)
    time_in_force = '' # str |  (optional) (default to '')
    trailing_delta = 56 # int |  (optional)

    try:
        # Cancel an Existing Order and Send a New Order (TRADE)
        api_response = api_instance.create_order_cancel_replace_v3(cancel_replace_mode, side, symbol, timestamp, type, cancel_new_client_order_id=cancel_new_client_order_id, cancel_order_id=cancel_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_restrictions=cancel_restrictions, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of SpotTradingApi->create_order_cancel_replace_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_cancel_replace_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_replace_mode** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **cancel_new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **cancel_order_id** | **int**|  | [optional] 
 **cancel_orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **cancel_restrictions** | **str**|  | [optional] [default to &#39;&#39;]
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **order_rate_limit_exceeded_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **quote_order_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**|  | [optional] 
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **trailing_delta** | **int**|  | [optional] 

### Return type

[**SpotCreateOrderCancelReplaceV3Resp**](SpotCreateOrderCancelReplaceV3Resp.md)

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

# **create_order_list_oco_v3**
> CreateOrderListOcoV3Resp create_order_list_oco_v3(above_type, below_type, quantity, side, symbol, timestamp, above_client_order_id=above_client_order_id, above_iceberg_qty=above_iceberg_qty, above_price=above_price, above_stop_price=above_stop_price, above_strategy_id=above_strategy_id, above_strategy_type=above_strategy_type, above_time_in_force=above_time_in_force, above_trailing_delta=above_trailing_delta, below_client_order_id=below_client_order_id, below_iceberg_qty=below_iceberg_qty, below_price=below_price, below_stop_price=below_stop_price, below_strategy_id=below_strategy_id, below_strategy_type=below_strategy_type, below_time_in_force=below_time_in_force, below_trailing_delta=below_trailing_delta, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode)

New Order list - OCO (TRADE)

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.
- An OCO has 2 orders called the above order and below order.
- One of the orders must be a LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT order and the other must be STOP_LOSS or STOP_LOSS_LIMIT order.
- Price restrictions

If the OCO is on the SELL side:

LIMIT_MAKER/TAKE_PROFIT_LIMIT price > Last Traded Price >  STOP_LOSS/STOP_LOSS_LIMIT stopPrice
TAKE_PROFIT stopPrice > Last Traded Price > STOP_LOSS/STOP_LOSS_LIMIT stopPrice


If the OCO is on the BUY side:

LIMIT_MAKER/TAKE_PROFIT_LIMIT price < Last Traded Price < stopPrice
TAKE_PROFIT stopPrice < Last Traded Price < STOP_LOSS/STOP_LOSS_LIMIT stopPrice
- OCOs add 2 orders to the unfilled order count, EXCHANGE_MAX_ORDERS filter, and the MAX_NUM_ORDERS filter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_order_list_oco_v3_resp import CreateOrderListOcoV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    above_type =  # str |  (default to )
    below_type =  # str |  (default to )
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    above_client_order_id = '' # str |  (optional) (default to '')
    above_iceberg_qty = 56 # int |  (optional)
    above_price = '' # str |  (optional) (default to '')
    above_stop_price = '' # str |  (optional) (default to '')
    above_strategy_id = 56 # int |  (optional)
    above_strategy_type = 56 # int |  (optional)
    above_time_in_force = '' # str |  (optional) (default to '')
    above_trailing_delta = 56 # int |  (optional)
    below_client_order_id = '' # str |  (optional) (default to '')
    below_iceberg_qty = 56 # int |  (optional)
    below_price = '' # str |  (optional) (default to '')
    below_stop_price = '' # str |  (optional) (default to '')
    below_strategy_id = 56 # int |  (optional)
    below_strategy_type = 56 # int |  (optional)
    below_time_in_force = '' # str |  (optional) (default to '')
    below_trailing_delta = 56 # int |  (optional)
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type =  # str |  (optional) (default to )
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')

    try:
        # New Order list - OCO (TRADE)
        api_response = api_instance.create_order_list_oco_v3(above_type, below_type, quantity, side, symbol, timestamp, above_client_order_id=above_client_order_id, above_iceberg_qty=above_iceberg_qty, above_price=above_price, above_stop_price=above_stop_price, above_strategy_id=above_strategy_id, above_strategy_type=above_strategy_type, above_time_in_force=above_time_in_force, above_trailing_delta=above_trailing_delta, below_client_order_id=below_client_order_id, below_iceberg_qty=below_iceberg_qty, below_price=below_price, below_stop_price=below_stop_price, below_strategy_id=below_strategy_id, below_strategy_type=below_strategy_type, below_time_in_force=below_time_in_force, below_trailing_delta=below_trailing_delta, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode)
        print("The response of SpotTradingApi->create_order_list_oco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_list_oco_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **above_type** | **str**|  | [default to ]
 **below_type** | **str**|  | [default to ]
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **above_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **above_iceberg_qty** | **int**|  | [optional] 
 **above_price** | **str**|  | [optional] [default to &#39;&#39;]
 **above_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **above_strategy_id** | **int**|  | [optional] 
 **above_strategy_type** | **int**|  | [optional] 
 **above_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **above_trailing_delta** | **int**|  | [optional] 
 **below_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **below_iceberg_qty** | **int**|  | [optional] 
 **below_price** | **str**|  | [optional] [default to &#39;&#39;]
 **below_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **below_strategy_id** | **int**|  | [optional] 
 **below_strategy_type** | **int**|  | [optional] 
 **below_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **below_trailing_delta** | **int**|  | [optional] 
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to ]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateOrderListOcoV3Resp**](CreateOrderListOcoV3Resp.md)

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

# **create_order_list_oto_v3**
> CreateOrderListOtoV3Resp create_order_list_oto_v3(pending_quantity, pending_side, pending_type, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_strategy_id=pending_strategy_id, pending_strategy_type=pending_strategy_type, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)

New Order list - OTO (TRADE)

Places an OTO.
- An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
- The first order is called the working order and must be LIMIT or LIMIT_MAKER. Initially, only the working order goes on the order book.
- The second order is called the pending order. It can be any order type except for MARKET orders using parameter quoteOrderQty. The pending order is only placed on the order book when the working order gets fully filled.
- If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
- When the order list is placed, if the working order gets immediately fully filled, the placement response will show the working order as FILLED but the pending order will still appear as PENDING_NEW. You need to query the status of the pending order again to see its updated status.
- OTOs add 2 orders to the unfilled order count, EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_order_list_oto_v3_resp import CreateOrderListOtoV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    pending_quantity = '' # str |  (default to '')
    pending_side = '' # str |  (default to '')
    pending_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    working_price = '' # str |  (default to '')
    working_quantity = '' # str |  (default to '')
    working_side = '' # str |  (default to '')
    working_type =  # str |  (default to )
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    pending_client_order_id = '' # str |  (optional) (default to '')
    pending_iceberg_qty = '' # str |  (optional) (default to '')
    pending_price = '' # str |  (optional) (default to '')
    pending_stop_price = '' # str |  (optional) (default to '')
    pending_strategy_id = 56 # int |  (optional)
    pending_strategy_type = 56 # int |  (optional)
    pending_time_in_force = '' # str |  (optional) (default to '')
    pending_trailing_delta = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    working_client_order_id = '' # str |  (optional) (default to '')
    working_iceberg_qty = '' # str |  (optional) (default to '')
    working_strategy_id = 56 # int |  (optional)
    working_strategy_type = 56 # int |  (optional)
    working_time_in_force = '' # str |  (optional) (default to '')

    try:
        # New Order list - OTO (TRADE)
        api_response = api_instance.create_order_list_oto_v3(pending_quantity, pending_side, pending_type, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_strategy_id=pending_strategy_id, pending_strategy_type=pending_strategy_type, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)
        print("The response of SpotTradingApi->create_order_list_oto_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_list_oto_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_quantity** | **str**|  | [default to &#39;&#39;]
 **pending_side** | **str**|  | [default to &#39;&#39;]
 **pending_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **working_price** | **str**|  | [default to &#39;&#39;]
 **working_quantity** | **str**|  | [default to &#39;&#39;]
 **working_side** | **str**|  | [default to &#39;&#39;]
 **working_type** | **str**|  | [default to ]
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_strategy_id** | **int**|  | [optional] 
 **pending_strategy_type** | **int**|  | [optional] 
 **pending_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **working_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **working_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **working_strategy_id** | **int**|  | [optional] 
 **working_strategy_type** | **int**|  | [optional] 
 **working_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateOrderListOtoV3Resp**](CreateOrderListOtoV3Resp.md)

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

# **create_order_list_otoco_v3**
> CreateOrderListOtocoV3Resp create_order_list_otoco_v3(pending_above_type, pending_quantity, pending_side, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_strategy_id=pending_above_strategy_id, pending_above_strategy_type=pending_above_strategy_type, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_strategy_id=pending_below_strategy_id, pending_below_strategy_type=pending_below_strategy_type, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)

New Order list - OTOCO (TRADE)

Place an OTOCO.
- An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
- The first order is called the working order and must be LIMIT or LIMIT_MAKER. Initially, only the working order goes on the order book.

The behavior of the working order is the same as the OTO.
- OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets fully filled.

The rules of the pending above and pending below follow the same rules as the Order list OCO.
- OTOCOs add 3 orders against the unfilled order count, EXCHANGE_MAX_NUM_ORDERS filter, and MAX_NUM_ORDERS filter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_order_list_otoco_v3_resp import CreateOrderListOtocoV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    pending_above_type =  # str |  (default to )
    pending_quantity = '' # str |  (default to '')
    pending_side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    working_price = '' # str |  (default to '')
    working_quantity = '' # str |  (default to '')
    working_side = '' # str |  (default to '')
    working_type =  # str |  (default to )
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    pending_above_client_order_id = '' # str |  (optional) (default to '')
    pending_above_iceberg_qty = '' # str |  (optional) (default to '')
    pending_above_price = '' # str |  (optional) (default to '')
    pending_above_stop_price = '' # str |  (optional) (default to '')
    pending_above_strategy_id = 56 # int |  (optional)
    pending_above_strategy_type = 56 # int |  (optional)
    pending_above_time_in_force = '' # str |  (optional) (default to '')
    pending_above_trailing_delta = '' # str |  (optional) (default to '')
    pending_below_client_order_id = '' # str |  (optional) (default to '')
    pending_below_iceberg_qty = '' # str |  (optional) (default to '')
    pending_below_price = '' # str |  (optional) (default to '')
    pending_below_stop_price = '' # str |  (optional) (default to '')
    pending_below_strategy_id = 56 # int |  (optional)
    pending_below_strategy_type = 56 # int |  (optional)
    pending_below_time_in_force = '' # str |  (optional) (default to '')
    pending_below_trailing_delta = '' # str |  (optional) (default to '')
    pending_below_type =  # str |  (optional) (default to )
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    working_client_order_id = '' # str |  (optional) (default to '')
    working_iceberg_qty = '' # str |  (optional) (default to '')
    working_strategy_id = 56 # int |  (optional)
    working_strategy_type = 56 # int |  (optional)
    working_time_in_force = '' # str |  (optional) (default to '')

    try:
        # New Order list - OTOCO (TRADE)
        api_response = api_instance.create_order_list_otoco_v3(pending_above_type, pending_quantity, pending_side, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_strategy_id=pending_above_strategy_id, pending_above_strategy_type=pending_above_strategy_type, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_strategy_id=pending_below_strategy_id, pending_below_strategy_type=pending_below_strategy_type, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)
        print("The response of SpotTradingApi->create_order_list_otoco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_list_otoco_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_above_type** | **str**|  | [default to ]
 **pending_quantity** | **str**|  | [default to &#39;&#39;]
 **pending_side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **working_price** | **str**|  | [default to &#39;&#39;]
 **working_quantity** | **str**|  | [default to &#39;&#39;]
 **working_side** | **str**|  | [default to &#39;&#39;]
 **working_type** | **str**|  | [default to ]
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_strategy_id** | **int**|  | [optional] 
 **pending_above_strategy_type** | **int**|  | [optional] 
 **pending_above_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_above_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_strategy_id** | **int**|  | [optional] 
 **pending_below_strategy_type** | **int**|  | [optional] 
 **pending_below_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_trailing_delta** | **str**|  | [optional] [default to &#39;&#39;]
 **pending_below_type** | **str**|  | [optional] [default to ]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **working_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **working_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **working_strategy_id** | **int**|  | [optional] 
 **working_strategy_type** | **int**|  | [optional] 
 **working_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateOrderListOtocoV3Resp**](CreateOrderListOtocoV3Resp.md)

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

# **create_order_oco_v3**
> CreateOrderOcoV3Resp create_order_oco_v3(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, trailing_delta=trailing_delta)

New OCO - Deprecated (TRADE)

Send in a new OCO.
- Price Restrictions:

SELL: Limit Price > Last Price > Stop Price
BUY: Limit Price < Last Price < Stop Price
- Quantity Restrictions:

Both legs must have the same quantity.
ICEBERG quantities however do not have to be the same
- OCO adds 2 orders to the unfilled order count, EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_order_oco_v3_resp import CreateOrderOcoV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    stop_price = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    limit_client_order_id = '' # str |  (optional) (default to '')
    limit_iceberg_qty = '' # str |  (optional) (default to '')
    limit_strategy_id = 56 # int |  (optional)
    limit_strategy_type = 56 # int |  (optional)
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_client_order_id = '' # str |  (optional) (default to '')
    stop_iceberg_qty = '' # str |  (optional) (default to '')
    stop_limit_price = '' # str |  (optional) (default to '')
    stop_limit_time_in_force = '' # str |  (optional) (default to '')
    stop_strategy_id = 56 # int |  (optional)
    stop_strategy_type = 56 # int |  (optional)
    trailing_delta = 56 # int |  (optional)

    try:
        # New OCO - Deprecated (TRADE)
        api_response = api_instance.create_order_oco_v3(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, trailing_delta=trailing_delta)
        print("The response of SpotTradingApi->create_order_oco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_oco_v3: %s\n" % e)
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
 **limit_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **limit_strategy_id** | **int**|  | [optional] 
 **limit_strategy_type** | **int**|  | [optional] 
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_price** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_strategy_id** | **int**|  | [optional] 
 **stop_strategy_type** | **int**|  | [optional] 
 **trailing_delta** | **int**|  | [optional] 

### Return type

[**CreateOrderOcoV3Resp**](CreateOrderOcoV3Resp.md)

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

# **create_order_test_v3**
> SpotCreateOrderTestV3Resp create_order_test_v3(side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

Test new order (TRADE)

Test new order creation and signature/recvWindow long.
Creates and validates a new order but does not send it into the matching engine.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_order_test_v3_resp import SpotCreateOrderTestV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    compute_commission_rates = True # bool |  (optional)
    iceberg_qty = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    quote_order_qty = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    strategy_type = 56 # int |  (optional)
    time_in_force = '' # str |  (optional) (default to '')
    trailing_delta = 56 # int |  (optional)

    try:
        # Test new order (TRADE)
        api_response = api_instance.create_order_test_v3(side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of SpotTradingApi->create_order_test_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_test_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **compute_commission_rates** | **bool**|  | [optional] 
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **quote_order_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**|  | [optional] 
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **trailing_delta** | **int**|  | [optional] 

### Return type

[**SpotCreateOrderTestV3Resp**](SpotCreateOrderTestV3Resp.md)

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

# **create_order_v3**
> SpotCreateOrderV3Resp create_order_v3(side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

New order (TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_order_v3_resp import SpotCreateOrderV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    iceberg_qty = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    quote_order_qty = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    strategy_type = 56 # int |  (optional)
    time_in_force = '' # str |  (optional) (default to '')
    trailing_delta = 56 # int |  (optional)

    try:
        # New order (TRADE)
        api_response = api_instance.create_order_v3(side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of SpotTradingApi->create_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **quote_order_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**|  | [optional] 
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **trailing_delta** | **int**|  | [optional] 

### Return type

[**SpotCreateOrderV3Resp**](SpotCreateOrderV3Resp.md)

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

# **create_sor_order_test_v3**
> SpotCreateSorOrderTestV3Resp create_sor_order_test_v3(quantity, side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)

Test new order using SOR (TRADE)

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_sor_order_test_v3_resp import SpotCreateSorOrderTestV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    compute_commission_rates = True # bool |  (optional)
    iceberg_qty = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    strategy_type = 56 # int |  (optional)
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # Test new order using SOR (TRADE)
        api_response = api_instance.create_sor_order_test_v3(quantity, side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)
        print("The response of SpotTradingApi->create_sor_order_test_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_sor_order_test_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **compute_commission_rates** | **bool**|  | [optional] 
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**|  | [optional] 
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**SpotCreateSorOrderTestV3Resp**](SpotCreateSorOrderTestV3Resp.md)

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

# **create_sor_order_v3**
> CreateSorOrderV3Resp create_sor_order_v3(quantity, side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)

New order using SOR (TRADE)

Places an order using smart order routing (SOR).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_sor_order_v3_resp import CreateSorOrderV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    iceberg_qty = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    strategy_type = 56 # int |  (optional)
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # New order using SOR (TRADE)
        api_response = api_instance.create_sor_order_v3(quantity, side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)
        print("The response of SpotTradingApi->create_sor_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_sor_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity** | **str**|  | [default to &#39;&#39;]
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**|  | [optional] 
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateSorOrderV3Resp**](CreateSorOrderV3Resp.md)

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

# **create_user_data_stream_v3**
> CreateUserDataStreamV3Resp create_user_data_stream_v3()

Start user data stream (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_user_data_stream_v3_resp import CreateUserDataStreamV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)

    try:
        # Start user data stream (USER_STREAM)
        api_response = api_instance.create_user_data_stream_v3()
        print("The response of SpotTradingApi->create_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->create_user_data_stream_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateUserDataStreamV3Resp**](CreateUserDataStreamV3Resp.md)

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

# **delete_open_orders_v3**
> List[List[SpotDeleteOpenOrdersV3RespInner]] delete_open_orders_v3(symbol, timestamp, recv_window=recv_window)

Cancel All Open Orders on a Symbol (TRADE)

Cancels all active orders on a symbol.
This includes orders that are part of an order list.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_delete_open_orders_v3_resp_inner import SpotDeleteOpenOrdersV3RespInner
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel All Open Orders on a Symbol (TRADE)
        api_response = api_instance.delete_open_orders_v3(symbol, timestamp, recv_window=recv_window)
        print("The response of SpotTradingApi->delete_open_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->delete_open_orders_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

**List[List[SpotDeleteOpenOrdersV3RespInner]]**

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

# **delete_order_list_v3**
> DeleteOrderListV3Resp delete_order_list_v3(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Order list (TRADE)

Cancel an entire Order list

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_order_list_v3_resp import DeleteOrderListV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel Order list (TRADE)
        api_response = api_instance.delete_order_list_v3(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of SpotTradingApi->delete_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->delete_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] 
 **list_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**DeleteOrderListV3Resp**](DeleteOrderListV3Resp.md)

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

# **delete_order_v3**
> DeleteOrderV3Resp delete_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)

Cancel order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.delete_order_v3_resp import DeleteOrderV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    cancel_restrictions = '' # str | Supported values: <br/>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br/> `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000`. (optional)

    try:
        # Cancel order (TRADE)
        api_response = api_instance.delete_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)
        print("The response of SpotTradingApi->delete_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->delete_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default. | [optional] [default to &#39;&#39;]
 **cancel_restrictions** | **str**| Supported values: &lt;br/&gt;&#x60;ONLY_NEW&#x60; - Cancel will succeed if the order status is &#x60;NEW&#x60;.&lt;br/&gt; &#x60;ONLY_PARTIALLY_FILLED &#x60; - Cancel will succeed if order status is &#x60;PARTIALLY_FILLED&#x60;. | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60;. | [optional] 

### Return type

[**DeleteOrderV3Resp**](DeleteOrderV3Resp.md)

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

# **delete_user_data_stream_v3**
> object delete_user_data_stream_v3(listen_key)

Close user data stream (USER_STREAM)

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
    api_instance = binance.spot.SpotTradingApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Close user data stream (USER_STREAM)
        api_response = api_instance.delete_user_data_stream_v3(listen_key)
        print("The response of SpotTradingApi->delete_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->delete_user_data_stream_v3: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_commission_v3**
> GetAccountCommissionV3Resp get_account_commission_v3(symbol)

Query Commission Rates (USER_DATA)

Get current account commission rates.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_account_commission_v3_resp import GetAccountCommissionV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Commission Rates (USER_DATA)
        api_response = api_instance.get_account_commission_v3(symbol)
        print("The response of SpotTradingApi->get_account_commission_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_account_commission_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**GetAccountCommissionV3Resp**](GetAccountCommissionV3Resp.md)

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
> GetAccountV3Resp get_account_v3(timestamp, omit_zero_balances=omit_zero_balances, recv_window=recv_window)

Account information (USER_DATA)

Get current account information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_account_v3_resp import GetAccountV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    omit_zero_balances = True # bool | When set to `true`, emits only the non-zero balances of an account. <br/>Default value: `false` (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Account information (USER_DATA)
        api_response = api_instance.get_account_v3(timestamp, omit_zero_balances=omit_zero_balances, recv_window=recv_window)
        print("The response of SpotTradingApi->get_account_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_account_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **omit_zero_balances** | **bool**| When set to &#x60;true&#x60;, emits only the non-zero balances of an account. &lt;br/&gt;Default value: &#x60;false&#x60; | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

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

# **get_agg_trades_v3**
> List[SpotGetAggTradesV3RespItem] get_agg_trades_v3(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate trades list

Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_agg_trades_v3_resp_item import SpotGetAggTradesV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate trades list
        api_response = api_instance.get_agg_trades_v3(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of SpotTradingApi->get_agg_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_agg_trades_v3: %s\n" % e)
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

[**List[SpotGetAggTradesV3RespItem]**](SpotGetAggTradesV3RespItem.md)

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

# **get_all_order_list_v3**
> List[GetAllOrderListV3RespItem] get_all_order_list_v3(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query all Order lists (USER_DATA)

Retrieves all order lists based on provided optional parameters.
Note that the time between startTime and endTime can't be longer than 24 hours.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_all_order_list_v3_resp_item import GetAllOrderListV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    from_id = 56 # int | If supplied, neither `startTime` or `endTime` can be provided (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 56 # int | Default Value: 500; Max Value: 1000 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query all Order lists (USER_DATA)
        api_response = api_instance.get_all_order_list_v3(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of SpotTradingApi->get_all_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_all_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_id** | **int**| If supplied, neither &#x60;startTime&#x60; or &#x60;endTime&#x60; can be provided | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default Value: 500; Max Value: 1000 | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetAllOrderListV3RespItem]**](GetAllOrderListV3RespItem.md)

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

# **get_all_orders_v3**
> List[GetAllOrdersV3RespItem] get_all_orders_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_all_orders_v3_resp_item import GetAllOrdersV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # All orders (USER_DATA)
        api_response = api_instance.get_all_orders_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of SpotTradingApi->get_all_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_all_orders_v3: %s\n" % e)
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
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetAllOrdersV3RespItem]**](GetAllOrdersV3RespItem.md)

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

# **get_avg_price_v3**
> GetAvgPriceV3Resp get_avg_price_v3(symbol)

Current average price

Current average price for a symbol.

### Example


```python
import binance.spot
from binance.spot.models.get_avg_price_v3_resp import GetAvgPriceV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Current average price
        api_response = api_instance.get_avg_price_v3(symbol)
        print("The response of SpotTradingApi->get_avg_price_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_avg_price_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**GetAvgPriceV3Resp**](GetAvgPriceV3Resp.md)

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

# **get_depth_v3**
> GetDepthV3Resp get_depth_v3(symbol, limit=limit)

Order book

### Example


```python
import binance.spot
from binance.spot.models.get_depth_v3_resp import GetDepthV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 5000. <br/> If limit &gt; 5000. then the response will truncate to 5000. (optional) (default to 100)

    try:
        # Order book
        api_response = api_instance.get_depth_v3(symbol, limit=limit)
        print("The response of SpotTradingApi->get_depth_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_depth_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 5000. &lt;br/&gt; If limit &amp;gt; 5000. then the response will truncate to 5000. | [optional] [default to 100]

### Return type

[**GetDepthV3Resp**](GetDepthV3Resp.md)

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

# **get_exchange_info_v3**
> SpotGetExchangeInfoV3Resp get_exchange_info_v3(symbol=symbol, symbols=symbols, permissions=permissions, show_permission_sets=show_permission_sets, symbol_status=symbol_status)

Exchange information

Current exchange trading rules and symbol information

### Example


```python
import binance.spot
from binance.spot.models.spot_get_exchange_info_v3_resp import SpotGetExchangeInfoV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Example: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC</a>&#34; (optional) (default to '')
    symbols = ['symbols_example'] # List[str] | Examples: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D</a>&#34; <br/> or <br/> curl -g -X  GET &#39;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BTCUSDT%22,%22BNBBTC\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbols=[&#34;BTCUSDT&#34;,&#34;BNBBTC</a>&#34;]&#39; (optional)
    permissions = '' # str | Examples: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT</a>&#34; <br/> or <br/> curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D</a>&#34; <br/> or <br/> curl -g -X GET &#39;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22,%22LEVERAGED\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=[&#34;MARGIN&#34;,&#34;LEVERAGED</a>&#34;]&#39; (optional) (default to '')
    show_permission_sets = True # bool | Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true` (optional)
    symbol_status =  # str | Filters symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK` <br/> Cannot be used in combination with `symbols` or `symbol`. (optional) (default to )

    try:
        # Exchange information
        api_response = api_instance.get_exchange_info_v3(symbol=symbol, symbols=symbols, permissions=permissions, show_permission_sets=show_permission_sets, symbol_status=symbol_status)
        print("The response of SpotTradingApi->get_exchange_info_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_exchange_info_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Example: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbol&#x3D;BNBBTC\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbol&#x3D;BNBBTC&lt;/a&gt;&amp;#34; | [optional] [default to &#39;&#39;]
 **symbols** | [**List[str]**](str.md)| Examples: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BNBBTC%22,%22BTCUSDT%22%5D\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BNBBTC%22,%22BTCUSDT%22%5D&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -g -X  GET &amp;#39;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BTCUSDT%22,%22BNBBTC\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;[&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBBTC&lt;/a&gt;&amp;#34;]&amp;#39; | [optional] 
 **permissions** | **str**| Examples: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;SPOT\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;SPOT&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22%2C%22LEVERAGED%22%5D\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22%2C%22LEVERAGED%22%5D&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -g -X GET &amp;#39;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22,%22LEVERAGED\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;[&amp;#34;MARGIN&amp;#34;,&amp;#34;LEVERAGED&lt;/a&gt;&amp;#34;]&amp;#39; | [optional] [default to &#39;&#39;]
 **show_permission_sets** | **bool**| Controls whether the content of the &#x60;permissionSets&#x60; field is populated or not. Defaults to &#x60;true&#x60; | [optional] 
 **symbol_status** | **str**| Filters symbols that have this &#x60;tradingStatus&#x60;. Valid values: &#x60;TRADING&#x60;, &#x60;HALT&#x60;, &#x60;BREAK&#x60; &lt;br/&gt; Cannot be used in combination with &#x60;symbols&#x60; or &#x60;symbol&#x60;. | [optional] [default to ]

### Return type

[**SpotGetExchangeInfoV3Resp**](SpotGetExchangeInfoV3Resp.md)

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

# **get_historical_trades_v3**
> List[GetHistoricalTradesV3RespItem] get_historical_trades_v3(symbol, limit=limit, from_id=from_id)

Old trade lookup

Get older trades.

### Example


```python
import binance.spot
from binance.spot.models.get_historical_trades_v3_resp_item import GetHistoricalTradesV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old trade lookup
        api_response = api_instance.get_historical_trades_v3(symbol, limit=limit, from_id=from_id)
        print("The response of SpotTradingApi->get_historical_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_historical_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[GetHistoricalTradesV3RespItem]**](GetHistoricalTradesV3RespItem.md)

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

# **get_klines_v3**
> List[List[GetKlinesV3200ResponseInnerInner]] get_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)

Kline/Candlestick data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.spot
from binance.spot.models.get_klines_v3200_response_inner_inner import GetKlinesV3200ResponseInnerInner
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Kline/Candlestick data
        api_response = api_instance.get_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)
        print("The response of SpotTradingApi->get_klines_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_klines_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

**List[List[GetKlinesV3200ResponseInnerInner]]**

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

# **get_my_allocations_v3**
> List[GetMyAllocationsV3RespItem] get_my_allocations_v3(symbol, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window, timestamp=timestamp)

Query Allocations (USER_DATA)

Retrieves allocations resulting from SOR order placement.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_my_allocations_v3_resp_item import GetMyAllocationsV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_allocation_id = 56 # int |  (optional)
    limit = 500 # int | Default 500;Max 1000 (optional) (default to 500)
    order_id = 56 # int |  (optional)
    recv_window = 56 # int | The value cannot be greater than `60000`. (optional)
    timestamp = 56 # int |  (optional)

    try:
        # Query Allocations (USER_DATA)
        api_response = api_instance.get_my_allocations_v3(symbol, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window, timestamp=timestamp)
        print("The response of SpotTradingApi->get_my_allocations_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_my_allocations_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_allocation_id** | **int**|  | [optional] 
 **limit** | **int**| Default 500;Max 1000 | [optional] [default to 500]
 **order_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60;. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**List[GetMyAllocationsV3RespItem]**](GetMyAllocationsV3RespItem.md)

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

# **get_my_prevented_matches_v3**
> List[GetMyPreventedMatchesV3RespItem] get_my_prevented_matches_v3(symbol, timestamp, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)

Query Prevented Matches (USER_DATA)

Displays the list of orders that were expired due to STP.
These are the combinations supported:
- symbol + preventedMatchId
- symbol + orderId
- symbol + orderId + fromPreventedMatchId (limit will default to 500)
- symbol + orderId + fromPreventedMatchId + limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_my_prevented_matches_v3_resp_item import GetMyPreventedMatchesV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    prevented_match_id = 56 # int |  (optional)
    order_id = 56 # int |  (optional)
    from_prevented_match_id = 56 # int |  (optional)
    limit = 500 # int | Default: `500`; Max: `1000` (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Prevented Matches (USER_DATA)
        api_response = api_instance.get_my_prevented_matches_v3(symbol, timestamp, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)
        print("The response of SpotTradingApi->get_my_prevented_matches_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_my_prevented_matches_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **prevented_match_id** | **int**|  | [optional] 
 **order_id** | **int**|  | [optional] 
 **from_prevented_match_id** | **int**|  | [optional] 
 **limit** | **int**| Default: &#x60;500&#x60;; Max: &#x60;1000&#x60; | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMyPreventedMatchesV3RespItem]**](GetMyPreventedMatchesV3RespItem.md)

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

# **get_my_trades_v3**
> List[GetMyTradesV3RespItem] get_my_trades_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account trade list (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_my_trades_v3_resp_item import GetMyTradesV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int | This can only be used in combination with `symbol`. (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Account trade list (USER_DATA)
        api_response = api_instance.get_my_trades_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of SpotTradingApi->get_my_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_my_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**| This can only be used in combination with &#x60;symbol&#x60;. | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetMyTradesV3RespItem]**](GetMyTradesV3RespItem.md)

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

# **get_open_order_list_v3**
> List[GetOpenOrderListV3RespItem] get_open_order_list_v3(timestamp, recv_window=recv_window)

Query Open Order lists (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_open_order_list_v3_resp_item import GetOpenOrderListV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Open Order lists (USER_DATA)
        api_response = api_instance.get_open_order_list_v3(timestamp, recv_window=recv_window)
        print("The response of SpotTradingApi->get_open_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_open_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetOpenOrderListV3RespItem]**](GetOpenOrderListV3RespItem.md)

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

# **get_open_orders_v3**
> List[GetOpenOrdersV3RespItem] get_open_orders_v3(timestamp, symbol=symbol, recv_window=recv_window)

Current open orders (USER_DATA)

Get all open orders on a symbol. Careful when accessing this with no symbol.
Weight:
6 for a single symbol; 80 when the symbol parameter is omitted

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_open_orders_v3_resp_item import GetOpenOrdersV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Current open orders (USER_DATA)
        api_response = api_instance.get_open_orders_v3(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of SpotTradingApi->get_open_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_open_orders_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetOpenOrdersV3RespItem]**](GetOpenOrdersV3RespItem.md)

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

# **get_order_list_v3**
> GetOrderListV3Resp get_order_list_v3(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order list (USER_DATA)

Retrieves a specific order list based on provided optional parameters.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_order_list_v3_resp import GetOrderListV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    orig_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Order list (USER_DATA)
        api_response = api_instance.get_order_list_v3(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of SpotTradingApi->get_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] 
 **orig_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetOrderListV3Resp**](GetOrderListV3Resp.md)

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

# **get_order_v3**
> GetOrderV3Resp get_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_order_v3_resp import GetOrderV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query order (USER_DATA)
        api_response = api_instance.get_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of SpotTradingApi->get_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetOrderV3Resp**](GetOrderV3Resp.md)

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

# **get_ping_v3**
> object get_ping_v3()

Test connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.spot
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
    api_instance = binance.spot.SpotTradingApi(api_client)

    try:
        # Test connectivity
        api_response = api_instance.get_ping_v3()
        print("The response of SpotTradingApi->get_ping_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ping_v3: %s\n" % e)
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

# **get_rate_limit_order_v3**
> List[GetRateLimitOrderV3RespItem] get_rate_limit_order_v3(timestamp, recv_window=recv_window)

Query Unfilled Order Count (USER_DATA)

Displays the user's unfilled order count for all intervals.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_rate_limit_order_v3_resp_item import GetRateLimitOrderV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Unfilled Order Count (USER_DATA)
        api_response = api_instance.get_rate_limit_order_v3(timestamp, recv_window=recv_window)
        print("The response of SpotTradingApi->get_rate_limit_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_rate_limit_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[GetRateLimitOrderV3RespItem]**](GetRateLimitOrderV3RespItem.md)

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

# **get_ticker24hr_v3**
> SpotGetTicker24hrV3Resp get_ticker24hr_v3(symbol=symbol, symbols=symbols, type=type)

24hr ticker price change statistics

24 hour rolling window price change statistics. Careful when accessing this with no symbol.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker24hr_v3_resp import SpotGetTicker24hrV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, tickers for all symbols will be returned in an array. <br/><br/>          Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, tickers for all symbols will be returned in an array. <br/><br/>          Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # 24hr ticker price change statistics
        api_response = api_instance.get_ticker24hr_v3(symbol=symbol, symbols=symbols, type=type)
        print("The response of SpotTradingApi->get_ticker24hr_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ticker24hr_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, tickers for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;          Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, tickers for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;          Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTicker24hrV3Resp**](SpotGetTicker24hrV3Resp.md)

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

# **get_ticker_book_ticker_v3**
> SpotGetTickerBookTickerV3Resp get_ticker_book_ticker_v3(symbol=symbol, symbols=symbols)

Symbol order book ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_book_ticker_v3_resp import SpotGetTickerBookTickerV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, bookTickers for all symbols will be returned in an array.          <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, bookTickers for all symbols will be returned in an array.          <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')

    try:
        # Symbol order book ticker
        api_response = api_instance.get_ticker_book_ticker_v3(symbol=symbol, symbols=symbols)
        print("The response of SpotTradingApi->get_ticker_book_ticker_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ticker_book_ticker_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, bookTickers for all symbols will be returned in an array.          &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, bookTickers for all symbols will be returned in an array.          &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]

### Return type

[**SpotGetTickerBookTickerV3Resp**](SpotGetTickerBookTickerV3Resp.md)

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

# **get_ticker_price_v3**
> SpotGetTickerPriceV3Resp get_ticker_price_v3(symbol=symbol, symbols=symbols)

Symbol price ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_price_v3_resp import SpotGetTickerPriceV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, prices for all symbols will be returned in an array. <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, prices for all symbols will be returned in an array. <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')

    try:
        # Symbol price ticker
        api_response = api_instance.get_ticker_price_v3(symbol=symbol, symbols=symbols)
        print("The response of SpotTradingApi->get_ticker_price_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ticker_price_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, prices for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, prices for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]

### Return type

[**SpotGetTickerPriceV3Resp**](SpotGetTickerPriceV3Resp.md)

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

# **get_ticker_trading_day_v3**
> SpotGetTickerTradingDayV3Resp get_ticker_trading_day_v3(symbol, symbols, time_zone=time_zone, type=type)

Trading Day Ticker

Price change statistics for a trading day.
4 for each requested symbol.  The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_trading_day_v3_resp import SpotGetTickerTradingDayV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    symbols = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # Trading Day Ticker
        api_response = api_instance.get_ticker_trading_day_v3(symbol, symbols, time_zone=time_zone, type=type)
        print("The response of SpotTradingApi->get_ticker_trading_day_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ticker_trading_day_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **symbols** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTickerTradingDayV3Resp**](SpotGetTickerTradingDayV3Resp.md)

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

# **get_ticker_v3**
> SpotGetTickerV3Resp get_ticker_v3(symbol, symbols, window_size=window_size, type=type)

Rolling window price change statistics

Note: This endpoint is different from the GET /api/v3/ticker/24hr endpoint.
The window used to compute statistics will be no more than 59999ms from the requested windowSize.
openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
As such, the effective window will be up to 59999ms wider than windowSize.
E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the openTime will be: 1641201420000 (January 3, 2022, 09:17:00)
4 for each requested symbol regardless of windowSize.  The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_v3_resp import SpotGetTickerV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    symbols = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    window_size = '' # str | Defaults to `1d` if no parameter provided <br/> Supported `windowSize` values: <br/> `1m`,`2m`....`59m` for minutes <br/> `1h`, `2h`....`23h` - for hours <br/> `1d`...`7d` - for days <br/><br/> Units cannot be combined (e.g. `1d2h` is not allowed) (optional) (default to '')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # Rolling window price change statistics
        api_response = api_instance.get_ticker_v3(symbol, symbols, window_size=window_size, type=type)
        print("The response of SpotTradingApi->get_ticker_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ticker_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **symbols** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **window_size** | **str**| Defaults to &#x60;1d&#x60; if no parameter provided &lt;br/&gt; Supported &#x60;windowSize&#x60; values: &lt;br/&gt; &#x60;1m&#x60;,&#x60;2m&#x60;....&#x60;59m&#x60; for minutes &lt;br/&gt; &#x60;1h&#x60;, &#x60;2h&#x60;....&#x60;23h&#x60; - for hours &lt;br/&gt; &#x60;1d&#x60;...&#x60;7d&#x60; - for days &lt;br/&gt;&lt;br/&gt; Units cannot be combined (e.g. &#x60;1d2h&#x60; is not allowed) | [optional] [default to &#39;&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTickerV3Resp**](SpotGetTickerV3Resp.md)

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

# **get_time_v3**
> GetTimeV3Resp get_time_v3()

Check server time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.spot
from binance.spot.models.get_time_v3_resp import GetTimeV3Resp
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
    api_instance = binance.spot.SpotTradingApi(api_client)

    try:
        # Check server time
        api_response = api_instance.get_time_v3()
        print("The response of SpotTradingApi->get_time_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_time_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTimeV3Resp**](GetTimeV3Resp.md)

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

# **get_trades_v3**
> List[GetTradesV3RespItem] get_trades_v3(symbol, limit=limit)

Recent trades list

Get recent trades.

### Example


```python
import binance.spot
from binance.spot.models.get_trades_v3_resp_item import GetTradesV3RespItem
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent trades list
        api_response = api_instance.get_trades_v3(symbol, limit=limit)
        print("The response of SpotTradingApi->get_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[GetTradesV3RespItem]**](GetTradesV3RespItem.md)

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

# **get_ui_klines_v3**
> List[List[GetKlinesV3200ResponseInnerInner]] get_ui_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)

UIKlines

The request is similar to klines having the same parameters and response.
uiKlines return modified kline data, optimized for presentation of candlestick charts.

### Example


```python
import binance.spot
from binance.spot.models.get_klines_v3200_response_inner_inner import GetKlinesV3200ResponseInnerInner
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
    api_instance = binance.spot.SpotTradingApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str | See <a href=\"/docs/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals\">`klines`</a> (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # UIKlines
        api_response = api_instance.get_ui_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)
        print("The response of SpotTradingApi->get_ui_klines_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->get_ui_klines_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**| See &lt;a href&#x3D;\&quot;/docs/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals\&quot;&gt;&#x60;klines&#x60;&lt;/a&gt; | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

**List[List[GetKlinesV3200ResponseInnerInner]]**

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

# **update_user_data_stream_v3**
> object update_user_data_stream_v3(listen_key)

Keepalive user data stream (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

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
    api_instance = binance.spot.SpotTradingApi(api_client)
    listen_key = '' # str |  (default to '')

    try:
        # Keepalive user data stream (USER_STREAM)
        api_response = api_instance.update_user_data_stream_v3(listen_key)
        print("The response of SpotTradingApi->update_user_data_stream_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpotTradingApi->update_user_data_stream_v3: %s\n" % e)
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

