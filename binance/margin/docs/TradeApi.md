# binance.margin.TradeApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_create_margin_api_key_v1**](TradeApi.md#margin_create_margin_api_key_v1) | **POST** /sapi/v1/margin/apiKey | Create Special Key(Low-Latency Trading)(TRADE)
[**margin_create_margin_exchange_small_liability_v1**](TradeApi.md#margin_create_margin_exchange_small_liability_v1) | **POST** /sapi/v1/margin/exchange-small-liability | Small Liability Exchange (MARGIN)
[**margin_create_margin_manual_liquidation_v1**](TradeApi.md#margin_create_margin_manual_liquidation_v1) | **POST** /sapi/v1/margin/manual-liquidation | Margin Manual Liquidation(MARGIN)
[**margin_create_margin_order_oco_v1**](TradeApi.md#margin_create_margin_order_oco_v1) | **POST** /sapi/v1/margin/order/oco | Margin Account New OCO (TRADE)
[**margin_create_margin_order_oto_v1**](TradeApi.md#margin_create_margin_order_oto_v1) | **POST** /sapi/v1/margin/order/oto | Margin Account New OTO (TRADE)
[**margin_create_margin_order_otoco_v1**](TradeApi.md#margin_create_margin_order_otoco_v1) | **POST** /sapi/v1/margin/order/otoco | Margin Account New OTOCO (TRADE)
[**margin_create_margin_order_v1**](TradeApi.md#margin_create_margin_order_v1) | **POST** /sapi/v1/margin/order | Margin Account New Order (TRADE)
[**margin_delete_margin_api_key_v1**](TradeApi.md#margin_delete_margin_api_key_v1) | **DELETE** /sapi/v1/margin/apiKey | Delete Special Key(Low-Latency Trading)(TRADE)
[**margin_delete_margin_open_orders_v1**](TradeApi.md#margin_delete_margin_open_orders_v1) | **DELETE** /sapi/v1/margin/openOrders | Margin Account Cancel all Open Orders on a Symbol (TRADE)
[**margin_delete_margin_order_list_v1**](TradeApi.md#margin_delete_margin_order_list_v1) | **DELETE** /sapi/v1/margin/orderList | Margin Account Cancel OCO (TRADE)
[**margin_delete_margin_order_v1**](TradeApi.md#margin_delete_margin_order_v1) | **DELETE** /sapi/v1/margin/order | Margin Account Cancel Order (TRADE)
[**margin_get_margin_all_order_list_v1**](TradeApi.md#margin_get_margin_all_order_list_v1) | **GET** /sapi/v1/margin/allOrderList | Query Margin Account&#39;s all OCO (USER_DATA)
[**margin_get_margin_all_orders_v1**](TradeApi.md#margin_get_margin_all_orders_v1) | **GET** /sapi/v1/margin/allOrders | Query Margin Account&#39;s All Orders (USER_DATA)
[**margin_get_margin_api_key_list_v1**](TradeApi.md#margin_get_margin_api_key_list_v1) | **GET** /sapi/v1/margin/api-key-list | Query Special key List(Low Latency Trading)(TRADE)
[**margin_get_margin_api_key_v1**](TradeApi.md#margin_get_margin_api_key_v1) | **GET** /sapi/v1/margin/apiKey | Query Special key(Low Latency Trading)(TRADE)
[**margin_get_margin_exchange_small_liability_history_v1**](TradeApi.md#margin_get_margin_exchange_small_liability_history_v1) | **GET** /sapi/v1/margin/exchange-small-liability-history | Get Small Liability Exchange History (USER_DATA)
[**margin_get_margin_exchange_small_liability_v1**](TradeApi.md#margin_get_margin_exchange_small_liability_v1) | **GET** /sapi/v1/margin/exchange-small-liability | Get Small Liability Exchange Coin List (USER_DATA)
[**margin_get_margin_force_liquidation_rec_v1**](TradeApi.md#margin_get_margin_force_liquidation_rec_v1) | **GET** /sapi/v1/margin/forceLiquidationRec | Get Force Liquidation Record (USER_DATA)
[**margin_get_margin_my_trades_v1**](TradeApi.md#margin_get_margin_my_trades_v1) | **GET** /sapi/v1/margin/myTrades | Query Margin Account&#39;s Trade List (USER_DATA)
[**margin_get_margin_open_order_list_v1**](TradeApi.md#margin_get_margin_open_order_list_v1) | **GET** /sapi/v1/margin/openOrderList | Query Margin Account&#39;s Open OCO (USER_DATA)
[**margin_get_margin_open_orders_v1**](TradeApi.md#margin_get_margin_open_orders_v1) | **GET** /sapi/v1/margin/openOrders | Query Margin Account&#39;s Open Orders (USER_DATA)
[**margin_get_margin_order_list_v1**](TradeApi.md#margin_get_margin_order_list_v1) | **GET** /sapi/v1/margin/orderList | Query Margin Account&#39;s OCO (USER_DATA)
[**margin_get_margin_order_v1**](TradeApi.md#margin_get_margin_order_v1) | **GET** /sapi/v1/margin/order | Query Margin Account&#39;s Order (USER_DATA)
[**margin_get_margin_rate_limit_order_v1**](TradeApi.md#margin_get_margin_rate_limit_order_v1) | **GET** /sapi/v1/margin/rateLimit/order | Query Current Margin Order Count Usage (TRADE)
[**margin_update_margin_api_key_ip_v1**](TradeApi.md#margin_update_margin_api_key_ip_v1) | **PUT** /sapi/v1/margin/apiKey/ip | Edit ip for Special Key(Low-Latency Trading)(TRADE)


# **margin_create_margin_api_key_v1**
> MarginCreateMarginApiKeyV1Resp margin_create_margin_api_key_v1(api_name, timestamp, ip=ip, permission_mode=permission_mode, public_key=public_key, recv_window=recv_window, symbol=symbol)

Create Special Key(Low-Latency Trading)(TRADE)

**Binance Margin offers low-latency trading through a special key, available exclusively to users with VIP level 4 or higher. **

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_api_key_v1_resp import MarginCreateMarginApiKeyV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    api_name = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip = '' # str |  (optional) (default to '')
    permission_mode = '' # str |  (optional) (default to '')
    public_key = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Create Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.margin_create_margin_api_key_v1(api_name, timestamp, ip=ip, permission_mode=permission_mode, public_key=public_key, recv_window=recv_window, symbol=symbol)
        print("The response of TradeApi->margin_create_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_api_key_v1: %s\n" % e)
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

[**MarginCreateMarginApiKeyV1Resp**](MarginCreateMarginApiKeyV1Resp.md)

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

# **margin_create_margin_exchange_small_liability_v1**
> MarginCreateMarginExchangeSmallLiabilityV1Resp margin_create_margin_exchange_small_liability_v1(asset_names, timestamp, recv_window=recv_window)

Small Liability Exchange (MARGIN)

Small Liability Exchange

### Example


```python
import binance.margin
from binance.margin.models.margin_create_margin_exchange_small_liability_v1_resp import MarginCreateMarginExchangeSmallLiabilityV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    asset_names = ['asset_names_example'] # List[str] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Small Liability Exchange (MARGIN)
        api_response = api_instance.margin_create_margin_exchange_small_liability_v1(asset_names, timestamp, recv_window=recv_window)
        print("The response of TradeApi->margin_create_margin_exchange_small_liability_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_exchange_small_liability_v1: %s\n" % e)
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

# **margin_create_margin_manual_liquidation_v1**
> MarginCreateMarginManualLiquidationV1Resp margin_create_margin_manual_liquidation_v1(timestamp, type, recv_window=recv_window, symbol=symbol)

Margin Manual Liquidation(MARGIN)

Margin Manual Liquidation

### Example


```python
import binance.margin
from binance.margin.models.margin_create_margin_manual_liquidation_v1_resp import MarginCreateMarginManualLiquidationV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Margin Manual Liquidation(MARGIN)
        api_response = api_instance.margin_create_margin_manual_liquidation_v1(timestamp, type, recv_window=recv_window, symbol=symbol)
        print("The response of TradeApi->margin_create_margin_manual_liquidation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_manual_liquidation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**MarginCreateMarginManualLiquidationV1Resp**](MarginCreateMarginManualLiquidationV1Resp.md)

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

# **margin_create_margin_order_oco_v1**
> MarginCreateMarginOrderOcoV1Resp margin_create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)

Margin Account New OCO (TRADE)

Send in a new OCO for a margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_order_oco_v1_resp import MarginCreateMarginOrderOcoV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)
        print("The response of TradeApi->margin_create_margin_order_oco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_order_oco_v1: %s\n" % e)
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

[**MarginCreateMarginOrderOcoV1Resp**](MarginCreateMarginOrderOcoV1Resp.md)

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

# **margin_create_margin_order_oto_v1**
> MarginCreateMarginOrderOtoV1Resp margin_create_margin_order_oto_v1(pending_quantity, pending_side, pending_type, symbol, working_iceberg_qty, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_time_in_force=working_time_in_force)

Margin Account New OTO (TRADE)

Post a new OTO order for margin account:

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_order_oto_v1_resp import MarginCreateMarginOrderOtoV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_create_margin_order_oto_v1(pending_quantity, pending_side, pending_type, symbol, working_iceberg_qty, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_client_order_id=pending_client_order_id, pending_iceberg_qty=pending_iceberg_qty, pending_price=pending_price, pending_stop_price=pending_stop_price, pending_time_in_force=pending_time_in_force, pending_trailing_delta=pending_trailing_delta, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_time_in_force=working_time_in_force)
        print("The response of TradeApi->margin_create_margin_order_oto_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_order_oto_v1: %s\n" % e)
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

[**MarginCreateMarginOrderOtoV1Resp**](MarginCreateMarginOrderOtoV1Resp.md)

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

# **margin_create_margin_order_otoco_v1**
> MarginCreateMarginOrderOtocoV1Resp margin_create_margin_order_otoco_v1(pending_above_type, pending_quantity, pending_side, symbol, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_time_in_force=working_time_in_force)

Margin Account New OTOCO (TRADE)

Post a new OTOCO order for margin account：

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_order_otoco_v1_resp import MarginCreateMarginOrderOtocoV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_create_margin_order_otoco_v1(pending_above_type, pending_quantity, pending_side, symbol, working_price, working_quantity, working_side, working_type, auto_repay_at_cancel=auto_repay_at_cancel, is_isolated=is_isolated, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, pending_above_client_order_id=pending_above_client_order_id, pending_above_iceberg_qty=pending_above_iceberg_qty, pending_above_price=pending_above_price, pending_above_stop_price=pending_above_stop_price, pending_above_time_in_force=pending_above_time_in_force, pending_above_trailing_delta=pending_above_trailing_delta, pending_below_client_order_id=pending_below_client_order_id, pending_below_iceberg_qty=pending_below_iceberg_qty, pending_below_price=pending_below_price, pending_below_stop_price=pending_below_stop_price, pending_below_time_in_force=pending_below_time_in_force, pending_below_trailing_delta=pending_below_trailing_delta, pending_below_type=pending_below_type, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, working_client_order_id=working_client_order_id, working_iceberg_qty=working_iceberg_qty, working_time_in_force=working_time_in_force)
        print("The response of TradeApi->margin_create_margin_order_otoco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_order_otoco_v1: %s\n" % e)
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

[**MarginCreateMarginOrderOtocoV1Resp**](MarginCreateMarginOrderOtocoV1Resp.md)

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

# **margin_create_margin_order_v1**
> MarginCreateMarginOrderV1Resp margin_create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, is_isolated=is_isolated, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)

Margin Account New Order (TRADE)

Post a new order for margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_create_margin_order_v1_resp import MarginCreateMarginOrderV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, is_isolated=is_isolated, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)
        print("The response of TradeApi->margin_create_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_create_margin_order_v1: %s\n" % e)
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

# **margin_delete_margin_api_key_v1**
> object margin_delete_margin_api_key_v1(timestamp, api_key=api_key, api_name=api_name, symbol=symbol, recv_window=recv_window)

Delete Special Key(Low-Latency Trading)(TRADE)

This only applies to Special Key for Low Latency Trading.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    api_key = '' # str |  (optional) (default to '')
    api_name = '' # str |  (optional) (default to '')
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Delete Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.margin_delete_margin_api_key_v1(timestamp, api_key=api_key, api_name=api_name, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->margin_delete_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_delete_margin_api_key_v1: %s\n" % e)
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

# **margin_delete_margin_open_orders_v1**
> List[MarginDeleteMarginOpenOrdersV1RespItem] margin_delete_margin_open_orders_v1(symbol, timestamp, is_isolated=is_isolated, recv_window=recv_window)

Margin Account Cancel all Open Orders on a Symbol (TRADE)

Cancels all active orders on a symbol for margin account.
This includes OCO orders.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_delete_margin_open_orders_v1_resp_item import MarginDeleteMarginOpenOrdersV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel all Open Orders on a Symbol (TRADE)
        api_response = api_instance.margin_delete_margin_open_orders_v1(symbol, timestamp, is_isolated=is_isolated, recv_window=recv_window)
        print("The response of TradeApi->margin_delete_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_delete_margin_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginDeleteMarginOpenOrdersV1RespItem]**](MarginDeleteMarginOpenOrdersV1RespItem.md)

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

# **margin_delete_margin_order_list_v1**
> MarginDeleteMarginOrderListV1Resp margin_delete_margin_order_list_v1(symbol, timestamp, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel OCO (TRADE)

Cancel an entire Order List for a margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_delete_margin_order_list_v1_resp import MarginDeleteMarginOrderListV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel OCO (TRADE)
        api_response = api_instance.margin_delete_margin_order_list_v1(symbol, timestamp, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->margin_delete_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_delete_margin_order_list_v1: %s\n" % e)
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

[**MarginDeleteMarginOrderListV1Resp**](MarginDeleteMarginOrderListV1Resp.md)

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

# **margin_delete_margin_order_v1**
> MarginDeleteMarginOrderV1Resp margin_delete_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel Order (TRADE)

Cancel an active order for margin account.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_delete_margin_order_v1_resp import MarginDeleteMarginOrderV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Account Cancel Order (TRADE)
        api_response = api_instance.margin_delete_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->margin_delete_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_delete_margin_order_v1: %s\n" % e)
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

[**MarginDeleteMarginOrderV1Resp**](MarginDeleteMarginOrderV1Resp.md)

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

# **margin_get_margin_all_order_list_v1**
> List[MarginGetMarginAllOrderListV1RespItem] margin_get_margin_all_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's all OCO (USER_DATA)

Retrieves all OCO for a specific margin account based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_all_order_list_v1_resp_item import MarginGetMarginAllOrderListV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_get_margin_all_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_all_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_all_order_list_v1: %s\n" % e)
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

[**List[MarginGetMarginAllOrderListV1RespItem]**](MarginGetMarginAllOrderListV1RespItem.md)

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

# **margin_get_margin_all_orders_v1**
> List[MarginGetMarginAllOrdersV1RespItem] margin_get_margin_all_orders_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's All Orders (USER_DATA)

Query Margin Account's All Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_all_orders_v1_resp_item import MarginGetMarginAllOrdersV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_get_margin_all_orders_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_all_orders_v1: %s\n" % e)
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

[**List[MarginGetMarginAllOrdersV1RespItem]**](MarginGetMarginAllOrdersV1RespItem.md)

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

# **margin_get_margin_api_key_list_v1**
> List[MarginGetMarginApiKeyListV1RespItem] margin_get_margin_api_key_list_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query Special key List(Low Latency Trading)(TRADE)

This only applies to Special Key for Low Latency Trading.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_api_key_list_v1_resp_item import MarginGetMarginApiKeyListV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Special key List(Low Latency Trading)(TRADE)
        api_response = api_instance.margin_get_margin_api_key_list_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_api_key_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_api_key_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**| isolated margin pair | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginApiKeyListV1RespItem]**](MarginGetMarginApiKeyListV1RespItem.md)

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

# **margin_get_margin_api_key_v1**
> MarginGetMarginApiKeyV1Resp margin_get_margin_api_key_v1(api_key, timestamp, symbol=symbol, recv_window=recv_window)

Query Special key(Low Latency Trading)(TRADE)

Query Special Key Information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_api_key_v1_resp import MarginGetMarginApiKeyV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    symbol = '' # str | isolated margin pair (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Special key(Low Latency Trading)(TRADE)
        api_response = api_instance.margin_get_margin_api_key_v1(api_key, timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **symbol** | **str**| isolated margin pair | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**MarginGetMarginApiKeyV1Resp**](MarginGetMarginApiKeyV1Resp.md)

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

# **margin_get_margin_exchange_small_liability_history_v1**
> MarginGetMarginExchangeSmallLiabilityHistoryV1Resp margin_get_margin_exchange_small_liability_history_v1(current, size, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)

Get Small Liability Exchange History (USER_DATA)

Get Small liability Exchange History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_exchange_small_liability_history_v1_resp import MarginGetMarginExchangeSmallLiabilityHistoryV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    current = 56 # int | Currently querying page. Start from 1. Default:1
    size = 56 # int | Default:10, Max:100
    timestamp = 56 # int | 
    start_time = 56 # int | Default: 30 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Small Liability Exchange History (USER_DATA)
        api_response = api_instance.margin_get_margin_exchange_small_liability_history_v1(current, size, timestamp, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_exchange_small_liability_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_exchange_small_liability_history_v1: %s\n" % e)
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

[**MarginGetMarginExchangeSmallLiabilityHistoryV1Resp**](MarginGetMarginExchangeSmallLiabilityHistoryV1Resp.md)

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

# **margin_get_margin_exchange_small_liability_v1**
> List[MarginGetMarginExchangeSmallLiabilityV1RespItem] margin_get_margin_exchange_small_liability_v1(timestamp, recv_window=recv_window)

Get Small Liability Exchange Coin List (USER_DATA)

Query the coins which can be small liability exchange

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_exchange_small_liability_v1_resp_item import MarginGetMarginExchangeSmallLiabilityV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Small Liability Exchange Coin List (USER_DATA)
        api_response = api_instance.margin_get_margin_exchange_small_liability_v1(timestamp, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_exchange_small_liability_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_exchange_small_liability_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[MarginGetMarginExchangeSmallLiabilityV1RespItem]**](MarginGetMarginExchangeSmallLiabilityV1RespItem.md)

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

# **margin_get_margin_force_liquidation_rec_v1**
> MarginGetMarginForceLiquidationRecV1Resp margin_get_margin_force_liquidation_rec_v1(timestamp, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)

Get Force Liquidation Record (USER_DATA)

Get Force Liquidation Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_force_liquidation_rec_v1_resp import MarginGetMarginForceLiquidationRecV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    isolated_symbol = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Get Force Liquidation Record (USER_DATA)
        api_response = api_instance.margin_get_margin_force_liquidation_rec_v1(timestamp, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_force_liquidation_rec_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_force_liquidation_rec_v1: %s\n" % e)
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

[**MarginGetMarginForceLiquidationRecV1Resp**](MarginGetMarginForceLiquidationRecV1Resp.md)

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

# **margin_get_margin_my_trades_v1**
> List[MarginGetMarginMyTradesV1RespItem] margin_get_margin_my_trades_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Query Margin Account's Trade List (USER_DATA)

Query Margin Account's Trade List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_my_trades_v1_resp_item import MarginGetMarginMyTradesV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
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
        api_response = api_instance.margin_get_margin_my_trades_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_my_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_my_trades_v1: %s\n" % e)
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

[**List[MarginGetMarginMyTradesV1RespItem]**](MarginGetMarginMyTradesV1RespItem.md)

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

# **margin_get_margin_open_order_list_v1**
> List[MarginGetMarginOpenOrderListV1RespItem] margin_get_margin_open_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Margin Account's Open OCO (USER_DATA)

Query Margin Account's Open OCO

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_open_order_list_v1_resp_item import MarginGetMarginOpenOrderListV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | mandatory for isolated margin, not supported for cross margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Open OCO (USER_DATA)
        api_response = api_instance.margin_get_margin_open_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_open_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_open_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| mandatory for isolated margin, not supported for cross margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginOpenOrderListV1RespItem]**](MarginGetMarginOpenOrderListV1RespItem.md)

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

# **margin_get_margin_open_orders_v1**
> List[MarginGetMarginOpenOrdersV1RespItem] margin_get_margin_open_orders_v1(timestamp, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)

Query Margin Account's Open Orders (USER_DATA)

Query Margin Account's Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_open_orders_v1_resp_item import MarginGetMarginOpenOrdersV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Open Orders (USER_DATA)
        api_response = api_instance.margin_get_margin_open_orders_v1(timestamp, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_open_orders_v1: %s\n" % e)
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

# **margin_get_margin_order_list_v1**
> MarginGetMarginOrderListV1Resp margin_get_margin_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_order_list_v1_resp import MarginGetMarginOrderListV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | mandatory for isolated margin, not supported for cross margin (optional) (default to '')
    order_list_id = 56 # int | Either `orderListId` or `origClientOrderId` must be provided (optional)
    orig_client_order_id = '' # str | Either `orderListId` or `origClientOrderId` must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's OCO (USER_DATA)
        api_response = api_instance.margin_get_margin_order_list_v1(timestamp, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_order_list_v1: %s\n" % e)
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

[**MarginGetMarginOrderListV1Resp**](MarginGetMarginOrderListV1Resp.md)

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

# **margin_get_margin_order_v1**
> MarginGetMarginOrderV1Resp margin_get_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's Order (USER_DATA)

Query Margin Account's Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_order_v1_resp import MarginGetMarginOrderV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Account's Order (USER_DATA)
        api_response = api_instance.margin_get_margin_order_v1(symbol, timestamp, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_order_v1: %s\n" % e)
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

[**MarginGetMarginOrderV1Resp**](MarginGetMarginOrderV1Resp.md)

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

# **margin_get_margin_rate_limit_order_v1**
> List[MarginGetMarginRateLimitOrderV1RespItem] margin_get_margin_rate_limit_order_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Current Margin Order Count Usage (TRADE)

Displays the user's current margin order count usage for all intervals.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_rate_limit_order_v1_resp_item import MarginGetMarginRateLimitOrderV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    timestamp = 56 # int | 
    is_isolated = '' # str | for isolated margin or not, &#34;TRUE&#34;, &#34;FALSE&#34;，default &#34;FALSE&#34; (optional) (default to '')
    symbol = '' # str | isolated symbol, mandatory for isolated margin (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Current Margin Order Count Usage (TRADE)
        api_response = api_instance.margin_get_margin_rate_limit_order_v1(timestamp, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->margin_get_margin_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_get_margin_rate_limit_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **is_isolated** | **str**| for isolated margin or not, &amp;#34;TRUE&amp;#34;, &amp;#34;FALSE&amp;#34;，default &amp;#34;FALSE&amp;#34; | [optional] [default to &#39;&#39;]
 **symbol** | **str**| isolated symbol, mandatory for isolated margin | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginRateLimitOrderV1RespItem]**](MarginGetMarginRateLimitOrderV1RespItem.md)

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

# **margin_update_margin_api_key_ip_v1**
> object margin_update_margin_api_key_ip_v1(api_key, ip, timestamp, recv_window=recv_window, symbol=symbol)

Edit ip for Special Key(Low-Latency Trading)(TRADE)

Edit ip restriction. This only applies to Special Key for Low Latency Trading.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.TradeApi(api_client)
    api_key = '' # str |  (default to '')
    ip = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Edit ip for Special Key(Low-Latency Trading)(TRADE)
        api_response = api_instance.margin_update_margin_api_key_ip_v1(api_key, ip, timestamp, recv_window=recv_window, symbol=symbol)
        print("The response of TradeApi->margin_update_margin_api_key_ip_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->margin_update_margin_api_key_ip_v1: %s\n" % e)
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

