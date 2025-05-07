# binance.spot.MiningApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mining_hash_transfer_config_cancel_v1**](MiningApi.md#create_mining_hash_transfer_config_cancel_v1) | **POST** /sapi/v1/mining/hash-transfer/config/cancel | Cancel hashrate resale configuration(USER_DATA)
[**create_mining_hash_transfer_config_v1**](MiningApi.md#create_mining_hash_transfer_config_v1) | **POST** /sapi/v1/mining/hash-transfer/config | Hashrate Resale Request(USER_DATA)
[**get_mining_hash_transfer_config_details_list_v1**](MiningApi.md#get_mining_hash_transfer_config_details_list_v1) | **GET** /sapi/v1/mining/hash-transfer/config/details/list | Hashrate Resale List (USER_DATA)
[**get_mining_hash_transfer_profit_details_v1**](MiningApi.md#get_mining_hash_transfer_profit_details_v1) | **GET** /sapi/v1/mining/hash-transfer/profit/details | Hashrate Resale Detail(USER_DATA)
[**get_mining_payment_list_v1**](MiningApi.md#get_mining_payment_list_v1) | **GET** /sapi/v1/mining/payment/list | Earnings List(USER_DATA)
[**get_mining_payment_other_v1**](MiningApi.md#get_mining_payment_other_v1) | **GET** /sapi/v1/mining/payment/other | Extra Bonus List(USER_DATA)
[**get_mining_payment_uid_v1**](MiningApi.md#get_mining_payment_uid_v1) | **GET** /sapi/v1/mining/payment/uid | Mining Account Earning(USER_DATA)
[**get_mining_pub_algo_list_v1**](MiningApi.md#get_mining_pub_algo_list_v1) | **GET** /sapi/v1/mining/pub/algoList | Acquiring Algorithm(MARKET_DATA)
[**get_mining_pub_coin_list_v1**](MiningApi.md#get_mining_pub_coin_list_v1) | **GET** /sapi/v1/mining/pub/coinList | Acquiring CoinName(MARKET_DATA)
[**get_mining_statistics_user_list_v1**](MiningApi.md#get_mining_statistics_user_list_v1) | **GET** /sapi/v1/mining/statistics/user/list | Account List(USER_DATA)
[**get_mining_statistics_user_status_v1**](MiningApi.md#get_mining_statistics_user_status_v1) | **GET** /sapi/v1/mining/statistics/user/status | Statistic List(USER_DATA)
[**get_mining_worker_detail_v1**](MiningApi.md#get_mining_worker_detail_v1) | **GET** /sapi/v1/mining/worker/detail | Request for Detail Miner List(USER_DATA)
[**get_mining_worker_list_v1**](MiningApi.md#get_mining_worker_list_v1) | **GET** /sapi/v1/mining/worker/list | Request for Miner List(USER_DATA)


# **create_mining_hash_transfer_config_cancel_v1**
> CreateMiningHashTransferConfigCancelV1Resp create_mining_hash_transfer_config_cancel_v1(config_id, timestamp, user_name, recv_window=recv_window)

Cancel hashrate resale configuration(USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_mining_hash_transfer_config_cancel_v1_resp import CreateMiningHashTransferConfigCancelV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    config_id = 56 # int | 
    timestamp = 56 # int | 
    user_name = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Cancel hashrate resale configuration(USER_DATA)
        api_response = api_instance.create_mining_hash_transfer_config_cancel_v1(config_id, timestamp, user_name, recv_window=recv_window)
        print("The response of MiningApi->create_mining_hash_transfer_config_cancel_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->create_mining_hash_transfer_config_cancel_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **user_name** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMiningHashTransferConfigCancelV1Resp**](CreateMiningHashTransferConfigCancelV1Resp.md)

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

# **create_mining_hash_transfer_config_v1**
> CreateMiningHashTransferConfigV1Resp create_mining_hash_transfer_config_v1(algo, end_date, hash_rate, start_date, timestamp, to_pool_user, user_name, recv_window=recv_window)

Hashrate Resale Request(USER_DATA)

Hashrate Resale Request

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_mining_hash_transfer_config_v1_resp import CreateMiningHashTransferConfigV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str |  (default to '')
    end_date = 56 # int | 
    hash_rate = 56 # int | 
    start_date = 56 # int | 
    timestamp = 56 # int | 
    to_pool_user = '' # str |  (default to '')
    user_name = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Hashrate Resale Request(USER_DATA)
        api_response = api_instance.create_mining_hash_transfer_config_v1(algo, end_date, hash_rate, start_date, timestamp, to_pool_user, user_name, recv_window=recv_window)
        print("The response of MiningApi->create_mining_hash_transfer_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->create_mining_hash_transfer_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**|  | [default to &#39;&#39;]
 **end_date** | **int**|  | 
 **hash_rate** | **int**|  | 
 **start_date** | **int**|  | 
 **timestamp** | **int**|  | 
 **to_pool_user** | **str**|  | [default to &#39;&#39;]
 **user_name** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateMiningHashTransferConfigV1Resp**](CreateMiningHashTransferConfigV1Resp.md)

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

# **get_mining_hash_transfer_config_details_list_v1**
> GetMiningHashTransferConfigDetailsListV1Resp get_mining_hash_transfer_config_details_list_v1(timestamp, page_index=page_index, page_size=page_size, recv_window=recv_window)

Hashrate Resale List (USER_DATA)

Hashrate Resale List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_hash_transfer_config_details_list_v1_resp import GetMiningHashTransferConfigDetailsListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    timestamp = 56 # int | 
    page_index = 56 # int | Page number, empty default first page, starting from 1 (optional)
    page_size = 56 # int | Number of pages, minimum 10, maximum 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Hashrate Resale List (USER_DATA)
        api_response = api_instance.get_mining_hash_transfer_config_details_list_v1(timestamp, page_index=page_index, page_size=page_size, recv_window=recv_window)
        print("The response of MiningApi->get_mining_hash_transfer_config_details_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_hash_transfer_config_details_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **page_index** | **int**| Page number, empty default first page, starting from 1 | [optional] 
 **page_size** | **int**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningHashTransferConfigDetailsListV1Resp**](GetMiningHashTransferConfigDetailsListV1Resp.md)

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

# **get_mining_hash_transfer_profit_details_v1**
> GetMiningHashTransferProfitDetailsV1Resp get_mining_hash_transfer_profit_details_v1(config_id, user_name, timestamp, page_index=page_index, page_size=page_size, recv_window=recv_window)

Hashrate Resale Detail(USER_DATA)

Hashrate Resale Detail(USER_DATA)

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_hash_transfer_profit_details_v1_resp import GetMiningHashTransferProfitDetailsV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    config_id = 56 # int | Mining ID
    user_name = '' # str | Mining Account (default to '')
    timestamp = 56 # int | 
    page_index = 56 # int | Page number, empty default first page, starting from 1 (optional)
    page_size = 56 # int | Number of pages, minimum 10, maximum 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Hashrate Resale Detail(USER_DATA)
        api_response = api_instance.get_mining_hash_transfer_profit_details_v1(config_id, user_name, timestamp, page_index=page_index, page_size=page_size, recv_window=recv_window)
        print("The response of MiningApi->get_mining_hash_transfer_profit_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_hash_transfer_profit_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| Mining ID | 
 **user_name** | **str**| Mining Account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **page_index** | **int**| Page number, empty default first page, starting from 1 | [optional] 
 **page_size** | **int**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningHashTransferProfitDetailsV1Resp**](GetMiningHashTransferProfitDetailsV1Resp.md)

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

# **get_mining_payment_list_v1**
> GetMiningPaymentListV1Resp get_mining_payment_list_v1(algo, user_name, timestamp, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Earnings List(USER_DATA)

Query Earnings List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_payment_list_v1_resp import GetMiningPaymentListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Transfer algorithm(sha256) (default to '')
    user_name = '' # str | Mining account (default to '')
    timestamp = 56 # int | 
    coin = '' # str | Coin name (optional) (default to '')
    start_date = 56 # int | Search date, millisecond timestamp, while empty query all (optional)
    end_date = 56 # int | Search date, millisecond timestamp, while empty query all (optional)
    page_index = 56 # int | Page number, empty default first page, starting from 1 (optional)
    page_size = 56 # int | Number of pages, minimum 10, maximum 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Earnings List(USER_DATA)
        api_response = api_instance.get_mining_payment_list_v1(algo, user_name, timestamp, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
        print("The response of MiningApi->get_mining_payment_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_payment_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Transfer algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **coin** | **str**| Coin name | [optional] [default to &#39;&#39;]
 **start_date** | **int**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **int**| Search date, millisecond timestamp, while empty query all | [optional] 
 **page_index** | **int**| Page number, empty default first page, starting from 1 | [optional] 
 **page_size** | **int**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningPaymentListV1Resp**](GetMiningPaymentListV1Resp.md)

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

# **get_mining_payment_other_v1**
> GetMiningPaymentOtherV1Resp get_mining_payment_other_v1(algo, user_name, timestamp, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Extra Bonus List(USER_DATA)

Extra Bonus List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_payment_other_v1_resp import GetMiningPaymentOtherV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Transfer algorithm(sha256) (default to '')
    user_name = '' # str | Mining Account (default to '')
    timestamp = 56 # int | 
    coin = '' # str | Coin Name (optional) (default to '')
    start_date = 56 # int | Search date, millisecond timestamp, while empty query all (optional)
    end_date = 56 # int | Search date, millisecond timestamp, while empty query all (optional)
    page_index = 56 # int | Page number, empty default first page, starting from 1 (optional)
    page_size = 56 # int | Number of pages, minimum 10, maximum 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Extra Bonus List(USER_DATA)
        api_response = api_instance.get_mining_payment_other_v1(algo, user_name, timestamp, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
        print("The response of MiningApi->get_mining_payment_other_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_payment_other_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Transfer algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining Account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **coin** | **str**| Coin Name | [optional] [default to &#39;&#39;]
 **start_date** | **int**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **int**| Search date, millisecond timestamp, while empty query all | [optional] 
 **page_index** | **int**| Page number, empty default first page, starting from 1 | [optional] 
 **page_size** | **int**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningPaymentOtherV1Resp**](GetMiningPaymentOtherV1Resp.md)

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

# **get_mining_payment_uid_v1**
> GetMiningPaymentUidV1Resp get_mining_payment_uid_v1(algo, timestamp, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Mining Account Earning(USER_DATA)

Mining Account Earning

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_payment_uid_v1_resp import GetMiningPaymentUidV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Algorithm(sha256) (default to '')
    timestamp = 56 # int | 
    start_date = 56 # int | Millisecond timestamp (optional)
    end_date = 56 # int | Millisecond timestamp (optional)
    page_index = 1 # int | Default 1 (optional) (default to 1)
    page_size = 56 # int | Min 10,Max 200 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Mining Account Earning(USER_DATA)
        api_response = api_instance.get_mining_payment_uid_v1(algo, timestamp, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
        print("The response of MiningApi->get_mining_payment_uid_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_payment_uid_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_date** | **int**| Millisecond timestamp | [optional] 
 **end_date** | **int**| Millisecond timestamp | [optional] 
 **page_index** | **int**| Default 1 | [optional] [default to 1]
 **page_size** | **int**| Min 10,Max 200 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningPaymentUidV1Resp**](GetMiningPaymentUidV1Resp.md)

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

# **get_mining_pub_algo_list_v1**
> GetMiningPubAlgoListV1Resp get_mining_pub_algo_list_v1()

Acquiring Algorithm(MARKET_DATA)

Acquiring Algorithm

### Example


```python
import binance.spot
from binance.spot.models.get_mining_pub_algo_list_v1_resp import GetMiningPubAlgoListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)

    try:
        # Acquiring Algorithm(MARKET_DATA)
        api_response = api_instance.get_mining_pub_algo_list_v1()
        print("The response of MiningApi->get_mining_pub_algo_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_pub_algo_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMiningPubAlgoListV1Resp**](GetMiningPubAlgoListV1Resp.md)

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

# **get_mining_pub_coin_list_v1**
> GetMiningPubCoinListV1Resp get_mining_pub_coin_list_v1()

Acquiring CoinName(MARKET_DATA)

Acquiring CoinName

### Example


```python
import binance.spot
from binance.spot.models.get_mining_pub_coin_list_v1_resp import GetMiningPubCoinListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)

    try:
        # Acquiring CoinName(MARKET_DATA)
        api_response = api_instance.get_mining_pub_coin_list_v1()
        print("The response of MiningApi->get_mining_pub_coin_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_pub_coin_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMiningPubCoinListV1Resp**](GetMiningPubCoinListV1Resp.md)

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

# **get_mining_statistics_user_list_v1**
> GetMiningStatisticsUserListV1Resp get_mining_statistics_user_list_v1(algo, user_name, timestamp, recv_window=recv_window)

Account List(USER_DATA)

Query Account List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_statistics_user_list_v1_resp import GetMiningStatisticsUserListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Algorithm(sha256) (default to '')
    user_name = '' # str | Mining account (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Account List(USER_DATA)
        api_response = api_instance.get_mining_statistics_user_list_v1(algo, user_name, timestamp, recv_window=recv_window)
        print("The response of MiningApi->get_mining_statistics_user_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_statistics_user_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningStatisticsUserListV1Resp**](GetMiningStatisticsUserListV1Resp.md)

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

# **get_mining_statistics_user_status_v1**
> GetMiningStatisticsUserStatusV1Resp get_mining_statistics_user_status_v1(algo, user_name, timestamp, recv_window=recv_window)

Statistic List(USER_DATA)

Statistic List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_statistics_user_status_v1_resp import GetMiningStatisticsUserStatusV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Algorithm(sha256) (default to '')
    user_name = '' # str | Mining account (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Statistic List(USER_DATA)
        api_response = api_instance.get_mining_statistics_user_status_v1(algo, user_name, timestamp, recv_window=recv_window)
        print("The response of MiningApi->get_mining_statistics_user_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_statistics_user_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningStatisticsUserStatusV1Resp**](GetMiningStatisticsUserStatusV1Resp.md)

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

# **get_mining_worker_detail_v1**
> GetMiningWorkerDetailV1Resp get_mining_worker_detail_v1(algo, user_name, worker_name, timestamp, recv_window=recv_window)

Request for Detail Miner List(USER_DATA)

Request for Detail Miner List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_worker_detail_v1_resp import GetMiningWorkerDetailV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Algorithm(sha256) (default to '')
    user_name = '' # str | Mining account (default to '')
    worker_name = '' # str | Miner’s name(required) (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Request for Detail Miner List(USER_DATA)
        api_response = api_instance.get_mining_worker_detail_v1(algo, user_name, worker_name, timestamp, recv_window=recv_window)
        print("The response of MiningApi->get_mining_worker_detail_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_worker_detail_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining account | [default to &#39;&#39;]
 **worker_name** | **str**| Miner’s name(required) | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningWorkerDetailV1Resp**](GetMiningWorkerDetailV1Resp.md)

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

# **get_mining_worker_list_v1**
> GetMiningWorkerListV1Resp get_mining_worker_list_v1(algo, user_name, timestamp, page_index=page_index, sort=sort, sort_column=sort_column, worker_status=worker_status, recv_window=recv_window)

Request for Miner List(USER_DATA)

Request for Miner List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_mining_worker_list_v1_resp import GetMiningWorkerListV1Resp
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
    api_instance = binance.spot.MiningApi(api_client)
    algo = '' # str | Algorithm(sha256) (default to '')
    user_name = '' # str | Mining account (default to '')
    timestamp = 56 # int | 
    page_index = 56 # int | Page number，default is first page，start form 1 (optional)
    sort = 56 # int | sort sequence(default=0)0 positive sequence，1 negative sequence (optional)
    sort_column = 1 # int | Sort by( default 1): <br/><br/>1: miner name, <br/><br/>2: real-time computing power, <br/><br/>3: daily average computing power, <br/><br/>4: real-time rejection rate, <br/><br/>5: last submission time (optional) (default to 1)
    worker_status = 56 # int | miners status(default=0),0 all，1 valid，2 invalid，3 failure (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Request for Miner List(USER_DATA)
        api_response = api_instance.get_mining_worker_list_v1(algo, user_name, timestamp, page_index=page_index, sort=sort, sort_column=sort_column, worker_status=worker_status, recv_window=recv_window)
        print("The response of MiningApi->get_mining_worker_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningApi->get_mining_worker_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | [default to &#39;&#39;]
 **user_name** | **str**| Mining account | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **page_index** | **int**| Page number，default is first page，start form 1 | [optional] 
 **sort** | **int**| sort sequence(default&#x3D;0)0 positive sequence，1 negative sequence | [optional] 
 **sort_column** | **int**| Sort by( default 1): &lt;br/&gt;&lt;br/&gt;1: miner name, &lt;br/&gt;&lt;br/&gt;2: real-time computing power, &lt;br/&gt;&lt;br/&gt;3: daily average computing power, &lt;br/&gt;&lt;br/&gt;4: real-time rejection rate, &lt;br/&gt;&lt;br/&gt;5: last submission time | [optional] [default to 1]
 **worker_status** | **int**| miners status(default&#x3D;0),0 all，1 valid，2 invalid，3 failure | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetMiningWorkerListV1Resp**](GetMiningWorkerListV1Resp.md)

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

