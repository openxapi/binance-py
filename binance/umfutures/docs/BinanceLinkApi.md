# binance.umfutures.BinanceLinkApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_referral_customization_v1**](BinanceLinkApi.md#create_api_referral_customization_v1) | **POST** /fapi/v1/apiReferral/customization | Customize Id For Client (USER DATA)(For Partner)
[**create_api_referral_user_customization_papiv1**](BinanceLinkApi.md#create_api_referral_user_customization_papiv1) | **POST** /papi/v1/apiReferral/userCustomization | Customize Id For Client  (USER DATA)(For client)(PAPI)
[**create_api_referral_user_customization_v1**](BinanceLinkApi.md#create_api_referral_user_customization_v1) | **POST** /fapi/v1/apiReferral/userCustomization | Customize Id For Client  (USER DATA)(For client)
[**get_api_referral_customization_v1**](BinanceLinkApi.md#get_api_referral_customization_v1) | **GET** /fapi/v1/apiReferral/customization | Get Client Email Customized Id (USER DATA)
[**get_api_referral_if_new_user_papiv1**](BinanceLinkApi.md#get_api_referral_if_new_user_papiv1) | **GET** /papi/v1/apiReferral/ifNewUser | Query Client If The New User (USER DATA)(PAPI)
[**get_api_referral_if_new_user_v1**](BinanceLinkApi.md#get_api_referral_if_new_user_v1) | **GET** /fapi/v1/apiReferral/ifNewUser | Query Client If The New User (USER DATA)
[**get_api_referral_overview_v1**](BinanceLinkApi.md#get_api_referral_overview_v1) | **GET** /fapi/v1/apiReferral/overview | Get Rebate Data Overview (USER DATA)
[**get_api_referral_rebate_vol_v1**](BinanceLinkApi.md#get_api_referral_rebate_vol_v1) | **GET** /fapi/v1/apiReferral/rebateVol | Get Rebate Volume (USER DATA)
[**get_api_referral_trade_vol_v1**](BinanceLinkApi.md#get_api_referral_trade_vol_v1) | **GET** /fapi/v1/apiReferral/tradeVol | Get User Trade Volume (USER DATA)
[**get_api_referral_trader_num_v1**](BinanceLinkApi.md#get_api_referral_trader_num_v1) | **GET** /fapi/v1/apiReferral/traderNum | Get Trader Number (USER DATA)
[**get_api_referral_trader_summary_v1**](BinanceLinkApi.md#get_api_referral_trader_summary_v1) | **GET** /fapi/v1/apiReferral/traderSummary | Get Trader Detail (USER DATA)
[**get_api_referral_user_customization_papiv1**](BinanceLinkApi.md#get_api_referral_user_customization_papiv1) | **GET** /papi/v1/apiReferral/userCustomization | Get User’s Customize Id (USER DATA)(PAPI)
[**get_api_referral_user_customization_v1**](BinanceLinkApi.md#get_api_referral_user_customization_v1) | **GET** /fapi/v1/apiReferral/userCustomization | Get User’s Customize Id (USER DATA)
[**get_income_v1**](BinanceLinkApi.md#get_income_v1) | **GET** /fapi/v1/income | Get Income History(USER DATA)


# **create_api_referral_customization_v1**
> CreateApiReferralCustomizationV1Resp create_api_referral_customization_v1(customer_id, email, timestamp, recv_window=recv_window)

Customize Id For Client (USER DATA)(For Partner)

- CustomerId must be unique

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_api_referral_customization_v1_resp import CreateApiReferralCustomizationV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    customer_id = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Customize Id For Client (USER DATA)(For Partner)
        api_response = api_instance.create_api_referral_customization_v1(customer_id, email, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_api_referral_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_api_referral_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | [default to &#39;&#39;]
 **email** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateApiReferralCustomizationV1Resp**](CreateApiReferralCustomizationV1Resp.md)

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

# **create_api_referral_user_customization_papiv1**
> CreateApiReferralUserCustomizationV1Resp create_api_referral_user_customization_papiv1(broker_id, customer_id, timestamp, recv_window=recv_window)

Customize Id For Client  (USER DATA)(For client)(PAPI)

- CustomerId must be unique

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_api_referral_user_customization_v1_resp import CreateApiReferralUserCustomizationV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    customer_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Customize Id For Client  (USER DATA)(For client)(PAPI)
        api_response = api_instance.create_api_referral_user_customization_papiv1(broker_id, customer_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_api_referral_user_customization_papiv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_api_referral_user_customization_papiv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **customer_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateApiReferralUserCustomizationV1Resp**](CreateApiReferralUserCustomizationV1Resp.md)

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

# **create_api_referral_user_customization_v1**
> CreateApiReferralUserCustomizationV1Resp create_api_referral_user_customization_v1(broker_id, customer_id, timestamp, recv_window=recv_window)

Customize Id For Client  (USER DATA)(For client)

- CustomerId must be unique
- If the user enabled Portfolio Margin, please user relevant /papi endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.create_api_referral_user_customization_v1_resp import CreateApiReferralUserCustomizationV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    customer_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Customize Id For Client  (USER DATA)(For client)
        api_response = api_instance.create_api_referral_user_customization_v1(broker_id, customer_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_api_referral_user_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_api_referral_user_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **customer_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateApiReferralUserCustomizationV1Resp**](CreateApiReferralUserCustomizationV1Resp.md)

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

# **get_api_referral_customization_v1**
> List[GetApiReferralCustomizationV1RespItem] get_api_referral_customization_v1(timestamp, customer_id=customer_id, email=email, page=page, limit=limit, recv_window=recv_window)

Get Client Email Customized Id (USER DATA)

- CustomerId and email can not be sent at the same time

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_customization_v1_resp_item import GetApiReferralCustomizationV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    customer_id = '' # str |  (optional) (default to '')
    email = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    limit = 100 # int | items num of one page，default 100，max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Client Email Customized Id (USER DATA)
        api_response = api_instance.get_api_referral_customization_v1(timestamp, customer_id=customer_id, email=email, page=page, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **customer_id** | **str**|  | [optional] [default to &#39;&#39;]
 **email** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **limit** | **int**| items num of one page，default 100，max 1000 | [optional] [default to 100]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralCustomizationV1RespItem]**](GetApiReferralCustomizationV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_if_new_user_papiv1**
> GetApiReferralIfNewUserV1Resp get_api_referral_if_new_user_papiv1(broker_id, timestamp, type=type, recv_window=recv_window)

Query Client If The New User (USER DATA)(PAPI)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_if_new_user_v1_resp import GetApiReferralIfNewUserV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT-margined Futures,  2: Coin-margined Futures ; Default：1:USDT-margined Futures (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Client If The New User (USER DATA)(PAPI)
        api_response = api_instance.get_api_referral_if_new_user_papiv1(broker_id, timestamp, type=type, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_if_new_user_papiv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_if_new_user_papiv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT-margined Futures,  2: Coin-margined Futures ; Default：1:USDT-margined Futures | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralIfNewUserV1Resp**](GetApiReferralIfNewUserV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_if_new_user_v1**
> GetApiReferralIfNewUserV1Resp get_api_referral_if_new_user_v1(broker_id, timestamp, type=type, recv_window=recv_window)

Query Client If The New User (USER DATA)

- If the user enabled Portfolio Margin, please user relevant /papi endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_if_new_user_v1_resp import GetApiReferralIfNewUserV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT-margined Futures，2: Coin-margined Futures; Default：1:USDT-margined Futures (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Client If The New User (USER DATA)
        api_response = api_instance.get_api_referral_if_new_user_v1(broker_id, timestamp, type=type, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_if_new_user_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_if_new_user_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT-margined Futures，2: Coin-margined Futures; Default：1:USDT-margined Futures | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralIfNewUserV1Resp**](GetApiReferralIfNewUserV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_overview_v1**
> GetApiReferralOverviewV1Resp get_api_referral_overview_v1(timestamp, type=type, recv_window=recv_window)

Get Rebate Data Overview (USER DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_overview_v1_resp import GetApiReferralOverviewV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Rebate Data Overview (USER DATA)
        api_response = api_instance.get_api_referral_overview_v1(timestamp, type=type, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_overview_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_overview_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralOverviewV1Resp**](GetApiReferralOverviewV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_rebate_vol_v1**
> List[GetApiReferralRebateVolV1RespItem] get_api_referral_rebate_vol_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Rebate Volume (USER DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_rebate_vol_v1_resp_item import GetApiReferralRebateVolV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Rebate Volume (USER DATA)
        api_response = api_instance.get_api_referral_rebate_vol_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_rebate_vol_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_rebate_vol_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralRebateVolV1RespItem]**](GetApiReferralRebateVolV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_trade_vol_v1**
> List[GetApiReferralTradeVolV1RespItem] get_api_referral_trade_vol_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get User Trade Volume (USER DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_trade_vol_v1_resp_item import GetApiReferralTradeVolV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get User Trade Volume (USER DATA)
        api_response = api_instance.get_api_referral_trade_vol_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_trade_vol_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_trade_vol_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralTradeVolV1RespItem]**](GetApiReferralTradeVolV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_trader_num_v1**
> List[GetApiReferralTraderNumV1RespItem] get_api_referral_trader_num_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Trader Number (USER DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_trader_num_v1_resp_item import GetApiReferralTraderNumV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Trader Number (USER DATA)
        api_response = api_instance.get_api_referral_trader_num_v1(timestamp, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_trader_num_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_trader_num_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralTraderNumV1RespItem]**](GetApiReferralTraderNumV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_trader_summary_v1**
> List[GetApiReferralTraderSummaryV1RespItem] get_api_referral_trader_summary_v1(timestamp, customer_id=customer_id, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Trader Detail (USER DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_trader_summary_v1_resp_item import GetApiReferralTraderSummaryV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    customer_id = '' # str |  (optional) (default to '')
    type = 56 # int | 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Get Trader Detail (USER DATA)
        api_response = api_instance.get_api_referral_trader_summary_v1(timestamp, customer_id=customer_id, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_trader_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_trader_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **customer_id** | **str**|  | [optional] [default to &#39;&#39;]
 **type** | **int**| 1:USDT Margined Futures, 2:COIN Margined Futures Default： USDT Margined Futures | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralTraderSummaryV1RespItem]**](GetApiReferralTraderSummaryV1RespItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_user_customization_papiv1**
> GetApiReferralUserCustomizationV1Resp get_api_referral_user_customization_papiv1(broker_id, timestamp, recv_window=recv_window)

Get User’s Customize Id (USER DATA)(PAPI)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_user_customization_v1_resp import GetApiReferralUserCustomizationV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User’s Customize Id (USER DATA)(PAPI)
        api_response = api_instance.get_api_referral_user_customization_papiv1(broker_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_user_customization_papiv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_user_customization_papiv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralUserCustomizationV1Resp**](GetApiReferralUserCustomizationV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_referral_user_customization_v1**
> GetApiReferralUserCustomizationV1Resp get_api_referral_user_customization_v1(broker_id, timestamp, recv_window=recv_window)

Get User’s Customize Id (USER DATA)

- CustomerId must be unique
- If the user enabled Portfolio Margin, please user relevant /papi endpoint

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_api_referral_user_customization_v1_resp import GetApiReferralUserCustomizationV1Resp
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    broker_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User’s Customize Id (USER DATA)
        api_response = api_instance.get_api_referral_user_customization_v1(broker_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_user_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_user_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralUserCustomizationV1Resp**](GetApiReferralUserCustomizationV1Resp.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

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
> List[GetIncomeV1RespItem] get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Income History(USER DATA)

- If incomeType  is not sent, all kinds of flow will be returned
- If startTime and endTime are not sent, the most recent limit datas will be returned.
- If the number of data between startTime and endTime is larger than limit, response will be return as startTime + limit.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.umfutures
from binance.umfutures.models.get_income_v1_resp_item import GetIncomeV1RespItem
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
    api_instance = binance.umfutures.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    income_type = '' # str | &#34;TRANSFER&#34;，&#34;WELCOME_BONUS&#34;, &#34;REALIZED_PNL&#34;，&#34;FUNDING_FEE&#34;, &#34;COMMISSION&#34;, and &#34;INSURANCE_CLEAR&#34; (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)
    recv_window = 56 # int |  (optional)

    try:
        # Get Income History(USER DATA)
        api_response = api_instance.get_income_v1(timestamp, symbol=symbol, income_type=income_type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_income_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_income_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **income_type** | **str**| &amp;#34;TRANSFER&amp;#34;，&amp;#34;WELCOME_BONUS&amp;#34;, &amp;#34;REALIZED_PNL&amp;#34;，&amp;#34;FUNDING_FEE&amp;#34;, &amp;#34;COMMISSION&amp;#34;, and &amp;#34;INSURANCE_CLEAR&amp;#34; | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding until INCLUSIVE. | [optional] 
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

