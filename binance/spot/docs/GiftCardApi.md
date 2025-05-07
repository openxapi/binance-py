# binance.spot.GiftCardApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_giftcard_buy_code_v1**](GiftCardApi.md#create_giftcard_buy_code_v1) | **POST** /sapi/v1/giftcard/buyCode | Create a dual-token gift card(fixed value, discount feature)(TRADE)
[**create_giftcard_create_code_v1**](GiftCardApi.md#create_giftcard_create_code_v1) | **POST** /sapi/v1/giftcard/createCode | Create a single-token gift card (USER_DATA)
[**create_giftcard_redeem_code_v1**](GiftCardApi.md#create_giftcard_redeem_code_v1) | **POST** /sapi/v1/giftcard/redeemCode | Redeem a Binance Gift Card(USER_DATA)
[**get_giftcard_buy_code_token_limit_v1**](GiftCardApi.md#get_giftcard_buy_code_token_limit_v1) | **GET** /sapi/v1/giftcard/buyCode/token-limit | Fetch Token Limit(USER_DATA)
[**get_giftcard_cryptography_rsa_public_key_v1**](GiftCardApi.md#get_giftcard_cryptography_rsa_public_key_v1) | **GET** /sapi/v1/giftcard/cryptography/rsa-public-key | Fetch RSA Public Key(USER_DATA)
[**get_giftcard_verify_v1**](GiftCardApi.md#get_giftcard_verify_v1) | **GET** /sapi/v1/giftcard/verify | Verify Binance Gift Card by Gift Card Number(USER_DATA)


# **create_giftcard_buy_code_v1**
> CreateGiftcardBuyCodeV1Resp create_giftcard_buy_code_v1(base_token, base_token_amount, face_token, timestamp, recv_window=recv_window)

Create a dual-token gift card(fixed value, discount feature)(TRADE)

This API is for creating a dual-token ( stablecoin-denominated) Binance Gift Card. You may create a gift card using USDT as baseToken, that is redeemable to another designated token (faceToken). For example, you can create a fixed-value BTC gift card and pay with 100 USDT plus 1 USDT fee. This gift card can keep the value fixed at 100 USDT before redemption, and will be redeemable to BTC equivalent to 100 USDT upon redemption.


Once successfully created, the amount of baseToken (e.g. USDT) in the fixed-value gift card along with the fee would be deducted from your funding wallet.


To get started with, please make sure:

You have a Binance account
You have passed KYB
You have a sufﬁcient balance(Gift Card amount and fee amount) in your Binance funding wallet
You need Enable Withdrawals for the API Key which requests this endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_giftcard_buy_code_v1_resp import CreateGiftcardBuyCodeV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    base_token = '' # str |  (default to '')
    base_token_amount = 3.4 # float | 
    face_token = '' # str |  (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Create a dual-token gift card(fixed value, discount feature)(TRADE)
        api_response = api_instance.create_giftcard_buy_code_v1(base_token, base_token_amount, face_token, timestamp, recv_window=recv_window)
        print("The response of GiftCardApi->create_giftcard_buy_code_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->create_giftcard_buy_code_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_token** | **str**|  | [default to &#39;&#39;]
 **base_token_amount** | **float**|  | 
 **face_token** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateGiftcardBuyCodeV1Resp**](CreateGiftcardBuyCodeV1Resp.md)

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

# **create_giftcard_create_code_v1**
> CreateGiftcardCreateCodeV1Resp create_giftcard_create_code_v1(amount, timestamp, token, recv_window=recv_window)

Create a single-token gift card (USER_DATA)

This API is for creating a Binance Gift Card.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_giftcard_create_code_v1_resp import CreateGiftcardCreateCodeV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    amount = 3.4 # float | 
    timestamp = 56 # int | 
    token = '' # str |  (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Create a single-token gift card (USER_DATA)
        api_response = api_instance.create_giftcard_create_code_v1(amount, timestamp, token, recv_window=recv_window)
        print("The response of GiftCardApi->create_giftcard_create_code_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->create_giftcard_create_code_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**|  | 
 **timestamp** | **int**|  | 
 **token** | **str**|  | [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateGiftcardCreateCodeV1Resp**](CreateGiftcardCreateCodeV1Resp.md)

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

# **create_giftcard_redeem_code_v1**
> CreateGiftcardRedeemCodeV1Resp create_giftcard_redeem_code_v1(code, timestamp, external_uid=external_uid, recv_window=recv_window)

Redeem a Binance Gift Card(USER_DATA)

This API is for redeeming a Binance Gift Card
Once redeemed, the coins will be deposited in your funding wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.create_giftcard_redeem_code_v1_resp import CreateGiftcardRedeemCodeV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    code = '' # str |  (default to '')
    timestamp = 56 # int | 
    external_uid = '' # str |  (optional) (default to '')
    recv_window = 56 # int |  (optional)

    try:
        # Redeem a Binance Gift Card(USER_DATA)
        api_response = api_instance.create_giftcard_redeem_code_v1(code, timestamp, external_uid=external_uid, recv_window=recv_window)
        print("The response of GiftCardApi->create_giftcard_redeem_code_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->create_giftcard_redeem_code_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **external_uid** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**|  | [optional] 

### Return type

[**CreateGiftcardRedeemCodeV1Resp**](CreateGiftcardRedeemCodeV1Resp.md)

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

# **get_giftcard_buy_code_token_limit_v1**
> GetGiftcardBuyCodeTokenLimitV1Resp get_giftcard_buy_code_token_limit_v1(base_token, timestamp, recv_window=recv_window)

Fetch Token Limit(USER_DATA)

This API is to help you verify which tokens are available for you to create Stablecoin-Denominated gift cards as mentioned in section 2 and its’ limitation.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_giftcard_buy_code_token_limit_v1_resp import GetGiftcardBuyCodeTokenLimitV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    base_token = '' # str | The token you want to pay, example: BUSD (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fetch Token Limit(USER_DATA)
        api_response = api_instance.get_giftcard_buy_code_token_limit_v1(base_token, timestamp, recv_window=recv_window)
        print("The response of GiftCardApi->get_giftcard_buy_code_token_limit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->get_giftcard_buy_code_token_limit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_token** | **str**| The token you want to pay, example: BUSD | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetGiftcardBuyCodeTokenLimitV1Resp**](GetGiftcardBuyCodeTokenLimitV1Resp.md)

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

# **get_giftcard_cryptography_rsa_public_key_v1**
> GetGiftcardCryptographyRsaPublicKeyV1Resp get_giftcard_cryptography_rsa_public_key_v1(timestamp, recv_window=recv_window)

Fetch RSA Public Key(USER_DATA)

This API is for fetching the RSA Public Key.
This RSA Public key will be used to encrypt the card code.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_giftcard_cryptography_rsa_public_key_v1_resp import GetGiftcardCryptographyRsaPublicKeyV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Fetch RSA Public Key(USER_DATA)
        api_response = api_instance.get_giftcard_cryptography_rsa_public_key_v1(timestamp, recv_window=recv_window)
        print("The response of GiftCardApi->get_giftcard_cryptography_rsa_public_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->get_giftcard_cryptography_rsa_public_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetGiftcardCryptographyRsaPublicKeyV1Resp**](GetGiftcardCryptographyRsaPublicKeyV1Resp.md)

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

# **get_giftcard_verify_v1**
> GetGiftcardVerifyV1Resp get_giftcard_verify_v1(reference_no, timestamp, recv_window=recv_window)

Verify Binance Gift Card by Gift Card Number(USER_DATA)

This API is for verifying whether the Binance Gift Card is valid or not by entering Gift Card Number.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.spot
from binance.spot.models.get_giftcard_verify_v1_resp import GetGiftcardVerifyV1Resp
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
    api_instance = binance.spot.GiftCardApi(api_client)
    reference_no = '' # str | Enter the Gift Card Number (default to '')
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Verify Binance Gift Card by Gift Card Number(USER_DATA)
        api_response = api_instance.get_giftcard_verify_v1(reference_no, timestamp, recv_window=recv_window)
        print("The response of GiftCardApi->get_giftcard_verify_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->get_giftcard_verify_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_no** | **str**| Enter the Gift Card Number | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**GetGiftcardVerifyV1Resp**](GetGiftcardVerifyV1Resp.md)

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

