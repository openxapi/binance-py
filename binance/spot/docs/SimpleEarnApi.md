# binance.spot.SimpleEarnApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simple_earn_flexible_redeem_v1**](SimpleEarnApi.md#create_simple_earn_flexible_redeem_v1) | **POST** /sapi/v1/simple-earn/flexible/redeem | Redeem Flexible Product(TRADE)
[**create_simple_earn_flexible_set_auto_subscribe_v1**](SimpleEarnApi.md#create_simple_earn_flexible_set_auto_subscribe_v1) | **POST** /sapi/v1/simple-earn/flexible/setAutoSubscribe | Set Flexible Auto Subscribe(USER_DATA)
[**create_simple_earn_flexible_subscribe_v1**](SimpleEarnApi.md#create_simple_earn_flexible_subscribe_v1) | **POST** /sapi/v1/simple-earn/flexible/subscribe | Subscribe Flexible Product(TRADE)
[**create_simple_earn_locked_redeem_v1**](SimpleEarnApi.md#create_simple_earn_locked_redeem_v1) | **POST** /sapi/v1/simple-earn/locked/redeem | Redeem Locked Product(TRADE)
[**create_simple_earn_locked_set_auto_subscribe_v1**](SimpleEarnApi.md#create_simple_earn_locked_set_auto_subscribe_v1) | **POST** /sapi/v1/simple-earn/locked/setAutoSubscribe | Set Locked Auto Subscribe(USER_DATA)
[**create_simple_earn_locked_set_redeem_option_v1**](SimpleEarnApi.md#create_simple_earn_locked_set_redeem_option_v1) | **POST** /sapi/v1/simple-earn/locked/setRedeemOption | Set Locked Product Redeem Option(USER_DATA)
[**create_simple_earn_locked_subscribe_v1**](SimpleEarnApi.md#create_simple_earn_locked_subscribe_v1) | **POST** /sapi/v1/simple-earn/locked/subscribe | Subscribe Locked Product(TRADE)
[**get_simple_earn_account_v1**](SimpleEarnApi.md#get_simple_earn_account_v1) | **GET** /sapi/v1/simple-earn/account | Simple Account(USER_DATA)
[**get_simple_earn_flexible_history_collateral_record_v1**](SimpleEarnApi.md#get_simple_earn_flexible_history_collateral_record_v1) | **GET** /sapi/v1/simple-earn/flexible/history/collateralRecord | Get Collateral Record(USER_DATA)
[**get_simple_earn_flexible_history_rate_history_v1**](SimpleEarnApi.md#get_simple_earn_flexible_history_rate_history_v1) | **GET** /sapi/v1/simple-earn/flexible/history/rateHistory | Get Rate History(USER_DATA)
[**get_simple_earn_flexible_history_redemption_record_v1**](SimpleEarnApi.md#get_simple_earn_flexible_history_redemption_record_v1) | **GET** /sapi/v1/simple-earn/flexible/history/redemptionRecord | Get Flexible Redemption Record(USER_DATA)
[**get_simple_earn_flexible_history_rewards_record_v1**](SimpleEarnApi.md#get_simple_earn_flexible_history_rewards_record_v1) | **GET** /sapi/v1/simple-earn/flexible/history/rewardsRecord | Get Flexible Rewards History(USER_DATA)
[**get_simple_earn_flexible_history_subscription_record_v1**](SimpleEarnApi.md#get_simple_earn_flexible_history_subscription_record_v1) | **GET** /sapi/v1/simple-earn/flexible/history/subscriptionRecord | Get Flexible Subscription Record(USER_DATA)
[**get_simple_earn_flexible_list_v1**](SimpleEarnApi.md#get_simple_earn_flexible_list_v1) | **GET** /sapi/v1/simple-earn/flexible/list | Get Simple Earn Flexible Product List(USER_DATA)
[**get_simple_earn_flexible_personal_left_quota_v1**](SimpleEarnApi.md#get_simple_earn_flexible_personal_left_quota_v1) | **GET** /sapi/v1/simple-earn/flexible/personalLeftQuota | Get Flexible Personal Left Quota(USER_DATA)
[**get_simple_earn_flexible_position_v1**](SimpleEarnApi.md#get_simple_earn_flexible_position_v1) | **GET** /sapi/v1/simple-earn/flexible/position | Get Flexible Product Position(USER_DATA)
[**get_simple_earn_flexible_subscription_preview_v1**](SimpleEarnApi.md#get_simple_earn_flexible_subscription_preview_v1) | **GET** /sapi/v1/simple-earn/flexible/subscriptionPreview | Get Flexible Subscription Preview(USER_DATA)
[**get_simple_earn_locked_history_redemption_record_v1**](SimpleEarnApi.md#get_simple_earn_locked_history_redemption_record_v1) | **GET** /sapi/v1/simple-earn/locked/history/redemptionRecord | Get Locked Redemption Record(USER_DATA)
[**get_simple_earn_locked_history_rewards_record_v1**](SimpleEarnApi.md#get_simple_earn_locked_history_rewards_record_v1) | **GET** /sapi/v1/simple-earn/locked/history/rewardsRecord | Get Locked Rewards History(USER_DATA)
[**get_simple_earn_locked_history_subscription_record_v1**](SimpleEarnApi.md#get_simple_earn_locked_history_subscription_record_v1) | **GET** /sapi/v1/simple-earn/locked/history/subscriptionRecord | Get Locked Subscription Record(USER_DATA)
[**get_simple_earn_locked_list_v1**](SimpleEarnApi.md#get_simple_earn_locked_list_v1) | **GET** /sapi/v1/simple-earn/locked/list | Get Simple Earn Locked Product List(USER_DATA)
[**get_simple_earn_locked_personal_left_quota_v1**](SimpleEarnApi.md#get_simple_earn_locked_personal_left_quota_v1) | **GET** /sapi/v1/simple-earn/locked/personalLeftQuota | Get Locked Personal Left Quota(USER_DATA)
[**get_simple_earn_locked_position_v1**](SimpleEarnApi.md#get_simple_earn_locked_position_v1) | **GET** /sapi/v1/simple-earn/locked/position | Get Locked Product Position
[**get_simple_earn_locked_subscription_preview_v1**](SimpleEarnApi.md#get_simple_earn_locked_subscription_preview_v1) | **GET** /sapi/v1/simple-earn/locked/subscriptionPreview | Get Locked Subscription Preview(USER_DATA)


# **create_simple_earn_flexible_redeem_v1**
> CreateSimpleEarnFlexibleRedeemV1Resp create_simple_earn_flexible_redeem_v1(product_id, timestamp, amount=amount, dest_account=dest_account, recv_window=recv_window, redeem_all=redeem_all)

Redeem Flexible Product(TRADE)

Redeem Flexible Product

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_flexible_redeem_v1_resp import CreateSimpleEarnFlexibleRedeemV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    product_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    amount = '' # str |  (optional) (default to '')
    dest_account = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    redeem_all = True # bool |  (optional)

    try:
        # Redeem Flexible Product(TRADE)
        api_response = api_instance.create_simple_earn_flexible_redeem_v1(product_id, timestamp, amount=amount, dest_account=dest_account, recv_window=recv_window, redeem_all=redeem_all)
        print("The response of SimpleEarnApi->create_simple_earn_flexible_redeem_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_flexible_redeem_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **amount** | **str**|  | [optional] [default to &#39;&#39;]
 **dest_account** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **redeem_all** | **bool**|  | [optional] 

### Return type

[**CreateSimpleEarnFlexibleRedeemV1Resp**](CreateSimpleEarnFlexibleRedeemV1Resp.md)

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

# **create_simple_earn_flexible_set_auto_subscribe_v1**
> CreateSimpleEarnFlexibleSetAutoSubscribeV1Resp create_simple_earn_flexible_set_auto_subscribe_v1(auto_subscribe, product_id, timestamp, recv_window=recv_window)

Set Flexible Auto Subscribe(USER_DATA)

Set Flexible Auto Subscribe

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_flexible_set_auto_subscribe_v1_resp import CreateSimpleEarnFlexibleSetAutoSubscribeV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    auto_subscribe = True # bool | 
    product_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Set Flexible Auto Subscribe(USER_DATA)
        api_response = api_instance.create_simple_earn_flexible_set_auto_subscribe_v1(auto_subscribe, product_id, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->create_simple_earn_flexible_set_auto_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_flexible_set_auto_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_subscribe** | **bool**|  | 
 **product_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSimpleEarnFlexibleSetAutoSubscribeV1Resp**](CreateSimpleEarnFlexibleSetAutoSubscribeV1Resp.md)

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

# **create_simple_earn_flexible_subscribe_v1**
> CreateSimpleEarnFlexibleSubscribeV1Resp create_simple_earn_flexible_subscribe_v1(amount, product_id, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window, source_account=source_account)

Subscribe Flexible Product(TRADE)

Subscribe Flexible Product

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_flexible_subscribe_v1_resp import CreateSimpleEarnFlexibleSubscribeV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    amount = '' # str |  (default to '')
    product_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    auto_subscribe = True # bool |  (optional) (default to True)
    recv_window = 56 # int |  (optional)
    source_account = '' # str |  (optional) (default to '')

    try:
        # Subscribe Flexible Product(TRADE)
        api_response = api_instance.create_simple_earn_flexible_subscribe_v1(amount, product_id, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window, source_account=source_account)
        print("The response of SimpleEarnApi->create_simple_earn_flexible_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_flexible_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **product_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **auto_subscribe** | **bool**|  | [optional] [default to True]
 **recv_window** | **int**|  | [optional] 
 **source_account** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateSimpleEarnFlexibleSubscribeV1Resp**](CreateSimpleEarnFlexibleSubscribeV1Resp.md)

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

# **create_simple_earn_locked_redeem_v1**
> CreateSimpleEarnLockedRedeemV1Resp create_simple_earn_locked_redeem_v1(position_id, timestamp, recv_window=recv_window)

Redeem Locked Product(TRADE)

Redeem Locked Product

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_locked_redeem_v1_resp import CreateSimpleEarnLockedRedeemV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    position_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Redeem Locked Product(TRADE)
        api_response = api_instance.create_simple_earn_locked_redeem_v1(position_id, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->create_simple_earn_locked_redeem_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_locked_redeem_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSimpleEarnLockedRedeemV1Resp**](CreateSimpleEarnLockedRedeemV1Resp.md)

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

# **create_simple_earn_locked_set_auto_subscribe_v1**
> CreateSimpleEarnLockedSetAutoSubscribeV1Resp create_simple_earn_locked_set_auto_subscribe_v1(auto_subscribe, position_id, timestamp, recv_window=recv_window)

Set Locked Auto Subscribe(USER_DATA)

Set locked auto subscribe

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_locked_set_auto_subscribe_v1_resp import CreateSimpleEarnLockedSetAutoSubscribeV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    auto_subscribe = True # bool | 
    position_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Set Locked Auto Subscribe(USER_DATA)
        api_response = api_instance.create_simple_earn_locked_set_auto_subscribe_v1(auto_subscribe, position_id, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->create_simple_earn_locked_set_auto_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_locked_set_auto_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_subscribe** | **bool**|  | 
 **position_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSimpleEarnLockedSetAutoSubscribeV1Resp**](CreateSimpleEarnLockedSetAutoSubscribeV1Resp.md)

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

# **create_simple_earn_locked_set_redeem_option_v1**
> CreateSimpleEarnLockedSetRedeemOptionV1Resp create_simple_earn_locked_set_redeem_option_v1(position_id, redeem_to, timestamp, recv_window=recv_window)

Set Locked Product Redeem Option(USER_DATA)

Set redeem option for Locked product

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_locked_set_redeem_option_v1_resp import CreateSimpleEarnLockedSetRedeemOptionV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    position_id = '' # str |  (default to '')
    redeem_to = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Set Locked Product Redeem Option(USER_DATA)
        api_response = api_instance.create_simple_earn_locked_set_redeem_option_v1(position_id, redeem_to, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->create_simple_earn_locked_set_redeem_option_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_locked_set_redeem_option_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**|  | [default to &#39;&#39;]
 **redeem_to** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateSimpleEarnLockedSetRedeemOptionV1Resp**](CreateSimpleEarnLockedSetRedeemOptionV1Resp.md)

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

# **create_simple_earn_locked_subscribe_v1**
> CreateSimpleEarnLockedSubscribeV1Resp create_simple_earn_locked_subscribe_v1(amount, project_id, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window, redeem_to=redeem_to, source_account=source_account)

Subscribe Locked Product(TRADE)

Subscribe Locked Product

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_simple_earn_locked_subscribe_v1_resp import CreateSimpleEarnLockedSubscribeV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    amount = '' # str |  (default to '')
    project_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    auto_subscribe = False # bool |  (optional) (default to False)
    recv_window = 56 # int |  (optional)
    redeem_to = '' # str |  (optional) (default to '')
    source_account = '' # str |  (optional) (default to '')

    try:
        # Subscribe Locked Product(TRADE)
        api_response = api_instance.create_simple_earn_locked_subscribe_v1(amount, project_id, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window, redeem_to=redeem_to, source_account=source_account)
        print("The response of SimpleEarnApi->create_simple_earn_locked_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->create_simple_earn_locked_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **project_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **auto_subscribe** | **bool**|  | [optional] [default to False]
 **recv_window** | **int**|  | [optional] 
 **redeem_to** | **str**|  | [optional] [default to &#39;&#39;]
 **source_account** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateSimpleEarnLockedSubscribeV1Resp**](CreateSimpleEarnLockedSubscribeV1Resp.md)

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

# **get_simple_earn_account_v1**
> GetSimpleEarnAccountV1Resp get_simple_earn_account_v1(timestamp, recv_window=recv_window)

Simple Account(USER_DATA)

Simple Account query

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_account_v1_resp import GetSimpleEarnAccountV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int | The value cannot be greater than `60000` (optional)

    try:
        # Simple Account(USER_DATA)
        api_response = api_instance.get_simple_earn_account_v1(timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**| The value cannot be greater than &#x60;60000&#x60; | [optional] 

### Return type

[**GetSimpleEarnAccountV1Resp**](GetSimpleEarnAccountV1Resp.md)

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

# **get_simple_earn_flexible_history_collateral_record_v1**
> GetSimpleEarnFlexibleHistoryCollateralRecordV1Resp get_simple_earn_flexible_history_collateral_record_v1(timestamp, product_id=product_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Collateral Record(USER_DATA)

Get Collateral Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_history_collateral_record_v1_resp import GetSimpleEarnFlexibleHistoryCollateralRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    product_id = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get Collateral Record(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_history_collateral_record_v1(timestamp, product_id=product_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_history_collateral_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_history_collateral_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **product_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetSimpleEarnFlexibleHistoryCollateralRecordV1Resp**](GetSimpleEarnFlexibleHistoryCollateralRecordV1Resp.md)

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

# **get_simple_earn_flexible_history_rate_history_v1**
> GetSimpleEarnFlexibleHistoryRateHistoryV1Resp get_simple_earn_flexible_history_rate_history_v1(product_id, timestamp, apr_period=apr_period, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Rate History(USER_DATA)

Get Rate History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_history_rate_history_v1_resp import GetSimpleEarnFlexibleHistoryRateHistoryV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    product_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    apr_period = '' # str | &#34;DAY&#34;,&#34;YEAR&#34;,default&#34;DAY&#34; (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int | The value cannot be greater than 60000 (optional)

    try:
        # Get Rate History(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_history_rate_history_v1(product_id, timestamp, apr_period=apr_period, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_history_rate_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_history_rate_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **apr_period** | **str**| &amp;#34;DAY&amp;#34;,&amp;#34;YEAR&amp;#34;,default&amp;#34;DAY&amp;#34; | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**GetSimpleEarnFlexibleHistoryRateHistoryV1Resp**](GetSimpleEarnFlexibleHistoryRateHistoryV1Resp.md)

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

# **get_simple_earn_flexible_history_redemption_record_v1**
> GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp get_simple_earn_flexible_history_redemption_record_v1(product_id=product_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size)

Get Flexible Redemption Record(USER_DATA)

Get Flexible Redemption Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_history_redemption_record_v1_resp import GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    product_id = '' # str |  (optional) (default to '')
    redeem_id = '' # str |  (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)

    try:
        # Get Flexible Redemption Record(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_history_redemption_record_v1(product_id=product_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_history_redemption_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_history_redemption_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [optional] [default to &#39;&#39;]
 **redeem_id** | **str**|  | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 

### Return type

[**GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp**](GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp.md)

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

# **get_simple_earn_flexible_history_rewards_record_v1**
> GetSimpleEarnFlexibleHistoryRewardsRecordV1Resp get_simple_earn_flexible_history_rewards_record_v1(type, timestamp, product_id=product_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Flexible Rewards History(USER_DATA)

Get Flexible Rewards History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_history_rewards_record_v1_resp import GetSimpleEarnFlexibleHistoryRewardsRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    type = '' # str | `Bonus` - Bonus tiered APR, `REALTIME` Real-time APR, `REWARDS` Historical rewards,`ALL`(set to default) (default to '')
    timestamp = 56 # int | 
    product_id = '' # str |  (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Rewards History(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_history_rewards_record_v1(type, timestamp, product_id=product_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_history_rewards_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_history_rewards_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &#x60;Bonus&#x60; - Bonus tiered APR, &#x60;REALTIME&#x60; Real-time APR, &#x60;REWARDS&#x60; Historical rewards,&#x60;ALL&#x60;(set to default) | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **product_id** | **str**|  | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexibleHistoryRewardsRecordV1Resp**](GetSimpleEarnFlexibleHistoryRewardsRecordV1Resp.md)

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

# **get_simple_earn_flexible_history_subscription_record_v1**
> GetSimpleEarnFlexibleHistorySubscriptionRecordV1Resp get_simple_earn_flexible_history_subscription_record_v1(timestamp, product_id=product_id, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Flexible Subscription Record(USER_DATA)

Get Flexible Subscription Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_history_subscription_record_v1_resp import GetSimpleEarnFlexibleHistorySubscriptionRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    product_id = '' # str |  (optional) (default to '')
    purchase_id = '' # str |  (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Subscription Record(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_history_subscription_record_v1(timestamp, product_id=product_id, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_history_subscription_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_history_subscription_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **product_id** | **str**|  | [optional] [default to &#39;&#39;]
 **purchase_id** | **str**|  | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexibleHistorySubscriptionRecordV1Resp**](GetSimpleEarnFlexibleHistorySubscriptionRecordV1Resp.md)

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

# **get_simple_earn_flexible_list_v1**
> GetSimpleEarnFlexibleListV1Resp get_simple_earn_flexible_list_v1(timestamp, asset=asset, current=current, size=size, recv_window=recv_window)

Get Simple Earn Flexible Product List(USER_DATA)

Get available Simple Earn flexible product list

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_list_v1_resp import GetSimpleEarnFlexibleListV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Simple Earn Flexible Product List(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_list_v1(timestamp, asset=asset, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexibleListV1Resp**](GetSimpleEarnFlexibleListV1Resp.md)

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

# **get_simple_earn_flexible_personal_left_quota_v1**
> GetSimpleEarnFlexiblePersonalLeftQuotaV1Resp get_simple_earn_flexible_personal_left_quota_v1(product_id, timestamp, recv_window=recv_window)

Get Flexible Personal Left Quota(USER_DATA)

Get Flexible Personal Left Quota

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_personal_left_quota_v1_resp import GetSimpleEarnFlexiblePersonalLeftQuotaV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    product_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Personal Left Quota(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_personal_left_quota_v1(product_id, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_personal_left_quota_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_personal_left_quota_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexiblePersonalLeftQuotaV1Resp**](GetSimpleEarnFlexiblePersonalLeftQuotaV1Resp.md)

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

# **get_simple_earn_flexible_position_v1**
> GetSimpleEarnFlexiblePositionV1Resp get_simple_earn_flexible_position_v1(timestamp, asset=asset, product_id=product_id, current=current, size=size, recv_window=recv_window)

Get Flexible Product Position(USER_DATA)

Get Flexible Product Position

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_position_v1_resp import GetSimpleEarnFlexiblePositionV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    product_id = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Product Position(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_position_v1(timestamp, asset=asset, product_id=product_id, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **product_id** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexiblePositionV1Resp**](GetSimpleEarnFlexiblePositionV1Resp.md)

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

# **get_simple_earn_flexible_subscription_preview_v1**
> GetSimpleEarnFlexibleSubscriptionPreviewV1Resp get_simple_earn_flexible_subscription_preview_v1(product_id, amount, timestamp, recv_window=recv_window)

Get Flexible Subscription Preview(USER_DATA)

Get Flexible Subscription Preview

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_flexible_subscription_preview_v1_resp import GetSimpleEarnFlexibleSubscriptionPreviewV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    product_id = '' # str |  (default to '')
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Flexible Subscription Preview(USER_DATA)
        api_response = api_instance.get_simple_earn_flexible_subscription_preview_v1(product_id, amount, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_flexible_subscription_preview_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_flexible_subscription_preview_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [default to &#39;&#39;]
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnFlexibleSubscriptionPreviewV1Resp**](GetSimpleEarnFlexibleSubscriptionPreviewV1Resp.md)

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

# **get_simple_earn_locked_history_redemption_record_v1**
> GetSimpleEarnLockedHistoryRedemptionRecordV1Resp get_simple_earn_locked_history_redemption_record_v1(timestamp, position_id=position_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Locked Redemption Record(USER_DATA)

Get Locked Redemption Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_history_redemption_record_v1_resp import GetSimpleEarnLockedHistoryRedemptionRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    position_id = 56 # int |  (optional)
    redeem_id = '' # str |  (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Redemption Record(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_history_redemption_record_v1(timestamp, position_id=position_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_history_redemption_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_history_redemption_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **position_id** | **int**|  | [optional] 
 **redeem_id** | **str**|  | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedHistoryRedemptionRecordV1Resp**](GetSimpleEarnLockedHistoryRedemptionRecordV1Resp.md)

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

# **get_simple_earn_locked_history_rewards_record_v1**
> GetSimpleEarnLockedHistoryRewardsRecordV1Resp get_simple_earn_locked_history_rewards_record_v1(timestamp, position_id=position_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Locked Rewards History(USER_DATA)

Get Locked Rewards History

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_history_rewards_record_v1_resp import GetSimpleEarnLockedHistoryRewardsRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    position_id = 56 # int |  (optional)
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1, Default:1, Max: 1,000 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Rewards History(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_history_rewards_record_v1(timestamp, position_id=position_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_history_rewards_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_history_rewards_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **position_id** | **int**|  | [optional] 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1, Default:1, Max: 1,000 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedHistoryRewardsRecordV1Resp**](GetSimpleEarnLockedHistoryRewardsRecordV1Resp.md)

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

# **get_simple_earn_locked_history_subscription_record_v1**
> GetSimpleEarnLockedHistorySubscriptionRecordV1Resp get_simple_earn_locked_history_subscription_record_v1(timestamp, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Locked Subscription Record(USER_DATA)

Get Locked Subscription Record

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_history_subscription_record_v1_resp import GetSimpleEarnLockedHistorySubscriptionRecordV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    purchase_id = '' # str |  (optional) (default to '')
    asset = '' # str |  (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Subscription Record(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_history_subscription_record_v1(timestamp, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_history_subscription_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_history_subscription_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **purchase_id** | **str**|  | [optional] [default to &#39;&#39;]
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedHistorySubscriptionRecordV1Resp**](GetSimpleEarnLockedHistorySubscriptionRecordV1Resp.md)

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

# **get_simple_earn_locked_list_v1**
> GetSimpleEarnLockedListV1Resp get_simple_earn_locked_list_v1(timestamp, asset=asset, current=current, size=size, recv_window=recv_window)

Get Simple Earn Locked Product List(USER_DATA)

Get Simple Earn Locked Product List

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_list_v1_resp import GetSimpleEarnLockedListV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Simple Earn Locked Product List(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_list_v1(timestamp, asset=asset, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedListV1Resp**](GetSimpleEarnLockedListV1Resp.md)

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

# **get_simple_earn_locked_personal_left_quota_v1**
> GetSimpleEarnLockedPersonalLeftQuotaV1Resp get_simple_earn_locked_personal_left_quota_v1(project_id, timestamp, recv_window=recv_window)

Get Locked Personal Left Quota(USER_DATA)

Get Locked Personal Left Quota

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_personal_left_quota_v1_resp import GetSimpleEarnLockedPersonalLeftQuotaV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    project_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Personal Left Quota(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_personal_left_quota_v1(project_id, timestamp, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_personal_left_quota_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_personal_left_quota_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedPersonalLeftQuotaV1Resp**](GetSimpleEarnLockedPersonalLeftQuotaV1Resp.md)

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

# **get_simple_earn_locked_position_v1**
> GetSimpleEarnLockedPositionV1Resp get_simple_earn_locked_position_v1(timestamp, asset=asset, position_id=position_id, project_id=project_id, current=current, size=size, recv_window=recv_window)

Get Locked Product Position

Get Locked Product Position

### Example


```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_position_v1_resp import GetSimpleEarnLockedPositionV1Resp
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    timestamp = 56 # int | 
    asset = '' # str |  (optional) (default to '')
    position_id = 56 # int |  (optional)
    project_id = '' # str |  (optional) (default to '')
    current = 56 # int | Currently querying the page. Start from 1. Default:1 (optional)
    size = 56 # int | Default:10, Max:100 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Product Position
        api_response = api_instance.get_simple_earn_locked_position_v1(timestamp, asset=asset, position_id=position_id, project_id=project_id, current=current, size=size, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_position_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_position_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **asset** | **str**|  | [optional] [default to &#39;&#39;]
 **position_id** | **int**|  | [optional] 
 **project_id** | **str**|  | [optional] [default to &#39;&#39;]
 **current** | **int**| Currently querying the page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10, Max:100 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetSimpleEarnLockedPositionV1Resp**](GetSimpleEarnLockedPositionV1Resp.md)

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

# **get_simple_earn_locked_subscription_preview_v1**
> List[GetSimpleEarnLockedSubscriptionPreviewV1RespItem] get_simple_earn_locked_subscription_preview_v1(project_id, amount, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window)

Get Locked Subscription Preview(USER_DATA)

Get Locked Subscription Preview

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_simple_earn_locked_subscription_preview_v1_resp_item import GetSimpleEarnLockedSubscriptionPreviewV1RespItem
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
    api_instance = binance.spot.SimpleEarnApi(api_client)
    project_id = '' # str |  (default to '')
    amount = '' # str |  (default to '')
    timestamp = 56 # int | 
    auto_subscribe = True # bool | true or false, default true. (optional) (default to True)
    recv_window = 56 # int |  (optional)

    try:
        # Get Locked Subscription Preview(USER_DATA)
        api_response = api_instance.get_simple_earn_locked_subscription_preview_v1(project_id, amount, timestamp, auto_subscribe=auto_subscribe, recv_window=recv_window)
        print("The response of SimpleEarnApi->get_simple_earn_locked_subscription_preview_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleEarnApi->get_simple_earn_locked_subscription_preview_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [default to &#39;&#39;]
 **amount** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **auto_subscribe** | **bool**| true or false, default true. | [optional] [default to True]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetSimpleEarnLockedSubscriptionPreviewV1RespItem]**](GetSimpleEarnLockedSubscriptionPreviewV1RespItem.md)

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

