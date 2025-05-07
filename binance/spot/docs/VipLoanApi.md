# binance.spot.VipLoanApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_vip_borrow_v1**](VipLoanApi.md#create_loan_vip_borrow_v1) | **POST** /sapi/v1/loan/vip/borrow | VIP Loan Borrow(TRADE)
[**create_loan_vip_renew_v1**](VipLoanApi.md#create_loan_vip_renew_v1) | **POST** /sapi/v1/loan/vip/renew | VIP Loan Renew(TRADE)
[**create_loan_vip_repay_v1**](VipLoanApi.md#create_loan_vip_repay_v1) | **POST** /sapi/v1/loan/vip/repay | VIP Loan Repay(TRADE)
[**get_loan_vip_accrued_interest_v1**](VipLoanApi.md#get_loan_vip_accrued_interest_v1) | **GET** /sapi/v1/loan/vip/accruedInterest | Get VIP Loan Accrued Interest(USER_DATA)
[**get_loan_vip_collateral_account_v1**](VipLoanApi.md#get_loan_vip_collateral_account_v1) | **GET** /sapi/v1/loan/vip/collateral/account | Check VIP Loan Collateral Account (USER_DATA)
[**get_loan_vip_collateral_data_v1**](VipLoanApi.md#get_loan_vip_collateral_data_v1) | **GET** /sapi/v1/loan/vip/collateral/data | Get Collateral Asset Data(USER_DATA)
[**get_loan_vip_interest_rate_history_v1**](VipLoanApi.md#get_loan_vip_interest_rate_history_v1) | **GET** /sapi/v1/loan/vip/interestRateHistory | Get VIP Loan Interest Rate History (USER_DATA)
[**get_loan_vip_loanable_data_v1**](VipLoanApi.md#get_loan_vip_loanable_data_v1) | **GET** /sapi/v1/loan/vip/loanable/data | Get Loanable Assets Data(USER_DATA)
[**get_loan_vip_ongoing_orders_v1**](VipLoanApi.md#get_loan_vip_ongoing_orders_v1) | **GET** /sapi/v1/loan/vip/ongoing/orders | Get VIP Loan Ongoing Orders(USER_DATA)
[**get_loan_vip_repay_history_v1**](VipLoanApi.md#get_loan_vip_repay_history_v1) | **GET** /sapi/v1/loan/vip/repay/history | Get VIP Loan Repayment History(USER_DATA)
[**get_loan_vip_request_data_v1**](VipLoanApi.md#get_loan_vip_request_data_v1) | **GET** /sapi/v1/loan/vip/request/data | Query Application Status(USER_DATA)
[**get_loan_vip_request_interest_rate_v1**](VipLoanApi.md#get_loan_vip_request_interest_rate_v1) | **GET** /sapi/v1/loan/vip/request/interestRate | Get Borrow Interest Rate(USER_DATA)


# **create_loan_vip_borrow_v1**
> CreateLoanVipBorrowV1Resp create_loan_vip_borrow_v1()

VIP Loan Borrow(TRADE)

VIP loan is available for VIP users only.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_vip_borrow_v1_resp import CreateLoanVipBorrowV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)

    try:
        # VIP Loan Borrow(TRADE)
        api_response = api_instance.create_loan_vip_borrow_v1()
        print("The response of VipLoanApi->create_loan_vip_borrow_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->create_loan_vip_borrow_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateLoanVipBorrowV1Resp**](CreateLoanVipBorrowV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_vip_renew_v1**
> CreateLoanVipRenewV1Resp create_loan_vip_renew_v1(loan_term, order_id, timestamp, recv_window=recv_window)

VIP Loan Renew(TRADE)

VIP loan is available for VIP users only.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_vip_renew_v1_resp import CreateLoanVipRenewV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    loan_term = 56 # int | 
    order_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # VIP Loan Renew(TRADE)
        api_response = api_instance.create_loan_vip_renew_v1(loan_term, order_id, timestamp, recv_window=recv_window)
        print("The response of VipLoanApi->create_loan_vip_renew_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->create_loan_vip_renew_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_term** | **int**|  | 
 **order_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLoanVipRenewV1Resp**](CreateLoanVipRenewV1Resp.md)

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

# **create_loan_vip_repay_v1**
> CreateLoanVipRepayV1Resp create_loan_vip_repay_v1(amount, order_id, timestamp, recv_window=recv_window)

VIP Loan Repay(TRADE)

VIP loan is available for VIP users only.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_loan_vip_repay_v1_resp import CreateLoanVipRepayV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    amount = '' # str |  (default to '')
    order_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # VIP Loan Repay(TRADE)
        api_response = api_instance.create_loan_vip_repay_v1(amount, order_id, timestamp, recv_window=recv_window)
        print("The response of VipLoanApi->create_loan_vip_repay_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->create_loan_vip_repay_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **order_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateLoanVipRepayV1Resp**](CreateLoanVipRepayV1Resp.md)

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

# **get_loan_vip_accrued_interest_v1**
> GetLoanVipAccruedInterestV1Resp get_loan_vip_accrued_interest_v1(recv_window, timestamp, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit)

Get VIP Loan Accrued Interest(USER_DATA)

GET /sapi/v1/loan/vip/accruedInterest

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_accrued_interest_v1_resp import GetLoanVipAccruedInterestV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    recv_window = 56 # int | 
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    loan_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Current querying page. Start from 1; default: 1; max: 1000 (optional) (default to 1)
    limit = 10 # int | Default: 10; max: 100 (optional) (default to 10)

    try:
        # Get VIP Loan Accrued Interest(USER_DATA)
        api_response = api_instance.get_loan_vip_accrued_interest_v1(recv_window, timestamp, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit)
        print("The response of VipLoanApi->get_loan_vip_accrued_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_accrued_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recv_window** | **int**|  | 
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1; default: 1; max: 1000 | [optional] [default to 1]
 **limit** | **int**| Default: 10; max: 100 | [optional] [default to 10]

### Return type

[**GetLoanVipAccruedInterestV1Resp**](GetLoanVipAccruedInterestV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_collateral_account_v1**
> GetLoanVipCollateralAccountV1Resp get_loan_vip_collateral_account_v1(timestamp, order_id=order_id, collateral_account_id=collateral_account_id, recv_window=recv_window)

Check VIP Loan Collateral Account (USER_DATA)

VIP loan is available for VIP users only

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_collateral_account_v1_resp import GetLoanVipCollateralAccountV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    collateral_account_id = 56 # int |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Check VIP Loan Collateral Account (USER_DATA)
        api_response = api_instance.get_loan_vip_collateral_account_v1(timestamp, order_id=order_id, collateral_account_id=collateral_account_id, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_collateral_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_collateral_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **collateral_account_id** | **int**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipCollateralAccountV1Resp**](GetLoanVipCollateralAccountV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_collateral_data_v1**
> GetLoanVipCollateralDataV1Resp get_loan_vip_collateral_data_v1(timestamp, collateral_coin=collateral_coin, recv_window=recv_window)

Get Collateral Asset Data(USER_DATA)

Get Collateral Asset Data

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_collateral_data_v1_resp import GetLoanVipCollateralDataV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    collateral_coin = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Collateral Asset Data(USER_DATA)
        api_response = api_instance.get_loan_vip_collateral_data_v1(timestamp, collateral_coin=collateral_coin, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_collateral_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_collateral_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipCollateralDataV1Resp**](GetLoanVipCollateralDataV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_interest_rate_history_v1**
> GetLoanVipInterestRateHistoryV1Resp get_loan_vip_interest_rate_history_v1(coin, recv_window, timestamp, start_time=start_time, end_time=end_time, current=current, limit=limit)

Get VIP Loan Interest Rate History (USER_DATA)

Get VIP Loan Interest Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_interest_rate_history_v1_resp import GetLoanVipInterestRateHistoryV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    coin = '' # str |  (default to '')
    recv_window = 56 # int | 
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Check current querying page, start from 1. Default：1；Max：1000. (optional)
    limit = 56 # int | Default：10; Max：100. (optional)

    try:
        # Get VIP Loan Interest Rate History (USER_DATA)
        api_response = api_instance.get_loan_vip_interest_rate_history_v1(coin, recv_window, timestamp, start_time=start_time, end_time=end_time, current=current, limit=limit)
        print("The response of VipLoanApi->get_loan_vip_interest_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_interest_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | 
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Check current querying page, start from 1. Default：1；Max：1000. | [optional] 
 **limit** | **int**| Default：10; Max：100. | [optional] 

### Return type

[**GetLoanVipInterestRateHistoryV1Resp**](GetLoanVipInterestRateHistoryV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_loanable_data_v1**
> GetLoanVipLoanableDataV1Resp get_loan_vip_loanable_data_v1(timestamp, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)

Get Loanable Assets Data(USER_DATA)

Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_loanable_data_v1_resp import GetLoanVipLoanableDataV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    loan_coin = '' # str |  (optional) (default to '')
    vip_level = 56 # int | default:user&#39;s vip level (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Loanable Assets Data(USER_DATA)
        api_response = api_instance.get_loan_vip_loanable_data_v1(timestamp, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_loanable_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_loanable_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **vip_level** | **int**| default:user&amp;#39;s vip level | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipLoanableDataV1Resp**](GetLoanVipLoanableDataV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_ongoing_orders_v1**
> GetLoanVipOngoingOrdersV1Resp get_loan_vip_ongoing_orders_v1(timestamp, order_id=order_id, collateral_account_id=collateral_account_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)

Get VIP Loan Ongoing Orders(USER_DATA)

VIP loan is available for VIP users only.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_ongoing_orders_v1_resp import GetLoanVipOngoingOrdersV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    collateral_account_id = 56 # int |  (optional)
    loan_coin = '' # str |  (optional) (default to '')
    collateral_coin = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying page. Start from 1, Default:1, Max: 1000. (optional)
    limit = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get VIP Loan Ongoing Orders(USER_DATA)
        api_response = api_instance.get_loan_vip_ongoing_orders_v1(timestamp, order_id=order_id, collateral_account_id=collateral_account_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_ongoing_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_ongoing_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **collateral_account_id** | **int**|  | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **collateral_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying page. Start from 1, Default:1, Max: 1000. | [optional] 
 **limit** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipOngoingOrdersV1Resp**](GetLoanVipOngoingOrdersV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_repay_history_v1**
> GetLoanVipRepayHistoryV1Resp get_loan_vip_repay_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get VIP Loan Repayment History(USER_DATA)

GET /sapi/v1/loan/vip/repay/history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_repay_history_v1_resp import GetLoanVipRepayHistoryV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    order_id = 56 # int |  (optional)
    loan_coin = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1, Default:1, Max: 1000 (optional)
    limit = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get VIP Loan Repayment History(USER_DATA)
        api_response = api_instance.get_loan_vip_repay_history_v1(timestamp, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_repay_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_repay_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **order_id** | **int**|  | [optional] 
 **loan_coin** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1, Default:1, Max: 1000 | [optional] 
 **limit** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipRepayHistoryV1Resp**](GetLoanVipRepayHistoryV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_request_data_v1**
> GetLoanVipRequestDataV1Resp get_loan_vip_request_data_v1(timestamp, current=current, limit=limit, recv_window=recv_window)

Query Application Status(USER_DATA)

Query Application Status

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_request_data_v1_resp import GetLoanVipRequestDataV1Resp
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
    api_instance = binance.spot.VipLoanApi(api_client)
    timestamp = 56 # int | 
    current = 56 # int | Currently querying page. Start from 1, Default:1, Max: 1000 (optional)
    limit = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Application Status(USER_DATA)
        api_response = api_instance.get_loan_vip_request_data_v1(timestamp, current=current, limit=limit, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_request_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_request_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **current** | **int**| Currently querying page. Start from 1, Default:1, Max: 1000 | [optional] 
 **limit** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetLoanVipRequestDataV1Resp**](GetLoanVipRequestDataV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_vip_request_interest_rate_v1**
> List[GetLoanVipRequestInterestRateV1RespItem] get_loan_vip_request_interest_rate_v1(loan_coin, timestamp, recv_window=recv_window)

Get Borrow Interest Rate(USER_DATA)

Get Borrow Interest Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_loan_vip_request_interest_rate_v1_resp_item import GetLoanVipRequestInterestRateV1RespItem
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
    api_instance = binance.spot.VipLoanApi(api_client)
    loan_coin = '' # str | Max 10 assets, Multiple split by &#34;,&#34; (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Borrow Interest Rate(USER_DATA)
        api_response = api_instance.get_loan_vip_request_interest_rate_v1(loan_coin, timestamp, recv_window=recv_window)
        print("The response of VipLoanApi->get_loan_vip_request_interest_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VipLoanApi->get_loan_vip_request_interest_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_coin** | **str**| Max 10 assets, Multiple split by &amp;#34;,&amp;#34; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetLoanVipRequestInterestRateV1RespItem]**](GetLoanVipRequestInterestRateV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

