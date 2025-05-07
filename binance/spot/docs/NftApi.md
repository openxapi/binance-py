# binance.spot.NftApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nft_history_deposit_v1**](NftApi.md#get_nft_history_deposit_v1) | **GET** /sapi/v1/nft/history/deposit | Get NFT Deposit History(USER_DATA)
[**get_nft_history_transactions_v1**](NftApi.md#get_nft_history_transactions_v1) | **GET** /sapi/v1/nft/history/transactions | Get NFT Transaction History(USER_DATA)
[**get_nft_history_withdraw_v1**](NftApi.md#get_nft_history_withdraw_v1) | **GET** /sapi/v1/nft/history/withdraw | Get NFT Withdraw History(USER_DATA)
[**get_nft_user_get_asset_v1**](NftApi.md#get_nft_user_get_asset_v1) | **GET** /sapi/v1/nft/user/getAsset | Get NFT Asset(USER_DATA)


# **get_nft_history_deposit_v1**
> GetNftHistoryDepositV1Resp get_nft_history_deposit_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Deposit History(USER_DATA)

et NFT Deposit History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_nft_history_deposit_v1_resp import GetNftHistoryDepositV1Resp
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
    api_instance = binance.spot.NftApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50, Max 50 (optional) (default to 50)
    page = 1 # int | Default 1 (optional) (default to 1)
    recv_window = 56 # int |  (optional)

    try:
        # Get NFT Deposit History(USER_DATA)
        api_response = api_instance.get_nft_history_deposit_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
        print("The response of NftApi->get_nft_history_deposit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_nft_history_deposit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] [default to 50]
 **page** | **int**| Default 1 | [optional] [default to 1]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetNftHistoryDepositV1Resp**](GetNftHistoryDepositV1Resp.md)

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

# **get_nft_history_transactions_v1**
> GetNftHistoryTransactionsV1Resp get_nft_history_transactions_v1(order_type, timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Transaction History(USER_DATA)

Get NFT Transaction History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_nft_history_transactions_v1_resp import GetNftHistoryTransactionsV1Resp
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
    api_instance = binance.spot.NftApi(api_client)
    order_type = 56 # int | 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50, Max 50 (optional) (default to 50)
    page = 1 # int | Default 1 (optional) (default to 1)
    recv_window = 56 # int |  (optional)

    try:
        # Get NFT Transaction History(USER_DATA)
        api_response = api_instance.get_nft_history_transactions_v1(order_type, timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
        print("The response of NftApi->get_nft_history_transactions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_nft_history_transactions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_type** | **int**| 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee | 
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] [default to 50]
 **page** | **int**| Default 1 | [optional] [default to 1]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetNftHistoryTransactionsV1Resp**](GetNftHistoryTransactionsV1Resp.md)

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

# **get_nft_history_withdraw_v1**
> GetNftHistoryWithdrawV1Resp get_nft_history_withdraw_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Withdraw History(USER_DATA)

Get NFT Withdraw History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_nft_history_withdraw_v1_resp import GetNftHistoryWithdrawV1Resp
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
    api_instance = binance.spot.NftApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 50 # int | Default 50, Max 50 (optional) (default to 50)
    page = 1 # int | Default 1 (optional) (default to 1)
    recv_window = 56 # int |  (optional)

    try:
        # Get NFT Withdraw History(USER_DATA)
        api_response = api_instance.get_nft_history_withdraw_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
        print("The response of NftApi->get_nft_history_withdraw_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_nft_history_withdraw_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] [default to 50]
 **page** | **int**| Default 1 | [optional] [default to 1]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetNftHistoryWithdrawV1Resp**](GetNftHistoryWithdrawV1Resp.md)

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

# **get_nft_user_get_asset_v1**
> GetNftUserGetAssetV1Resp get_nft_user_get_asset_v1(timestamp, limit=limit, page=page, recv_window=recv_window)

Get NFT Asset(USER_DATA)

Get NFT Asset

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_nft_user_get_asset_v1_resp import GetNftUserGetAssetV1Resp
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
    api_instance = binance.spot.NftApi(api_client)
    timestamp = 56 # int | 
    limit = 50 # int | Default 50, Max 50 (optional) (default to 50)
    page = 1 # int | Default 1 (optional) (default to 1)
    recv_window = 56 # int |  (optional)

    try:
        # Get NFT Asset(USER_DATA)
        api_response = api_instance.get_nft_user_get_asset_v1(timestamp, limit=limit, page=page, recv_window=recv_window)
        print("The response of NftApi->get_nft_user_get_asset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_nft_user_get_asset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **limit** | **int**| Default 50, Max 50 | [optional] [default to 50]
 **page** | **int**| Default 1 | [optional] [default to 1]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetNftUserGetAssetV1Resp**](GetNftUserGetAssetV1Resp.md)

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

