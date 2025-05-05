# binance.pmargin.PortfolioMarginApi

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_collection_v1**](PortfolioMarginApi.md#create_asset_collection_v1) | **POST** /papi/v1/asset-collection | Fund Collection by Asset(TRADE)
[**create_auto_collection_v1**](PortfolioMarginApi.md#create_auto_collection_v1) | **POST** /papi/v1/auto-collection | Fund Auto-collection(TRADE)
[**create_bnb_transfer_v1**](PortfolioMarginApi.md#create_bnb_transfer_v1) | **POST** /papi/v1/bnb-transfer | BNB transfer (TRADE)
[**create_cm_conditional_order_v1**](PortfolioMarginApi.md#create_cm_conditional_order_v1) | **POST** /papi/v1/cm/conditional/order | New CM Conditional Order(TRADE)
[**create_cm_leverage_v1**](PortfolioMarginApi.md#create_cm_leverage_v1) | **POST** /papi/v1/cm/leverage | Change CM Initial Leverage (TRADE)
[**create_cm_order_v1**](PortfolioMarginApi.md#create_cm_order_v1) | **POST** /papi/v1/cm/order | New CM Order(TRADE)
[**create_cm_position_side_dual_v1**](PortfolioMarginApi.md#create_cm_position_side_dual_v1) | **POST** /papi/v1/cm/positionSide/dual | Change CM Position Mode(TRADE)
[**create_listen_key_v1**](PortfolioMarginApi.md#create_listen_key_v1) | **POST** /papi/v1/listenKey | Start User Data Stream(USER_STREAM)
[**create_margin_loan_v1**](PortfolioMarginApi.md#create_margin_loan_v1) | **POST** /papi/v1/marginLoan | Margin Account Borrow(MARGIN)
[**create_margin_order_oco_v1**](PortfolioMarginApi.md#create_margin_order_oco_v1) | **POST** /papi/v1/margin/order/oco | Margin Account New OCO(TRADE)
[**create_margin_order_v1**](PortfolioMarginApi.md#create_margin_order_v1) | **POST** /papi/v1/margin/order | New Margin Order(TRADE)
[**create_margin_repay_debt_v1**](PortfolioMarginApi.md#create_margin_repay_debt_v1) | **POST** /papi/v1/margin/repay-debt | Margin Account Repay Debt(TRADE)
[**create_repay_futures_negative_balance_v1**](PortfolioMarginApi.md#create_repay_futures_negative_balance_v1) | **POST** /papi/v1/repay-futures-negative-balance | Repay futures Negative Balance(USER_DATA)
[**create_repay_futures_switch_v1**](PortfolioMarginApi.md#create_repay_futures_switch_v1) | **POST** /papi/v1/repay-futures-switch | Change Auto-repay-futures Status(TRADE)
[**create_repay_loan_v1**](PortfolioMarginApi.md#create_repay_loan_v1) | **POST** /papi/v1/repayLoan | Margin Account Repay(MARGIN)
[**create_um_conditional_order_v1**](PortfolioMarginApi.md#create_um_conditional_order_v1) | **POST** /papi/v1/um/conditional/order | New UM Conditional Order (TRADE)
[**create_um_fee_burn_v1**](PortfolioMarginApi.md#create_um_fee_burn_v1) | **POST** /papi/v1/um/feeBurn | Toggle BNB Burn On UM Futures Trade (TRADE)
[**create_um_leverage_v1**](PortfolioMarginApi.md#create_um_leverage_v1) | **POST** /papi/v1/um/leverage | Change UM Initial Leverage(TRADE)
[**create_um_order_v1**](PortfolioMarginApi.md#create_um_order_v1) | **POST** /papi/v1/um/order | New UM Order (TRADE)
[**create_um_position_side_dual_v1**](PortfolioMarginApi.md#create_um_position_side_dual_v1) | **POST** /papi/v1/um/positionSide/dual | Change UM Position Mode(TRADE)
[**delete_cm_all_open_orders_v1**](PortfolioMarginApi.md#delete_cm_all_open_orders_v1) | **DELETE** /papi/v1/cm/allOpenOrders | Cancel All CM Open Orders(TRADE)
[**delete_cm_conditional_all_open_orders_v1**](PortfolioMarginApi.md#delete_cm_conditional_all_open_orders_v1) | **DELETE** /papi/v1/cm/conditional/allOpenOrders | Cancel All CM Open Conditional Orders(TRADE)
[**delete_cm_conditional_order_v1**](PortfolioMarginApi.md#delete_cm_conditional_order_v1) | **DELETE** /papi/v1/cm/conditional/order | Cancel CM Conditional Order(TRADE)
[**delete_cm_order_v1**](PortfolioMarginApi.md#delete_cm_order_v1) | **DELETE** /papi/v1/cm/order | Cancel CM Order(TRADE)
[**delete_listen_key_v1**](PortfolioMarginApi.md#delete_listen_key_v1) | **DELETE** /papi/v1/listenKey | Close User Data Stream(USER_STREAM)
[**delete_margin_all_open_orders_v1**](PortfolioMarginApi.md#delete_margin_all_open_orders_v1) | **DELETE** /papi/v1/margin/allOpenOrders | Cancel Margin Account All Open Orders on a Symbol(TRADE)
[**delete_margin_order_list_v1**](PortfolioMarginApi.md#delete_margin_order_list_v1) | **DELETE** /papi/v1/margin/orderList | Cancel Margin Account OCO Orders(TRADE)
[**delete_margin_order_v1**](PortfolioMarginApi.md#delete_margin_order_v1) | **DELETE** /papi/v1/margin/order | Cancel Margin Account Order(TRADE)
[**delete_um_all_open_orders_v1**](PortfolioMarginApi.md#delete_um_all_open_orders_v1) | **DELETE** /papi/v1/um/allOpenOrders | Cancel All UM Open Orders(TRADE)
[**delete_um_conditional_all_open_orders_v1**](PortfolioMarginApi.md#delete_um_conditional_all_open_orders_v1) | **DELETE** /papi/v1/um/conditional/allOpenOrders | Cancel All UM Open Conditional Orders (TRADE)
[**delete_um_conditional_order_v1**](PortfolioMarginApi.md#delete_um_conditional_order_v1) | **DELETE** /papi/v1/um/conditional/order | Cancel UM Conditional Order(TRADE)
[**delete_um_order_v1**](PortfolioMarginApi.md#delete_um_order_v1) | **DELETE** /papi/v1/um/order | Cancel UM Order(TRADE)
[**get_account_v1**](PortfolioMarginApi.md#get_account_v1) | **GET** /papi/v1/account | Account Information(USER_DATA)
[**get_balance_v1**](PortfolioMarginApi.md#get_balance_v1) | **GET** /papi/v1/balance | Account Balance(USER_DATA)
[**get_cm_account_v1**](PortfolioMarginApi.md#get_cm_account_v1) | **GET** /papi/v1/cm/account | Get CM Account Detail(USER_DATA)
[**get_cm_adl_quantile_v1**](PortfolioMarginApi.md#get_cm_adl_quantile_v1) | **GET** /papi/v1/cm/adlQuantile | CM Position ADL Quantile Estimation(USER_DATA)
[**get_cm_all_orders_v1**](PortfolioMarginApi.md#get_cm_all_orders_v1) | **GET** /papi/v1/cm/allOrders | Query All CM Orders (USER_DATA)
[**get_cm_commission_rate_v1**](PortfolioMarginApi.md#get_cm_commission_rate_v1) | **GET** /papi/v1/cm/commissionRate | Get User Commission Rate for CM(USER_DATA)
[**get_cm_conditional_all_orders_v1**](PortfolioMarginApi.md#get_cm_conditional_all_orders_v1) | **GET** /papi/v1/cm/conditional/allOrders | Query All CM Conditional Orders(USER_DATA)
[**get_cm_conditional_open_order_v1**](PortfolioMarginApi.md#get_cm_conditional_open_order_v1) | **GET** /papi/v1/cm/conditional/openOrder | Query Current CM Open Conditional Order(USER_DATA)
[**get_cm_conditional_open_orders_v1**](PortfolioMarginApi.md#get_cm_conditional_open_orders_v1) | **GET** /papi/v1/cm/conditional/openOrders | Query All Current CM Open Conditional Orders (USER_DATA)
[**get_cm_conditional_order_history_v1**](PortfolioMarginApi.md#get_cm_conditional_order_history_v1) | **GET** /papi/v1/cm/conditional/orderHistory | Query CM Conditional Order History(USER_DATA)
[**get_cm_force_orders_v1**](PortfolioMarginApi.md#get_cm_force_orders_v1) | **GET** /papi/v1/cm/forceOrders | Query User&#39;s CM Force Orders(USER_DATA)
[**get_cm_income_v1**](PortfolioMarginApi.md#get_cm_income_v1) | **GET** /papi/v1/cm/income | Get CM Income History(USER_DATA)
[**get_cm_leverage_bracket_v1**](PortfolioMarginApi.md#get_cm_leverage_bracket_v1) | **GET** /papi/v1/cm/leverageBracket | CM Notional and Leverage Brackets(USER_DATA)
[**get_cm_open_order_v1**](PortfolioMarginApi.md#get_cm_open_order_v1) | **GET** /papi/v1/cm/openOrder | Query Current CM Open Order (USER_DATA)
[**get_cm_open_orders_v1**](PortfolioMarginApi.md#get_cm_open_orders_v1) | **GET** /papi/v1/cm/openOrders | Query All Current CM Open Orders(USER_DATA)
[**get_cm_order_amendment_v1**](PortfolioMarginApi.md#get_cm_order_amendment_v1) | **GET** /papi/v1/cm/orderAmendment | Query CM Modify Order History(TRADE)
[**get_cm_order_v1**](PortfolioMarginApi.md#get_cm_order_v1) | **GET** /papi/v1/cm/order | Query CM Order(USER_DATA)
[**get_cm_position_risk_v1**](PortfolioMarginApi.md#get_cm_position_risk_v1) | **GET** /papi/v1/cm/positionRisk | Query CM Position Information(USER_DATA)
[**get_cm_position_side_dual_v1**](PortfolioMarginApi.md#get_cm_position_side_dual_v1) | **GET** /papi/v1/cm/positionSide/dual | Get CM Current Position Mode(USER_DATA)
[**get_cm_user_trades_v1**](PortfolioMarginApi.md#get_cm_user_trades_v1) | **GET** /papi/v1/cm/userTrades | CM Account Trade List(USER_DATA)
[**get_margin_all_order_list_v1**](PortfolioMarginApi.md#get_margin_all_order_list_v1) | **GET** /papi/v1/margin/allOrderList | Query Margin Account&#39;s all OCO (USER_DATA)
[**get_margin_all_orders_v1**](PortfolioMarginApi.md#get_margin_all_orders_v1) | **GET** /papi/v1/margin/allOrders | Query All Margin Account Orders (USER_DATA)
[**get_margin_force_orders_v1**](PortfolioMarginApi.md#get_margin_force_orders_v1) | **GET** /papi/v1/margin/forceOrders | Query User&#39;s Margin Force Orders(USER_DATA)
[**get_margin_margin_interest_history_v1**](PortfolioMarginApi.md#get_margin_margin_interest_history_v1) | **GET** /papi/v1/margin/marginInterestHistory | Get Margin Borrow/Loan Interest History(USER_DATA)
[**get_margin_margin_loan_v1**](PortfolioMarginApi.md#get_margin_margin_loan_v1) | **GET** /papi/v1/margin/marginLoan | Query Margin Loan Record(USER_DATA)
[**get_margin_max_borrowable_v1**](PortfolioMarginApi.md#get_margin_max_borrowable_v1) | **GET** /papi/v1/margin/maxBorrowable | Margin Max Borrow(USER_DATA)
[**get_margin_max_withdraw_v1**](PortfolioMarginApi.md#get_margin_max_withdraw_v1) | **GET** /papi/v1/margin/maxWithdraw | Query Margin Max Withdraw(USER_DATA)
[**get_margin_my_trades_v1**](PortfolioMarginApi.md#get_margin_my_trades_v1) | **GET** /papi/v1/margin/myTrades | Margin Account Trade List (USER_DATA)
[**get_margin_open_order_list_v1**](PortfolioMarginApi.md#get_margin_open_order_list_v1) | **GET** /papi/v1/margin/openOrderList | Query Margin Account&#39;s Open OCO (USER_DATA)
[**get_margin_open_orders_v1**](PortfolioMarginApi.md#get_margin_open_orders_v1) | **GET** /papi/v1/margin/openOrders | Query Current Margin Open Order (USER_DATA)
[**get_margin_order_list_v1**](PortfolioMarginApi.md#get_margin_order_list_v1) | **GET** /papi/v1/margin/orderList | Query Margin Account&#39;s OCO (USER_DATA)
[**get_margin_order_v1**](PortfolioMarginApi.md#get_margin_order_v1) | **GET** /papi/v1/margin/order | Query Margin Account Order (USER_DATA)
[**get_margin_repay_loan_v1**](PortfolioMarginApi.md#get_margin_repay_loan_v1) | **GET** /papi/v1/margin/repayLoan | Query Margin repay Record(USER_DATA)
[**get_ping_v1**](PortfolioMarginApi.md#get_ping_v1) | **GET** /papi/v1/ping | Test Connectivity
[**get_portfolio_interest_history_v1**](PortfolioMarginApi.md#get_portfolio_interest_history_v1) | **GET** /papi/v1/portfolio/interest-history | Query Portfolio Margin Negative Balance Interest History(USER_DATA)
[**get_portfolio_negative_balance_exchange_record_v1**](PortfolioMarginApi.md#get_portfolio_negative_balance_exchange_record_v1) | **GET** /papi/v1/portfolio/negative-balance-exchange-record | Query User Negative Balance Auto Exchange Record (USER_DATA)
[**get_rate_limit_order_v1**](PortfolioMarginApi.md#get_rate_limit_order_v1) | **GET** /papi/v1/rateLimit/order | Query User Rate Limit (USER_DATA)
[**get_repay_futures_switch_v1**](PortfolioMarginApi.md#get_repay_futures_switch_v1) | **GET** /papi/v1/repay-futures-switch | Get Auto-repay-futures Status(USER_DATA)
[**get_um_account_config_v1**](PortfolioMarginApi.md#get_um_account_config_v1) | **GET** /papi/v1/um/accountConfig | UM Futures Account Configuration(USER_DATA)
[**get_um_account_v1**](PortfolioMarginApi.md#get_um_account_v1) | **GET** /papi/v1/um/account | Get UM Account Detail(USER_DATA)
[**get_um_account_v2**](PortfolioMarginApi.md#get_um_account_v2) | **GET** /papi/v2/um/account | Get UM Account Detail V2(USER_DATA)
[**get_um_adl_quantile_v1**](PortfolioMarginApi.md#get_um_adl_quantile_v1) | **GET** /papi/v1/um/adlQuantile | UM Position ADL Quantile Estimation(USER_DATA)
[**get_um_all_orders_v1**](PortfolioMarginApi.md#get_um_all_orders_v1) | **GET** /papi/v1/um/allOrders | Query All UM Orders(USER_DATA)
[**get_um_api_trading_status_v1**](PortfolioMarginApi.md#get_um_api_trading_status_v1) | **GET** /papi/v1/um/apiTradingStatus | Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)
[**get_um_commission_rate_v1**](PortfolioMarginApi.md#get_um_commission_rate_v1) | **GET** /papi/v1/um/commissionRate | Get User Commission Rate for UM(USER_DATA)
[**get_um_conditional_all_orders_v1**](PortfolioMarginApi.md#get_um_conditional_all_orders_v1) | **GET** /papi/v1/um/conditional/allOrders | Query All UM Conditional Orders(USER_DATA)
[**get_um_conditional_open_order_v1**](PortfolioMarginApi.md#get_um_conditional_open_order_v1) | **GET** /papi/v1/um/conditional/openOrder | Query Current UM Open Conditional Order(USER_DATA)
[**get_um_conditional_open_orders_v1**](PortfolioMarginApi.md#get_um_conditional_open_orders_v1) | **GET** /papi/v1/um/conditional/openOrders | Query All Current UM Open Conditional Orders(USER_DATA)
[**get_um_conditional_order_history_v1**](PortfolioMarginApi.md#get_um_conditional_order_history_v1) | **GET** /papi/v1/um/conditional/orderHistory | Query UM Conditional Order History(USER_DATA)
[**get_um_fee_burn_v1**](PortfolioMarginApi.md#get_um_fee_burn_v1) | **GET** /papi/v1/um/feeBurn | Get UM Futures BNB Burn Status (USER_DATA)
[**get_um_force_orders_v1**](PortfolioMarginApi.md#get_um_force_orders_v1) | **GET** /papi/v1/um/forceOrders | Query User&#39;s UM Force Orders (USER_DATA)
[**get_um_income_asyn_id_v1**](PortfolioMarginApi.md#get_um_income_asyn_id_v1) | **GET** /papi/v1/um/income/asyn/id | Get UM Futures Transaction Download Link by Id(USER_DATA)
[**get_um_income_asyn_v1**](PortfolioMarginApi.md#get_um_income_asyn_v1) | **GET** /papi/v1/um/income/asyn | Get Download Id For UM Futures Transaction History (USER_DATA)
[**get_um_income_v1**](PortfolioMarginApi.md#get_um_income_v1) | **GET** /papi/v1/um/income | Get UM Income History(USER_DATA)
[**get_um_leverage_bracket_v1**](PortfolioMarginApi.md#get_um_leverage_bracket_v1) | **GET** /papi/v1/um/leverageBracket | UM Notional and Leverage Brackets (USER_DATA)
[**get_um_open_order_v1**](PortfolioMarginApi.md#get_um_open_order_v1) | **GET** /papi/v1/um/openOrder | Query Current UM Open Order(USER_DATA)
[**get_um_open_orders_v1**](PortfolioMarginApi.md#get_um_open_orders_v1) | **GET** /papi/v1/um/openOrders | Query All Current UM Open Orders(USER_DATA)
[**get_um_order_amendment_v1**](PortfolioMarginApi.md#get_um_order_amendment_v1) | **GET** /papi/v1/um/orderAmendment | Query UM Modify Order History(TRADE)
[**get_um_order_asyn_id_v1**](PortfolioMarginApi.md#get_um_order_asyn_id_v1) | **GET** /papi/v1/um/order/asyn/id | Get UM Futures Order Download Link by Id(USER_DATA)
[**get_um_order_asyn_v1**](PortfolioMarginApi.md#get_um_order_asyn_v1) | **GET** /papi/v1/um/order/asyn | Get Download Id For UM Futures Order History (USER_DATA)
[**get_um_order_v1**](PortfolioMarginApi.md#get_um_order_v1) | **GET** /papi/v1/um/order | Query UM Order (USER_DATA)
[**get_um_position_risk_v1**](PortfolioMarginApi.md#get_um_position_risk_v1) | **GET** /papi/v1/um/positionRisk | Query UM Position Information(USER_DATA)
[**get_um_position_side_dual_v1**](PortfolioMarginApi.md#get_um_position_side_dual_v1) | **GET** /papi/v1/um/positionSide/dual | Get UM Current Position Mode(USER_DATA)
[**get_um_symbol_config_v1**](PortfolioMarginApi.md#get_um_symbol_config_v1) | **GET** /papi/v1/um/symbolConfig | UM Futures Symbol Configuration(USER_DATA)
[**get_um_trade_asyn_id_v1**](PortfolioMarginApi.md#get_um_trade_asyn_id_v1) | **GET** /papi/v1/um/trade/asyn/id | Get UM Futures Trade Download Link by Id(USER_DATA)
[**get_um_trade_asyn_v1**](PortfolioMarginApi.md#get_um_trade_asyn_v1) | **GET** /papi/v1/um/trade/asyn | Get Download Id For UM Futures Trade History (USER_DATA)
[**get_um_user_trades_v1**](PortfolioMarginApi.md#get_um_user_trades_v1) | **GET** /papi/v1/um/userTrades | UM Account Trade List(USER_DATA)
[**update_cm_order_v1**](PortfolioMarginApi.md#update_cm_order_v1) | **PUT** /papi/v1/cm/order | Modify CM Order(TRADE)
[**update_listen_key_v1**](PortfolioMarginApi.md#update_listen_key_v1) | **PUT** /papi/v1/listenKey | Keepalive User Data Stream (USER_STREAM)
[**update_um_order_v1**](PortfolioMarginApi.md#update_um_order_v1) | **PUT** /papi/v1/um/order | Modify UM Order(TRADE)


# **create_asset_collection_v1**
> CreateAssetCollectionV1Resp create_asset_collection_v1(asset, timestamp, recv_window=recv_window)

Fund Collection by Asset(TRADE)

Transfers specific asset from Futures Account to Margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_asset_collection_v1_resp import CreateAssetCollectionV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Collection by Asset(TRADE)
        api_response = api_instance.create_asset_collection_v1(asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_asset_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_asset_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateAssetCollectionV1Resp**](CreateAssetCollectionV1Resp.md)

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

# **create_auto_collection_v1**
> CreateAutoCollectionV1Resp create_auto_collection_v1(timestamp, recv_window=recv_window)

Fund Auto-collection(TRADE)

Fund collection for Portfolio Margin

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_auto_collection_v1_resp import CreateAutoCollectionV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fund Auto-collection(TRADE)
        api_response = api_instance.create_auto_collection_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_auto_collection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_auto_collection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateAutoCollectionV1Resp**](CreateAutoCollectionV1Resp.md)

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

# **create_bnb_transfer_v1**
> CreateBnbTransferV1Resp create_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)

BNB transfer (TRADE)

Transfer BNB in and out of UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_bnb_transfer_v1_resp import CreateBnbTransferV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    transfer_side = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # BNB transfer (TRADE)
        api_response = api_instance.create_bnb_transfer_v1(amount, timestamp, transfer_side, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_bnb_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_bnb_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **transfer_side** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBnbTransferV1Resp**](CreateBnbTransferV1Resp.md)

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

# **create_cm_conditional_order_v1**
> CreateCmConditionalOrderV1Resp create_cm_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New CM Conditional Order(TRADE)

New CM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_cm_conditional_order_v1_resp import CreateCmConditionalOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_cm_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of PortfolioMarginApi->create_cm_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_cm_conditional_order_v1: %s\n" % e)
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

[**CreateCmConditionalOrderV1Resp**](CreateCmConditionalOrderV1Resp.md)

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

# **create_cm_leverage_v1**
> CreateCmLeverageV1Resp create_cm_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change CM Initial Leverage (TRADE)

Change user's initial leverage of specific symbol in CM.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_cm_leverage_v1_resp import CreateCmLeverageV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change CM Initial Leverage (TRADE)
        api_response = api_instance.create_cm_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_cm_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_cm_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateCmLeverageV1Resp**](CreateCmLeverageV1Resp.md)

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

# **create_cm_order_v1**
> CreateCmOrderV1Resp create_cm_order_v1(side, symbol, timestamp, type, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)

New CM Order(TRADE)

Place new CM order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_cm_order_v1_resp import CreateCmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_cm_order_v1(side, symbol, timestamp, type, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, time_in_force=time_in_force)
        print("The response of PortfolioMarginApi->create_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_cm_order_v1: %s\n" % e)
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

[**CreateCmOrderV1Resp**](CreateCmOrderV1Resp.md)

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

# **create_cm_position_side_dual_v1**
> CreateCmPositionSideDualV1Resp create_cm_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change CM Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_cm_position_side_dual_v1_resp import CreateCmPositionSideDualV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change CM Position Mode(TRADE)
        api_response = api_instance.create_cm_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_cm_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_cm_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateCmPositionSideDualV1Resp**](CreateCmPositionSideDualV1Resp.md)

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

Start User Data Stream(USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_listen_key_v1_resp import CreateListenKeyV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Start User Data Stream(USER_STREAM)
        api_response = api_instance.create_listen_key_v1()
        print("The response of PortfolioMarginApi->create_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_listen_key_v1: %s\n" % e)
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

# **create_margin_loan_v1**
> CreateMarginLoanV1Resp create_margin_loan_v1(amount, asset, timestamp, recv_window=recv_window)

Margin Account Borrow(MARGIN)

Apply for a margin loan.

### Example


```python
import binance.pmargin
from binance.pmargin.models.create_margin_loan_v1_resp import CreateMarginLoanV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Account Borrow(MARGIN)
        api_response = api_instance.create_margin_loan_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_margin_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_margin_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMarginLoanV1Resp**](CreateMarginLoanV1Resp.md)

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

# **create_margin_order_oco_v1**
> CreateMarginOrderOcoV1Resp create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)

Margin Account New OCO(TRADE)

Send in a new OCO for a margin account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_margin_order_oco_v1_resp import CreateMarginOrderOcoV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_margin_order_oco_v1(price, quantity, side, stop_price, symbol, timestamp, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, list_client_order_id=list_client_order_id, new_order_resp_type=new_order_resp_type, recv_window=recv_window, side_effect_type=side_effect_type, stop_client_order_id=stop_client_order_id, stop_iceberg_qty=stop_iceberg_qty, stop_limit_price=stop_limit_price, stop_limit_time_in_force=stop_limit_time_in_force)
        print("The response of PortfolioMarginApi->create_margin_order_oco_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_margin_order_oco_v1: %s\n" % e)
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

# **create_margin_order_v1**
> CreateMarginOrderV1Resp create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)

New Margin Order(TRADE)

New Margin Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_margin_order_v1_resp import CreateMarginOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_margin_order_v1(side, symbol, timestamp, type, auto_repay_at_cancel=auto_repay_at_cancel, iceberg_qty=iceberg_qty, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, price=price, quantity=quantity, quote_order_qty=quote_order_qty, recv_window=recv_window, self_trade_prevention_mode=self_trade_prevention_mode, side_effect_type=side_effect_type, stop_price=stop_price, time_in_force=time_in_force)
        print("The response of PortfolioMarginApi->create_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_margin_order_v1: %s\n" % e)
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

[**CreateMarginOrderV1Resp**](CreateMarginOrderV1Resp.md)

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

# **create_margin_repay_debt_v1**
> CreateMarginRepayDebtV1Resp create_margin_repay_debt_v1(asset, timestamp, amount=amount, recv_window=recv_window, specify_repay_assets=specify_repay_assets)

Margin Account Repay Debt(TRADE)

Repay debt for a margin loan.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_margin_repay_debt_v1_resp import CreateMarginRepayDebtV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    specify_repay_assets = '' # str |  (optional) (default to '')

    try:
        # Margin Account Repay Debt(TRADE)
        api_response = api_instance.create_margin_repay_debt_v1(asset, timestamp, amount=amount, recv_window=recv_window, specify_repay_assets=specify_repay_assets)
        print("The response of PortfolioMarginApi->create_margin_repay_debt_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_margin_repay_debt_v1: %s\n" % e)
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

[**CreateMarginRepayDebtV1Resp**](CreateMarginRepayDebtV1Resp.md)

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

# **create_repay_futures_negative_balance_v1**
> CreateRepayFuturesNegativeBalanceV1Resp create_repay_futures_negative_balance_v1(timestamp, recv_window=recv_window)

Repay futures Negative Balance(USER_DATA)

Repay futures Negative Balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_repay_futures_negative_balance_v1_resp import CreateRepayFuturesNegativeBalanceV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Repay futures Negative Balance(USER_DATA)
        api_response = api_instance.create_repay_futures_negative_balance_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_repay_futures_negative_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_repay_futures_negative_balance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateRepayFuturesNegativeBalanceV1Resp**](CreateRepayFuturesNegativeBalanceV1Resp.md)

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

# **create_repay_futures_switch_v1**
> CreateRepayFuturesSwitchV1Resp create_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)

Change Auto-repay-futures Status(TRADE)

Change Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_repay_futures_switch_v1_resp import CreateRepayFuturesSwitchV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    auto_repay = 'true' # str |  (default to 'true')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Auto-repay-futures Status(TRADE)
        api_response = api_instance.create_repay_futures_switch_v1(auto_repay, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_repay** | **str**|  | [default to &#39;true&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateRepayFuturesSwitchV1Resp**](CreateRepayFuturesSwitchV1Resp.md)

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

# **create_repay_loan_v1**
> CreateRepayLoanV1Resp create_repay_loan_v1(amount, asset, timestamp, recv_window=recv_window)

Margin Account Repay(MARGIN)

Repay for a margin loan.

### Example


```python
import binance.pmargin
from binance.pmargin.models.create_repay_loan_v1_resp import CreateRepayLoanV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Margin Account Repay(MARGIN)
        api_response = api_instance.create_repay_loan_v1(amount, asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_repay_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_repay_loan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateRepayLoanV1Resp**](CreateRepayLoanV1Resp.md)

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

# **create_um_conditional_order_v1**
> CreateUmConditionalOrderV1Resp create_um_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, good_till_date=good_till_date, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)

New UM Conditional Order (TRADE)

Place new UM conditional order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_um_conditional_order_v1_resp import CreateUmConditionalOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_um_conditional_order_v1(side, strategy_type, symbol, timestamp, activation_price=activation_price, callback_rate=callback_rate, good_till_date=good_till_date, new_client_strategy_id=new_client_strategy_id, position_side=position_side, price=price, price_match=price_match, price_protect=price_protect, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, stop_price=stop_price, time_in_force=time_in_force, working_type=working_type)
        print("The response of PortfolioMarginApi->create_um_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_um_conditional_order_v1: %s\n" % e)
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

[**CreateUmConditionalOrderV1Resp**](CreateUmConditionalOrderV1Resp.md)

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

# **create_um_fee_burn_v1**
> CreateUmFeeBurnV1Resp create_um_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)

Toggle BNB Burn On UM Futures Trade (TRADE)

Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on EVERY symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_um_fee_burn_v1_resp import CreateUmFeeBurnV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    fee_burn = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Toggle BNB Burn On UM Futures Trade (TRADE)
        api_response = api_instance.create_um_fee_burn_v1(fee_burn, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_um_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_um_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_burn** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateUmFeeBurnV1Resp**](CreateUmFeeBurnV1Resp.md)

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

# **create_um_leverage_v1**
> CreateUmLeverageV1Resp create_um_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)

Change UM Initial Leverage(TRADE)

Change user's initial leverage of specific symbol in UM.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_um_leverage_v1_resp import CreateUmLeverageV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    leverage = 56 # int | 
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change UM Initial Leverage(TRADE)
        api_response = api_instance.create_um_leverage_v1(leverage, symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_um_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_um_leverage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leverage** | **int**|  | 
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateUmLeverageV1Resp**](CreateUmLeverageV1Resp.md)

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

# **create_um_order_v1**
> CreateUmOrderV1Resp create_um_order_v1(side, symbol, timestamp, type, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, time_in_force=time_in_force)

New UM Order (TRADE)

Place new UM order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_um_order_v1_resp import CreateUmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.create_um_order_v1(side, symbol, timestamp, type, good_till_date=good_till_date, new_client_order_id=new_client_order_id, new_order_resp_type=new_order_resp_type, position_side=position_side, price=price, price_match=price_match, quantity=quantity, recv_window=recv_window, reduce_only=reduce_only, self_trade_prevention_mode=self_trade_prevention_mode, time_in_force=time_in_force)
        print("The response of PortfolioMarginApi->create_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_um_order_v1: %s\n" % e)
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

[**CreateUmOrderV1Resp**](CreateUmOrderV1Resp.md)

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

# **create_um_position_side_dual_v1**
> CreateUmPositionSideDualV1Resp create_um_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)

Change UM Position Mode(TRADE)

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.create_um_position_side_dual_v1_resp import CreateUmPositionSideDualV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    dual_side_position = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change UM Position Mode(TRADE)
        api_response = api_instance.create_um_position_side_dual_v1(dual_side_position, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->create_um_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->create_um_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_side_position** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateUmPositionSideDualV1Resp**](CreateUmPositionSideDualV1Resp.md)

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

# **delete_cm_all_open_orders_v1**
> DeleteCmAllOpenOrdersV1Resp delete_cm_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All CM Open Orders(TRADE)

Cancel all active LIMIT orders on specific symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_cm_all_open_orders_v1_resp import DeleteCmAllOpenOrdersV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All CM Open Orders(TRADE)
        api_response = api_instance.delete_cm_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_cm_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_cm_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteCmAllOpenOrdersV1Resp**](DeleteCmAllOpenOrdersV1Resp.md)

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

# **delete_cm_conditional_all_open_orders_v1**
> DeleteCmConditionalAllOpenOrdersV1Resp delete_cm_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All CM Open Conditional Orders(TRADE)

Cancel All CM Open Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_cm_conditional_all_open_orders_v1_resp import DeleteCmConditionalAllOpenOrdersV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All CM Open Conditional Orders(TRADE)
        api_response = api_instance.delete_cm_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_cm_conditional_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_cm_conditional_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteCmConditionalAllOpenOrdersV1Resp**](DeleteCmConditionalAllOpenOrdersV1Resp.md)

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

# **delete_cm_conditional_order_v1**
> DeleteCmConditionalOrderV1Resp delete_cm_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Cancel CM Conditional Order(TRADE)

Cancel CM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_cm_conditional_order_v1_resp import DeleteCmConditionalOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel CM Conditional Order(TRADE)
        api_response = api_instance.delete_cm_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_cm_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_cm_conditional_order_v1: %s\n" % e)
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

[**DeleteCmConditionalOrderV1Resp**](DeleteCmConditionalOrderV1Resp.md)

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

# **delete_cm_order_v1**
> DeleteCmOrderV1Resp delete_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel CM Order(TRADE)

Cancel an active LIMIT order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_cm_order_v1_resp import DeleteCmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel CM Order(TRADE)
        api_response = api_instance.delete_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_cm_order_v1: %s\n" % e)
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

[**DeleteCmOrderV1Resp**](DeleteCmOrderV1Resp.md)

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
import binance.pmargin
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Close User Data Stream(USER_STREAM)
        api_response = api_instance.delete_listen_key_v1()
        print("The response of PortfolioMarginApi->delete_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_listen_key_v1: %s\n" % e)
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

# **delete_margin_all_open_orders_v1**
> List[PmarginDeleteMarginAllOpenOrdersV1RespInner] delete_margin_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel Margin Account All Open Orders on a Symbol(TRADE)

Cancel Margin Account All Open Orders on a Symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.pmargin_delete_margin_all_open_orders_v1_resp_inner import PmarginDeleteMarginAllOpenOrdersV1RespInner
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Margin Account All Open Orders on a Symbol(TRADE)
        api_response = api_instance.delete_margin_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_margin_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_margin_all_open_orders_v1: %s\n" % e)
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

# **delete_margin_order_list_v1**
> DeleteMarginOrderListV1Resp delete_margin_order_list_v1(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Margin Account OCO Orders(TRADE)

Cancel Margin Account OCO Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_margin_order_list_v1_resp import DeleteMarginOrderListV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either `orderListId` or `listClientOrderId` must be provided (optional)
    list_client_order_id = '' # str | Either `orderListId` or `listClientOrderId` must be provided (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Cancel Margin Account OCO Orders(TRADE)
        api_response = api_instance.delete_margin_order_list_v1(symbol, timestamp, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_margin_order_list_v1: %s\n" % e)
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
> DeleteMarginOrderV1Resp delete_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel Margin Account Order(TRADE)

Cancel Margin Account Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_margin_order_v1_resp import DeleteMarginOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    new_client_order_id = '' # str | Used to uniquely identify this cancel. Automatically generated by default. (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Cancel Margin Account Order(TRADE)
        api_response = api_instance.delete_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_margin_order_v1: %s\n" % e)
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

# **delete_um_all_open_orders_v1**
> DeleteUmAllOpenOrdersV1Resp delete_um_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All UM Open Orders(TRADE)

Cancel all active LIMIT orders on specific symbol

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_um_all_open_orders_v1_resp import DeleteUmAllOpenOrdersV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All UM Open Orders(TRADE)
        api_response = api_instance.delete_um_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_um_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_um_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteUmAllOpenOrdersV1Resp**](DeleteUmAllOpenOrdersV1Resp.md)

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

# **delete_um_conditional_all_open_orders_v1**
> DeleteUmConditionalAllOpenOrdersV1Resp delete_um_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Cancel All UM Open Conditional Orders (TRADE)

Cancel All UM Open Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_um_conditional_all_open_orders_v1_resp import DeleteUmConditionalAllOpenOrdersV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Cancel All UM Open Conditional Orders (TRADE)
        api_response = api_instance.delete_um_conditional_all_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_um_conditional_all_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_um_conditional_all_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteUmConditionalAllOpenOrdersV1Resp**](DeleteUmConditionalAllOpenOrdersV1Resp.md)

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

# **delete_um_conditional_order_v1**
> DeleteUmConditionalOrderV1Resp delete_um_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Cancel UM Conditional Order(TRADE)

Cancel UM Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_um_conditional_order_v1_resp import DeleteUmConditionalOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel UM Conditional Order(TRADE)
        api_response = api_instance.delete_um_conditional_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_um_conditional_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_um_conditional_order_v1: %s\n" % e)
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

[**DeleteUmConditionalOrderV1Resp**](DeleteUmConditionalOrderV1Resp.md)

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

# **delete_um_order_v1**
> DeleteUmOrderV1Resp delete_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Cancel UM Order(TRADE)

Cancel an active UM LIMIT order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.delete_um_order_v1_resp import DeleteUmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel UM Order(TRADE)
        api_response = api_instance.delete_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->delete_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->delete_um_order_v1: %s\n" % e)
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

[**DeleteUmOrderV1Resp**](DeleteUmOrderV1Resp.md)

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

Account Information(USER_DATA)

Query account information

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_account_v1_resp import GetAccountV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account Information(USER_DATA)
        api_response = api_instance.get_account_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_account_v1: %s\n" % e)
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

# **get_balance_v1**
> PmarginGetBalanceV1Resp get_balance_v1(timestamp, asset=asset, recv_window=recv_window)

Account Balance(USER_DATA)

Query account balance

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.pmargin_get_balance_v1_resp import PmarginGetBalanceV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Account Balance(USER_DATA)
        api_response = api_instance.get_balance_v1(timestamp, asset=asset, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_balance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_balance_v1: %s\n" % e)
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

# **get_cm_account_v1**
> GetCmAccountV1Resp get_cm_account_v1(timestamp, recv_window=recv_window)

Get CM Account Detail(USER_DATA)

Get current CM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_account_v1_resp import GetCmAccountV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get CM Account Detail(USER_DATA)
        api_response = api_instance.get_cm_account_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetCmAccountV1Resp**](GetCmAccountV1Resp.md)

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

# **get_cm_adl_quantile_v1**
> List[GetCmAdlQuantileV1RespItem] get_cm_adl_quantile_v1()

CM Position ADL Quantile Estimation(USER_DATA)

Query CM Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_adl_quantile_v1_resp_item import GetCmAdlQuantileV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # CM Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.get_cm_adl_quantile_v1()
        print("The response of PortfolioMarginApi->get_cm_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_adl_quantile_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetCmAdlQuantileV1RespItem]**](GetCmAdlQuantileV1RespItem.md)

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

# **get_cm_all_orders_v1**
> List[GetCmAllOrdersV1RespItem] get_cm_all_orders_v1(symbol, timestamp, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All CM Orders (USER_DATA)

Get all account CM orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_all_orders_v1_resp_item import GetCmAllOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_cm_all_orders_v1(symbol, timestamp, pair=pair, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_all_orders_v1: %s\n" % e)
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

[**List[GetCmAllOrdersV1RespItem]**](GetCmAllOrdersV1RespItem.md)

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

# **get_cm_commission_rate_v1**
> GetCmCommissionRateV1Resp get_cm_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

Get User Commission Rate for CM(USER_DATA)

Get User Commission Rate for CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_commission_rate_v1_resp import GetCmCommissionRateV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User Commission Rate for CM(USER_DATA)
        api_response = api_instance.get_cm_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetCmCommissionRateV1Resp**](GetCmCommissionRateV1Resp.md)

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

# **get_cm_conditional_all_orders_v1**
> List[GetCmConditionalAllOrdersV1RespItem] get_cm_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All CM Conditional Orders(USER_DATA)

Query All CM Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_conditional_all_orders_v1_resp_item import GetCmConditionalAllOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All CM Conditional Orders(USER_DATA)
        api_response = api_instance.get_cm_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_conditional_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_conditional_all_orders_v1: %s\n" % e)
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

[**List[GetCmConditionalAllOrdersV1RespItem]**](GetCmConditionalAllOrdersV1RespItem.md)

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

# **get_cm_conditional_open_order_v1**
> GetCmConditionalOpenOrderV1Resp get_cm_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query Current CM Open Conditional Order(USER_DATA)

Query Current CM Open Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_conditional_open_order_v1_resp import GetCmConditionalOpenOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current CM Open Conditional Order(USER_DATA)
        api_response = api_instance.get_cm_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_conditional_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_conditional_open_order_v1: %s\n" % e)
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

[**GetCmConditionalOpenOrderV1Resp**](GetCmConditionalOpenOrderV1Resp.md)

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

# **get_cm_conditional_open_orders_v1**
> List[GetCmConditionalOpenOrdersV1RespItem] get_cm_conditional_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query All Current CM Open Conditional Orders (USER_DATA)

Get all open conditional orders on a symbol. Careful when accessing this with no symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_conditional_open_orders_v1_resp_item import GetCmConditionalOpenOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current CM Open Conditional Orders (USER_DATA)
        api_response = api_instance.get_cm_conditional_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_conditional_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_conditional_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetCmConditionalOpenOrdersV1RespItem]**](GetCmConditionalOpenOrdersV1RespItem.md)

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

# **get_cm_conditional_order_history_v1**
> GetCmConditionalOrderHistoryV1Resp get_cm_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query CM Conditional Order History(USER_DATA)

Query CM Conditional Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_conditional_order_history_v1_resp import GetCmConditionalOrderHistoryV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Conditional Order History(USER_DATA)
        api_response = api_instance.get_cm_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_conditional_order_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_conditional_order_history_v1: %s\n" % e)
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

[**GetCmConditionalOrderHistoryV1Resp**](GetCmConditionalOrderHistoryV1Resp.md)

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

# **get_cm_force_orders_v1**
> List[GetCmForceOrdersV1RespItem] get_cm_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query User's CM Force Orders(USER_DATA)

Query User's CM Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_force_orders_v1_resp_item import GetCmForceOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | &#34;LIQUIDATION&#34; for liquidation orders, &#34;ADL&#34; for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's CM Force Orders(USER_DATA)
        api_response = api_instance.get_cm_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_force_orders_v1: %s\n" % e)
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

[**List[GetCmForceOrdersV1RespItem]**](GetCmForceOrdersV1RespItem.md)

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

# **get_cm_income_v1**
> List[GetCmIncomeV1RespItem] get_cm_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get CM Income History(USER_DATA)

Get CM Income History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_income_v1_resp_item import GetCmIncomeV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_cm_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_income_v1: %s\n" % e)
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

[**List[GetCmIncomeV1RespItem]**](GetCmIncomeV1RespItem.md)

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

# **get_cm_leverage_bracket_v1**
> List[GetCmLeverageBracketV1RespItem] get_cm_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

CM Notional and Leverage Brackets(USER_DATA)

Query CM notional and leverage brackets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_leverage_bracket_v1_resp_item import GetCmLeverageBracketV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # CM Notional and Leverage Brackets(USER_DATA)
        api_response = api_instance.get_cm_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetCmLeverageBracketV1RespItem]**](GetCmLeverageBracketV1RespItem.md)

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

# **get_cm_open_order_v1**
> GetCmOpenOrderV1Resp get_cm_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current CM Open Order (USER_DATA)

Query current CM open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_open_order_v1_resp import GetCmOpenOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current CM Open Order (USER_DATA)
        api_response = api_instance.get_cm_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_open_order_v1: %s\n" % e)
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

[**GetCmOpenOrderV1Resp**](GetCmOpenOrderV1Resp.md)

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

# **get_cm_open_orders_v1**
> List[GetCmOpenOrdersV1RespItem] get_cm_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)

Query All Current CM Open Orders(USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_open_orders_v1_resp_item import GetCmOpenOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current CM Open Orders(USER_DATA)
        api_response = api_instance.get_cm_open_orders_v1(timestamp, symbol=symbol, pair=pair, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetCmOpenOrdersV1RespItem]**](GetCmOpenOrdersV1RespItem.md)

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

# **get_cm_order_amendment_v1**
> List[GetCmOrderAmendmentV1RespItem] get_cm_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query CM Modify Order History(TRADE)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_order_amendment_v1_resp_item import GetCmOrderAmendmentV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_cm_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_order_amendment_v1: %s\n" % e)
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

[**List[GetCmOrderAmendmentV1RespItem]**](GetCmOrderAmendmentV1RespItem.md)

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

# **get_cm_order_v1**
> GetCmOrderV1Resp get_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query CM Order(USER_DATA)

Check an CM order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_order_v1_resp import GetCmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Order(USER_DATA)
        api_response = api_instance.get_cm_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_order_v1: %s\n" % e)
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

[**GetCmOrderV1Resp**](GetCmOrderV1Resp.md)

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

# **get_cm_position_risk_v1**
> List[GetCmPositionRiskV1RespItem] get_cm_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)

Query CM Position Information(USER_DATA)

Get current CM position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_position_risk_v1_resp_item import GetCmPositionRiskV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    margin_asset = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query CM Position Information(USER_DATA)
        api_response = api_instance.get_cm_position_risk_v1(timestamp, margin_asset=margin_asset, pair=pair, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_position_risk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **margin_asset** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetCmPositionRiskV1RespItem]**](GetCmPositionRiskV1RespItem.md)

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

# **get_cm_position_side_dual_v1**
> GetCmPositionSideDualV1Resp get_cm_position_side_dual_v1(timestamp, recv_window=recv_window)

Get CM Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_position_side_dual_v1_resp import GetCmPositionSideDualV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get CM Current Position Mode(USER_DATA)
        api_response = api_instance.get_cm_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetCmPositionSideDualV1Resp**](GetCmPositionSideDualV1Resp.md)

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

# **get_cm_user_trades_v1**
> List[GetCmUserTradesV1RespItem] get_cm_user_trades_v1(timestamp, symbol=symbol, pair=pair, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

CM Account Trade List(USER_DATA)

Get trades for a specific account and CM symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_cm_user_trades_v1_resp_item import GetCmUserTradesV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_cm_user_trades_v1(timestamp, symbol=symbol, pair=pair, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_cm_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_cm_user_trades_v1: %s\n" % e)
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

[**List[GetCmUserTradesV1RespItem]**](GetCmUserTradesV1RespItem.md)

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

# **get_margin_all_order_list_v1**
> List[GetMarginAllOrderListV1RespItem] get_margin_all_order_list_v1(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's all OCO (USER_DATA)

Query all OCO for a specific margin account based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_all_order_list_v1_resp_item import GetMarginAllOrderListV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    from_id = 56 # int | If supplied, neither startTime or endTime can be provided (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 500. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's all OCO (USER_DATA)
        api_response = api_instance.get_margin_all_order_list_v1(timestamp, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_all_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_all_order_list_v1: %s\n" % e)
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
> List[GetMarginAllOrdersV1RespItem] get_margin_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All Margin Account Orders (USER_DATA)

Query All Margin Account Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_all_orders_v1_resp_item import GetMarginAllOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 500. (optional) (default to 500)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query All Margin Account Orders (USER_DATA)
        api_response = api_instance.get_margin_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_all_orders_v1: %s\n" % e)
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

# **get_margin_force_orders_v1**
> GetMarginForceOrdersV1Resp get_margin_force_orders_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Query User's Margin Force Orders(USER_DATA)

Query user's margin force orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_force_orders_v1_resp import GetMarginForceOrdersV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's Margin Force Orders(USER_DATA)
        api_response = api_instance.get_margin_force_orders_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_force_orders_v1: %s\n" % e)
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

[**GetMarginForceOrdersV1Resp**](GetMarginForceOrdersV1Resp.md)

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

# **get_margin_margin_interest_history_v1**
> GetMarginMarginInterestHistoryV1Resp get_margin_margin_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Get Margin Borrow/Loan Interest History(USER_DATA)

Get Margin Borrow/Loan Interest History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_margin_interest_history_v1_resp import GetMarginMarginInterestHistoryV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_margin_margin_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_margin_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_margin_interest_history_v1: %s\n" % e)
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

[**GetMarginMarginInterestHistoryV1Resp**](GetMarginMarginInterestHistoryV1Resp.md)

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

# **get_margin_margin_loan_v1**
> GetMarginMarginLoanV1Resp get_margin_margin_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Margin Loan Record(USER_DATA)

Query margin loan record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_margin_loan_v1_resp import GetMarginMarginLoanV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_margin_margin_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_margin_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_margin_loan_v1: %s\n" % e)
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

[**GetMarginMarginLoanV1Resp**](GetMarginMarginLoanV1Resp.md)

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

# **get_margin_max_borrowable_v1**
> GetMarginMaxBorrowableV1Resp get_margin_max_borrowable_v1(asset, timestamp, recv_window=recv_window)

Margin Max Borrow(USER_DATA)

Query margin max borrow

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_max_borrowable_v1_resp import GetMarginMaxBorrowableV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Margin Max Borrow(USER_DATA)
        api_response = api_instance.get_margin_max_borrowable_v1(asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_max_borrowable_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_max_borrowable_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
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

# **get_margin_max_withdraw_v1**
> GetMarginMaxWithdrawV1Resp get_margin_max_withdraw_v1(asset, timestamp, recv_window=recv_window)

Query Margin Max Withdraw(USER_DATA)

Query Margin Max Withdraw

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_max_withdraw_v1_resp import GetMarginMaxWithdrawV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Query Margin Max Withdraw(USER_DATA)
        api_response = api_instance.get_margin_max_withdraw_v1(asset, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_max_withdraw_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_max_withdraw_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetMarginMaxWithdrawV1Resp**](GetMarginMaxWithdrawV1Resp.md)

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
> List[GetMarginMyTradesV1RespItem] get_margin_my_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Margin Account Trade List (USER_DATA)

Margin Account Trade List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_my_trades_v1_resp_item import GetMarginMyTradesV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_margin_my_trades_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_my_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_my_trades_v1: %s\n" % e)
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

# **get_margin_open_order_list_v1**
> List[GetMarginOpenOrderListV1RespItem] get_margin_open_order_list_v1(timestamp, recv_window=recv_window)

Query Margin Account's Open OCO (USER_DATA)

Query Margin Account's Open OCO

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_open_order_list_v1_resp_item import GetMarginOpenOrderListV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's Open OCO (USER_DATA)
        api_response = api_instance.get_margin_open_order_list_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_open_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_open_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

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
> List[GetMarginOpenOrdersV1RespItem] get_margin_open_orders_v1(symbol, timestamp, recv_window=recv_window)

Query Current Margin Open Order (USER_DATA)

Query Current Margin Open Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_open_orders_v1_resp_item import GetMarginOpenOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Current Margin Open Order (USER_DATA)
        api_response = api_instance.get_margin_open_orders_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**List[GetMarginOpenOrdersV1RespItem]**](GetMarginOpenOrdersV1RespItem.md)

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
> GetMarginOrderListV1Resp get_margin_order_list_v1(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_order_list_v1_resp import GetMarginOrderListV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    order_list_id = 56 # int | Either orderListId or origClientOrderId must be provided (optional)
    orig_client_order_id = '' # str | Either orderListId or origClientOrderId must be provided (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account's OCO (USER_DATA)
        api_response = api_instance.get_margin_order_list_v1(timestamp, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_order_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_list_id** | **int**| Either orderListId or origClientOrderId must be provided | [optional] 
 **orig_client_order_id** | **str**| Either orderListId or origClientOrderId must be provided | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

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
> GetMarginOrderV1Resp get_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account Order (USER_DATA)

Query Margin Account Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_order_v1_resp import GetMarginOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query Margin Account Order (USER_DATA)
        api_response = api_instance.get_margin_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_order_v1: %s\n" % e)
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

# **get_margin_repay_loan_v1**
> GetMarginRepayLoanV1Resp get_margin_repay_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Margin repay Record(USER_DATA)

Query margin repay record.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_margin_repay_loan_v1_resp import GetMarginRepayLoanV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_margin_repay_loan_v1(asset, timestamp, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_margin_repay_loan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_margin_repay_loan_v1: %s\n" % e)
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

[**GetMarginRepayLoanV1Resp**](GetMarginRepayLoanV1Resp.md)

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
import binance.pmargin
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.get_ping_v1()
        print("The response of PortfolioMarginApi->get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_ping_v1: %s\n" % e)
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

# **get_portfolio_interest_history_v1**
> List[GetPortfolioInterestHistoryV1RespItem] get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)

Query Portfolio Margin Negative Balance Interest History(USER_DATA)

Query interest history of negative balance for portfolio margin.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_portfolio_interest_history_v1_resp_item import GetPortfolioInterestHistoryV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    size = 56 # int | Default:10 Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Portfolio Margin Negative Balance Interest History(USER_DATA)
        api_response = api_instance.get_portfolio_interest_history_v1(timestamp, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_portfolio_interest_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_portfolio_interest_history_v1: %s\n" % e)
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

# **get_portfolio_negative_balance_exchange_record_v1**
> GetPortfolioNegativeBalanceExchangeRecordV1Resp get_portfolio_negative_balance_exchange_record_v1(start_time, end_time, timestamp, recv_window=recv_window)

Query User Negative Balance Auto Exchange Record (USER_DATA)

Query user negative balance auto exchange record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_portfolio_negative_balance_exchange_record_v1_resp import GetPortfolioNegativeBalanceExchangeRecordV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User Negative Balance Auto Exchange Record (USER_DATA)
        api_response = api_instance.get_portfolio_negative_balance_exchange_record_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_portfolio_negative_balance_exchange_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_portfolio_negative_balance_exchange_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetPortfolioNegativeBalanceExchangeRecordV1Resp**](GetPortfolioNegativeBalanceExchangeRecordV1Resp.md)

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

# **get_rate_limit_order_v1**
> List[GetRateLimitOrderV1RespItem] get_rate_limit_order_v1(timestamp, recv_window=recv_window)

Query User Rate Limit (USER_DATA)

Query User Rate Limit

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_rate_limit_order_v1_resp_item import GetRateLimitOrderV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query User Rate Limit (USER_DATA)
        api_response = api_instance.get_rate_limit_order_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_rate_limit_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_rate_limit_order_v1: %s\n" % e)
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

# **get_repay_futures_switch_v1**
> GetRepayFuturesSwitchV1Resp get_repay_futures_switch_v1(timestamp, recv_window=recv_window)

Get Auto-repay-futures Status(USER_DATA)

Query Auto-repay-futures Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_repay_futures_switch_v1_resp import GetRepayFuturesSwitchV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Auto-repay-futures Status(USER_DATA)
        api_response = api_instance.get_repay_futures_switch_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_repay_futures_switch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_repay_futures_switch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetRepayFuturesSwitchV1Resp**](GetRepayFuturesSwitchV1Resp.md)

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

# **get_um_account_config_v1**
> GetUmAccountConfigV1Resp get_um_account_config_v1(timestamp, recv_window=recv_window)

UM Futures Account Configuration(USER_DATA)

Query UM Futures account configuration

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_account_config_v1_resp import GetUmAccountConfigV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # UM Futures Account Configuration(USER_DATA)
        api_response = api_instance.get_um_account_config_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_account_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_account_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmAccountConfigV1Resp**](GetUmAccountConfigV1Resp.md)

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

# **get_um_account_v1**
> GetUmAccountV1Resp get_um_account_v1(timestamp, recv_window=recv_window)

Get UM Account Detail(USER_DATA)

Get current UM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_account_v1_resp import GetUmAccountV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Account Detail(USER_DATA)
        api_response = api_instance.get_um_account_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmAccountV1Resp**](GetUmAccountV1Resp.md)

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

# **get_um_account_v2**
> GetUmAccountV2Resp get_um_account_v2(timestamp, recv_window=recv_window)

Get UM Account Detail V2(USER_DATA)

Get current UM account asset and position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_account_v2_resp import GetUmAccountV2Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Account Detail V2(USER_DATA)
        api_response = api_instance.get_um_account_v2(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmAccountV2Resp**](GetUmAccountV2Resp.md)

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

# **get_um_adl_quantile_v1**
> List[GetUmAdlQuantileV1RespItem] get_um_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Position ADL Quantile Estimation(USER_DATA)

Query UM Position ADL Quantile Estimation

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_adl_quantile_v1_resp_item import GetUmAdlQuantileV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Position ADL Quantile Estimation(USER_DATA)
        api_response = api_instance.get_um_adl_quantile_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_adl_quantile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_adl_quantile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetUmAdlQuantileV1RespItem]**](GetUmAdlQuantileV1RespItem.md)

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

# **get_um_all_orders_v1**
> List[GetUmAllOrdersV1RespItem] get_um_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All UM Orders(USER_DATA)

Get all account UM orders; active, canceled, or filled.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_all_orders_v1_resp_item import GetUmAllOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All UM Orders(USER_DATA)
        api_response = api_instance.get_um_all_orders_v1(symbol, timestamp, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_all_orders_v1: %s\n" % e)
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

[**List[GetUmAllOrdersV1RespItem]**](GetUmAllOrdersV1RespItem.md)

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

# **get_um_api_trading_status_v1**
> GetUmApiTradingStatusV1Resp get_um_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)

Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)

Portfolio Margin UM Trading Quantitative Rules Indicators

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_api_trading_status_v1_resp import GetUmApiTradingStatusV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)
        api_response = api_instance.get_um_api_trading_status_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_api_trading_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_api_trading_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmApiTradingStatusV1Resp**](GetUmApiTradingStatusV1Resp.md)

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

# **get_um_commission_rate_v1**
> GetUmCommissionRateV1Resp get_um_commission_rate_v1(symbol, timestamp, recv_window=recv_window)

Get User Commission Rate for UM(USER_DATA)

Get User Commission Rate for UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_commission_rate_v1_resp import GetUmCommissionRateV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User Commission Rate for UM(USER_DATA)
        api_response = api_instance.get_um_commission_rate_v1(symbol, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_commission_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_commission_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmCommissionRateV1Resp**](GetUmCommissionRateV1Resp.md)

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

# **get_um_conditional_all_orders_v1**
> List[GetUmConditionalAllOrdersV1RespItem] get_um_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query All UM Conditional Orders(USER_DATA)

Query All UM Conditional Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_conditional_all_orders_v1_resp_item import GetUmConditionalAllOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    strategy_id = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query All UM Conditional Orders(USER_DATA)
        api_response = api_instance.get_um_conditional_all_orders_v1(timestamp, symbol=symbol, strategy_id=strategy_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_conditional_all_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_conditional_all_orders_v1: %s\n" % e)
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

[**List[GetUmConditionalAllOrdersV1RespItem]**](GetUmConditionalAllOrdersV1RespItem.md)

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

# **get_um_conditional_open_order_v1**
> GetUmConditionalOpenOrderV1Resp get_um_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query Current UM Open Conditional Order(USER_DATA)

Query Current UM Open Conditional Order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_conditional_open_order_v1_resp import GetUmConditionalOpenOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current UM Open Conditional Order(USER_DATA)
        api_response = api_instance.get_um_conditional_open_order_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_conditional_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_conditional_open_order_v1: %s\n" % e)
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

[**GetUmConditionalOpenOrderV1Resp**](GetUmConditionalOpenOrderV1Resp.md)

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

# **get_um_conditional_open_orders_v1**
> List[GetUmConditionalOpenOrdersV1RespItem] get_um_conditional_open_orders_v1()

Query All Current UM Open Conditional Orders(USER_DATA)

Get all open conditional orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_conditional_open_orders_v1_resp_item import GetUmConditionalOpenOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Query All Current UM Open Conditional Orders(USER_DATA)
        api_response = api_instance.get_um_conditional_open_orders_v1()
        print("The response of PortfolioMarginApi->get_um_conditional_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_conditional_open_orders_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetUmConditionalOpenOrdersV1RespItem]**](GetUmConditionalOpenOrdersV1RespItem.md)

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

# **get_um_conditional_order_history_v1**
> GetUmConditionalOrderHistoryV1Resp get_um_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)

Query UM Conditional Order History(USER_DATA)

Query UM Conditional Order History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_conditional_order_history_v1_resp import GetUmConditionalOrderHistoryV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    strategy_id = 56 # int |  (optional)
    new_client_strategy_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query UM Conditional Order History(USER_DATA)
        api_response = api_instance.get_um_conditional_order_history_v1(symbol, timestamp, strategy_id=strategy_id, new_client_strategy_id=new_client_strategy_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_conditional_order_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_conditional_order_history_v1: %s\n" % e)
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

[**GetUmConditionalOrderHistoryV1Resp**](GetUmConditionalOrderHistoryV1Resp.md)

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

# **get_um_fee_burn_v1**
> GetUmFeeBurnV1Resp get_um_fee_burn_v1(timestamp, recv_window=recv_window)

Get UM Futures BNB Burn Status (USER_DATA)

Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_fee_burn_v1_resp import GetUmFeeBurnV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures BNB Burn Status (USER_DATA)
        api_response = api_instance.get_um_fee_burn_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_fee_burn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_fee_burn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmFeeBurnV1Resp**](GetUmFeeBurnV1Resp.md)

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

# **get_um_force_orders_v1**
> List[GetUmForceOrdersV1RespItem] get_um_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query User's UM Force Orders (USER_DATA)

Query User's UM Force Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_force_orders_v1_resp_item import GetUmForceOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    auto_close_type = '' # str | `LIQUIDATION` for liquidation orders, `ADL` for ADL orders. (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50; max 100. (optional) (default to 50)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Query User's UM Force Orders (USER_DATA)
        api_response = api_instance.get_um_force_orders_v1(timestamp, symbol=symbol, auto_close_type=auto_close_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_force_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_force_orders_v1: %s\n" % e)
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

[**List[GetUmForceOrdersV1RespItem]**](GetUmForceOrdersV1RespItem.md)

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

# **get_um_income_asyn_id_v1**
> GetUmIncomeAsynIdV1Resp get_um_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Transaction Download Link by Id(USER_DATA)

Get UM futures Transaction download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_income_asyn_id_v1_resp import GetUmIncomeAsynIdV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Transaction Download Link by Id(USER_DATA)
        api_response = api_instance.get_um_income_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_income_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_income_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmIncomeAsynIdV1Resp**](GetUmIncomeAsynIdV1Resp.md)

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

# **get_um_income_asyn_v1**
> GetUmIncomeAsynV1Resp get_um_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Transaction History (USER_DATA)

Get download id for UM futures transaction history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_income_asyn_v1_resp import GetUmIncomeAsynV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Transaction History (USER_DATA)
        api_response = api_instance.get_um_income_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_income_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_income_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmIncomeAsynV1Resp**](GetUmIncomeAsynV1Resp.md)

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

# **get_um_income_v1**
> List[GetUmIncomeV1RespItem] get_um_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Get UM Income History(USER_DATA)

Get UM Income History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_income_v1_resp_item import GetUmIncomeV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_um_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_income_v1: %s\n" % e)
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

[**List[GetUmIncomeV1RespItem]**](GetUmIncomeV1RespItem.md)

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

# **get_um_leverage_bracket_v1**
> List[GetUmLeverageBracketV1RespItem] get_um_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Notional and Leverage Brackets (USER_DATA)

Query UM notional and leverage brackets

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_leverage_bracket_v1_resp_item import GetUmLeverageBracketV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Notional and Leverage Brackets (USER_DATA)
        api_response = api_instance.get_um_leverage_bracket_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_leverage_bracket_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetUmLeverageBracketV1RespItem]**](GetUmLeverageBracketV1RespItem.md)

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

# **get_um_open_order_v1**
> GetUmOpenOrderV1Resp get_um_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Current UM Open Order(USER_DATA)

Query current UM open order

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_open_order_v1_resp import GetUmOpenOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Current UM Open Order(USER_DATA)
        api_response = api_instance.get_um_open_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_open_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_open_order_v1: %s\n" % e)
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

[**GetUmOpenOrderV1Resp**](GetUmOpenOrderV1Resp.md)

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

# **get_um_open_orders_v1**
> List[GetUmOpenOrdersV1RespItem] get_um_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)

Query All Current UM Open Orders(USER_DATA)

Get all open orders on a symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_open_orders_v1_resp_item import GetUmOpenOrdersV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query All Current UM Open Orders(USER_DATA)
        api_response = api_instance.get_um_open_orders_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_open_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_open_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetUmOpenOrdersV1RespItem]**](GetUmOpenOrdersV1RespItem.md)

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

# **get_um_order_amendment_v1**
> List[GetUmOrderAmendmentV1RespItem] get_um_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query UM Modify Order History(TRADE)

Get order modification history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_order_amendment_v1_resp_item import GetUmOrderAmendmentV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.get_um_order_amendment_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_order_amendment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_order_amendment_v1: %s\n" % e)
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

[**List[GetUmOrderAmendmentV1RespItem]**](GetUmOrderAmendmentV1RespItem.md)

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

# **get_um_order_asyn_id_v1**
> GetUmOrderAsynIdV1Resp get_um_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Order Download Link by Id(USER_DATA)

Get UM futures order download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_order_asyn_id_v1_resp import GetUmOrderAsynIdV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Order Download Link by Id(USER_DATA)
        api_response = api_instance.get_um_order_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_order_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_order_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmOrderAsynIdV1Resp**](GetUmOrderAsynIdV1Resp.md)

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

# **get_um_order_asyn_v1**
> GetUmOrderAsynV1Resp get_um_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Order History (USER_DATA)

Get download id for UM futures order history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_order_asyn_v1_resp import GetUmOrderAsynV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Order History (USER_DATA)
        api_response = api_instance.get_um_order_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_order_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_order_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmOrderAsynV1Resp**](GetUmOrderAsynV1Resp.md)

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

# **get_um_order_v1**
> GetUmOrderV1Resp get_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query UM Order (USER_DATA)

Check an UM order's status.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_order_v1_resp import GetUmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    orig_client_order_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query UM Order (USER_DATA)
        api_response = api_instance.get_um_order_v1(symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_order_v1: %s\n" % e)
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

[**GetUmOrderV1Resp**](GetUmOrderV1Resp.md)

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

# **get_um_position_risk_v1**
> List[GetUmPositionRiskV1RespItem] get_um_position_risk_v1()

Query UM Position Information(USER_DATA)

Get current UM position information.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_position_risk_v1_resp_item import GetUmPositionRiskV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Query UM Position Information(USER_DATA)
        api_response = api_instance.get_um_position_risk_v1()
        print("The response of PortfolioMarginApi->get_um_position_risk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_position_risk_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetUmPositionRiskV1RespItem]**](GetUmPositionRiskV1RespItem.md)

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

# **get_um_position_side_dual_v1**
> GetUmPositionSideDualV1Resp get_um_position_side_dual_v1(timestamp, recv_window=recv_window)

Get UM Current Position Mode(USER_DATA)

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_position_side_dual_v1_resp import GetUmPositionSideDualV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Current Position Mode(USER_DATA)
        api_response = api_instance.get_um_position_side_dual_v1(timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_position_side_dual_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_position_side_dual_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmPositionSideDualV1Resp**](GetUmPositionSideDualV1Resp.md)

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

# **get_um_symbol_config_v1**
> List[GetUmSymbolConfigV1RespItem] get_um_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)

UM Futures Symbol Configuration(USER_DATA)

Get current UM account symbol configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_symbol_config_v1_resp_item import GetUmSymbolConfigV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # UM Futures Symbol Configuration(USER_DATA)
        api_response = api_instance.get_um_symbol_config_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_symbol_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_symbol_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetUmSymbolConfigV1RespItem]**](GetUmSymbolConfigV1RespItem.md)

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

# **get_um_trade_asyn_id_v1**
> GetUmTradeAsynIdV1Resp get_um_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)

Get UM Futures Trade Download Link by Id(USER_DATA)

Get UM futures trade download link by Id

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_trade_asyn_id_v1_resp import GetUmTradeAsynIdV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    download_id = '' # str | get by download id api (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get UM Futures Trade Download Link by Id(USER_DATA)
        api_response = api_instance.get_um_trade_asyn_id_v1(download_id, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_trade_asyn_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_trade_asyn_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| get by download id api | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmTradeAsynIdV1Resp**](GetUmTradeAsynIdV1Resp.md)

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

# **get_um_trade_asyn_v1**
> GetUmTradeAsynV1Resp get_um_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)

Get Download Id For UM Futures Trade History (USER_DATA)

Get download id for UM futures trade history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_trade_asyn_v1_resp import GetUmTradeAsynV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    start_time = 56 # int | Timestamp in ms
    end_time = 56 # int | Timestamp in ms
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Download Id For UM Futures Trade History (USER_DATA)
        api_response = api_instance.get_um_trade_asyn_v1(start_time, end_time, timestamp, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_trade_asyn_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_trade_asyn_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Timestamp in ms | 
 **end_time** | **int**| Timestamp in ms | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetUmTradeAsynV1Resp**](GetUmTradeAsynV1Resp.md)

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

# **get_um_user_trades_v1**
> List[GetUmUserTradesV1RespItem] get_um_user_trades_v1(symbol, timestamp, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

UM Account Trade List(USER_DATA)

Get trades for a specific account and UM symbol.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.get_um_user_trades_v1_resp_item import GetUmUserTradesV1RespItem
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    from_id = 56 # int | Trade id to fetch from. Default gets most recent trades. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # UM Account Trade List(USER_DATA)
        api_response = api_instance.get_um_user_trades_v1(symbol, timestamp, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
        print("The response of PortfolioMarginApi->get_um_user_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->get_um_user_trades_v1: %s\n" % e)
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

[**List[GetUmUserTradesV1RespItem]**](GetUmUserTradesV1RespItem.md)

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

# **update_cm_order_v1**
> UpdateCmOrderV1Resp update_cm_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify CM Order(TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.update_cm_order_v1_resp import UpdateCmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.update_cm_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of PortfolioMarginApi->update_cm_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->update_cm_order_v1: %s\n" % e)
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

[**UpdateCmOrderV1Resp**](UpdateCmOrderV1Resp.md)

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

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)

    try:
        # Keepalive User Data Stream (USER_STREAM)
        api_response = api_instance.update_listen_key_v1()
        print("The response of PortfolioMarginApi->update_listen_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->update_listen_key_v1: %s\n" % e)
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

# **update_um_order_v1**
> UpdateUmOrderV1Resp update_um_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)

Modify UM Order(TRADE)

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

### Example

* Api Key Authentication (ApiKey):

```python
import binance.pmargin
from binance.pmargin.models.update_um_order_v1_resp import UpdateUmOrderV1Resp
from binance.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.pmargin.Configuration(
    host = "https://papi.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.pmargin.Configuration(
    auth=binance.pmargin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.pmargin.PortfolioMarginApi(api_client)
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
        api_response = api_instance.update_um_order_v1(price, quantity, side, symbol, timestamp, order_id=order_id, orig_client_order_id=orig_client_order_id, price_match=price_match, recv_window=recv_window)
        print("The response of PortfolioMarginApi->update_um_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMarginApi->update_um_order_v1: %s\n" % e)
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

[**UpdateUmOrderV1Resp**](UpdateUmOrderV1Resp.md)

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

