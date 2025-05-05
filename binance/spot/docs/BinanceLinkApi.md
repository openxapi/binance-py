# binance.spot.BinanceLinkApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_referral_customization_v1**](BinanceLinkApi.md#create_api_referral_customization_v1) | **POST** /sapi/v1/apiReferral/customization | Customize Id For Client (USER DATA) （For Partner）
[**create_api_referral_user_customization_v1**](BinanceLinkApi.md#create_api_referral_user_customization_v1) | **POST** /sapi/v1/apiReferral/userCustomization | Customize Id For Client  (USER DATA)(For client)
[**create_broker_sub_account_api_commission_coin_futures_v1**](BinanceLinkApi.md#create_broker_sub_account_api_commission_coin_futures_v1) | **POST** /sapi/v1/broker/subAccountApi/commission/coinFutures | Change Sub Account COIN-Ⓜ Futures Commission Adjustment
[**create_broker_sub_account_api_commission_futures_v1**](BinanceLinkApi.md#create_broker_sub_account_api_commission_futures_v1) | **POST** /sapi/v1/broker/subAccountApi/commission/futures | Change Sub Account USDT-Ⓜ Futures Commission Adjustment
[**create_broker_sub_account_api_commission_v1**](BinanceLinkApi.md#create_broker_sub_account_api_commission_v1) | **POST** /sapi/v1/broker/subAccountApi/commission | Change Sub Account Commission
[**create_broker_sub_account_api_ip_restriction_v2**](BinanceLinkApi.md#create_broker_sub_account_api_ip_restriction_v2) | **POST** /sapi/v2/broker/subAccountApi/ipRestriction | Update IP Restriction for Sub-Account API key (For Master Account)
[**create_broker_sub_account_api_permission_universal_transfer_v1**](BinanceLinkApi.md#create_broker_sub_account_api_permission_universal_transfer_v1) | **POST** /sapi/v1/broker/subAccountApi/permission/universalTransfer | Enable Universal Transfer Permission For Sub Account Api Key
[**create_broker_sub_account_api_permission_v1**](BinanceLinkApi.md#create_broker_sub_account_api_permission_v1) | **POST** /sapi/v1/broker/subAccountApi/permission | Change Sub Account Api Permission
[**create_broker_sub_account_api_v1**](BinanceLinkApi.md#create_broker_sub_account_api_v1) | **POST** /sapi/v1/broker/subAccountApi | Create Api Key for Sub Account
[**create_broker_sub_account_bnb_burn_margin_interest_v1**](BinanceLinkApi.md#create_broker_sub_account_bnb_burn_margin_interest_v1) | **POST** /sapi/v1/broker/subAccount/bnbBurn/marginInterest | Enable Or Disable BNB Burn for Sub Account Margin Interest
[**create_broker_sub_account_bnb_burn_spot_v1**](BinanceLinkApi.md#create_broker_sub_account_bnb_burn_spot_v1) | **POST** /sapi/v1/broker/subAccount/bnbBurn/spot | Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN
[**create_broker_sub_account_futures_v1**](BinanceLinkApi.md#create_broker_sub_account_futures_v1) | **POST** /sapi/v1/broker/subAccount/futures | Enable Futures for Sub Account
[**create_broker_sub_account_v1**](BinanceLinkApi.md#create_broker_sub_account_v1) | **POST** /sapi/v1/broker/subAccount | Create a Sub Account
[**create_broker_transfer_futures_v1**](BinanceLinkApi.md#create_broker_transfer_futures_v1) | **POST** /sapi/v1/broker/transfer/futures | Sub Account Transfer（FUTURES）
[**create_broker_transfer_v1**](BinanceLinkApi.md#create_broker_transfer_v1) | **POST** /sapi/v1/broker/transfer | Sub Account Transfer（SPOT）
[**create_broker_universal_transfer_v1**](BinanceLinkApi.md#create_broker_universal_transfer_v1) | **POST** /sapi/v1/broker/universalTransfer | Universal Transfer
[**delete_broker_sub_account_api_ip_restriction_ip_list_v1**](BinanceLinkApi.md#delete_broker_sub_account_api_ip_restriction_ip_list_v1) | **DELETE** /sapi/v1/broker/subAccountApi/ipRestriction/ipList | Delete IP Restriction for Sub Account Api Key
[**delete_broker_sub_account_api_v1**](BinanceLinkApi.md#delete_broker_sub_account_api_v1) | **DELETE** /sapi/v1/broker/subAccountApi | Delete Sub Account Api Key
[**delete_broker_sub_account_v1**](BinanceLinkApi.md#delete_broker_sub_account_v1) | **DELETE** /sapi/v1/broker/subAccount | Delete Sub Account
[**get_api_referral_customization_v1**](BinanceLinkApi.md#get_api_referral_customization_v1) | **GET** /sapi/v1/apiReferral/customization | Get Client Email Customized Id (USER DATA) （For Partner）
[**get_api_referral_if_new_user_v1**](BinanceLinkApi.md#get_api_referral_if_new_user_v1) | **GET** /sapi/v1/apiReferral/ifNewUser | Query Client If The New User (USER  DATA)
[**get_api_referral_kickback_recent_record_v1**](BinanceLinkApi.md#get_api_referral_kickback_recent_record_v1) | **GET** /sapi/v1/apiReferral/kickback/recentRecord | Query Rebate Recent Record(For Client)
[**get_api_referral_rebate_recent_record_v1**](BinanceLinkApi.md#get_api_referral_rebate_recent_record_v1) | **GET** /sapi/v1/apiReferral/rebate/recentRecord | Query Rebate Recent Record （USER DATA）(For Partner)
[**get_api_referral_user_customization_v1**](BinanceLinkApi.md#get_api_referral_user_customization_v1) | **GET** /sapi/v1/apiReferral/userCustomization | Get User’s Customize Id (USER DATA)
[**get_broker_info_v1**](BinanceLinkApi.md#get_broker_info_v1) | **GET** /sapi/v1/broker/info | Link Account Information
[**get_broker_rebate_futures_recent_record_v1**](BinanceLinkApi.md#get_broker_rebate_futures_recent_record_v1) | **GET** /sapi/v1/broker/rebate/futures/recentRecord | Query Broker Futures Commission Rebate Record
[**get_broker_rebate_recent_record_v1**](BinanceLinkApi.md#get_broker_rebate_recent_record_v1) | **GET** /sapi/v1/broker/rebate/recentRecord | Query Broker Commission Rebate Recent Record（Spot）
[**get_broker_sub_account_api_commission_coin_futures_v1**](BinanceLinkApi.md#get_broker_sub_account_api_commission_coin_futures_v1) | **GET** /sapi/v1/broker/subAccountApi/commission/coinFutures | Query Sub Account COIN-Ⓜ Futures Commission Adjustment
[**get_broker_sub_account_api_commission_futures_v1**](BinanceLinkApi.md#get_broker_sub_account_api_commission_futures_v1) | **GET** /sapi/v1/broker/subAccountApi/commission/futures | Query Sub Account USDT-Ⓜ Futures Commission Adjustment
[**get_broker_sub_account_api_ip_restriction_v1**](BinanceLinkApi.md#get_broker_sub_account_api_ip_restriction_v1) | **GET** /sapi/v1/broker/subAccountApi/ipRestriction | Get IP Restriction for Sub Account Api Key
[**get_broker_sub_account_api_v1**](BinanceLinkApi.md#get_broker_sub_account_api_v1) | **GET** /sapi/v1/broker/subAccountApi | Query Sub Account Api Key
[**get_broker_sub_account_bnb_burn_status_v1**](BinanceLinkApi.md#get_broker_sub_account_bnb_burn_status_v1) | **GET** /sapi/v1/broker/subAccount/bnbBurn/status | Get BNB Burn Status for Sub Account
[**get_broker_sub_account_deposit_hist_v1**](BinanceLinkApi.md#get_broker_sub_account_deposit_hist_v1) | **GET** /sapi/v1/broker/subAccount/depositHist | Get Sub Account Deposit History
[**get_broker_sub_account_deposit_hist_v2**](BinanceLinkApi.md#get_broker_sub_account_deposit_hist_v2) | **GET** /sapi/v2/broker/subAccount/depositHist | Get Sub Account Deposit History V2
[**get_broker_sub_account_futures_summary_v3**](BinanceLinkApi.md#get_broker_sub_account_futures_summary_v3) | **GET** /sapi/v3/broker/subAccount/futuresSummary | Query Sub Account Futures Asset info (V3)
[**get_broker_sub_account_margin_summary_v1**](BinanceLinkApi.md#get_broker_sub_account_margin_summary_v1) | **GET** /sapi/v1/broker/subAccount/marginSummary | Query Sub Account Margin Asset info
[**get_broker_sub_account_spot_summary_v1**](BinanceLinkApi.md#get_broker_sub_account_spot_summary_v1) | **GET** /sapi/v1/broker/subAccount/spotSummary | Query Sub Account Spot Asset info
[**get_broker_sub_account_v1**](BinanceLinkApi.md#get_broker_sub_account_v1) | **GET** /sapi/v1/broker/subAccount | Query Sub Account
[**get_broker_transfer_futures_v1**](BinanceLinkApi.md#get_broker_transfer_futures_v1) | **GET** /sapi/v1/broker/transfer/futures | Query Sub Account Transfer History（FUTURES）
[**get_broker_transfer_v1**](BinanceLinkApi.md#get_broker_transfer_v1) | **GET** /sapi/v1/broker/transfer | Query Sub Account Transfer History（SPOT）
[**get_broker_universal_transfer_v1**](BinanceLinkApi.md#get_broker_universal_transfer_v1) | **GET** /sapi/v1/broker/universalTransfer | Query Universal Transfer History


# **create_api_referral_customization_v1**
> CreateApiReferralCustomizationV1Resp create_api_referral_customization_v1(customer_id, email, timestamp, recv_window=recv_window)

Customize Id For Client (USER DATA) （For Partner）

- CustomerId must be unique
- For the same email, the customerId will be modified in real time

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_api_referral_customization_v1_resp import CreateApiReferralCustomizationV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    customer_id = '' # str |  (default to '')
    email = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Customize Id For Client (USER DATA) （For Partner）
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

# **create_api_referral_user_customization_v1**
> CreateApiReferralUserCustomizationV1Resp create_api_referral_user_customization_v1(api_agent_code, customer_id, timestamp, recv_window=recv_window)

Customize Id For Client  (USER DATA)(For client)

- CustomerId must be unique for each apiAgent

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_api_referral_user_customization_v1_resp import CreateApiReferralUserCustomizationV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    api_agent_code = '' # str |  (default to '')
    customer_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Customize Id For Client  (USER DATA)(For client)
        api_response = api_instance.create_api_referral_user_customization_v1(api_agent_code, customer_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_api_referral_user_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_api_referral_user_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_agent_code** | **str**|  | [default to &#39;&#39;]
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

# **create_broker_sub_account_api_commission_coin_futures_v1**
> CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp create_broker_sub_account_api_commission_coin_futures_v1(maker_adjustment, pair, sub_account_id, taker_adjustment, timestamp, recv_window=recv_window)

Change Sub Account COIN-Ⓜ Futures Commission Adjustment

This request will change the COIN-Ⓜ futures commission for a sub account.
You need to enable "trade" option for the api key which requests this endpoint.
The sub-account's COIN-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the sub-account's fee tier plus the commission adjustment.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_commission_coin_futures_v1_resp import CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    maker_adjustment = 56 # int | 
    pair = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    taker_adjustment = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Sub Account COIN-Ⓜ Futures Commission Adjustment
        api_response = api_instance.create_broker_sub_account_api_commission_coin_futures_v1(maker_adjustment, pair, sub_account_id, taker_adjustment, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_commission_coin_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_commission_coin_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maker_adjustment** | **int**|  | 
 **pair** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **taker_adjustment** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp**](CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp.md)

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

# **create_broker_sub_account_api_commission_futures_v1**
> CreateBrokerSubAccountApiCommissionFuturesV1Resp create_broker_sub_account_api_commission_futures_v1(maker_adjustment, sub_account_id, symbol, taker_adjustment, timestamp, recv_window=recv_window)

Change Sub Account USDT-Ⓜ Futures Commission Adjustment

This request will change the USDT-Ⓜ futures commission for a sub account.
You need to enable "trade" option for the api key which requests this endpoint.
The sub-account's USDT-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the sub-account's fee tier plus the commission adjustment.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_commission_futures_v1_resp import CreateBrokerSubAccountApiCommissionFuturesV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    maker_adjustment = 56 # int | 
    sub_account_id = '' # str |  (default to '')
    symbol = '' # str |  (default to '')
    taker_adjustment = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Sub Account USDT-Ⓜ Futures Commission Adjustment
        api_response = api_instance.create_broker_sub_account_api_commission_futures_v1(maker_adjustment, sub_account_id, symbol, taker_adjustment, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_commission_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_commission_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maker_adjustment** | **int**|  | 
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **symbol** | **str**|  | [default to &#39;&#39;]
 **taker_adjustment** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiCommissionFuturesV1Resp**](CreateBrokerSubAccountApiCommissionFuturesV1Resp.md)

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

# **create_broker_sub_account_api_commission_v1**
> CreateBrokerSubAccountApiCommissionV1Resp create_broker_sub_account_api_commission_v1(maker_commission, sub_account_id, taker_commission, timestamp, margin_maker_commission=margin_maker_commission, margin_taker_commission=margin_taker_commission, recv_window=recv_window)

Change Sub Account Commission

This request will change the commission for a sub account.
You need to enable "trade" option for the api key which requests this endpoint.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_commission_v1_resp import CreateBrokerSubAccountApiCommissionV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    maker_commission = 3.4 # float | 
    sub_account_id = '' # str |  (default to '')
    taker_commission = 3.4 # float | 
    timestamp = 56 # int | 
    margin_maker_commission = 3.4 # float |  (optional)
    margin_taker_commission = 3.4 # float |  (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Change Sub Account Commission
        api_response = api_instance.create_broker_sub_account_api_commission_v1(maker_commission, sub_account_id, taker_commission, timestamp, margin_maker_commission=margin_maker_commission, margin_taker_commission=margin_taker_commission, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_commission_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_commission_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maker_commission** | **float**|  | 
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **taker_commission** | **float**|  | 
 **timestamp** | **int**|  | 
 **margin_maker_commission** | **float**|  | [optional] 
 **margin_taker_commission** | **float**|  | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiCommissionV1Resp**](CreateBrokerSubAccountApiCommissionV1Resp.md)

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

# **create_broker_sub_account_api_ip_restriction_v2**
> CreateBrokerSubAccountApiIpRestrictionV2Resp create_broker_sub_account_api_ip_restriction_v2(status, sub_account_api_key, sub_account_id, timestamp, ip_address=ip_address, recv_window=recv_window)

Update IP Restriction for Sub-Account API key (For Master Account)

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_ip_restriction_v2_resp import CreateBrokerSubAccountApiIpRestrictionV2Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    status = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Update IP Restriction for Sub-Account API key (For Master Account)
        api_response = api_instance.create_broker_sub_account_api_ip_restriction_v2(status, sub_account_api_key, sub_account_id, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_ip_restriction_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_ip_restriction_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **ip_address** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiIpRestrictionV2Resp**](CreateBrokerSubAccountApiIpRestrictionV2Resp.md)

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

# **create_broker_sub_account_api_permission_universal_transfer_v1**
> CreateBrokerSubAccountApiPermissionUniversalTransferV1Resp create_broker_sub_account_api_permission_universal_transfer_v1(can_universal_transfer, sub_account_api_key, sub_account_id, timestamp, recv_window=recv_window)

Enable Universal Transfer Permission For Sub Account Api Key

Caution:
- This request will enable the api permission for a sub account to use POST /sapi/v1/asset/transferendpoint.
- You need to enable "trade" option for the api key which requests this endpoint.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_permission_universal_transfer_v1_resp import CreateBrokerSubAccountApiPermissionUniversalTransferV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    can_universal_transfer = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    sub_account_id = 56 # int | 
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Universal Transfer Permission For Sub Account Api Key
        api_response = api_instance.create_broker_sub_account_api_permission_universal_transfer_v1(can_universal_transfer, sub_account_api_key, sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_permission_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_permission_universal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_universal_transfer** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **int**|  | 
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiPermissionUniversalTransferV1Resp**](CreateBrokerSubAccountApiPermissionUniversalTransferV1Resp.md)

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

# **create_broker_sub_account_api_permission_v1**
> CreateBrokerSubAccountApiPermissionV1Resp create_broker_sub_account_api_permission_v1(can_trade, futures_trade, margin_trade, sub_account_api_key, sub_account_id, timestamp, recv_window=recv_window)

Change Sub Account Api Permission

Caution:
- This request will change the api permission for a sub account.
- You need to enable "trade" option for the api key which requests this endpoint.
- Sub account should be enable margin before its api-key's marginTrade being enabled.
- Sub account should be enable futures before its api-key's futuresTrade being enabled.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_permission_v1_resp import CreateBrokerSubAccountApiPermissionV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    can_trade = '' # str |  (default to '')
    futures_trade = '' # str |  (default to '')
    margin_trade = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Change Sub Account Api Permission
        api_response = api_instance.create_broker_sub_account_api_permission_v1(can_trade, futures_trade, margin_trade, sub_account_api_key, sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_permission_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_permission_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_trade** | **str**|  | [default to &#39;&#39;]
 **futures_trade** | **str**|  | [default to &#39;&#39;]
 **margin_trade** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiPermissionV1Resp**](CreateBrokerSubAccountApiPermissionV1Resp.md)

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

# **create_broker_sub_account_api_v1**
> CreateBrokerSubAccountApiV1Resp create_broker_sub_account_api_v1(can_trade, sub_account_id, timestamp, futures_trade=futures_trade, margin_trade=margin_trade, public_key=public_key, recv_window=recv_window)

Create Api Key for Sub Account

Caution:
- This request will generate a api key for a sub account.
- You need to enable "trade" option for the api key which requests this endpoint
- Sub account should be enable margin before its api-key's marginTrade being enabled
- Sub account should be enable futures before its api-key's futuresTrade being enabled
- You can only create 1 api key for each sub account per second

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_api_v1_resp import CreateBrokerSubAccountApiV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    can_trade = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    futures_trade = '' # str |  (optional) (default to '')
    margin_trade = '' # str |  (optional) (default to '')
    public_key = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Create Api Key for Sub Account
        api_response = api_instance.create_broker_sub_account_api_v1(can_trade, sub_account_id, timestamp, futures_trade=futures_trade, margin_trade=margin_trade, public_key=public_key, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_trade** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **futures_trade** | **str**|  | [optional] [default to &#39;&#39;]
 **margin_trade** | **str**|  | [optional] [default to &#39;&#39;]
 **public_key** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountApiV1Resp**](CreateBrokerSubAccountApiV1Resp.md)

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

# **create_broker_sub_account_bnb_burn_margin_interest_v1**
> CreateBrokerSubAccountBnbBurnMarginInterestV1Resp create_broker_sub_account_bnb_burn_margin_interest_v1(interest_bnb_burn, sub_account_id, timestamp, recv_window=recv_window)

Enable Or Disable BNB Burn for Sub Account Margin Interest

- Subaccount must be enabled margin before using this switch

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_bnb_burn_margin_interest_v1_resp import CreateBrokerSubAccountBnbBurnMarginInterestV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    interest_bnb_burn = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Or Disable BNB Burn for Sub Account Margin Interest
        api_response = api_instance.create_broker_sub_account_bnb_burn_margin_interest_v1(interest_bnb_burn, sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_bnb_burn_margin_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_bnb_burn_margin_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interest_bnb_burn** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountBnbBurnMarginInterestV1Resp**](CreateBrokerSubAccountBnbBurnMarginInterestV1Resp.md)

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

# **create_broker_sub_account_bnb_burn_spot_v1**
> CreateBrokerSubAccountBnbBurnSpotV1Resp create_broker_sub_account_bnb_burn_spot_v1(spot_bnb_burn, sub_account_id, timestamp, recv_window=recv_window)

Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_bnb_burn_spot_v1_resp import CreateBrokerSubAccountBnbBurnSpotV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    spot_bnb_burn = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN
        api_response = api_instance.create_broker_sub_account_bnb_burn_spot_v1(spot_bnb_burn, sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_bnb_burn_spot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_bnb_burn_spot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_bnb_burn** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountBnbBurnSpotV1Resp**](CreateBrokerSubAccountBnbBurnSpotV1Resp.md)

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

# **create_broker_sub_account_futures_v1**
> CreateBrokerSubAccountFuturesV1Resp create_broker_sub_account_futures_v1(futures, sub_account_id, timestamp, recv_window=recv_window)

Enable Futures for Sub Account

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_futures_v1_resp import CreateBrokerSubAccountFuturesV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    futures = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Enable Futures for Sub Account
        api_response = api_instance.create_broker_sub_account_futures_v1(futures, sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->create_broker_sub_account_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateBrokerSubAccountFuturesV1Resp**](CreateBrokerSubAccountFuturesV1Resp.md)

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

# **create_broker_sub_account_v1**
> CreateBrokerSubAccountV1Resp create_broker_sub_account_v1(timestamp, recv_window=recv_window, tag=tag)

Create a Sub Account

To create a link sub-account

### Example


```python
import binance.spot
from binance.spot.models.create_broker_sub_account_v1_resp import CreateBrokerSubAccountV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)
    tag = '' # str |  (optional) (default to '')

    try:
        # Create a Sub Account
        api_response = api_instance.create_broker_sub_account_v1(timestamp, recv_window=recv_window, tag=tag)
        print("The response of BinanceLinkApi->create_broker_sub_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_sub_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 
 **tag** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateBrokerSubAccountV1Resp**](CreateBrokerSubAccountV1Resp.md)

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

# **create_broker_transfer_futures_v1**
> CreateBrokerTransferFuturesV1Resp create_broker_transfer_futures_v1(amount, asset, futures_type, timestamp, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)

Sub Account Transfer（FUTURES）

Caution:
- You need to enable "internal transfer" option for the api key which requests this endpoint.
- Transfer from master account if fromId not sent.
- Transfer to master account if toId not sent.
- Each master account could transfer 5000 times/min

### Example


```python
import binance.spot
from binance.spot.models.create_broker_transfer_futures_v1_resp import CreateBrokerTransferFuturesV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    futures_type = 56 # int | 
    timestamp = 56 # int | 
    client_tran_id = '' # str |  (optional) (default to '')
    from_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_id = '' # str |  (optional) (default to '')

    try:
        # Sub Account Transfer（FUTURES）
        api_response = api_instance.create_broker_transfer_futures_v1(amount, asset, futures_type, timestamp, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)
        print("The response of BinanceLinkApi->create_broker_transfer_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_transfer_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **futures_type** | **int**|  | 
 **timestamp** | **int**|  | 
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **from_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateBrokerTransferFuturesV1Resp**](CreateBrokerTransferFuturesV1Resp.md)

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

# **create_broker_transfer_v1**
> CreateBrokerTransferV1Resp create_broker_transfer_v1(amount, asset, timestamp, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)

Sub Account Transfer（SPOT）

Caution:
- You need to enable "internal transfer" option for the api key which requests this endpoint.
- Transfer from master account if fromId not sent.
- Transfer to master account if toId not sent.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_transfer_v1_resp import CreateBrokerTransferV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    timestamp = 56 # int | 
    client_tran_id = '' # str |  (optional) (default to '')
    from_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_id = '' # str |  (optional) (default to '')

    try:
        # Sub Account Transfer（SPOT）
        api_response = api_instance.create_broker_transfer_v1(amount, asset, timestamp, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)
        print("The response of BinanceLinkApi->create_broker_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **from_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateBrokerTransferV1Resp**](CreateBrokerTransferV1Resp.md)

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

# **create_broker_universal_transfer_v1**
> CreateBrokerUniversalTransferV1Resp create_broker_universal_transfer_v1(amount, asset, from_account_type, timestamp, to_account_type, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)

Universal Transfer

Caution:
- You need to enable "internal transfer" option for the api key which requests this endpoint.
- Transfer from master account if fromId not sent.
- Transfer to master account if toId not sent.
- Transfer between futures acount is not supported.

### Example


```python
import binance.spot
from binance.spot.models.create_broker_universal_transfer_v1_resp import CreateBrokerUniversalTransferV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    amount = '' # str |  (default to '')
    asset = '' # str |  (default to '')
    from_account_type = '' # str |  (default to '')
    timestamp = 56 # int | 
    to_account_type = '' # str |  (default to '')
    client_tran_id = '' # str |  (optional) (default to '')
    from_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)
    to_id = '' # str |  (optional) (default to '')

    try:
        # Universal Transfer
        api_response = api_instance.create_broker_universal_transfer_v1(amount, asset, from_account_type, timestamp, to_account_type, client_tran_id=client_tran_id, from_id=from_id, recv_window=recv_window, to_id=to_id)
        print("The response of BinanceLinkApi->create_broker_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->create_broker_universal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | [default to &#39;&#39;]
 **asset** | **str**|  | [default to &#39;&#39;]
 **from_account_type** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **to_account_type** | **str**|  | [default to &#39;&#39;]
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **from_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 
 **to_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CreateBrokerUniversalTransferV1Resp**](CreateBrokerUniversalTransferV1Resp.md)

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

# **delete_broker_sub_account_api_ip_restriction_ip_list_v1**
> DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp delete_broker_sub_account_api_ip_restriction_ip_list_v1(sub_account_id, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)

Delete IP Restriction for Sub Account Api Key

### Example


```python
import binance.spot
from binance.spot.models.delete_broker_sub_account_api_ip_restriction_ip_list_v1_resp import DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    ip_address = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Delete IP Restriction for Sub Account Api Key
        api_response = api_instance.delete_broker_sub_account_api_ip_restriction_ip_list_v1(sub_account_id, sub_account_api_key, timestamp, ip_address=ip_address, recv_window=recv_window)
        print("The response of BinanceLinkApi->delete_broker_sub_account_api_ip_restriction_ip_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->delete_broker_sub_account_api_ip_restriction_ip_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **ip_address** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp**](DeleteBrokerSubAccountApiIpRestrictionIpListV1Resp.md)

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

# **delete_broker_sub_account_api_v1**
> object delete_broker_sub_account_api_v1(sub_account_id, sub_account_api_key, timestamp, recv_window=recv_window)

Delete Sub Account Api Key

Caution:
- This request will delete a api key for a sub account
- You need to enable "trade" option for the api key which requests this endpoint
- You can only delete 1 api key for each sub account per second

### Example


```python
import binance.spot
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Delete Sub Account Api Key
        api_response = api_instance.delete_broker_sub_account_api_v1(sub_account_id, sub_account_api_key, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->delete_broker_sub_account_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->delete_broker_sub_account_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

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

# **delete_broker_sub_account_v1**
> object delete_broker_sub_account_v1(sub_account_id, timestamp, recv_window=recv_window)

Delete Sub Account

### Example


```python
import binance.spot
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Delete Sub Account
        api_response = api_instance.delete_broker_sub_account_v1(sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->delete_broker_sub_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->delete_broker_sub_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

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

# **get_api_referral_customization_v1**
> List[GetApiReferralCustomizationV1RespItem] get_api_referral_customization_v1(timestamp, customer_id=customer_id, email=email, recv_window=recv_window)

Get Client Email Customized Id (USER DATA) （For Partner）

- CustomerId and email can not be sent at the same time

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_api_referral_customization_v1_resp_item import GetApiReferralCustomizationV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    customer_id = '' # str |  (optional) (default to '')
    email = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Get Client Email Customized Id (USER DATA) （For Partner）
        api_response = api_instance.get_api_referral_customization_v1(timestamp, customer_id=customer_id, email=email, recv_window=recv_window)
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

# **get_api_referral_if_new_user_v1**
> GetApiReferralIfNewUserV1Resp get_api_referral_if_new_user_v1(api_agent_code, timestamp, recv_window=recv_window)

Query Client If The New User (USER  DATA)

### Example


```python
import binance.spot
from binance.spot.models.get_api_referral_if_new_user_v1_resp import GetApiReferralIfNewUserV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    api_agent_code = '' # str | brokerId (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Query Client If The New User (USER  DATA)
        api_response = api_instance.get_api_referral_if_new_user_v1(api_agent_code, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_if_new_user_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_if_new_user_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_agent_code** | **str**| brokerId | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetApiReferralIfNewUserV1Resp**](GetApiReferralIfNewUserV1Resp.md)

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

# **get_api_referral_kickback_recent_record_v1**
> List[GetApiReferralKickbackRecentRecordV1RespItem] get_api_referral_kickback_recent_record_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Rebate Recent Record(For Client)

- Only get the latest history of past 7 days.

### Example


```python
import binance.spot
from binance.spot.models.get_api_referral_kickback_recent_record_v1_resp_item import GetApiReferralKickbackRecentRecordV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500, max 1000 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Rebate Recent Record(For Client)
        api_response = api_instance.get_api_referral_kickback_recent_record_v1(timestamp, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_kickback_recent_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_kickback_recent_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500, max 1000 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralKickbackRecentRecordV1RespItem]**](GetApiReferralKickbackRecentRecordV1RespItem.md)

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

# **get_api_referral_rebate_recent_record_v1**
> List[GetApiReferralRebateRecentRecordV1RespItem] get_api_referral_rebate_recent_record_v1(start_time, end_time, limit, timestamp, customer_id=customer_id, recv_window=recv_window)

Query Rebate Recent Record （USER DATA）(For Partner)

- startTime and endTime must be both specified or both omitted.
- When both omitted it returns last 7 days.
- When both specified the span has to be within 7 days.

### Example


```python
import binance.spot
from binance.spot.models.get_api_referral_rebate_recent_record_v1_resp_item import GetApiReferralRebateRecentRecordV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    start_time = 56 # int | 
    end_time = 56 # int | 
    limit = 56 # int | max 500
    timestamp = 56 # int | 
    customer_id = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Rebate Recent Record （USER DATA）(For Partner)
        api_response = api_instance.get_api_referral_rebate_recent_record_v1(start_time, end_time, limit, timestamp, customer_id=customer_id, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_rebate_recent_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_rebate_recent_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **limit** | **int**| max 500 | 
 **timestamp** | **int**|  | 
 **customer_id** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetApiReferralRebateRecentRecordV1RespItem]**](GetApiReferralRebateRecentRecordV1RespItem.md)

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

# **get_api_referral_user_customization_v1**
> GetApiReferralUserCustomizationV1Resp get_api_referral_user_customization_v1(api_agent_code, timestamp, recv_window=recv_window)

Get User’s Customize Id (USER DATA)

- CustomerId must be unique

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_api_referral_user_customization_v1_resp import GetApiReferralUserCustomizationV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    api_agent_code = '' # str | brokerId (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get User’s Customize Id (USER DATA)
        api_response = api_instance.get_api_referral_user_customization_v1(api_agent_code, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_api_referral_user_customization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_api_referral_user_customization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_agent_code** | **str**| brokerId | [default to &#39;&#39;]
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

# **get_broker_info_v1**
> GetBrokerInfoV1Resp get_broker_info_v1(timestamp, recv_window=recv_window)

Link Account Information

### Example


```python
import binance.spot
from binance.spot.models.get_broker_info_v1_resp import GetBrokerInfoV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Link Account Information
        api_response = api_instance.get_broker_info_v1(timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerInfoV1Resp**](GetBrokerInfoV1Resp.md)

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

# **get_broker_rebate_futures_recent_record_v1**
> List[GetBrokerRebateFuturesRecentRecordV1RespItem] get_broker_rebate_futures_recent_record_v1(futures_type, start_time, end_time, timestamp, page=page, size=size, filter_result=filter_result, recv_window=recv_window)

Query Broker Futures Commission Rebate Record

- If filterResult = TRUE, rebates not from its own sub accounts will be filtered out in response.

### Example


```python
import binance.spot
from binance.spot.models.get_broker_rebate_futures_recent_record_v1_resp_item import GetBrokerRebateFuturesRecentRecordV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    futures_type = 56 # int | 1:USDT Futures, 2: Coin Futures
    start_time = 56 # int | 
    end_time = 56 # int | 
    timestamp = 56 # int | 
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 100 (optional) (default to 10)
    filter_result = True # bool | TRUE or FALSE. Default: FALSE (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Broker Futures Commission Rebate Record
        api_response = api_instance.get_broker_rebate_futures_recent_record_v1(futures_type, start_time, end_time, timestamp, page=page, size=size, filter_result=filter_result, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_rebate_futures_recent_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_rebate_futures_recent_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_type** | **int**| 1:USDT Futures, 2: Coin Futures | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **timestamp** | **int**|  | 
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 100 | [optional] [default to 10]
 **filter_result** | **bool**| TRUE or FALSE. Default: FALSE | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerRebateFuturesRecentRecordV1RespItem]**](GetBrokerRebateFuturesRecentRecordV1RespItem.md)

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

# **get_broker_rebate_recent_record_v1**
> List[GetBrokerRebateRecentRecordV1RespItem] get_broker_rebate_recent_record_v1(timestamp, sub_account_id=sub_account_id, start_time=start_time, end_time=end_time, page=page, size=size, recv_window=recv_window)

Query Broker Commission Rebate Recent Record（Spot）

- The query time period must be less than 7 days (default as the recent 7 days).

### Example


```python
import binance.spot
from binance.spot.models.get_broker_rebate_recent_record_v1_resp_item import GetBrokerRebateRecentRecordV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | Default: 7 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    page = 1 # int | default 1 (optional) (default to 1)
    size = 500 # int | default 500，max500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Broker Commission Rebate Recent Record（Spot）
        api_response = api_instance.get_broker_rebate_recent_record_v1(timestamp, sub_account_id=sub_account_id, start_time=start_time, end_time=end_time, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_rebate_recent_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_rebate_recent_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Default: 7 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 500，max500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerRebateRecentRecordV1RespItem]**](GetBrokerRebateRecentRecordV1RespItem.md)

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

# **get_broker_sub_account_api_commission_coin_futures_v1**
> List[GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem] get_broker_sub_account_api_commission_coin_futures_v1(sub_account_id, timestamp, pair=pair, recv_window=recv_window)

Query Sub Account COIN-Ⓜ Futures Commission Adjustment

- The sub-account's COIN-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the sub-account's fee tier plus the commission adjustment.
- If symbol not sent, commission adjustment of all symbols will be returned.
- If futures disabled, it is not allowed to set subaccount's COIN-Ⓜ futures commission adjustment on any symbol.
- Different symbols have the same commission for the same pair

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_api_commission_coin_futures_v1_resp_item import GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    pair = '' # str | BTCUSD (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account COIN-Ⓜ Futures Commission Adjustment
        api_response = api_instance.get_broker_sub_account_api_commission_coin_futures_v1(sub_account_id, timestamp, pair=pair, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_api_commission_coin_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_api_commission_coin_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **pair** | **str**| BTCUSD | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem]**](GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem.md)

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

# **get_broker_sub_account_api_commission_futures_v1**
> List[GetBrokerSubAccountApiCommissionFuturesV1RespItem] get_broker_sub_account_api_commission_futures_v1(sub_account_id, timestamp, symbol=symbol, recv_window=recv_window)

Query Sub Account USDT-Ⓜ Futures Commission Adjustment

The sub-account's USDT-Ⓜ futures commission of a symbol equals to the base commission of the symbol on the sub-account's fee tier plus the commission adjustment.

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_api_commission_futures_v1_resp_item import GetBrokerSubAccountApiCommissionFuturesV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account USDT-Ⓜ Futures Commission Adjustment
        api_response = api_instance.get_broker_sub_account_api_commission_futures_v1(sub_account_id, timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_api_commission_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_api_commission_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountApiCommissionFuturesV1RespItem]**](GetBrokerSubAccountApiCommissionFuturesV1RespItem.md)

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

# **get_broker_sub_account_api_ip_restriction_v1**
> GetBrokerSubAccountApiIpRestrictionV1Resp get_broker_sub_account_api_ip_restriction_v1(sub_account_id, sub_account_api_key, timestamp, recv_window=recv_window)

Get IP Restriction for Sub Account Api Key

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_api_ip_restriction_v1_resp import GetBrokerSubAccountApiIpRestrictionV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    sub_account_api_key = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get IP Restriction for Sub Account Api Key
        api_response = api_instance.get_broker_sub_account_api_ip_restriction_v1(sub_account_id, sub_account_api_key, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_api_ip_restriction_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_api_ip_restriction_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **sub_account_api_key** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerSubAccountApiIpRestrictionV1Resp**](GetBrokerSubAccountApiIpRestrictionV1Resp.md)

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

# **get_broker_sub_account_api_v1**
> List[GetBrokerSubAccountApiV1RespItem] get_broker_sub_account_api_v1(sub_account_id, timestamp, sub_account_api_key=sub_account_api_key, page=page, size=size, recv_window=recv_window)

Query Sub Account Api Key

Caution:
- You need to enable "trade" option for the api key which requests this endpoint

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_api_v1_resp_item import GetBrokerSubAccountApiV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    sub_account_api_key = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 500 # int | default 500, max 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Api Key
        api_response = api_instance.get_broker_sub_account_api_v1(sub_account_id, timestamp, sub_account_api_key=sub_account_api_key, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **sub_account_api_key** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 500, max 500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountApiV1RespItem]**](GetBrokerSubAccountApiV1RespItem.md)

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

# **get_broker_sub_account_bnb_burn_status_v1**
> GetBrokerSubAccountBnbBurnStatusV1Resp get_broker_sub_account_bnb_burn_status_v1(sub_account_id, timestamp, recv_window=recv_window)

Get BNB Burn Status for Sub Account

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_bnb_burn_status_v1_resp import GetBrokerSubAccountBnbBurnStatusV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get BNB Burn Status for Sub Account
        api_response = api_instance.get_broker_sub_account_bnb_burn_status_v1(sub_account_id, timestamp, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_bnb_burn_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_bnb_burn_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerSubAccountBnbBurnStatusV1Resp**](GetBrokerSubAccountBnbBurnStatusV1Resp.md)

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

# **get_broker_sub_account_deposit_hist_v1**
> List[GetBrokerSubAccountDepositHistV1RespItem] get_broker_sub_account_deposit_hist_v1(timestamp, sub_account_id=sub_account_id, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window)

Get Sub Account Deposit History

- The query time period must be less than 7 days( default as the recent 7 days).

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_deposit_hist_v1_resp_item import GetBrokerSubAccountDepositHistV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    coin = '' # str |  (optional) (default to '')
    status = 56 # int | 0(0:pending,6: credited but cannot withdraw, 1:success) (optional)
    start_time = 56 # int | Default: 7 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    limit = 56 # int | Default：500 (optional)
    offset = 56 # int | Default：0 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub Account Deposit History
        api_response = api_instance.get_broker_sub_account_deposit_hist_v1(timestamp, sub_account_id=sub_account_id, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_deposit_hist_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_deposit_hist_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **int**| 0(0:pending,6: credited but cannot withdraw, 1:success) | [optional] 
 **start_time** | **int**| Default: 7 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **limit** | **int**| Default：500 | [optional] 
 **offset** | **int**| Default：0 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountDepositHistV1RespItem]**](GetBrokerSubAccountDepositHistV1RespItem.md)

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

# **get_broker_sub_account_deposit_hist_v2**
> List[GetBrokerSubAccountDepositHistV2RespItem] get_broker_sub_account_deposit_hist_v2(deposit_id, sub_account_id, timestamp, limit=limit, offset=offset, recv_window=recv_window)

Get Sub Account Deposit History V2

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_deposit_hist_v2_resp_item import GetBrokerSubAccountDepositHistV2RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    deposit_id = '' # str |  (default to '')
    sub_account_id = '' # str |  (default to '')
    timestamp = 56 # int | 
    limit = 56 # int | Default：500 (optional)
    offset = 56 # int | Default：0 (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Get Sub Account Deposit History V2
        api_response = api_instance.get_broker_sub_account_deposit_hist_v2(deposit_id, sub_account_id, timestamp, limit=limit, offset=offset, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_deposit_hist_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_deposit_hist_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_id** | **str**|  | [default to &#39;&#39;]
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **limit** | **int**| Default：500 | [optional] 
 **offset** | **int**| Default：0 | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountDepositHistV2RespItem]**](GetBrokerSubAccountDepositHistV2RespItem.md)

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

# **get_broker_sub_account_futures_summary_v3**
> ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp get_broker_sub_account_futures_summary_v3(futures_type, timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)

Query Sub Account Futures Asset info (V3)

### Example


```python
import binance.spot
from binance.spot.models.exchangelink_get_broker_sub_account_futures_summary_v3_resp import ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    futures_type = 56 # int | 1:USD Margined Futures, 2:COIN Margined Futures
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 20 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Futures Asset info (V3)
        api_response = api_instance.get_broker_sub_account_futures_summary_v3(futures_type, timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_futures_summary_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_futures_summary_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_type** | **int**| 1:USD Margined Futures, 2:COIN Margined Futures | 
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 20 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp**](ExchangelinkGetBrokerSubAccountFuturesSummaryV3Resp.md)

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

# **get_broker_sub_account_margin_summary_v1**
> GetBrokerSubAccountMarginSummaryV1Resp get_broker_sub_account_margin_summary_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)

Query Sub Account Margin Asset info

- If subaccountId is not sent, the size must be sent

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_margin_summary_v1_resp import GetBrokerSubAccountMarginSummaryV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 20 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Margin Asset info
        api_response = api_instance.get_broker_sub_account_margin_summary_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_margin_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_margin_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 20 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerSubAccountMarginSummaryV1Resp**](GetBrokerSubAccountMarginSummaryV1Resp.md)

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

# **get_broker_sub_account_spot_summary_v1**
> GetBrokerSubAccountSpotSummaryV1Resp get_broker_sub_account_spot_summary_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)

Query Sub Account Spot Asset info

- If subaccountId is not sent, the size must be sent
- Requests per UID are limited to 60 requests per minute

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_spot_summary_v1_resp import GetBrokerSubAccountSpotSummaryV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 10 # int | default 10, max 20 (optional) (default to 10)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Spot Asset info
        api_response = api_instance.get_broker_sub_account_spot_summary_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_spot_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_spot_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 10, max 20 | [optional] [default to 10]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerSubAccountSpotSummaryV1Resp**](GetBrokerSubAccountSpotSummaryV1Resp.md)

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

# **get_broker_sub_account_v1**
> List[GetBrokerSubAccountV1RespItem] get_broker_sub_account_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)

Query Sub Account

### Example


```python
import binance.spot
from binance.spot.models.get_broker_sub_account_v1_resp_item import GetBrokerSubAccountV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    sub_account_id = '' # str |  (optional) (default to '')
    page = 1 # int | default 1 (optional) (default to 1)
    size = 500 # int | default 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account
        api_response = api_instance.get_broker_sub_account_v1(timestamp, sub_account_id=sub_account_id, page=page, size=size, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_sub_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_sub_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **sub_account_id** | **str**|  | [optional] [default to &#39;&#39;]
 **page** | **int**| default 1 | [optional] [default to 1]
 **size** | **int**| default 500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerSubAccountV1RespItem]**](GetBrokerSubAccountV1RespItem.md)

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

# **get_broker_transfer_futures_v1**
> GetBrokerTransferFuturesV1Resp get_broker_transfer_futures_v1(sub_account_id, futures_type, timestamp, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Sub Account Transfer History（FUTURES）

- Only get the latest history of past 30 days.

### Example


```python
import binance.spot
from binance.spot.models.get_broker_transfer_futures_v1_resp import GetBrokerTransferFuturesV1Resp
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    sub_account_id = '' # str |  (default to '')
    futures_type = 56 # int | 1:USDT Futures,2: COIN Futures
    timestamp = 56 # int | 
    client_tran_id = '' # str |  (optional) (default to '')
    start_time = 56 # int | default 30 days records (optional)
    end_time = 56 # int | default 30 days records (optional)
    page = 1 # int | default 1 (optional) (default to 1)
    limit = 50 # int | default 50, max 500 (optional) (default to 50)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Transfer History（FUTURES）
        api_response = api_instance.get_broker_transfer_futures_v1(sub_account_id, futures_type, timestamp, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_transfer_futures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_transfer_futures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_id** | **str**|  | [default to &#39;&#39;]
 **futures_type** | **int**| 1:USDT Futures,2: COIN Futures | 
 **timestamp** | **int**|  | 
 **client_tran_id** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| default 30 days records | [optional] 
 **end_time** | **int**| default 30 days records | [optional] 
 **page** | **int**| default 1 | [optional] [default to 1]
 **limit** | **int**| default 50, max 500 | [optional] [default to 50]
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetBrokerTransferFuturesV1Resp**](GetBrokerTransferFuturesV1Resp.md)

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

# **get_broker_transfer_v1**
> List[GetBrokerTransferV1RespItem] get_broker_transfer_v1(timestamp, from_id=from_id, to_id=to_id, client_tran_id=client_tran_id, show_all_status=show_all_status, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Sub Account Transfer History（SPOT）

Caution:
- If showAllStatus is true, the status in response will show four types: INIT,PROCESS,SUCCESS,FAILURE.
- If showAllStatus is false, the status in response will show three types: INIT,PROCESS,SUCCESS.
- Either fromId or toId must be sent. Return fromId equal master account by default.
Query scope is limited to 100 days:
- Both startTime and endTime are provided: If it exceeds, the endTime will be re-calculated 100 days after the startTime.
- Neither startTime nor endTime are provided: Calculate 100 days before today.
- endTime is not provided: Calculate 100 days after startTime.
- startTime is not provided: Calculate 100 days before endTime.

### Example


```python
import binance.spot
from binance.spot.models.get_broker_transfer_v1_resp_item import GetBrokerTransferV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    from_id = '' # str |  (optional) (default to '')
    to_id = '' # str |  (optional) (default to '')
    client_tran_id = '' # str | client transfer id (optional) (default to '')
    show_all_status = 'false' # str | true or false, default: false (optional) (default to 'false')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 56 # int |  (optional)
    limit = 500 # int | default 500, max 500 (optional) (default to 500)
    recv_window = 56 # int |  (optional)

    try:
        # Query Sub Account Transfer History（SPOT）
        api_response = api_instance.get_broker_transfer_v1(timestamp, from_id=from_id, to_id=to_id, client_tran_id=client_tran_id, show_all_status=show_all_status, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_id** | **str**|  | [optional] [default to &#39;&#39;]
 **to_id** | **str**|  | [optional] [default to &#39;&#39;]
 **client_tran_id** | **str**| client transfer id | [optional] [default to &#39;&#39;]
 **show_all_status** | **str**| true or false, default: false | [optional] [default to &#39;false&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| default 500, max 500 | [optional] [default to 500]
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerTransferV1RespItem]**](GetBrokerTransferV1RespItem.md)

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

# **get_broker_universal_transfer_v1**
> List[GetBrokerUniversalTransferV1RespItem] get_broker_universal_transfer_v1(timestamp, from_id=from_id, to_id=to_id, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, show_all_status=show_all_status, recv_window=recv_window)

Query Universal Transfer History

Caution:
- Either fromId or toId must be sent.
- If either fromId or toId is the master account itself, it will not return in response.
- If showAllStatus is true, the status in response will show four types: INIT,PROCESS,SUCCESS,FAILURE.
Query scope is limited to 100 days:
- Both startTime and endTime are provided: If it exceeds, the endTime will be re-calculated 100 days after the startTime.
- Neither startTime nor endTime are provided: Calculate 30 days before today.
- endTime is not provided: Calculate as Current time.
- startTime is not provided: Calculate 30 days before endTime.

### Example


```python
import binance.spot
from binance.spot.models.get_broker_universal_transfer_v1_resp_item import GetBrokerUniversalTransferV1RespItem
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
    api_instance = binance.spot.BinanceLinkApi(api_client)
    timestamp = 56 # int | 
    from_id = '' # str |  (optional) (default to '')
    to_id = '' # str |  (optional) (default to '')
    client_tran_id = '' # str | client transfer id (optional) (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    page = 1 # int | default 1 (optional) (default to 1)
    limit = 500 # int | default 500, max 500 (optional) (default to 500)
    show_all_status = True # bool | TRUE or FALSE (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Query Universal Transfer History
        api_response = api_instance.get_broker_universal_transfer_v1(timestamp, from_id=from_id, to_id=to_id, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, show_all_status=show_all_status, recv_window=recv_window)
        print("The response of BinanceLinkApi->get_broker_universal_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinanceLinkApi->get_broker_universal_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **from_id** | **str**|  | [optional] [default to &#39;&#39;]
 **to_id** | **str**|  | [optional] [default to &#39;&#39;]
 **client_tran_id** | **str**| client transfer id | [optional] [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **page** | **int**| default 1 | [optional] [default to 1]
 **limit** | **int**| default 500, max 500 | [optional] [default to 500]
 **show_all_status** | **bool**| TRUE or FALSE | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[GetBrokerUniversalTransferV1RespItem]**](GetBrokerUniversalTransferV1RespItem.md)

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

