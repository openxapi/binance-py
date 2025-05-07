# binance.spot.CryptoLoanApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_flexible_adjust_ltv_v2**](CryptoLoanApi.md#create_loan_flexible_adjust_ltv_v2) | **POST** /sapi/v2/loan/flexible/adjust/ltv | Flexible Loan Adjust LTV(TRADE)
[**create_loan_flexible_borrow_v2**](CryptoLoanApi.md#create_loan_flexible_borrow_v2) | **POST** /sapi/v2/loan/flexible/borrow | Flexible Loan Borrow(TRADE)
[**create_loan_flexible_repay_collateral_v2**](CryptoLoanApi.md#create_loan_flexible_repay_collateral_v2) | **POST** /sapi/v2/loan/flexible/repay/collateral | Flexible Loan Collateral Repayment (TRADE)
[**create_loan_flexible_repay_v2**](CryptoLoanApi.md#create_loan_flexible_repay_v2) | **POST** /sapi/v2/loan/flexible/repay | Flexible Loan Repay(TRADE)
[**get_loan_borrow_history_v1**](CryptoLoanApi.md#get_loan_borrow_history_v1) | **GET** /sapi/v1/loan/borrow/history | Get Loan Borrow History(USER_DATA)
[**get_loan_flexible_borrow_history_v2**](CryptoLoanApi.md#get_loan_flexible_borrow_history_v2) | **GET** /sapi/v2/loan/flexible/borrow/history | Get Flexible Loan Borrow History(USER_DATA)
[**get_loan_flexible_collateral_data_v2**](CryptoLoanApi.md#get_loan_flexible_collateral_data_v2) | **GET** /sapi/v2/loan/flexible/collateral/data | Get Flexible Loan Collateral Assets Data(USER_DATA)
[**get_loan_flexible_liquidation_history_v2**](CryptoLoanApi.md#get_loan_flexible_liquidation_history_v2) | **GET** /sapi/v2/loan/flexible/liquidation/history | Get Flexible Loan Liquidation History (USER_DATA)
[**get_loan_flexible_loanable_data_v2**](CryptoLoanApi.md#get_loan_flexible_loanable_data_v2) | **GET** /sapi/v2/loan/flexible/loanable/data | Get Flexible Loan Assets Data(USER_DATA)
[**get_loan_flexible_ltv_adjustment_history_v2**](CryptoLoanApi.md#get_loan_flexible_ltv_adjustment_history_v2) | **GET** /sapi/v2/loan/flexible/ltv/adjustment/history | Get Flexible Loan LTV Adjustment History(USER_DATA)
[**get_loan_flexible_ongoing_orders_v2**](CryptoLoanApi.md#get_loan_flexible_ongoing_orders_v2) | **GET** /sapi/v2/loan/flexible/ongoing/orders | Get Flexible Loan Ongoing Orders(USER_DATA)
[**get_loan_flexible_repay_history_v2**](CryptoLoanApi.md#get_loan_flexible_repay_history_v2) | **GET** /sapi/v2/loan/flexible/repay/history | Get Flexible Loan Repayment History(USER_DATA)
[**get_loan_flexible_repay_rate_v2**](CryptoLoanApi.md#get_loan_flexible_repay_rate_v2) | **GET** /sapi/v2/loan/flexible/repay/rate | Check Collateral Repay Rate (USER_DATA)
[**get_loan_income_v1**](CryptoLoanApi.md#get_loan_income_v1) | **GET** /sapi/v1/loan/income | Get Crypto Loans Income History(USER_DATA)
[**get_loan_ltv_adjustment_history_v1**](CryptoLoanApi.md#get_loan_ltv_adjustment_history_v1) | **GET** /sapi/v1/loan/ltv/adjustment/history | Get Loan LTV Adjustment History(USER_DATA)
[**get_loan_repay_history_v1**](CryptoLoanApi.md#get_loan_repay_history_v1) | **GET** /sapi/v1/loan/repay/history | Get Loan Repayment History(USER_DATA)


# **create_loan_flexible_adjust_ltv_v2**
> CreateLoanFlexibleAdjustLtvV2Resp create_loan_flexible_adjust_ltv_v2(adjustment_amount, collateral_coin, direction, loan_coin, timestamp, recv_window=recv_window)

Flexible Loan Adjust LTV(TRADE)

Flexible Loan Adjust LTV

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_flexible_adjust_ltv_v2_resp import CreateLoanFlexibleAdjustLtvV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    adjustment_amount = '' # str |  (default to '')
    collateral_coin = '' # str |  (default to '')
    direction = '' # str |  (default to '')
    loan_coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Flexible Loan Adjust LTV(TRADE)
        api_response = api_instance.create_loan_flexible_adjust_ltv_v2(adjustment_amount, collateral_coin, direction, loan_coin, timestamp, recv_window=recv_window)
        print("The response of CryptoLoanApi->create_loan_flexible_adjust_ltv_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->create_loan_flexible_adjust_ltv_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adjustment_amount** | **str**|  | [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [default to &#39;&#39;]
 **direction** | **str**|  | [default to &#39;&#39;]
 **loan_coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLoanFlexibleAdjustLtvV2Resp**](CreateLoanFlexibleAdjustLtvV2Resp.md)

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

# **create_loan_flexible_borrow_v2**
> CreateLoanFlexibleBorrowV2Resp create_loan_flexible_borrow_v2(collateral_coin, loan_coin, timestamp, collateral_amount=collateral_amount, loan_amount=loan_amount, recv_window=recv_window)

Flexible Loan Borrow(TRADE)

Borrow Flexible Loan

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_flexible_borrow_v2_resp import CreateLoanFlexibleBorrowV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    collateral_coin = '' # str |  (default to '')
    loan_coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    collateral_amount = '' # str |  (optional) (default to '')
    loan_amount = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Flexible Loan Borrow(TRADE)
        api_response = api_instance.create_loan_flexible_borrow_v2(collateral_coin, loan_coin, timestamp, collateral_amount=collateral_amount, loan_amount=loan_amount, recv_window=recv_window)
        print("The response of CryptoLoanApi->create_loan_flexible_borrow_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->create_loan_flexible_borrow_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_coin** | **str**|  | [default to &#39;&#39;]
 **loan_coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **collateral_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **loan_amount** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLoanFlexibleBorrowV2Resp**](CreateLoanFlexibleBorrowV2Resp.md)

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

# **create_loan_flexible_repay_collateral_v2**
> CreateLoanFlexibleRepayCollateralV2Resp create_loan_flexible_repay_collateral_v2()

Flexible Loan Collateral Repayment (TRADE)

** Request Weight(UID)
** 6000
Parameters:
- repayAmount refers to the loan amount the user would like to repay

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_flexible_repay_collateral_v2_resp import CreateLoanFlexibleRepayCollateralV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)

    try:
        # Flexible Loan Collateral Repayment (TRADE)
        api_response = api_instance.create_loan_flexible_repay_collateral_v2()
        print("The response of CryptoLoanApi->create_loan_flexible_repay_collateral_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->create_loan_flexible_repay_collateral_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateLoanFlexibleRepayCollateralV2Resp**](CreateLoanFlexibleRepayCollateralV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_flexible_repay_v2**
> CreateLoanFlexibleRepayV2Resp create_loan_flexible_repay_v2(collateral_coin, loan_coin, repay_amount, timestamp, collateral_return=collateral_return, full_repayment=full_repayment, recv_window=recv_window)

Flexible Loan Repay(TRADE)

Flexible Loan Repay

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_flexible_repay_v2_resp import CreateLoanFlexibleRepayV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    collateral_coin = '' # str |  (default to '')
    loan_coin = '' # str |  (default to '')
    repay_amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    collateral_return = True # bool |  (optional)
    full_repayment = True # bool |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Flexible Loan Repay(TRADE)
        api_response = api_instance.create_loan_flexible_repay_v2(collateral_coin, loan_coin, repay_amount, timestamp, collateral_return=collateral_return, full_repayment=full_repayment, recv_window=recv_window)
        print("The response of CryptoLoanApi->create_loan_flexible_repay_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->create_loan_flexible_repay_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_coin** | **str**|  | [default to &#39;&#39;]
 **loan_coin** | **str**|  | [default to &#39;&#39;]
 **repay_amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **collateral_return** | **bool**|  | [optional] 
 **full_repayment** | **bool**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLoanFlexibleRepayV2Resp**](CreateLoanFlexibleRepayV2Resp.md)

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

# **get_loan_borrow_history_v1**
> GetLoanBorrowHistoryV1Resp get_loan_borrow_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Loan Borrow History(USER_DATA)

Get Loan Borrow History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_borrow_history_v1_resp import GetLoanBorrowHistoryV1Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int | orderId in `POST /sapi/v1/loan/borrow` (optional)
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000. (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100. (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Loan Borrow History(USER_DATA)
        api_response = api_instance.get_loan_borrow_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_borrow_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_borrow_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**| orderId in &#x60;POST /sapi/v1/loan/borrow&#x60; | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000. | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100. | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanBorrowHistoryV1Resp**](GetLoanBorrowHistoryV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_borrow_history_v2**
> GetLoanFlexibleBorrowHistoryV2Resp get_loan_flexible_borrow_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Flexible Loan Borrow History(USER_DATA)

Get Flexible Loan Borrow History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_borrow_history_v2_resp import GetLoanFlexibleBorrowHistoryV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Borrow History(USER_DATA)
        api_response = api_instance.get_loan_flexible_borrow_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_borrow_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_borrow_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleBorrowHistoryV2Resp**](GetLoanFlexibleBorrowHistoryV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_collateral_data_v2**
> GetLoanFlexibleCollateralDataV2Resp get_loan_flexible_collateral_data_v2(timestamp, collateral_coin=collateral_coin, recv_window=recv_window)

Get Flexible Loan Collateral Assets Data(USER_DATA)

Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown in USD value.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_collateral_data_v2_resp import GetLoanFlexibleCollateralDataV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    collateral_coin = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Collateral Assets Data(USER_DATA)
        api_response = api_instance.get_loan_flexible_collateral_data_v2(timestamp, collateral_coin=collateral_coin, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_collateral_data_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_collateral_data_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleCollateralDataV2Resp**](GetLoanFlexibleCollateralDataV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_liquidation_history_v2**
> GetLoanFlexibleLiquidationHistoryV2Resp get_loan_flexible_liquidation_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Flexible Loan Liquidation History (USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_liquidation_history_v2_resp import GetLoanFlexibleLiquidationHistoryV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Liquidation History (USER_DATA)
        api_response = api_instance.get_loan_flexible_liquidation_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_liquidation_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_liquidation_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleLiquidationHistoryV2Resp**](GetLoanFlexibleLiquidationHistoryV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_loanable_data_v2**
> GetLoanFlexibleLoanableDataV2Resp get_loan_flexible_loanable_data_v2(timestamp, loan_coin=loan_coin, recv_window=recv_window)

Get Flexible Loan Assets Data(USER_DATA)

Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_loanable_data_v2_resp import GetLoanFlexibleLoanableDataV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Assets Data(USER_DATA)
        api_response = api_instance.get_loan_flexible_loanable_data_v2(timestamp, loan_coin=loan_coin, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_loanable_data_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_loanable_data_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleLoanableDataV2Resp**](GetLoanFlexibleLoanableDataV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_ltv_adjustment_history_v2**
> GetLoanFlexibleLtvAdjustmentHistoryV2Resp get_loan_flexible_ltv_adjustment_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Flexible Loan LTV Adjustment History(USER_DATA)

Get Flexible Loan LTV Adjustment History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_ltv_adjustment_history_v2_resp import GetLoanFlexibleLtvAdjustmentHistoryV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan LTV Adjustment History(USER_DATA)
        api_response = api_instance.get_loan_flexible_ltv_adjustment_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_ltv_adjustment_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_ltv_adjustment_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleLtvAdjustmentHistoryV2Resp**](GetLoanFlexibleLtvAdjustmentHistoryV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_ongoing_orders_v2**
> GetLoanFlexibleOngoingOrdersV2Resp get_loan_flexible_ongoing_orders_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)

Get Flexible Loan Ongoing Orders(USER_DATA)

Get Flexible Loan Ongoing Orders

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_ongoing_orders_v2_resp import GetLoanFlexibleOngoingOrdersV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Ongoing Orders(USER_DATA)
        api_response = api_instance.get_loan_flexible_ongoing_orders_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_ongoing_orders_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_ongoing_orders_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleOngoingOrdersV2Resp**](GetLoanFlexibleOngoingOrdersV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_repay_history_v2**
> GetLoanFlexibleRepayHistoryV2Resp get_loan_flexible_repay_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Flexible Loan Repayment History(USER_DATA)

Get Flexible Loan Repayment History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_repay_history_v2_resp import GetLoanFlexibleRepayHistoryV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Loan Repayment History(USER_DATA)
        api_response = api_instance.get_loan_flexible_repay_history_v2(timestamp, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_repay_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_repay_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleRepayHistoryV2Resp**](GetLoanFlexibleRepayHistoryV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_flexible_repay_rate_v2**
> GetLoanFlexibleRepayRateV2Resp get_loan_flexible_repay_rate_v2(loan_coin, collateral_coin, timestamp, recv_window=recv_window)

Check Collateral Repay Rate (USER_DATA)

Get the latest rate of collateral coin/loan coin when using collateral repay.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_flexible_repay_rate_v2_resp import GetLoanFlexibleRepayRateV2Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    loan_coin = '' # str |  (default to '')
    collateral_coin = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Check Collateral Repay Rate (USER_DATA)
        api_response = api_instance.get_loan_flexible_repay_rate_v2(loan_coin, collateral_coin, timestamp, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_flexible_repay_rate_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_flexible_repay_rate_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_coin** | **str**|  | [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanFlexibleRepayRateV2Resp**](GetLoanFlexibleRepayRateV2Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_income_v1**
> List[GetLoanIncomeV1RespItem] get_loan_income_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Crypto Loans Income History(USER_DATA)

Get Crypto Loans Income History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_income_v1_resp_item import GetLoanIncomeV1RespItem
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    type = '' # str | All types will be returned by default. Enum：`borrowIn` ,`collateralSpent`, `repayAmount`, `collateralReturn`(Collateral return after repayment), `addCollateral`, `removeCollateral`, `collateralReturnAfterLiquidation` (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 20 # int | default 20, max 100 (optional) (default to 20)
    recv_window = 56 # int |  (optional)

    try:
        # Get Crypto Loans Income History(USER_DATA)
        api_response = api_instance.get_loan_income_v1(timestamp, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **type** | **str**| All types will be returned by default. Enum：&#x60;borrowIn&#x60; ,&#x60;collateralSpent&#x60;, &#x60;repayAmount&#x60;, &#x60;collateralReturn&#x60;(Collateral return after repayment), &#x60;addCollateral&#x60;, &#x60;removeCollateral&#x60;, &#x60;collateralReturnAfterLiquidation&#x60; | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 20, max 100 | [optional] [default to 20]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetLoanIncomeV1RespItem]**](GetLoanIncomeV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_ltv_adjustment_history_v1**
> GetLoanLtvAdjustmentHistoryV1Resp get_loan_ltv_adjustment_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Loan LTV Adjustment History(USER_DATA)

Get Loan LTV Adjustment History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_ltv_adjustment_history_v1_resp import GetLoanLtvAdjustmentHistoryV1Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Loan LTV Adjustment History(USER_DATA)
        api_response = api_instance.get_loan_ltv_adjustment_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_ltv_adjustment_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_ltv_adjustment_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanLtvAdjustmentHistoryV1Resp**](GetLoanLtvAdjustmentHistoryV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_repay_history_v1**
> GetLoanRepayHistoryV1Resp get_loan_repay_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Loan Repayment History(USER_DATA)

Get Loan Repayment History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_repay_history_v1_resp import GetLoanRepayHistoryV1Resp
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
    api_instance = binance.spot.CryptoLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Loan Repayment History(USER_DATA)
        api_response = api_instance.get_loan_repay_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of CryptoLoanApi->get_loan_repay_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLoanApi->get_loan_repay_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanRepayHistoryV1Resp**](GetLoanRepayHistoryV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

