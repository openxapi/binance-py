# binance.derivatives.pmargin.TradeApi

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmargin_create_cm_conditional_order_v1**](TradeApi.md#pmargin_create_cm_conditional_order_v1) | **POST** /papi/v1/cm/conditional/order | New CM Conditional Order(TRADE)
[**pmargin_create_cm_order_v1**](TradeApi.md#pmargin_create_cm_order_v1) | **POST** /papi/v1/cm/order | New CM Order(TRADE)
[**pmargin_create_margin_loan_v1**](TradeApi.md#pmargin_create_margin_loan_v1) | **POST** /papi/v1/marginLoan | Margin Account Borrow(MARGIN)
[**pmargin_create_margin_order_oco_v1**](TradeApi.md#pmargin_create_margin_order_oco_v1) | **POST** /papi/v1/margin/order/oco | Margin Account New OCO(TRADE)
[**pmargin_create_margin_order_v1**](TradeApi.md#pmargin_create_margin_order_v1) | **POST** /papi/v1/margin/order | New Margin Order(TRADE)
[**pmargin_create_margin_repay_debt_v1**](TradeApi.md#pmargin_create_margin_repay_debt_v1) | **POST** /papi/v1/margin/repay-debt | Margin Account Repay Debt(TRADE)
[**pmargin_create_repay_loan_v1**](TradeApi.md#pmargin_create_repay_loan_v1) | **POST** /papi/v1/repayLoan | Margin Account Repay(MARGIN)
[**pmargin_create_um_conditional_order_v1**](TradeApi.md#pmargin_create_um_conditional_order_v1) | **POST** /papi/v1/um/conditional/order | New UM Conditional Order (TRADE)
[**pmargin_create_um_fee_burn_v1**](TradeApi.md#pmargin_create_um_fee_burn_v1) | **POST** /papi/v1/um/feeBurn | Toggle BNB Burn On UM Futures Trade (TRADE)
[**pmargin_create_um_order_v1**](TradeApi.md#pmargin_create_um_order_v1) | **POST** /papi/v1/um/order | New UM Order (TRADE)
[**pmargin_delete_cm_all_open_orders_v1**](TradeApi.md#pmargin_delete_cm_all_open_orders_v1) | **DELETE** /papi/v1/cm/allOpenOrders | Cancel All CM Open Orders(TRADE)
[**pmargin_delete_cm_conditional_all_open_orders_v1**](TradeApi.md#pmargin_delete_cm_conditional_all_open_orders_v1) | **DELETE** /papi/v1/cm/conditional/allOpenOrders | Cancel All CM Open Conditional Orders(TRADE)
[**pmargin_delete_cm_conditional_order_v1**](TradeApi.md#pmargin_delete_cm_conditional_order_v1) | **DELETE** /papi/v1/cm/conditional/order | Cancel CM Conditional Order(TRADE)
[**pmargin_delete_cm_order_v1**](TradeApi.md#pmargin_delete_cm_order_v1) | **DELETE** /papi/v1/cm/order | Cancel CM Order(TRADE)
[**pmargin_delete_margin_all_open_orders_v1**](TradeApi.md#pmargin_delete_margin_all_open_orders_v1) | **DELETE** /papi/v1/margin/allOpenOrders | Cancel Margin Account All Open Orders on a Symbol(TRADE)
[**pmargin_delete_margin_order_list_v1**](TradeApi.md#pmargin_delete_margin_order_list_v1) | **DELETE** /papi/v1/margin/orderList | Cancel Margin Account OCO Orders(TRADE)
[**pmargin_delete_margin_order_v1**](TradeApi.md#pmargin_delete_margin_order_v1) | **DELETE** /papi/v1/margin/order | Cancel Margin Account Order(TRADE)
[**pmargin_delete_um_all_open_orders_v1**](TradeApi.md#pmargin_delete_um_all_open_orders_v1) | **DELETE** /papi/v1/um/allOpenOrders | Cancel All UM Open Orders(TRADE)
[**pmargin_delete_um_conditional_all_open_orders_v1**](TradeApi.md#pmargin_delete_um_conditional_all_open_orders_v1) | **DELETE** /papi/v1/um/conditional/allOpenOrders | Cancel All UM Open Conditional Orders (TRADE)
[**pmargin_delete_um_conditional_order_v1**](TradeApi.md#pmargin_delete_um_conditional_order_v1) | **DELETE** /papi/v1/um/conditional/order | Cancel UM Conditional Order(TRADE)
[**pmargin_delete_um_order_v1**](TradeApi.md#pmargin_delete_um_order_v1) | **DELETE** /papi/v1/um/order | Cancel UM Order(TRADE)
[**pmargin_get_cm_adl_quantile_v1**](TradeApi.md#pmargin_get_cm_adl_quantile_v1) | **GET** /papi/v1/cm/adlQuantile | CM Position ADL Quantile Estimation(USER_DATA)
[**pmargin_get_cm_all_orders_v1**](TradeApi.md#pmargin_get_cm_all_orders_v1) | **GET** /papi/v1/cm/allOrders | Query All CM Orders (USER_DATA)
[**pmargin_get_cm_conditional_all_orders_v1**](TradeApi.md#pmargin_get_cm_conditional_all_orders_v1) | **GET** /papi/v1/cm/conditional/allOrders | Query All CM Conditional Orders(USER_DATA)
[**pmargin_get_cm_conditional_open_order_v1**](TradeApi.md#pmargin_get_cm_conditional_open_order_v1) | **GET** /papi/v1/cm/conditional/openOrder | Query Current CM Open Conditional Order(USER_DATA)
[**pmargin_get_cm_conditional_open_orders_v1**](TradeApi.md#pmargin_get_cm_conditional_open_orders_v1) | **GET** /papi/v1/cm/conditional/openOrders | Query All Current CM Open Conditional Orders (USER_DATA)
[**pmargin_get_cm_conditional_order_history_v1**](TradeApi.md#pmargin_get_cm_conditional_order_history_v1) | **GET** /papi/v1/cm/conditional/orderHistory | Query CM Conditional Order History(USER_DATA)
[**pmargin_get_cm_force_orders_v1**](TradeApi.md#pmargin_get_cm_force_orders_v1) | **GET** /papi/v1/cm/forceOrders | Query User&#39;s CM Force Orders(USER_DATA)
[**pmargin_get_cm_open_order_v1**](TradeApi.md#pmargin_get_cm_open_order_v1) | **GET** /papi/v1/cm/openOrder | Query Current CM Open Order (USER_DATA)
[**pmargin_get_cm_open_orders_v1**](TradeApi.md#pmargin_get_cm_open_orders_v1) | **GET** /papi/v1/cm/openOrders | Query All Current CM Open Orders(USER_DATA)
[**pmargin_get_cm_order_amendment_v1**](TradeApi.md#pmargin_get_cm_order_amendment_v1) | **GET** /papi/v1/cm/orderAmendment | Query CM Modify Order History(TRADE)
[**pmargin_get_cm_order_v1**](TradeApi.md#pmargin_get_cm_order_v1) | **GET** /papi/v1/cm/order | Query CM Order(USER_DATA)
[**pmargin_get_cm_user_trades_v1**](TradeApi.md#pmargin_get_cm_user_trades_v1) | **GET** /papi/v1/cm/userTrades | CM Account Trade List(USER_DATA)
[**pmargin_get_margin_all_order_list_v1**](TradeApi.md#pmargin_get_margin_all_order_list_v1) | **GET** /papi/v1/margin/allOrderList | Query Margin Account&#39;s all OCO (USER_DATA)
[**pmargin_get_margin_all_orders_v1**](TradeApi.md#pmargin_get_margin_all_orders_v1) | **GET** /papi/v1/margin/allOrders | Query All Margin Account Orders (USER_DATA)
[**pmargin_get_margin_force_orders_v1**](TradeApi.md#pmargin_get_margin_force_orders_v1) | **GET** /papi/v1/margin/forceOrders | Query User&#39;s Margin Force Orders(USER_DATA)
[**pmargin_get_margin_my_trades_v1**](TradeApi.md#pmargin_get_margin_my_trades_v1) | **GET** /papi/v1/margin/myTrades | Margin Account Trade List (USER_DATA)
[**pmargin_get_margin_open_order_list_v1**](TradeApi.md#pmargin_get_margin_open_order_list_v1) | **GET** /papi/v1/margin/openOrderList | Query Margin Account&#39;s Open OCO (USER_DATA)
[**pmargin_get_margin_open_orders_v1**](TradeApi.md#pmargin_get_margin_open_orders_v1) | **GET** /papi/v1/margin/openOrders | Query Current Margin Open Order (USER_DATA)
[**pmargin_get_margin_order_list_v1**](TradeApi.md#pmargin_get_margin_order_list_v1) | **GET** /papi/v1/margin/orderList | Query Margin Account&#39;s OCO (USER_DATA)
[**pmargin_get_margin_order_v1**](TradeApi.md#pmargin_get_margin_order_v1) | **GET** /papi/v1/margin/order | Query Margin Account Order (USER_DATA)
[**pmargin_get_um_adl_quantile_v1**](TradeApi.md#pmargin_get_um_adl_quantile_v1) | **GET** /papi/v1/um/adlQuantile | UM Position ADL Quantile Estimation(USER_DATA)
[**pmargin_get_um_all_orders_v1**](TradeApi.md#pmargin_get_um_all_orders_v1) | **GET** /papi/v1/um/allOrders | Query All UM Orders(USER_DATA)
[**pmargin_get_um_conditional_all_orders_v1**](TradeApi.md#pmargin_get_um_conditional_all_orders_v1) | **GET** /papi/v1/um/conditional/allOrders | Query All UM Conditional Orders(USER_DATA)
[**pmargin_get_um_conditional_open_order_v1**](TradeApi.md#pmargin_get_um_conditional_open_order_v1) | **GET** /papi/v1/um/conditional/openOrder | Query Current UM Open Conditional Order(USER_DATA)
[**pmargin_get_um_conditional_open_orders_v1**](TradeApi.md#pmargin_get_um_conditional_open_orders_v1) | **GET** /papi/v1/um/conditional/openOrders | Query All Current UM Open Conditional Orders(USER_DATA)
[**pmargin_get_um_conditional_order_history_v1**](TradeApi.md#pmargin_get_um_conditional_order_history_v1) | **GET** /papi/v1/um/conditional/orderHistory | Query UM Conditional Order History(USER_DATA)
[**pmargin_get_um_fee_burn_v1**](TradeApi.md#pmargin_get_um_fee_burn_v1) | **GET** /papi/v1/um/feeBurn | Get UM Futures BNB Burn Status (USER_DATA)
[**pmargin_get_um_force_orders_v1**](TradeApi.md#pmargin_get_um_force_orders_v1) | **GET** /papi/v1/um/forceOrders | Query User&#39;s UM Force Orders (USER_DATA)
[**pmargin_get_um_open_order_v1**](TradeApi.md#pmargin_get_um_open_order_v1) | **GET** /papi/v1/um/openOrder | Query Current UM Open Order(USER_DATA)
[**pmargin_get_um_open_orders_v1**](TradeApi.md#pmargin_get_um_open_orders_v1) | **GET** /papi/v1/um/openOrders | Query All Current UM Open Orders(USER_DATA)
[**pmargin_get_um_order_amendment_v1**](TradeApi.md#pmargin_get_um_order_amendment_v1) | **GET** /papi/v1/um/orderAmendment | Query UM Modify Order History(TRADE)
[**pmargin_get_um_order_v1**](TradeApi.md#pmargin_get_um_order_v1) | **GET** /papi/v1/um/order | Query UM Order (USER_DATA)
[**pmargin_get_um_user_trades_v1**](TradeApi.md#pmargin_get_um_user_trades_v1) | **GET** /papi/v1/um/userTrades | UM Account Trade List(USER_DATA)
[**pmargin_update_cm_order_v1**](TradeApi.md#pmargin_update_cm_order_v1) | **PUT** /papi/v1/cm/order | Modify CM Order(TRADE)
[**pmargin_update_um_order_v1**](TradeApi.md#pmargin_update_um_order_v1) | **PUT** /papi/v1/um/order | Modify UM Order(TRADE)


# **pmargin_create_cm_conditional_order_v1**
> PmarginCreateCmConditionalOrderV1Resp pmargin_create_cm_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New CM Conditional Order(TRADE)

New CM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_cm_conditional_order_v1_resp import PmarginCreateCmConditionalOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    side = '' # str |  (default to '')
    strategy_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    new_client_strategy_id = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_protect = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    stop_price = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')
    working_type = '' # str |  (optional) (default to '')

    try:
        # New CM Conditional Order(TRADE)
        api_response = api_instance.pmargin_create_cm_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of TradeApi->pmargin_create_cm_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_cm_conditional_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **strategy_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **activation_price** | **str**|  | [optional] [default to &#39;&#39;]
 **callback_rate** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_protect** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_price** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]
 **working_type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PmarginCreateCmConditionalOrderV1Resp**](PmarginCreateCmConditionalOrderV1Resp.md)

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

# **pmargin_create_cm_order_v1**
> PmarginCreateCmOrderV1Resp pmargin_create_cm_order_v1(side, symbol, timestamp, type, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)

New CM Order(TRADE)

Place new CM order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_cm_order_v1_resp import PmarginCreateCmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # New CM Order(TRADE)
        api_response = api_instance.pmargin_create_cm_order_v1(side, symbol, timestamp, type, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)
        print("The response of TradeApi->pmargin_create_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_cm_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PmarginCreateCmOrderV1Resp**](PmarginCreateCmOrderV1Resp.md)

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

# **pmargin_create_margin_loan_v1**
> PmarginCreateMarginLoanV1Resp pmargin_create_margin_loan_v1(amount, asset, timestamp, recv_window=recv_window)

Margin Account Borrow(MARGIN)

Apply for a margin loan.

### Example


```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_margin_loan_v1_resp import PmarginCreateMarginLoanV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Account Borrow(MARGIN)
        api_response = api_instance.pmargin_create_margin_loan_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_create_margin_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_margin_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateMarginLoanV1Resp**](PmarginCreateMarginLoanV1Resp.md)

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

# **pmargin_create_margin_order_oco_v1**
> PmarginCreateMarginOrderOcoV1Resp pmargin_create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)

Margin Account New OCO(TRADE)

Send in a new OCO for a margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_margin_order_oco_v1_resp import PmarginCreateMarginOrderOcoV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    price = '' # str |  (default to '')
    quantity = '' # str |  (default to '')
    side = '' # str |  (default to '')
    stop_price = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    limit_client_order_id = '' # str |  (optional) (default to '')
    limit_iceberg_qty = '' # str |  (optional) (default to '')
    list_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    side_effect_type = '' # str |  (optional) (default to '')
    stop_client_order_id = '' # str |  (optional) (default to '')
    stop_iceberg_qty = '' # str |  (optional) (default to '')
    stop_limit_price = '' # str |  (optional) (default to '')
    stop_limit_time_in_force = '' # str |  (optional) (default to '')

    try:
        # Margin Account New OCO(TRADE)
        api_response = api_instance.pmargin_create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)
        print("The response of TradeApi->pmargin_create_margin_order_oco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_margin_order_oco_v1: %s\n" % e)
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
 **list_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **side_effect_type** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_iceberg_qty** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_price** | **str**|  | [optional] [default to &#39;&#39;]
 **stop_limit_time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PmarginCreateMarginOrderOcoV1Resp**](PmarginCreateMarginOrderOcoV1Resp.md)

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

# **pmargin_create_margin_order_v1**
> PmarginCreateMarginOrderV1Resp pmargin_create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)

New Margin Order(TRADE)

New Margin Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_margin_order_v1_resp import PmarginCreateMarginOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    auto_repay_at_cancel = True # bool |  (optional)
    iceberg_qty = '' # str |  (optional) (default to '')
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
        # New Margin Order(TRADE)
        api_response = api_instance.pmargin_create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)
        print("The response of TradeApi->pmargin_create_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_margin_order_v1: %s\n" % e)
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

[**PmarginCreateMarginOrderV1Resp**](PmarginCreateMarginOrderV1Resp.md)

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

# **pmargin_create_margin_repay_debt_v1**
> PmarginCreateMarginRepayDebtV1Resp pmargin_create_margin_repay_debt_v1(asset, timestamp, amount=amount, recv_window=recv_window, specify_repay_assets=specify_repay_assets)

Margin Account Repay Debt(TRADE)

Repay debt for a margin loan.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_margin_repay_debt_v1_resp import PmarginCreateMarginRepayDebtV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    specify_repay_assets = '' # str |  (optional) (default to '')

    try:
        # Margin Account Repay Debt(TRADE)
        api_response = api_instance.pmargin_create_margin_repay_debt_v1(asset, timestamp, amount=amount, recv_window=recv_window, specify_repay_assets=specify_repay_assets)
        print("The response of TradeApi->pmargin_create_margin_repay_debt_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_margin_repay_debt_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **specify_repay_assets** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PmarginCreateMarginRepayDebtV1Resp**](PmarginCreateMarginRepayDebtV1Resp.md)

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

# **pmargin_create_repay_loan_v1**
> PmarginCreateRepayLoanV1Resp pmargin_create_repay_loan_v1(amount, asset, timestamp, recv_window=recv_window)

Margin Account Repay(MARGIN)

Repay for a margin loan.

### Example


```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_repay_loan_v1_resp import PmarginCreateRepayLoanV1Resp
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Account Repay(MARGIN)
        api_response = api_instance.pmargin_create_repay_loan_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_create_repay_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_repay_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateRepayLoanV1Resp**](PmarginCreateRepayLoanV1Resp.md)

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

# **pmargin_create_um_conditional_order_v1**
> PmarginCreateUmConditionalOrderV1Resp pmargin_create_um_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, good_till_date=good_till_date, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New UM Conditional Order (TRADE)

Place new UM conditional order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_um_conditional_order_v1_resp import PmarginCreateUmConditionalOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    side = '' # str |  (default to '')
    strategy_type = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    activation_price = '' # str |  (optional) (default to '')
    callback_rate = '' # str |  (optional) (default to '')
    good_till_date = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
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
        # New UM Conditional Order (TRADE)
        api_response = api_instance.pmargin_create_um_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, good_till_date=good_till_date, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of TradeApi->pmargin_create_um_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_um_conditional_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **strategy_type** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **activation_price** | **str**|  | [optional] [default to &#39;&#39;]
 **callback_rate** | **str**|  | [optional] [default to &#39;&#39;]
 **good_till_date** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
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

[**PmarginCreateUmConditionalOrderV1Resp**](PmarginCreateUmConditionalOrderV1Resp.md)

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

# **pmargin_create_um_fee_burn_v1**
> PmarginCreateUmFeeBurnV1Resp pmargin_create_um_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)

Toggle BNB Burn On UM Futures Trade (TRADE)

Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_um_fee_burn_v1_resp import PmarginCreateUmFeeBurnV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    fee_burn = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Toggle BNB Burn On UM Futures Trade (TRADE)
        api_response = api_instance.pmargin_create_um_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_create_um_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_um_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_burn** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginCreateUmFeeBurnV1Resp**](PmarginCreateUmFeeBurnV1Resp.md)

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

# **pmargin_create_um_order_v1**
> PmarginCreateUmOrderV1Resp pmargin_create_um_order_v1(side, symbol, timestamp, type, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, time_in_force=time_in_force)

New UM Order (TRADE)

Place new UM order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_create_um_order_v1_resp import PmarginCreateUmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    side = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = '' # str |  (default to '')
    good_till_date = 56 # int |  (optional)
    new_client_order_id = '' # str |  (optional) (default to '')
    new_order_resp_type = '' # str |  (optional) (default to '')
    position_side = '' # str |  (optional) (default to '')
    price = '' # str |  (optional) (default to '')
    price_match = '' # str |  (optional) (default to '')
    quantity = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    reduce_only = '' # str |  (optional) (default to '')
    self_trade_prevention_mode = '' # str |  (optional) (default to '')
    time_in_force = '' # str |  (optional) (default to '')

    try:
        # New UM Order (TRADE)
        api_response = api_instance.pmargin_create_um_order_v1(side, symbol, timestamp, type, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, time_in_force=time_in_force)
        print("The response of TradeApi->pmargin_create_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_create_um_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **str**|  | [default to &#39;&#39;]
 **good_till_date** | **int**|  | [optional] 
 **new_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_order_resp_type** | **str**|  | [optional] [default to &#39;&#39;]
 **position_side** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **str**|  | [optional] [default to &#39;&#39;]
 **price_match** | **str**|  | [optional] [default to &#39;&#39;]
 **quantity** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **reduce_only** | **str**|  | [optional] [default to &#39;&#39;]
 **self_trade_prevention_mode** | **str**|  | [optional] [default to &#39;&#39;]
 **time_in_force** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PmarginCreateUmOrderV1Resp**](PmarginCreateUmOrderV1Resp.md)

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

# **pmargin_delete_cm_all_open_orders_v1**
> PmarginDeleteCmAllOpenOrdersV1Resp pmargin_delete_cm_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All CM Open Orders(TRADE)

Cancel all active LIMIT orders on specific symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_cm_all_open_orders_v1_resp import PmarginDeleteCmAllOpenOrdersV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All CM Open Orders(TRADE)
        api_response = api_instance.pmargin_delete_cm_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_cm_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_cm_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteCmAllOpenOrdersV1Resp**](PmarginDeleteCmAllOpenOrdersV1Resp.md)

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

# **pmargin_delete_cm_conditional_all_open_orders_v1**
> PmarginDeleteCmConditionalAllOpenOrdersV1Resp pmargin_delete_cm_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All CM Open Conditional Orders(TRADE)

Cancel All CM Open Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_cm_conditional_all_open_orders_v1_resp import PmarginDeleteCmConditionalAllOpenOrdersV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All CM Open Conditional Orders(TRADE)
        api_response = api_instance.pmargin_delete_cm_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_cm_conditional_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_cm_conditional_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteCmConditionalAllOpenOrdersV1Resp**](PmarginDeleteCmConditionalAllOpenOrdersV1Resp.md)

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

# **pmargin_delete_cm_conditional_order_v1**
> PmarginDeleteCmConditionalOrderV1Resp pmargin_delete_cm_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Cancel CM Conditional Order(TRADE)

Cancel CM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_cm_conditional_order_v1_resp import PmarginDeleteCmConditionalOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel CM Conditional Order(TRADE)
        api_response = api_instance.pmargin_delete_cm_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_cm_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_cm_conditional_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteCmConditionalOrderV1Resp**](PmarginDeleteCmConditionalOrderV1Resp.md)

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

# **pmargin_delete_cm_order_v1**
> PmarginDeleteCmOrderV1Resp pmargin_delete_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel CM Order(TRADE)

Cancel an active LIMIT order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_cm_order_v1_resp import PmarginDeleteCmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel CM Order(TRADE)
        api_response = api_instance.pmargin_delete_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_cm_order_v1: %s\n" % e)
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

[**PmarginDeleteCmOrderV1Resp**](PmarginDeleteCmOrderV1Resp.md)

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

# **pmargin_delete_margin_all_open_orders_v1**
> List[PmarginDeleteMarginAllOpenOrdersV1RespInner] pmargin_delete_margin_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel Margin Account All Open Orders on a Symbol(TRADE)

Cancel Margin Account All Open Orders on a Symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_inner import PmarginDeleteMarginAllOpenOrdersV1RespInner
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Margin Account All Open Orders on a Symbol(TRADE)
        api_response = api_instance.pmargin_delete_margin_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_margin_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_margin_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginDeleteMarginAllOpenOrdersV1RespInner]**](PmarginDeleteMarginAllOpenOrdersV1RespInner.md)

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

# **pmargin_delete_margin_order_list_v1**
> PmarginDeleteMarginOrderListV1Resp pmargin_delete_margin_order_list_v1(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Margin Account OCO Orders(TRADE)

Cancel Margin Account OCO Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_margin_order_list_v1_resp import PmarginDeleteMarginOrderListV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Margin Account OCO Orders(TRADE)
        api_response = api_instance.pmargin_delete_margin_order_list_v1(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_margin_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] 
 **list_client_order_id** | **str**| Either &#x60;orderListId&#x60; or &#x60;listClientOrderId&#x60; must be provided | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginDeleteMarginOrderListV1Resp**](PmarginDeleteMarginOrderListV1Resp.md)

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

# **pmargin_delete_margin_order_v1**
> PmarginDeleteMarginOrderV1Resp pmargin_delete_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Margin Account Order(TRADE)

Cancel Margin Account Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_margin_order_v1_resp import PmarginDeleteMarginOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel Margin Account Order(TRADE)
        api_response = api_instance.pmargin_delete_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_margin_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default. | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**PmarginDeleteMarginOrderV1Resp**](PmarginDeleteMarginOrderV1Resp.md)

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

# **pmargin_delete_um_all_open_orders_v1**
> PmarginDeleteUmAllOpenOrdersV1Resp pmargin_delete_um_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All UM Open Orders(TRADE)

Cancel all active LIMIT orders on specific symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_um_all_open_orders_v1_resp import PmarginDeleteUmAllOpenOrdersV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All UM Open Orders(TRADE)
        api_response = api_instance.pmargin_delete_um_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_um_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_um_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteUmAllOpenOrdersV1Resp**](PmarginDeleteUmAllOpenOrdersV1Resp.md)

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

# **pmargin_delete_um_conditional_all_open_orders_v1**
> PmarginDeleteUmConditionalAllOpenOrdersV1Resp pmargin_delete_um_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All UM Open Conditional Orders (TRADE)

Cancel All UM Open Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_um_conditional_all_open_orders_v1_resp import PmarginDeleteUmConditionalAllOpenOrdersV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All UM Open Conditional Orders (TRADE)
        api_response = api_instance.pmargin_delete_um_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_um_conditional_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_um_conditional_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteUmConditionalAllOpenOrdersV1Resp**](PmarginDeleteUmConditionalAllOpenOrdersV1Resp.md)

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

# **pmargin_delete_um_conditional_order_v1**
> PmarginDeleteUmConditionalOrderV1Resp pmargin_delete_um_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Cancel UM Conditional Order(TRADE)

Cancel UM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_um_conditional_order_v1_resp import PmarginDeleteUmConditionalOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel UM Conditional Order(TRADE)
        api_response = api_instance.pmargin_delete_um_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_um_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_um_conditional_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginDeleteUmConditionalOrderV1Resp**](PmarginDeleteUmConditionalOrderV1Resp.md)

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

# **pmargin_delete_um_order_v1**
> PmarginDeleteUmOrderV1Resp pmargin_delete_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel UM Order(TRADE)

Cancel an active UM LIMIT order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_delete_um_order_v1_resp import PmarginDeleteUmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel UM Order(TRADE)
        api_response = api_instance.pmargin_delete_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_delete_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_delete_um_order_v1: %s\n" % e)
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

[**PmarginDeleteUmOrderV1Resp**](PmarginDeleteUmOrderV1Resp.md)

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

# **pmargin_get_cm_adl_quantile_v1**
> List[PmarginGetCmAdlQuantileV1RespItem] pmargin_get_cm_adl_quantile_v1()

CM Position ADL Quantile Estimation(USER_DATA)

Query CM Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_adl_quantile_v1_resp_item import PmarginGetCmAdlQuantileV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)

    try:
        # CM Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.pmargin_get_cm_adl_quantile_v1()
        print("The response of TradeApi->pmargin_get_cm_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_adl_quantile_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PmarginGetCmAdlQuantileV1RespItem]**](PmarginGetCmAdlQuantileV1RespItem.md)

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

# **pmargin_get_cm_all_orders_v1**
> List[PmarginGetCmAllOrdersV1RespItem] pmargin_get_cm_all_orders_v1(symbol, timestamp, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All CM Orders (USER_DATA)

Get all account CM orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_all_orders_v1_resp_item import PmarginGetCmAllOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    pair = '' # str |  (optional) (default to '')
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Query All CM Orders (USER_DATA)
        api_response = api_instance.pmargin_get_cm_all_orders_v1(symbol, timestamp, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmAllOrdersV1RespItem]**](PmarginGetCmAllOrdersV1RespItem.md)

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

# **pmargin_get_cm_conditional_all_orders_v1**
> List[PmarginGetCmConditionalAllOrdersV1RespItem] pmargin_get_cm_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All CM Conditional Orders(USER_DATA)

Query All CM Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_all_orders_v1_resp_item import PmarginGetCmConditionalAllOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All CM Conditional Orders(USER_DATA)
        api_response = api_instance.pmargin_get_cm_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_conditional_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_conditional_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmConditionalAllOrdersV1RespItem]**](PmarginGetCmConditionalAllOrdersV1RespItem.md)

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

# **pmargin_get_cm_conditional_open_order_v1**
> PmarginGetCmConditionalOpenOrderV1Resp pmargin_get_cm_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query Current CM Open Conditional Order(USER_DATA)

Query Current CM Open Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_open_order_v1_resp import PmarginGetCmConditionalOpenOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current CM Open Conditional Order(USER_DATA)
        api_response = api_instance.pmargin_get_cm_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_conditional_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_conditional_open_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetCmConditionalOpenOrderV1Resp**](PmarginGetCmConditionalOpenOrderV1Resp.md)

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

# **pmargin_get_cm_conditional_open_orders_v1**
> List[PmarginGetCmConditionalOpenOrdersV1RespItem] pmargin_get_cm_conditional_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query All Current CM Open Conditional Orders (USER_DATA)

Get all open conditional orders on a symbol. Careful when accessing this with no symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_open_orders_v1_resp_item import PmarginGetCmConditionalOpenOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current CM Open Conditional Orders (USER_DATA)
        api_response = api_instance.pmargin_get_cm_conditional_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_conditional_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_conditional_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmConditionalOpenOrdersV1RespItem]**](PmarginGetCmConditionalOpenOrdersV1RespItem.md)

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

# **pmargin_get_cm_conditional_order_history_v1**
> PmarginGetCmConditionalOrderHistoryV1Resp pmargin_get_cm_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query CM Conditional Order History(USER_DATA)

Query CM Conditional Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_order_history_v1_resp import PmarginGetCmConditionalOrderHistoryV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Conditional Order History(USER_DATA)
        api_response = api_instance.pmargin_get_cm_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_conditional_order_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_conditional_order_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetCmConditionalOrderHistoryV1Resp**](PmarginGetCmConditionalOrderHistoryV1Resp.md)

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

# **pmargin_get_cm_force_orders_v1**
> List[PmarginGetCmForceOrdersV1RespItem] pmargin_get_cm_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query User's CM Force Orders(USER_DATA)

Query User's CM Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_force_orders_v1_resp_item import PmarginGetCmForceOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | &#34;LIQUIDATION&#34; for liquidation orders, &#34;ADL&#34; for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's CM Force Orders(USER_DATA)
        api_response = api_instance.pmargin_get_cm_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_force_orders_v1: %s\n" % e)
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
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetCmForceOrdersV1RespItem]**](PmarginGetCmForceOrdersV1RespItem.md)

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

# **pmargin_get_cm_open_order_v1**
> PmarginGetCmOpenOrderV1Resp pmargin_get_cm_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current CM Open Order (USER_DATA)

Query current CM open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_open_order_v1_resp import PmarginGetCmOpenOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current CM Open Order (USER_DATA)
        api_response = api_instance.pmargin_get_cm_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_open_order_v1: %s\n" % e)
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

[**PmarginGetCmOpenOrderV1Resp**](PmarginGetCmOpenOrderV1Resp.md)

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

# **pmargin_get_cm_open_orders_v1**
> List[PmarginGetCmOpenOrdersV1RespItem] pmargin_get_cm_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)

Query All Current CM Open Orders(USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_open_orders_v1_resp_item import PmarginGetCmOpenOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current CM Open Orders(USER_DATA)
        api_response = api_instance.pmargin_get_cm_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmOpenOrdersV1RespItem]**](PmarginGetCmOpenOrdersV1RespItem.md)

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

# **pmargin_get_cm_order_amendment_v1**
> List[PmarginGetCmOrderAmendmentV1RespItem] pmargin_get_cm_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query CM Modify Order History(TRADE)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item import PmarginGetCmOrderAmendmentV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get modification history from INCLUSIVE (optional)
    end_time = 56 # int | Timestamp in ms to get modification history until INCLUSIVE (optional)
    limit = 50 # int | Default 50, max 100 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Modify Order History(TRADE)
        api_response = api_instance.pmargin_get_cm_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_order_amendment_v1: %s\n" % e)
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
 **limit** | **int**| Default 50, max 100 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmOrderAmendmentV1RespItem]**](PmarginGetCmOrderAmendmentV1RespItem.md)

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

# **pmargin_get_cm_order_v1**
> PmarginGetCmOrderV1Resp pmargin_get_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query CM Order(USER_DATA)

Check an CM order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_order_v1_resp import PmarginGetCmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Order(USER_DATA)
        api_response = api_instance.pmargin_get_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_order_v1: %s\n" % e)
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

[**PmarginGetCmOrderV1Resp**](PmarginGetCmOrderV1Resp.md)

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

# **pmargin_get_cm_user_trades_v1**
> List[PmarginGetCmUserTradesV1RespItem] pmargin_get_cm_user_trades_v1(timestamp, symbol=symbol, pair=pair, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

CM Account Trade List(USER_DATA)

Get trades for a specific account and CM symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_cm_user_trades_v1_resp_item import PmarginGetCmUserTradesV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 50 # int | Default 50; max 1000. (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # CM Account Trade List(USER_DATA)
        api_response = api_instance.pmargin_get_cm_user_trades_v1(timestamp, symbol=symbol, pair=pair, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_cm_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_cm_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 50; max 1000. | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetCmUserTradesV1RespItem]**](PmarginGetCmUserTradesV1RespItem.md)

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

# **pmargin_get_margin_all_order_list_v1**
> List[PmarginGetMarginAllOrderListV1RespItem] pmargin_get_margin_all_order_list_v1(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's all OCO (USER_DATA)

Query all OCO for a specific margin account based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_all_order_list_v1_resp_item import PmarginGetMarginAllOrderListV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    from_id = 56 # int | If supplied, neither startTime or endTime can be provided (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 500. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's all OCO (USER_DATA)
        api_response = api_instance.pmargin_get_margin_all_order_list_v1(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_all_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_all_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_id** | **int**| If supplied, neither startTime or endTime can be provided | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 500. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetMarginAllOrderListV1RespItem]**](PmarginGetMarginAllOrderListV1RespItem.md)

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

# **pmargin_get_margin_all_orders_v1**
> List[PmarginGetMarginAllOrdersV1RespItem] pmargin_get_margin_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All Margin Account Orders (USER_DATA)

Query All Margin Account Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_all_orders_v1_resp_item import PmarginGetMarginAllOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 500. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query All Margin Account Orders (USER_DATA)
        api_response = api_instance.pmargin_get_margin_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 500. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetMarginAllOrdersV1RespItem]**](PmarginGetMarginAllOrdersV1RespItem.md)

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

# **pmargin_get_margin_force_orders_v1**
> PmarginGetMarginForceOrdersV1Resp pmargin_get_margin_force_orders_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Query User's Margin Force Orders(USER_DATA)

Query user's margin force orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_force_orders_v1_resp import PmarginGetMarginForceOrdersV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's Margin Force Orders(USER_DATA)
        api_response = api_instance.pmargin_get_margin_force_orders_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetMarginForceOrdersV1Resp**](PmarginGetMarginForceOrdersV1Resp.md)

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

# **pmargin_get_margin_my_trades_v1**
> List[PmarginGetMarginMyTradesV1RespItem] pmargin_get_margin_my_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Margin Account Trade List (USER_DATA)

Margin Account Trade List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_my_trades_v1_resp_item import PmarginGetMarginMyTradesV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Margin Account Trade List (USER_DATA)
        api_response = api_instance.pmargin_get_margin_my_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_my_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_my_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetMarginMyTradesV1RespItem]**](PmarginGetMarginMyTradesV1RespItem.md)

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

# **pmargin_get_margin_open_order_list_v1**
> List[PmarginGetMarginOpenOrderListV1RespItem] pmargin_get_margin_open_order_list_v1(timestamp, recv_window=recv_window)

Query Margin Account's Open OCO (USER_DATA)

Query Margin Account's Open OCO

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_open_order_list_v1_resp_item import PmarginGetMarginOpenOrderListV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's Open OCO (USER_DATA)
        api_response = api_instance.pmargin_get_margin_open_order_list_v1(timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_open_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_open_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetMarginOpenOrderListV1RespItem]**](PmarginGetMarginOpenOrderListV1RespItem.md)

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

# **pmargin_get_margin_open_orders_v1**
> List[PmarginGetMarginOpenOrdersV1RespItem] pmargin_get_margin_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Query Current Margin Open Order (USER_DATA)

Query Current Margin Open Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_open_orders_v1_resp_item import PmarginGetMarginOpenOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Current Margin Open Order (USER_DATA)
        api_response = api_instance.pmargin_get_margin_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetMarginOpenOrdersV1RespItem]**](PmarginGetMarginOpenOrdersV1RespItem.md)

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

# **pmargin_get_margin_order_list_v1**
> PmarginGetMarginOrderListV1Resp pmargin_get_margin_order_list_v1(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_order_list_v1_resp import PmarginGetMarginOrderListV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either orderListId or origClientOrderId must be provided (optional)
    orig_client_order_id = '' # str | Either orderListId or origClientOrderId must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's OCO (USER_DATA)
        api_response = api_instance.pmargin_get_margin_order_list_v1(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either orderListId or origClientOrderId must be provided | [optional] 
 **orig_client_order_id** | **str**| Either orderListId or origClientOrderId must be provided | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetMarginOrderListV1Resp**](PmarginGetMarginOrderListV1Resp.md)

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

# **pmargin_get_margin_order_v1**
> PmarginGetMarginOrderV1Resp pmargin_get_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account Order (USER_DATA)

Query Margin Account Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_margin_order_v1_resp import PmarginGetMarginOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account Order (USER_DATA)
        api_response = api_instance.pmargin_get_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_margin_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **orig_client_order_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**PmarginGetMarginOrderV1Resp**](PmarginGetMarginOrderV1Resp.md)

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

# **pmargin_get_um_adl_quantile_v1**
> List[PmarginGetUmAdlQuantileV1RespItem] pmargin_get_um_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Position ADL Quantile Estimation(USER_DATA)

Query UM Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_adl_quantile_v1_resp_item import PmarginGetUmAdlQuantileV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.pmargin_get_um_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmAdlQuantileV1RespItem]**](PmarginGetUmAdlQuantileV1RespItem.md)

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

# **pmargin_get_um_all_orders_v1**
> List[PmarginGetUmAllOrdersV1RespItem] pmargin_get_um_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All UM Orders(USER_DATA)

Get all account UM orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_all_orders_v1_resp_item import PmarginGetUmAllOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All UM Orders(USER_DATA)
        api_response = api_instance.pmargin_get_um_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_all_orders_v1: %s\n" % e)
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

[**List[PmarginGetUmAllOrdersV1RespItem]**](PmarginGetUmAllOrdersV1RespItem.md)

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

# **pmargin_get_um_conditional_all_orders_v1**
> List[PmarginGetUmConditionalAllOrdersV1RespItem] pmargin_get_um_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All UM Conditional Orders(USER_DATA)

Query All UM Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_conditional_all_orders_v1_resp_item import PmarginGetUmConditionalAllOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All UM Conditional Orders(USER_DATA)
        api_response = api_instance.pmargin_get_um_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_conditional_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_conditional_all_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **strategy_id** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmConditionalAllOrdersV1RespItem]**](PmarginGetUmConditionalAllOrdersV1RespItem.md)

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

# **pmargin_get_um_conditional_open_order_v1**
> PmarginGetUmConditionalOpenOrderV1Resp pmargin_get_um_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query Current UM Open Conditional Order(USER_DATA)

Query Current UM Open Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_conditional_open_order_v1_resp import PmarginGetUmConditionalOpenOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current UM Open Conditional Order(USER_DATA)
        api_response = api_instance.pmargin_get_um_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_conditional_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_conditional_open_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmConditionalOpenOrderV1Resp**](PmarginGetUmConditionalOpenOrderV1Resp.md)

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

# **pmargin_get_um_conditional_open_orders_v1**
> List[PmarginGetUmConditionalOpenOrdersV1RespItem] pmargin_get_um_conditional_open_orders_v1()

Query All Current UM Open Conditional Orders(USER_DATA)

Get all open conditional orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_conditional_open_orders_v1_resp_item import PmarginGetUmConditionalOpenOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)

    try:
        # Query All Current UM Open Conditional Orders(USER_DATA)
        api_response = api_instance.pmargin_get_um_conditional_open_orders_v1()
        print("The response of TradeApi->pmargin_get_um_conditional_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_conditional_open_orders_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PmarginGetUmConditionalOpenOrdersV1RespItem]**](PmarginGetUmConditionalOpenOrdersV1RespItem.md)

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

# **pmargin_get_um_conditional_order_history_v1**
> PmarginGetUmConditionalOrderHistoryV1Resp pmargin_get_um_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query UM Conditional Order History(USER_DATA)

Query UM Conditional Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_conditional_order_history_v1_resp import PmarginGetUmConditionalOrderHistoryV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query UM Conditional Order History(USER_DATA)
        api_response = api_instance.pmargin_get_um_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_conditional_order_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_conditional_order_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **strategy_id** | **int**|  | [optional] 
 **new_client_strategy_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmConditionalOrderHistoryV1Resp**](PmarginGetUmConditionalOrderHistoryV1Resp.md)

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

# **pmargin_get_um_fee_burn_v1**
> PmarginGetUmFeeBurnV1Resp pmargin_get_um_fee_burn_v1(timestamp, recv_window=recv_window)

Get UM Futures BNB Burn Status (USER_DATA)

Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_fee_burn_v1_resp import PmarginGetUmFeeBurnV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures BNB Burn Status (USER_DATA)
        api_response = api_instance.pmargin_get_um_fee_burn_v1(timestamp, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**PmarginGetUmFeeBurnV1Resp**](PmarginGetUmFeeBurnV1Resp.md)

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

# **pmargin_get_um_force_orders_v1**
> List[PmarginGetUmForceOrdersV1RespItem] pmargin_get_um_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query User's UM Force Orders (USER_DATA)

Query User's UM Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_force_orders_v1_resp_item import PmarginGetUmForceOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | `LIQUIDATION` for liquidation orders, `ADL` for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's UM Force Orders (USER_DATA)
        api_response = api_instance.pmargin_get_um_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_force_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **auto_close_type** | **str**| &#x60;LIQUIDATION&#x60; for liquidation orders, &#x60;ADL&#x60; for ADL orders. | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50; max 100. | [optional] [default to 50]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[PmarginGetUmForceOrdersV1RespItem]**](PmarginGetUmForceOrdersV1RespItem.md)

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

# **pmargin_get_um_open_order_v1**
> PmarginGetUmOpenOrderV1Resp pmargin_get_um_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current UM Open Order(USER_DATA)

Query current UM open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_open_order_v1_resp import PmarginGetUmOpenOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current UM Open Order(USER_DATA)
        api_response = api_instance.pmargin_get_um_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_open_order_v1: %s\n" % e)
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

[**PmarginGetUmOpenOrderV1Resp**](PmarginGetUmOpenOrderV1Resp.md)

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

# **pmargin_get_um_open_orders_v1**
> List[PmarginGetUmOpenOrdersV1RespItem] pmargin_get_um_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query All Current UM Open Orders(USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_open_orders_v1_resp_item import PmarginGetUmOpenOrdersV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current UM Open Orders(USER_DATA)
        api_response = api_instance.pmargin_get_um_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmOpenOrdersV1RespItem]**](PmarginGetUmOpenOrdersV1RespItem.md)

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

# **pmargin_get_um_order_amendment_v1**
> List[PmarginGetUmOrderAmendmentV1RespItem] pmargin_get_um_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query UM Modify Order History(TRADE)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_order_amendment_v1_resp_item import PmarginGetUmOrderAmendmentV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get modification history from INCLUSIVE (optional)
    end_time = 56 # int | Timestamp in ms to get modification history until INCLUSIVE (optional)
    limit = 500 # int | Default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query UM Modify Order History(TRADE)
        api_response = api_instance.pmargin_get_um_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_order_amendment_v1: %s\n" % e)
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
 **limit** | **int**| Default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmOrderAmendmentV1RespItem]**](PmarginGetUmOrderAmendmentV1RespItem.md)

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

# **pmargin_get_um_order_v1**
> PmarginGetUmOrderV1Resp pmargin_get_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query UM Order (USER_DATA)

Check an UM order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_order_v1_resp import PmarginGetUmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query UM Order (USER_DATA)
        api_response = api_instance.pmargin_get_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_order_v1: %s\n" % e)
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

[**PmarginGetUmOrderV1Resp**](PmarginGetUmOrderV1Resp.md)

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

# **pmargin_get_um_user_trades_v1**
> List[PmarginGetUmUserTradesV1RespItem] pmargin_get_um_user_trades_v1(symbol, timestamp, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

UM Account Trade List(USER_DATA)

Get trades for a specific account and UM symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_get_um_user_trades_v1_resp_item import PmarginGetUmUserTradesV1RespItem
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # UM Account Trade List(USER_DATA)
        api_response = api_instance.pmargin_get_um_user_trades_v1(symbol, timestamp, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of TradeApi->pmargin_get_um_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_get_um_user_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginGetUmUserTradesV1RespItem]**](PmarginGetUmUserTradesV1RespItem.md)

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

# **pmargin_update_cm_order_v1**
> PmarginUpdateCmOrderV1Resp pmargin_update_cm_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify CM Order(TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_update_cm_order_v1_resp import PmarginUpdateCmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
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
        # Modify CM Order(TRADE)
        api_response = api_instance.pmargin_update_cm_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of TradeApi->pmargin_update_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_update_cm_order_v1: %s\n" % e)
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

[**PmarginUpdateCmOrderV1Resp**](PmarginUpdateCmOrderV1Resp.md)

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

# **pmargin_update_um_order_v1**
> PmarginUpdateUmOrderV1Resp pmargin_update_um_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify UM Order(TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.models.pmargin_update_um_order_v1_resp import PmarginUpdateUmOrderV1Resp
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
    api_instance = binance.derivatives.pmargin.TradeApi(api_client)
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
        # Modify UM Order(TRADE)
        api_response = api_instance.pmargin_update_um_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of TradeApi->pmargin_update_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->pmargin_update_um_order_v1: %s\n" % e)
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

[**PmarginUpdateUmOrderV1Resp**](PmarginUpdateUmOrderV1Resp.md)

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

