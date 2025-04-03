# binance.spot.TradingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spot_create_order_cancel_replace_v3**](TradingApi.md#spot_create_order_cancel_replace_v3) | **POST** /api/v3/order/cancelReplace | Cancel an Existing Order and Send a New Order (TRADE)
[**spot_create_order_list_oco_v3**](TradingApi.md#spot_create_order_list_oco_v3) | **POST** /api/v3/orderList/oco | New Order list - OCO (TRADE)
[**spot_create_order_list_oto_v3**](TradingApi.md#spot_create_order_list_oto_v3) | **POST** /api/v3/orderList/oto | New Order list - OTO (TRADE)
[**spot_create_order_list_otoco_v3**](TradingApi.md#spot_create_order_list_otoco_v3) | **POST** /api/v3/orderList/otoco | New Order list - OTOCO (TRADE)
[**spot_create_order_oco_v3**](TradingApi.md#spot_create_order_oco_v3) | **POST** /api/v3/order/oco | New OCO - Deprecated (TRADE)
[**spot_create_order_test_v3**](TradingApi.md#spot_create_order_test_v3) | **POST** /api/v3/order/test | Test new order (TRADE)
[**spot_create_order_v3**](TradingApi.md#spot_create_order_v3) | **POST** /api/v3/order | New order (TRADE)
[**spot_create_sor_order_test_v3**](TradingApi.md#spot_create_sor_order_test_v3) | **POST** /api/v3/sor/order/test | Test new order using SOR (TRADE)
[**spot_create_sor_order_v3**](TradingApi.md#spot_create_sor_order_v3) | **POST** /api/v3/sor/order | New order using SOR (TRADE)
[**spot_delete_open_orders_v3**](TradingApi.md#spot_delete_open_orders_v3) | **DELETE** /api/v3/openOrders | Cancel All Open Orders on a Symbol (TRADE)
[**spot_delete_order_list_v3**](TradingApi.md#spot_delete_order_list_v3) | **DELETE** /api/v3/orderList | Cancel Order list (TRADE)
[**spot_delete_order_v3**](TradingApi.md#spot_delete_order_v3) | **DELETE** /api/v3/order | Cancel order (TRADE)
[**spot_get_all_order_list_v3**](TradingApi.md#spot_get_all_order_list_v3) | **GET** /api/v3/allOrderList | Query all Order lists (USER_DATA)
[**spot_get_all_orders_v3**](TradingApi.md#spot_get_all_orders_v3) | **GET** /api/v3/allOrders | All orders (USER_DATA)
[**spot_get_open_order_list_v3**](TradingApi.md#spot_get_open_order_list_v3) | **GET** /api/v3/openOrderList | Query Open Order lists (USER_DATA)
[**spot_get_open_orders_v3**](TradingApi.md#spot_get_open_orders_v3) | **GET** /api/v3/openOrders | Current open orders (USER_DATA)
[**spot_get_order_list_v3**](TradingApi.md#spot_get_order_list_v3) | **GET** /api/v3/orderList | Query Order list (USER_DATA)
[**spot_get_order_v3**](TradingApi.md#spot_get_order_v3) | **GET** /api/v3/order | Query order (USER_DATA)


# **spot_create_order_cancel_replace_v3**
> SpotCreateOrderCancelReplaceV3Resp spot_create_order_cancel_replace_v3(cancel_replace_mode, side, symbol, timestamp, type, cancel_new_client_order_id=cancel_new_client_order_id, cancel_order_id=cancel_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_restrictions=cancel_restrictions, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_cancel_replace_v3(cancel_replace_mode, side, symbol, timestamp, type, cancel_new_client_order_id=cancel_new_client_order_id, cancel_order_id=cancel_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_restrictions=cancel_restrictions, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of TradingApi->spot_create_order_cancel_replace_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_cancel_replace_v3: %s\n" % e)
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

# **spot_create_order_list_oco_v3**
> SpotCreateOrderListOcoV3Resp spot_create_order_list_oco_v3(above_type, below_type, quantity, side, symbol, timestamp, above_client_order_id=above_client_order_id, above_iceberg_qty=above_iceberg_qty, above_price=above_price, above_stop_price=above_stop_price, above_strategy_id=above_strategy_id, above_strategy_type=above_strategy_type, above_time_in_force=above_time_in_force, above_trailing_delta=above_trailing_delta, below_client_order_id=below_client_order_id, below_iceberg_qty=below_iceberg_qty, below_price=below_price, below_stop_price=below_stop_price, below_strategy_id=below_strategy_id, below_strategy_type=below_strategy_type, below_time_in_force=below_time_in_force, below_trailing_delta=below_trailing_delta, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode)

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
from binance.spot.models.spot_create_order_list_oco_v3_resp import SpotCreateOrderListOcoV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_list_oco_v3(above_type, below_type, quantity, side, symbol, timestamp, above_client_order_id=above_client_order_id, above_iceberg_qty=above_iceberg_qty, above_price=above_price, above_stop_price=above_stop_price, above_strategy_id=above_strategy_id, above_strategy_type=above_strategy_type, above_time_in_force=above_time_in_force, above_trailing_delta=above_trailing_delta, below_client_order_id=below_client_order_id, below_iceberg_qty=below_iceberg_qty, below_price=below_price, below_stop_price=below_stop_price, below_strategy_id=below_strategy_id, below_strategy_type=below_strategy_type, below_time_in_force=below_time_in_force, below_trailing_delta=below_trailing_delta, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode)
        print("The response of TradingApi->spot_create_order_list_oco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_list_oco_v3: %s\n" % e)
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

[**SpotCreateOrderListOcoV3Resp**](SpotCreateOrderListOcoV3Resp.md)

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

# **spot_create_order_list_oto_v3**
> SpotCreateOrderListOtoV3Resp spot_create_order_list_oto_v3(pending_quantity, pending_side, pending_type, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_strategy_id=pending_strategy_id, pending_strategy_type=pending_strategy_type, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)

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
from binance.spot.models.spot_create_order_list_oto_v3_resp import SpotCreateOrderListOtoV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_list_oto_v3(pending_quantity, pending_side, pending_type, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_strategy_id=pending_strategy_id, pending_strategy_type=pending_strategy_type, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)
        print("The response of TradingApi->spot_create_order_list_oto_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_list_oto_v3: %s\n" % e)
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

[**SpotCreateOrderListOtoV3Resp**](SpotCreateOrderListOtoV3Resp.md)

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

# **spot_create_order_list_otoco_v3**
> SpotCreateOrderListOtocoV3Resp spot_create_order_list_otoco_v3(pending_above_type, pending_quantity, pending_side, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_strategy_id=pending_above_strategy_id, pending_above_strategy_type=pending_above_strategy_type, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_strategy_id=pending_below_strategy_id, pending_below_strategy_type=pending_below_strategy_type, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)

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
from binance.spot.models.spot_create_order_list_otoco_v3_resp import SpotCreateOrderListOtocoV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_list_otoco_v3(pending_above_type, pending_quantity, pending_side, symbol, timestamp, working_price, working_quantity, working_side, working_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_strategy_id=pending_above_strategy_id, pending_above_strategy_type=pending_above_strategy_type, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_strategy_id=pending_below_strategy_id, pending_below_strategy_type=pending_below_strategy_type, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_strategy_id=working_strategy_id, working_strategy_type=working_strategy_type, working_time_in_force=working_time_in_force)
        print("The response of TradingApi->spot_create_order_list_otoco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_list_otoco_v3: %s\n" % e)
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

[**SpotCreateOrderListOtocoV3Resp**](SpotCreateOrderListOtocoV3Resp.md)

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

# **spot_create_order_oco_v3**
> SpotCreateOrderOcoV3Resp spot_create_order_oco_v3(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, trailing_delta=trailing_delta)

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
from binance.spot.models.spot_create_order_oco_v3_resp import SpotCreateOrderOcoV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_oco_v3(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, trailing_delta=trailing_delta)
        print("The response of TradingApi->spot_create_order_oco_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_oco_v3: %s\n" % e)
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

[**SpotCreateOrderOcoV3Resp**](SpotCreateOrderOcoV3Resp.md)

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

# **spot_create_order_test_v3**
> SpotCreateOrderTestV3Resp spot_create_order_test_v3(side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_test_v3(side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of TradingApi->spot_create_order_test_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_test_v3: %s\n" % e)
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

# **spot_create_order_v3**
> SpotCreateOrderV3Resp spot_create_order_v3(side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)

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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_order_v3(side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force, trailing_delta=trailing_delta)
        print("The response of TradingApi->spot_create_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_order_v3: %s\n" % e)
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

# **spot_create_sor_order_test_v3**
> SpotCreateSorOrderTestV3Resp spot_create_sor_order_test_v3(quantity, side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)

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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_sor_order_test_v3(quantity, side, symbol, timestamp, type, compute_commission_rates=compute_commission_rates, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)
        print("The response of TradingApi->spot_create_sor_order_test_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_sor_order_test_v3: %s\n" % e)
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

# **spot_create_sor_order_v3**
> SpotCreateSorOrderV3Resp spot_create_sor_order_v3(quantity, side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)

New order using SOR (TRADE)

Places an order using smart order routing (SOR).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_create_sor_order_v3_resp import SpotCreateSorOrderV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
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
        api_response = api_instance.spot_create_sor_order_v3(quantity, side, symbol, timestamp, type, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, strategy_id=strategy_id, strategy_type=strategy_type, time_in_force=time_in_force)
        print("The response of TradingApi->spot_create_sor_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_create_sor_order_v3: %s\n" % e)
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

[**SpotCreateSorOrderV3Resp**](SpotCreateSorOrderV3Resp.md)

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

# **spot_delete_open_orders_v3**
> List[List[SpotDeleteOpenOrdersV3RespInner]] spot_delete_open_orders_v3(symbol, timestamp, recv_window=recv_window)

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
    api_instance = binance.spot.TradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel All Open Orders on a Symbol (TRADE)
        api_response = api_instance.spot_delete_open_orders_v3(symbol, timestamp, recv_window=recv_window)
        print("The response of TradingApi->spot_delete_open_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_delete_open_orders_v3: %s\n" % e)
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

# **spot_delete_order_list_v3**
> SpotDeleteOrderListV3Resp spot_delete_order_list_v3(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Order list (TRADE)

Cancel an entire Order list

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_delete_order_list_v3_resp import SpotDeleteOrderListV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel Order list (TRADE)
        api_response = api_instance.spot_delete_order_list_v3(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of TradingApi->spot_delete_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_delete_order_list_v3: %s\n" % e)
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

[**SpotDeleteOrderListV3Resp**](SpotDeleteOrderListV3Resp.md)

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

# **spot_delete_order_v3**
> SpotDeleteOrderV3Resp spot_delete_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)

Cancel order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_delete_order_v3_resp import SpotDeleteOrderV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    cancel_restrictions = '' # str | Supported values: <br/>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br/> `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000`. (optional)

    try:
        # Cancel order (TRADE)
        api_response = api_instance.spot_delete_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)
        print("The response of TradingApi->spot_delete_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_delete_order_v3: %s\n" % e)
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

[**SpotDeleteOrderV3Resp**](SpotDeleteOrderV3Resp.md)

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

# **spot_get_all_order_list_v3**
> List[SpotGetAllOrderListV3RespItem] spot_get_all_order_list_v3(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query all Order lists (USER_DATA)

Retrieves all order lists based on provided optional parameters.
Note that the time between startTime and endTime can't be longer than 24 hours.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_all_order_list_v3_resp_item import SpotGetAllOrderListV3RespItem
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
    api_instance = binance.spot.TradingApi(api_client)
    timestamp = 56 # int | 
    from_id = 56 # int | If supplied, neither `startTime` or `endTime` can be provided (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 56 # int | Default Value: 500; Max Value: 1000 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query all Order lists (USER_DATA)
        api_response = api_instance.spot_get_all_order_list_v3(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradingApi->spot_get_all_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_all_order_list_v3: %s\n" % e)
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

[**List[SpotGetAllOrderListV3RespItem]**](SpotGetAllOrderListV3RespItem.md)

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

# **spot_get_all_orders_v3**
> List[SpotGetAllOrdersV3RespItem] spot_get_all_orders_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_all_orders_v3_resp_item import SpotGetAllOrdersV3RespItem
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
    api_instance = binance.spot.TradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # All orders (USER_DATA)
        api_response = api_instance.spot_get_all_orders_v3(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradingApi->spot_get_all_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_all_orders_v3: %s\n" % e)
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

[**List[SpotGetAllOrdersV3RespItem]**](SpotGetAllOrdersV3RespItem.md)

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

# **spot_get_open_order_list_v3**
> List[SpotGetOpenOrderListV3RespItem] spot_get_open_order_list_v3(timestamp, recv_window=recv_window)

Query Open Order lists (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_open_order_list_v3_resp_item import SpotGetOpenOrderListV3RespItem
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
    api_instance = binance.spot.TradingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Open Order lists (USER_DATA)
        api_response = api_instance.spot_get_open_order_list_v3(timestamp, recv_window=recv_window)
        print("The response of TradingApi->spot_get_open_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_open_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[SpotGetOpenOrderListV3RespItem]**](SpotGetOpenOrderListV3RespItem.md)

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

# **spot_get_open_orders_v3**
> List[SpotGetOpenOrdersV3RespItem] spot_get_open_orders_v3(timestamp, symbol=symbol, recv_window=recv_window)

Current open orders (USER_DATA)

Get all open orders on a symbol. Careful when accessing this with no symbol.
Weight:
6 for a single symbol; 80 when the symbol parameter is omitted

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_open_orders_v3_resp_item import SpotGetOpenOrdersV3RespItem
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
    api_instance = binance.spot.TradingApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Current open orders (USER_DATA)
        api_response = api_instance.spot_get_open_orders_v3(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradingApi->spot_get_open_orders_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_open_orders_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[SpotGetOpenOrdersV3RespItem]**](SpotGetOpenOrdersV3RespItem.md)

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

# **spot_get_order_list_v3**
> SpotGetOrderListV3Resp spot_get_order_list_v3(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order list (USER_DATA)

Retrieves a specific order list based on provided optional parameters.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_order_list_v3_resp import SpotGetOrderListV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    orig_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Order list (USER_DATA)
        api_response = api_instance.spot_get_order_list_v3(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradingApi->spot_get_order_list_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_order_list_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] 
 **orig_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**SpotGetOrderListV3Resp**](SpotGetOrderListV3Resp.md)

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

# **spot_get_order_v3**
> SpotGetOrderV3Resp spot_get_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.spot_get_order_v3_resp import SpotGetOrderV3Resp
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
    api_instance = binance.spot.TradingApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query order (USER_DATA)
        api_response = api_instance.spot_get_order_v3(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradingApi->spot_get_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->spot_get_order_v3: %s\n" % e)
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

[**SpotGetOrderV3Resp**](SpotGetOrderV3Resp.md)

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

