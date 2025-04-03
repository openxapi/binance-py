# binance.derivatives.umfutures.TradeApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_create_batch_orders_v1**](TradeApi.md#umfutures_create_batch_orders_v1) | **POST** /fapi/v1/batchOrders | Place Multiple Orders(TRADE)
[**umfutures_create_countdown_cancel_all_v1**](TradeApi.md#umfutures_create_countdown_cancel_all_v1) | **POST** /fapi/v1/countdownCancelAll | Auto-Cancel All Open Orders (TRADE)
[**umfutures_create_leverage_v1**](TradeApi.md#umfutures_create_leverage_v1) | **POST** /fapi/v1/leverage | Change Initial Leverage(TRADE)
[**umfutures_create_margin_type_v1**](TradeApi.md#umfutures_create_margin_type_v1) | **POST** /fapi/v1/marginType | Change Margin Type(TRADE)
[**umfutures_create_multi_assets_margin_v1**](TradeApi.md#umfutures_create_multi_assets_margin_v1) | **POST** /fapi/v1/multiAssetsMargin | Change Multi-Assets Mode (TRADE)
[**umfutures_create_order_test_v1**](TradeApi.md#umfutures_create_order_test_v1) | **POST** /fapi/v1/order/test | Test Order(TRADE)
[**umfutures_create_order_v1**](TradeApi.md#umfutures_create_order_v1) | **POST** /fapi/v1/order | New Order(TRADE)
[**umfutures_create_position_margin_v1**](TradeApi.md#umfutures_create_position_margin_v1) | **POST** /fapi/v1/positionMargin | Modify Isolated Position Margin(TRADE)
[**umfutures_create_position_side_dual_v1**](TradeApi.md#umfutures_create_position_side_dual_v1) | **POST** /fapi/v1/positionSide/dual | Change Position Mode(TRADE)
[**umfutures_delete_all_open_orders_v1**](TradeApi.md#umfutures_delete_all_open_orders_v1) | **DELETE** /fapi/v1/allOpenOrders | Cancel All Open Orders (TRADE)
[**umfutures_delete_batch_orders_v1**](TradeApi.md#umfutures_delete_batch_orders_v1) | **DELETE** /fapi/v1/batchOrders | Cancel Multiple Orders (TRADE)
[**umfutures_delete_order_v1**](TradeApi.md#umfutures_delete_order_v1) | **DELETE** /fapi/v1/order | Cancel Order (TRADE)
[**umfutures_get_adl_quantile_v1**](TradeApi.md#umfutures_get_adl_quantile_v1) | **GET** /fapi/v1/adlQuantile | Position ADL Quantile Estimation(USER_DATA)
[**umfutures_get_all_orders_v1**](TradeApi.md#umfutures_get_all_orders_v1) | **GET** /fapi/v1/allOrders | All Orders (USER_DATA)
[**umfutures_get_force_orders_v1**](TradeApi.md#umfutures_get_force_orders_v1) | **GET** /fapi/v1/forceOrders | User&#39;s Force Orders (USER_DATA)
[**umfutures_get_open_order_v1**](TradeApi.md#umfutures_get_open_order_v1) | **GET** /fapi/v1/openOrder | Query Current Open Order (USER_DATA)
[**umfutures_get_open_orders_v1**](TradeApi.md#umfutures_get_open_orders_v1) | **GET** /fapi/v1/openOrders | Current All Open Orders (USER_DATA)
[**umfutures_get_order_amendment_v1**](TradeApi.md#umfutures_get_order_amendment_v1) | **GET** /fapi/v1/orderAmendment | Get Order Modify History (USER_DATA)
[**umfutures_get_order_v1**](TradeApi.md#umfutures_get_order_v1) | **GET** /fapi/v1/order | Query Order (USER_DATA)
[**umfutures_get_position_margin_history_v1**](TradeApi.md#umfutures_get_position_margin_history_v1) | **GET** /fapi/v1/positionMargin/history | Get Position Margin Change History (TRADE)
[**umfutures_get_position_risk_v2**](TradeApi.md#umfutures_get_position_risk_v2) | **GET** /fapi/v2/positionRisk | Position Information V2 (USER_DATA)
[**umfutures_get_position_risk_v3**](TradeApi.md#umfutures_get_position_risk_v3) | **GET** /fapi/v3/positionRisk | Position Information V3 (USER_DATA)
[**umfutures_get_user_trades_v1**](TradeApi.md#umfutures_get_user_trades_v1) | **GET** /fapi/v1/userTrades | Account Trade List (USER_DATA)
[**umfutures_update_batch_orders_v1**](TradeApi.md#umfutures_update_batch_orders_v1) | **PUT** /fapi/v1/batchOrders | Modify Multiple Orders(TRADE)
[**umfutures_update_order_v1**](TradeApi.md#umfutures_update_order_v1) | **PUT** /fapi/v1/order | Modify Order (TRADE)


# **umfutures_create_batch_orders_v1**
> List[UmfuturesCreateBatchOrdersV1RespInner] umfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Place Multiple Orders(TRADE)

Place Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_req_batch_orders_item import UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_create_batch_orders_v1_resp_inner import UmfuturesCreateBatchOrdersV1RespInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    batch_orders = [binance.derivatives.umfutures.UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesCreateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Place Multiple Orders(TRADE)
        api_response = api_instance.umfutures_create_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_batch_orders_v1: %s\n" % e)
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

# **umfutures_create_countdown_cancel_all_v1**
> UmfuturesCreateCountdownCancelAllV1Resp umfutures_create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)

Auto-Cancel All Open Orders (TRADE)

Cancel all open orders of the specified symbol at the end of the specified countdown.
The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_resp import UmfuturesCreateCountdownCancelAllV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    umfutures_create_countdown_cancel_all_v1_req = binance.derivatives.umfutures.UmfuturesCreateCountdownCancelAllV1Req() # UmfuturesCreateCountdownCancelAllV1Req |  (optional)

    try:
        # Auto-Cancel All Open Orders (TRADE)
        api_response = api_instance.umfutures_create_countdown_cancel_all_v1(umfutures_create_countdown_cancel_all_v1_req=umfutures_create_countdown_cancel_all_v1_req)
        print("The response of TradeApi->umfutures_create_countdown_cancel_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_countdown_cancel_all_v1: %s\n" % e)
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

# **umfutures_create_leverage_v1**
> UmfuturesCreateLeverageV1Resp umfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change Initial Leverage(TRADE)

Change user's initial leverage of specific symbol market.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_leverage_v1_resp import UmfuturesCreateLeverageV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Initial Leverage(TRADE)
        api_response = api_instance.umfutures_create_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateLeverageV1Resp**](UmfuturesCreateLeverageV1Resp.md)

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

# **umfutures_create_margin_type_v1**
> UmfuturesCreateMarginTypeV1Resp umfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)

Change Margin Type(TRADE)

Change symbol level margin type

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_margin_type_v1_resp import UmfuturesCreateMarginTypeV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    margin_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Margin Type(TRADE)
        api_response = api_instance.umfutures_create_margin_type_v1(margin_type, symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_margin_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_margin_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateMarginTypeV1Resp**](UmfuturesCreateMarginTypeV1Resp.md)

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

# **umfutures_create_multi_assets_margin_v1**
> UmfuturesCreateMultiAssetsMarginV1Resp umfutures_create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)

Change Multi-Assets Mode (TRADE)

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_multi_assets_margin_v1_resp import UmfuturesCreateMultiAssetsMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    multi_assets_margin = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Multi-Assets Mode (TRADE)
        api_response = api_instance.umfutures_create_multi_assets_margin_v1(multi_assets_margin, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_multi_assets_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_multi_assets_margin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_assets_margin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreateMultiAssetsMarginV1Resp**](UmfuturesCreateMultiAssetsMarginV1Resp.md)

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

# **umfutures_create_order_test_v1**
> UmfuturesCreateOrderTestV1Resp umfutures_create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

Test Order(TRADE)

Testing order request, this order will not be submitted to matching engine

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_order_test_v1_resp import UmfuturesCreateOrderTestV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
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
        api_response = api_instance.umfutures_create_order_test_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of TradeApi->umfutures_create_order_test_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_order_test_v1: %s\n" % e)
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

[**UmfuturesCreateOrderTestV1Resp**](UmfuturesCreateOrderTestV1Resp.md)

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

# **umfutures_create_order_v1**
> UmfuturesCreateOrderV1Resp umfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New Order(TRADE)

Send in a new order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_order_v1_resp import UmfuturesCreateOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
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
        api_response = api_instance.umfutures_create_order_v1(side, symbol, timestamp, type, activation_price=activation_price, callback_rate=callback_rate, close_position=close_position, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of TradeApi->umfutures_create_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_order_v1: %s\n" % e)
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

[**UmfuturesCreateOrderV1Resp**](UmfuturesCreateOrderV1Resp.md)

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

# **umfutures_create_position_margin_v1**
> UmfuturesCreatePositionMarginV1Resp umfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)

Modify Isolated Position Margin(TRADE)

Modify Isolated Position Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_position_margin_v1_resp import UmfuturesCreatePositionMarginV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    amount = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 
    position_side = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Modify Isolated Position Margin(TRADE)
        api_response = api_instance.umfutures_create_position_margin_v1(amount, symbol, timestamp, type, position_side=position_side, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_position_margin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_position_margin_v1: %s\n" % e)
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

[**UmfuturesCreatePositionMarginV1Resp**](UmfuturesCreatePositionMarginV1Resp.md)

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

# **umfutures_create_position_side_dual_v1**
> UmfuturesCreatePositionSideDualV1Resp umfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_create_position_side_dual_v1_resp import UmfuturesCreatePositionSideDualV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Position Mode(TRADE)
        api_response = api_instance.umfutures_create_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_create_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_create_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesCreatePositionSideDualV1Resp**](UmfuturesCreatePositionSideDualV1Resp.md)

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

# **umfutures_delete_all_open_orders_v1**
> UmfuturesDeleteAllOpenOrdersV1Resp umfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All Open Orders (TRADE)

Cancel All Open Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_all_open_orders_v1_resp import UmfuturesDeleteAllOpenOrdersV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All Open Orders (TRADE)
        api_response = api_instance.umfutures_delete_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_delete_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_delete_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**UmfuturesDeleteAllOpenOrdersV1Resp**](UmfuturesDeleteAllOpenOrdersV1Resp.md)

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

# **umfutures_delete_batch_orders_v1**
> List[UmfuturesDeleteBatchOrdersV1RespInner] umfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)

Cancel Multiple Orders (TRADE)

Cancel Multiple Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_batch_orders_v1_resp_inner import UmfuturesDeleteBatchOrdersV1RespInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id_list = [56] # List[int] | max length 10 <br/> e.g. [1234567,2345678] (optional)
    orig_client_order_id_list = ['orig_client_order_id_list_example'] # List[str] | max length 10<br/> e.g. [&#34;my_id_1&#34;,&#34;my_id_2&#34;], encode the double quotes. No space after comma. (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Multiple Orders (TRADE)
        api_response = api_instance.umfutures_delete_batch_orders_v1(symbol, timestamp, order_id_list=order_id_list, orig_client_order_id_list=orig_client_order_id_list, recv_window=recv_window)
        print("The response of TradeApi->umfutures_delete_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_delete_batch_orders_v1: %s\n" % e)
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

# **umfutures_delete_order_v1**
> UmfuturesDeleteOrderV1Resp umfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel Order (TRADE)

Cancel an active order.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_delete_order_v1_resp import UmfuturesDeleteOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel Order (TRADE)
        api_response = api_instance.umfutures_delete_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->umfutures_delete_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_delete_order_v1: %s\n" % e)
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

[**UmfuturesDeleteOrderV1Resp**](UmfuturesDeleteOrderV1Resp.md)

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

# **umfutures_get_adl_quantile_v1**
> List[UmfuturesGetAdlQuantileV1RespItem] umfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

Position ADL Quantile Estimation(USER_DATA)

Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item import UmfuturesGetAdlQuantileV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.umfutures_get_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetAdlQuantileV1RespItem]**](UmfuturesGetAdlQuantileV1RespItem.md)

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

# **umfutures_get_all_orders_v1**
> List[UmfuturesGetAllOrdersV1RespItem] umfutures_get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_all_orders_v1_resp_item import UmfuturesGetAllOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # All Orders (USER_DATA)
        api_response = api_instance.umfutures_get_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_all_orders_v1: %s\n" % e)
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

[**List[UmfuturesGetAllOrdersV1RespItem]**](UmfuturesGetAllOrdersV1RespItem.md)

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

# **umfutures_get_force_orders_v1**
> List[UmfuturesGetForceOrdersV1RespItem] umfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

User's Force Orders (USER_DATA)

Query user's Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_force_orders_v1_resp_item import UmfuturesGetForceOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | &#34;LIQUIDATION&#34; for liquidation orders, &#34;ADL&#34; for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # User's Force Orders (USER_DATA)
        api_response = api_instance.umfutures_get_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_force_orders_v1: %s\n" % e)
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

[**List[UmfuturesGetForceOrdersV1RespItem]**](UmfuturesGetForceOrdersV1RespItem.md)

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

# **umfutures_get_open_order_v1**
> UmfuturesGetOpenOrderV1Resp umfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current Open Order (USER_DATA)

Query open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_order_v1_resp import UmfuturesGetOpenOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current Open Order (USER_DATA)
        api_response = api_instance.umfutures_get_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_open_order_v1: %s\n" % e)
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

[**UmfuturesGetOpenOrderV1Resp**](UmfuturesGetOpenOrderV1Resp.md)

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

# **umfutures_get_open_orders_v1**
> List[UmfuturesGetOpenOrdersV1RespItem] umfutures_get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Current All Open Orders (USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_orders_v1_resp_item import UmfuturesGetOpenOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Current All Open Orders (USER_DATA)
        api_response = api_instance.umfutures_get_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetOpenOrdersV1RespItem]**](UmfuturesGetOpenOrdersV1RespItem.md)

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

# **umfutures_get_order_amendment_v1**
> List[UmfuturesGetOrderAmendmentV1RespItem] umfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Order Modify History (USER_DATA)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item import UmfuturesGetOrderAmendmentV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
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
        api_response = api_instance.umfutures_get_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_order_amendment_v1: %s\n" % e)
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

[**List[UmfuturesGetOrderAmendmentV1RespItem]**](UmfuturesGetOrderAmendmentV1RespItem.md)

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

# **umfutures_get_order_v1**
> UmfuturesGetOrderV1Resp umfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order (USER_DATA)

Check an order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_order_v1_resp import UmfuturesGetOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Order (USER_DATA)
        api_response = api_instance.umfutures_get_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_order_v1: %s\n" % e)
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

[**UmfuturesGetOrderV1Resp**](UmfuturesGetOrderV1Resp.md)

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

# **umfutures_get_position_margin_history_v1**
> List[UmfuturesGetPositionMarginHistoryV1RespItem] umfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Position Margin Change History (TRADE)

Get Position Margin Change History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_margin_history_v1_resp_item import UmfuturesGetPositionMarginHistoryV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1: Add position margin，2: Reduce position margin (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int | Default current time if not pass (optional)
    limit = 500 # int | Default: 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Position Margin Change History (TRADE)
        api_response = api_instance.umfutures_get_position_margin_history_v1(symbol, timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_position_margin_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_position_margin_history_v1: %s\n" % e)
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

[**List[UmfuturesGetPositionMarginHistoryV1RespItem]**](UmfuturesGetPositionMarginHistoryV1RespItem.md)

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

# **umfutures_get_position_risk_v2**
> List[UmfuturesGetPositionRiskV2RespItem] umfutures_get_position_risk_v2(timestamp, symbol=symbol, recv_window=recv_window)

Position Information V2 (USER_DATA)

Get current position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_risk_v2_resp_item import UmfuturesGetPositionRiskV2RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information V2 (USER_DATA)
        api_response = api_instance.umfutures_get_position_risk_v2(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_position_risk_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_position_risk_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetPositionRiskV2RespItem]**](UmfuturesGetPositionRiskV2RespItem.md)

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

# **umfutures_get_position_risk_v3**
> List[UmfuturesGetPositionRiskV3RespItem] umfutures_get_position_risk_v3(timestamp, symbol=symbol, recv_window=recv_window)

Position Information V3 (USER_DATA)

Get current position information(only symbol that has position or open orders will be returned).

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_position_risk_v3_resp_item import UmfuturesGetPositionRiskV3RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Position Information V3 (USER_DATA)
        api_response = api_instance.umfutures_get_position_risk_v3(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_position_risk_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_position_risk_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetPositionRiskV3RespItem]**](UmfuturesGetPositionRiskV3RespItem.md)

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

# **umfutures_get_user_trades_v1**
> List[UmfuturesGetUserTradesV1RespItem] umfutures_get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_user_trades_v1_resp_item import UmfuturesGetUserTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
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
        api_response = api_instance.umfutures_get_user_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->umfutures_get_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_get_user_trades_v1: %s\n" % e)
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

[**List[UmfuturesGetUserTradesV1RespItem]**](UmfuturesGetUserTradesV1RespItem.md)

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

# **umfutures_update_batch_orders_v1**
> List[UmfuturesUpdateBatchOrdersV1RespItem] umfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)

Modify Multiple Orders(TRADE)

Modify Multiple Orders (TRADE)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_req_batch_orders_item import UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
from binance.derivatives.umfutures.models.umfutures_update_batch_orders_v1_resp_item import UmfuturesUpdateBatchOrdersV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
    batch_orders = [binance.derivatives.umfutures.UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem()] # List[UmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem] | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Modify Multiple Orders(TRADE)
        api_response = api_instance.umfutures_update_batch_orders_v1(batch_orders, timestamp, recv_window=recv_window)
        print("The response of TradeApi->umfutures_update_batch_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_update_batch_orders_v1: %s\n" % e)
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

# **umfutures_update_order_v1**
> UmfuturesUpdateOrderV1Resp umfutures_update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify Order (TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_update_order_v1_resp import UmfuturesUpdateOrderV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.umfutures.Configuration(
    auth=binance.derivatives.umfutures.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.TradeApi(api_client)
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
        api_response = api_instance.umfutures_update_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of TradeApi->umfutures_update_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->umfutures_update_order_v1: %s\n" % e)
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

[**UmfuturesUpdateOrderV1Resp**](UmfuturesUpdateOrderV1Resp.md)

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

