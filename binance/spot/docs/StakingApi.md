# binance.spot.StakingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eth_staking_eth_redeem_v1**](StakingApi.md#create_eth_staking_eth_redeem_v1) | **POST** /sapi/v1/eth-staking/eth/redeem | Redeem ETH(TRADE)
[**create_eth_staking_eth_stake_v2**](StakingApi.md#create_eth_staking_eth_stake_v2) | **POST** /sapi/v2/eth-staking/eth/stake | Subscribe ETH Staking(TRADE)
[**create_eth_staking_wbeth_wrap_v1**](StakingApi.md#create_eth_staking_wbeth_wrap_v1) | **POST** /sapi/v1/eth-staking/wbeth/wrap | Wrap BETH(TRADE)
[**create_sol_staking_sol_claim_v1**](StakingApi.md#create_sol_staking_sol_claim_v1) | **POST** /sapi/v1/sol-staking/sol/claim | Claim Boost Rewards(TRADE)
[**create_sol_staking_sol_redeem_v1**](StakingApi.md#create_sol_staking_sol_redeem_v1) | **POST** /sapi/v1/sol-staking/sol/redeem | Redeem SOL(TRADE)
[**create_sol_staking_sol_stake_v1**](StakingApi.md#create_sol_staking_sol_stake_v1) | **POST** /sapi/v1/sol-staking/sol/stake | Subscribe SOL Staking(TRADE)
[**get_eth_staking_account_v2**](StakingApi.md#get_eth_staking_account_v2) | **GET** /sapi/v2/eth-staking/account | ETH Staking account(USER_DATA)
[**get_eth_staking_eth_history_rate_history_v1**](StakingApi.md#get_eth_staking_eth_history_rate_history_v1) | **GET** /sapi/v1/eth-staking/eth/history/rateHistory | Get WBETH Rate History(USER_DATA)
[**get_eth_staking_eth_history_redemption_history_v1**](StakingApi.md#get_eth_staking_eth_history_redemption_history_v1) | **GET** /sapi/v1/eth-staking/eth/history/redemptionHistory | Get ETH redemption history(USER_DATA)
[**get_eth_staking_eth_history_rewards_history_v1**](StakingApi.md#get_eth_staking_eth_history_rewards_history_v1) | **GET** /sapi/v1/eth-staking/eth/history/rewardsHistory | Get BETH rewards distribution history(USER_DATA)
[**get_eth_staking_eth_history_staking_history_v1**](StakingApi.md#get_eth_staking_eth_history_staking_history_v1) | **GET** /sapi/v1/eth-staking/eth/history/stakingHistory | Get ETH staking history(USER_DATA)
[**get_eth_staking_eth_history_wbeth_rewards_history_v1**](StakingApi.md#get_eth_staking_eth_history_wbeth_rewards_history_v1) | **GET** /sapi/v1/eth-staking/eth/history/wbethRewardsHistory | Get WBETH rewards history(USER_DATA)
[**get_eth_staking_eth_quota_v1**](StakingApi.md#get_eth_staking_eth_quota_v1) | **GET** /sapi/v1/eth-staking/eth/quota | Get current ETH staking quota(USER_DATA)
[**get_eth_staking_wbeth_history_unwrap_history_v1**](StakingApi.md#get_eth_staking_wbeth_history_unwrap_history_v1) | **GET** /sapi/v1/eth-staking/wbeth/history/unwrapHistory | Get WBETH unwrap history(USER_DATA)
[**get_eth_staking_wbeth_history_wrap_history_v1**](StakingApi.md#get_eth_staking_wbeth_history_wrap_history_v1) | **GET** /sapi/v1/eth-staking/wbeth/history/wrapHistory | Get WBETH wrap history(USER_DATA)
[**get_sol_staking_account_v1**](StakingApi.md#get_sol_staking_account_v1) | **GET** /sapi/v1/sol-staking/account | SOL Staking account(USER_DATA)
[**get_sol_staking_sol_history_bnsol_rewards_history_v1**](StakingApi.md#get_sol_staking_sol_history_bnsol_rewards_history_v1) | **GET** /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory | Get BNSOL rewards history(USER_DATA)
[**get_sol_staking_sol_history_boost_rewards_history_v1**](StakingApi.md#get_sol_staking_sol_history_boost_rewards_history_v1) | **GET** /sapi/v1/sol-staking/sol/history/boostRewardsHistory | Get Boost Rewards History(USER_DATA)
[**get_sol_staking_sol_history_rate_history_v1**](StakingApi.md#get_sol_staking_sol_history_rate_history_v1) | **GET** /sapi/v1/sol-staking/sol/history/rateHistory | Get BNSOL Rate History(USER_DATA)
[**get_sol_staking_sol_history_redemption_history_v1**](StakingApi.md#get_sol_staking_sol_history_redemption_history_v1) | **GET** /sapi/v1/sol-staking/sol/history/redemptionHistory | Get SOL redemption history(USER_DATA)
[**get_sol_staking_sol_history_staking_history_v1**](StakingApi.md#get_sol_staking_sol_history_staking_history_v1) | **GET** /sapi/v1/sol-staking/sol/history/stakingHistory | Get SOL staking history(USER_DATA)
[**get_sol_staking_sol_history_unclaimed_rewards_v1**](StakingApi.md#get_sol_staking_sol_history_unclaimed_rewards_v1) | **GET** /sapi/v1/sol-staking/sol/history/unclaimedRewards | Get Unclaimed Rewards(USER_DATA)
[**get_sol_staking_sol_quota_v1**](StakingApi.md#get_sol_staking_sol_quota_v1) | **GET** /sapi/v1/sol-staking/sol/quota | Get SOL staking quota details(USER_DATA)


# **create_eth_staking_eth_redeem_v1**
> CreateEthStakingEthRedeemV1Resp create_eth_staking_eth_redeem_v1(amount, timestamp, asset=asset, recv_window=recv_window)

Redeem ETH(TRADE)

Redeem WBETH or BETH and get ETH

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_eth_staking_eth_redeem_v1_resp import CreateEthStakingEthRedeemV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Redeem ETH(TRADE)
        api_response = api_instance.create_eth_staking_eth_redeem_v1(amount, timestamp, asset=asset, recv_window=recv_window)
        print("The response of StakingApi->create_eth_staking_eth_redeem_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_eth_staking_eth_redeem_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateEthStakingEthRedeemV1Resp**](CreateEthStakingEthRedeemV1Resp.md)

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

# **create_eth_staking_eth_stake_v2**
> CreateEthStakingEthStakeV2Resp create_eth_staking_eth_stake_v2(amount, timestamp, recv_window=recv_window)

Subscribe ETH Staking(TRADE)

Subscribe ETH Staking

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_eth_staking_eth_stake_v2_resp import CreateEthStakingEthStakeV2Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Subscribe ETH Staking(TRADE)
        api_response = api_instance.create_eth_staking_eth_stake_v2(amount, timestamp, recv_window=recv_window)
        print("The response of StakingApi->create_eth_staking_eth_stake_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_eth_staking_eth_stake_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateEthStakingEthStakeV2Resp**](CreateEthStakingEthStakeV2Resp.md)

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

# **create_eth_staking_wbeth_wrap_v1**
> CreateEthStakingWbethWrapV1Resp create_eth_staking_wbeth_wrap_v1(amount, timestamp, recv_window=recv_window)

Wrap BETH(TRADE)

Wrap BETH

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_eth_staking_wbeth_wrap_v1_resp import CreateEthStakingWbethWrapV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Wrap BETH(TRADE)
        api_response = api_instance.create_eth_staking_wbeth_wrap_v1(amount, timestamp, recv_window=recv_window)
        print("The response of StakingApi->create_eth_staking_wbeth_wrap_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_eth_staking_wbeth_wrap_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateEthStakingWbethWrapV1Resp**](CreateEthStakingWbethWrapV1Resp.md)

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

# **create_sol_staking_sol_claim_v1**
> CreateSolStakingSolClaimV1Resp create_sol_staking_sol_claim_v1(timestamp, recv_window=recv_window)

Claim Boost Rewards(TRADE)

Claim Boost APR Airdrop Rewards

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_sol_staking_sol_claim_v1_resp import CreateSolStakingSolClaimV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Claim Boost Rewards(TRADE)
        api_response = api_instance.create_sol_staking_sol_claim_v1(timestamp, recv_window=recv_window)
        print("The response of StakingApi->create_sol_staking_sol_claim_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_sol_staking_sol_claim_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSolStakingSolClaimV1Resp**](CreateSolStakingSolClaimV1Resp.md)

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

# **create_sol_staking_sol_redeem_v1**
> CreateSolStakingSolRedeemV1Resp create_sol_staking_sol_redeem_v1(amount, timestamp, recv_window=recv_window)

Redeem SOL(TRADE)

Redeem BNSOL get SOL

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_sol_staking_sol_redeem_v1_resp import CreateSolStakingSolRedeemV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Redeem SOL(TRADE)
        api_response = api_instance.create_sol_staking_sol_redeem_v1(amount, timestamp, recv_window=recv_window)
        print("The response of StakingApi->create_sol_staking_sol_redeem_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_sol_staking_sol_redeem_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSolStakingSolRedeemV1Resp**](CreateSolStakingSolRedeemV1Resp.md)

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

# **create_sol_staking_sol_stake_v1**
> CreateSolStakingSolStakeV1Resp create_sol_staking_sol_stake_v1(amount, timestamp, recv_window=recv_window)

Subscribe SOL Staking(TRADE)

Subscribe SOL Staking

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_sol_staking_sol_stake_v1_resp import CreateSolStakingSolStakeV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Subscribe SOL Staking(TRADE)
        api_response = api_instance.create_sol_staking_sol_stake_v1(amount, timestamp, recv_window=recv_window)
        print("The response of StakingApi->create_sol_staking_sol_stake_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->create_sol_staking_sol_stake_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSolStakingSolStakeV1Resp**](CreateSolStakingSolStakeV1Resp.md)

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

# **get_eth_staking_account_v2**
> GetEthStakingAccountV2Resp get_eth_staking_account_v2(timestamp, recv_window=recv_window)

ETH Staking account(USER_DATA)

ETH Staking account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_account_v2_resp import GetEthStakingAccountV2Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # ETH Staking account(USER_DATA)
        api_response = api_instance.get_eth_staking_account_v2(timestamp, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingAccountV2Resp**](GetEthStakingAccountV2Resp.md)

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

# **get_eth_staking_eth_history_rate_history_v1**
> GetEthStakingEthHistoryRateHistoryV1Resp get_eth_staking_eth_history_rate_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get WBETH Rate History(USER_DATA)

Get WBETH Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_history_rate_history_v1_resp import GetEthStakingEthHistoryRateHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get WBETH Rate History(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_history_rate_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_history_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_history_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthHistoryRateHistoryV1Resp**](GetEthStakingEthHistoryRateHistoryV1Resp.md)

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

# **get_eth_staking_eth_history_redemption_history_v1**
> GetEthStakingEthHistoryRedemptionHistoryV1Resp get_eth_staking_eth_history_redemption_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get ETH redemption history(USER_DATA)

Get ETH redemption history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_history_redemption_history_v1_resp import GetEthStakingEthHistoryRedemptionHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get ETH redemption history(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_history_redemption_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_history_redemption_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_history_redemption_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthHistoryRedemptionHistoryV1Resp**](GetEthStakingEthHistoryRedemptionHistoryV1Resp.md)

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

# **get_eth_staking_eth_history_rewards_history_v1**
> GetEthStakingEthHistoryRewardsHistoryV1Resp get_eth_staking_eth_history_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get BETH rewards distribution history(USER_DATA)

Get BETH rewards distribution history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_history_rewards_history_v1_resp import GetEthStakingEthHistoryRewardsHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get BETH rewards distribution history(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_history_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_history_rewards_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_history_rewards_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthHistoryRewardsHistoryV1Resp**](GetEthStakingEthHistoryRewardsHistoryV1Resp.md)

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

# **get_eth_staking_eth_history_staking_history_v1**
> GetEthStakingEthHistoryStakingHistoryV1Resp get_eth_staking_eth_history_staking_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get ETH staking history(USER_DATA)

Get ETH staking history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_history_staking_history_v1_resp import GetEthStakingEthHistoryStakingHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get ETH staking history(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_history_staking_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_history_staking_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_history_staking_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthHistoryStakingHistoryV1Resp**](GetEthStakingEthHistoryStakingHistoryV1Resp.md)

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

# **get_eth_staking_eth_history_wbeth_rewards_history_v1**
> GetEthStakingEthHistoryWbethRewardsHistoryV1Resp get_eth_staking_eth_history_wbeth_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get WBETH rewards history(USER_DATA)

Get WBETH rewards history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_history_wbeth_rewards_history_v1_resp import GetEthStakingEthHistoryWbethRewardsHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get WBETH rewards history(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_history_wbeth_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_history_wbeth_rewards_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_history_wbeth_rewards_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthHistoryWbethRewardsHistoryV1Resp**](GetEthStakingEthHistoryWbethRewardsHistoryV1Resp.md)

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

# **get_eth_staking_eth_quota_v1**
> GetEthStakingEthQuotaV1Resp get_eth_staking_eth_quota_v1(timestamp, recv_window=recv_window)

Get current ETH staking quota(USER_DATA)

Get current ETH staking quota

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_eth_quota_v1_resp import GetEthStakingEthQuotaV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get current ETH staking quota(USER_DATA)
        api_response = api_instance.get_eth_staking_eth_quota_v1(timestamp, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_eth_quota_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_eth_quota_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingEthQuotaV1Resp**](GetEthStakingEthQuotaV1Resp.md)

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

# **get_eth_staking_wbeth_history_unwrap_history_v1**
> GetEthStakingWbethHistoryUnwrapHistoryV1Resp get_eth_staking_wbeth_history_unwrap_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get WBETH unwrap history(USER_DATA)

Get WBETH unwrap history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_wbeth_history_unwrap_history_v1_resp import GetEthStakingWbethHistoryUnwrapHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get WBETH unwrap history(USER_DATA)
        api_response = api_instance.get_eth_staking_wbeth_history_unwrap_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_wbeth_history_unwrap_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_wbeth_history_unwrap_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingWbethHistoryUnwrapHistoryV1Resp**](GetEthStakingWbethHistoryUnwrapHistoryV1Resp.md)

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

# **get_eth_staking_wbeth_history_wrap_history_v1**
> GetEthStakingWbethHistoryWrapHistoryV1Resp get_eth_staking_wbeth_history_wrap_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get WBETH wrap history(USER_DATA)

Get WBETH wrap history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_eth_staking_wbeth_history_wrap_history_v1_resp import GetEthStakingWbethHistoryWrapHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get WBETH wrap history(USER_DATA)
        api_response = api_instance.get_eth_staking_wbeth_history_wrap_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_eth_staking_wbeth_history_wrap_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_eth_staking_wbeth_history_wrap_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetEthStakingWbethHistoryWrapHistoryV1Resp**](GetEthStakingWbethHistoryWrapHistoryV1Resp.md)

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

# **get_sol_staking_account_v1**
> GetSolStakingAccountV1Resp get_sol_staking_account_v1(timestamp, recv_window=recv_window)

SOL Staking account(USER_DATA)

SOL Staking account

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_account_v1_resp import GetSolStakingAccountV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # SOL Staking account(USER_DATA)
        api_response = api_instance.get_sol_staking_account_v1(timestamp, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetSolStakingAccountV1Resp**](GetSolStakingAccountV1Resp.md)

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

# **get_sol_staking_sol_history_bnsol_rewards_history_v1**
> GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp get_sol_staking_sol_history_bnsol_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get BNSOL rewards history(USER_DATA)

Get BNSOL rewards history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_bnsol_rewards_history_v1_resp import GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get BNSOL rewards history(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_bnsol_rewards_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_bnsol_rewards_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_bnsol_rewards_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp**](GetSolStakingSolHistoryBnsolRewardsHistoryV1Resp.md)

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

# **get_sol_staking_sol_history_boost_rewards_history_v1**
> GetSolStakingSolHistoryBoostRewardsHistoryV1Resp get_sol_staking_sol_history_boost_rewards_history_v1(type, timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Boost Rewards History(USER_DATA)

Get Boost rewards history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_boost_rewards_history_v1_resp import GetSolStakingSolHistoryBoostRewardsHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    type = '' # str | &#34;CLAIM&#34;, &#34;DISTRIBUTE&#34;, default &#34;CLAIM&#34; (default to '')
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get Boost Rewards History(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_boost_rewards_history_v1(type, timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_boost_rewards_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_boost_rewards_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &amp;#34;CLAIM&amp;#34;, &amp;#34;DISTRIBUTE&amp;#34;, default &amp;#34;CLAIM&amp;#34; | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSolStakingSolHistoryBoostRewardsHistoryV1Resp**](GetSolStakingSolHistoryBoostRewardsHistoryV1Resp.md)

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

# **get_sol_staking_sol_history_rate_history_v1**
> GetSolStakingSolHistoryRateHistoryV1Resp get_sol_staking_sol_history_rate_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get BNSOL Rate History(USER_DATA)

Get BNSOL Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_rate_history_v1_resp import GetSolStakingSolHistoryRateHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get BNSOL Rate History(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_rate_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetSolStakingSolHistoryRateHistoryV1Resp**](GetSolStakingSolHistoryRateHistoryV1Resp.md)

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

# **get_sol_staking_sol_history_redemption_history_v1**
> GetSolStakingSolHistoryRedemptionHistoryV1Resp get_sol_staking_sol_history_redemption_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get SOL redemption history(USER_DATA)

Get SOL redemption history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_redemption_history_v1_resp import GetSolStakingSolHistoryRedemptionHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get SOL redemption history(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_redemption_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_redemption_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_redemption_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSolStakingSolHistoryRedemptionHistoryV1Resp**](GetSolStakingSolHistoryRedemptionHistoryV1Resp.md)

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

# **get_sol_staking_sol_history_staking_history_v1**
> GetSolStakingSolHistoryStakingHistoryV1Resp get_sol_staking_sol_history_staking_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get SOL staking history(USER_DATA)

Get SOL staking history

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_staking_history_v1_resp import GetSolStakingSolHistoryStakingHistoryV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 1 # int | Currently querying page. Start from 1. Default: 1 (optional) (default to 1)
    size = 10 # int | Default: 10, Max: 100 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Get SOL staking history(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_staking_history_v1(timestamp, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_staking_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_staking_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default: 1 | [optional] [default to 1]
 **size** | **int**| Default: 10, Max: 100 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSolStakingSolHistoryStakingHistoryV1Resp**](GetSolStakingSolHistoryStakingHistoryV1Resp.md)

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

# **get_sol_staking_sol_history_unclaimed_rewards_v1**
> List[GetSolStakingSolHistoryUnclaimedRewardsV1RespItem] get_sol_staking_sol_history_unclaimed_rewards_v1(timestamp, recv_window=recv_window)

Get Unclaimed Rewards(USER_DATA)

Get Unclaimed rewards

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_history_unclaimed_rewards_v1_resp_item import GetSolStakingSolHistoryUnclaimedRewardsV1RespItem
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Unclaimed Rewards(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_history_unclaimed_rewards_v1(timestamp, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_history_unclaimed_rewards_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_history_unclaimed_rewards_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetSolStakingSolHistoryUnclaimedRewardsV1RespItem]**](GetSolStakingSolHistoryUnclaimedRewardsV1RespItem.md)

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

# **get_sol_staking_sol_quota_v1**
> GetSolStakingSolQuotaV1Resp get_sol_staking_sol_quota_v1(timestamp, recv_window=recv_window)

Get SOL staking quota details(USER_DATA)

Get SOL staking quota

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_sol_staking_sol_quota_v1_resp import GetSolStakingSolQuotaV1Resp
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
    api_instance = binance.spot.StakingApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get SOL staking quota details(USER_DATA)
        api_response = api_instance.get_sol_staking_sol_quota_v1(timestamp, recv_window=recv_window)
        print("The response of StakingApi->get_sol_staking_sol_quota_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_sol_staking_sol_quota_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetSolStakingSolQuotaV1Resp**](GetSolStakingSolQuotaV1Resp.md)

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

