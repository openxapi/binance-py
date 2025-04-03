# binance.margin.MarketDataApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_get_margin_all_assets_v1**](MarketDataApi.md#margin_get_margin_all_assets_v1) | **GET** /sapi/v1/margin/allAssets | Get All Margin Assets (MARKET_DATA)
[**margin_get_margin_all_pairs_v1**](MarketDataApi.md#margin_get_margin_all_pairs_v1) | **GET** /sapi/v1/margin/allPairs | Get All Cross Margin Pairs (MARKET_DATA)
[**margin_get_margin_available_inventory_v1**](MarketDataApi.md#margin_get_margin_available_inventory_v1) | **GET** /sapi/v1/margin/available-inventory | Query Margin Available Inventory(USER_DATA)
[**margin_get_margin_cross_margin_collateral_ratio_v1**](MarketDataApi.md#margin_get_margin_cross_margin_collateral_ratio_v1) | **GET** /sapi/v1/margin/crossMarginCollateralRatio | Cross margin collateral ratio (MARKET_DATA)
[**margin_get_margin_delist_schedule_v1**](MarketDataApi.md#margin_get_margin_delist_schedule_v1) | **GET** /sapi/v1/margin/delist-schedule | Get Delist Schedule (MARKET_DATA)
[**margin_get_margin_isolated_all_pairs_v1**](MarketDataApi.md#margin_get_margin_isolated_all_pairs_v1) | **GET** /sapi/v1/margin/isolated/allPairs | Get All Isolated Margin Symbol(MARKET_DATA)
[**margin_get_margin_isolated_margin_tier_v1**](MarketDataApi.md#margin_get_margin_isolated_margin_tier_v1) | **GET** /sapi/v1/margin/isolatedMarginTier | Query Isolated Margin Tier Data (USER_DATA)
[**margin_get_margin_leverage_bracket_v1**](MarketDataApi.md#margin_get_margin_leverage_bracket_v1) | **GET** /sapi/v1/margin/leverageBracket | Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
[**margin_get_margin_price_index_v1**](MarketDataApi.md#margin_get_margin_price_index_v1) | **GET** /sapi/v1/margin/priceIndex | Query Margin PriceIndex (MARKET_DATA)


# **margin_get_margin_all_assets_v1**
> List[MarginGetMarginAllAssetsV1RespItem] margin_get_margin_all_assets_v1(asset=asset)

Get All Margin Assets (MARKET_DATA)

Get All Margin Assets.

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_all_assets_v1_resp_item import MarginGetMarginAllAssetsV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    asset = '' # str |  (optional) (default to '')

    try:
        # Get All Margin Assets (MARKET_DATA)
        api_response = api_instance.margin_get_margin_all_assets_v1(asset=asset)
        print("The response of MarketDataApi->margin_get_margin_all_assets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_all_assets_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[MarginGetMarginAllAssetsV1RespItem]**](MarginGetMarginAllAssetsV1RespItem.md)

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

# **margin_get_margin_all_pairs_v1**
> List[MarginGetMarginAllPairsV1RespItem] margin_get_margin_all_pairs_v1(symbol=symbol)

Get All Cross Margin Pairs (MARKET_DATA)

Get All Cross Margin Pairs

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_all_pairs_v1_resp_item import MarginGetMarginAllPairsV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Get All Cross Margin Pairs (MARKET_DATA)
        api_response = api_instance.margin_get_margin_all_pairs_v1(symbol=symbol)
        print("The response of MarketDataApi->margin_get_margin_all_pairs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_all_pairs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[MarginGetMarginAllPairsV1RespItem]**](MarginGetMarginAllPairsV1RespItem.md)

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

# **margin_get_margin_available_inventory_v1**
> MarginGetMarginAvailableInventoryV1Resp margin_get_margin_available_inventory_v1(type)

Query Margin Available Inventory(USER_DATA)

Margin available Inventory query

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_available_inventory_v1_resp import MarginGetMarginAvailableInventoryV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    type = '' # str | MARGIN,ISOLATED (default to '')

    try:
        # Query Margin Available Inventory(USER_DATA)
        api_response = api_instance.margin_get_margin_available_inventory_v1(type)
        print("The response of MarketDataApi->margin_get_margin_available_inventory_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_available_inventory_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| MARGIN,ISOLATED | [default to &#39;&#39;]

### Return type

[**MarginGetMarginAvailableInventoryV1Resp**](MarginGetMarginAvailableInventoryV1Resp.md)

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

# **margin_get_margin_cross_margin_collateral_ratio_v1**
> List[MarginGetMarginCrossMarginCollateralRatioV1RespItem] margin_get_margin_cross_margin_collateral_ratio_v1()

Cross margin collateral ratio (MARKET_DATA)

Cross margin collateral ratio

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_cross_margin_collateral_ratio_v1_resp_item import MarginGetMarginCrossMarginCollateralRatioV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)

    try:
        # Cross margin collateral ratio (MARKET_DATA)
        api_response = api_instance.margin_get_margin_cross_margin_collateral_ratio_v1()
        print("The response of MarketDataApi->margin_get_margin_cross_margin_collateral_ratio_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_cross_margin_collateral_ratio_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MarginGetMarginCrossMarginCollateralRatioV1RespItem]**](MarginGetMarginCrossMarginCollateralRatioV1RespItem.md)

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

# **margin_get_margin_delist_schedule_v1**
> List[MarginGetMarginDelistScheduleV1RespItem] margin_get_margin_delist_schedule_v1(timestamp, recv_window=recv_window)

Get Delist Schedule (MARKET_DATA)

Get tokens or symbols delist schedule for cross margin and isolated margin

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_delist_schedule_v1_resp_item import MarginGetMarginDelistScheduleV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Get Delist Schedule (MARKET_DATA)
        api_response = api_instance.margin_get_margin_delist_schedule_v1(timestamp, recv_window=recv_window)
        print("The response of MarketDataApi->margin_get_margin_delist_schedule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_delist_schedule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[MarginGetMarginDelistScheduleV1RespItem]**](MarginGetMarginDelistScheduleV1RespItem.md)

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

# **margin_get_margin_isolated_all_pairs_v1**
> List[MarginGetMarginIsolatedAllPairsV1RespItem] margin_get_margin_isolated_all_pairs_v1(timestamp, symbol=symbol, recv_window=recv_window)

Get All Isolated Margin Symbol(MARKET_DATA)

Get All Isolated Margin Symbol

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_isolated_all_pairs_v1_resp_item import MarginGetMarginIsolatedAllPairsV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    timestamp = 56 # int | 
    symbol = '' # str |  (optional) (default to '')
    recv_window = 56 # int | No more than 60000 (optional)

    try:
        # Get All Isolated Margin Symbol(MARKET_DATA)
        api_response = api_instance.margin_get_margin_isolated_all_pairs_v1(timestamp, symbol=symbol, recv_window=recv_window)
        print("The response of MarketDataApi->margin_get_margin_isolated_all_pairs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_isolated_all_pairs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **recv_window** | **int**| No more than 60000 | [optional] 

### Return type

[**List[MarginGetMarginIsolatedAllPairsV1RespItem]**](MarginGetMarginIsolatedAllPairsV1RespItem.md)

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

# **margin_get_margin_isolated_margin_tier_v1**
> List[MarginGetMarginIsolatedMarginTierV1RespItem] margin_get_margin_isolated_margin_tier_v1(symbol, timestamp, tier=tier, recv_window=recv_window)

Query Isolated Margin Tier Data (USER_DATA)

Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

### Example

* Api Key Authentication (ApiKey):

```python
import binance.margin
from binance.margin.models.margin_get_margin_isolated_margin_tier_v1_resp_item import MarginGetMarginIsolatedMarginTierV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.margin.Configuration(
    auth=binance.margin.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    timestamp = 56 # int | 
    tier = 56 # int | All margin tier data will be returned if tier is omitted (optional)
    recv_window = 56 # int | No more than `60000` (optional)

    try:
        # Query Isolated Margin Tier Data (USER_DATA)
        api_response = api_instance.margin_get_margin_isolated_margin_tier_v1(symbol, timestamp, tier=tier, recv_window=recv_window)
        print("The response of MarketDataApi->margin_get_margin_isolated_margin_tier_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_isolated_margin_tier_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **timestamp** | **int**|  | 
 **tier** | **int**| All margin tier data will be returned if tier is omitted | [optional] 
 **recv_window** | **int**| No more than &#x60;60000&#x60; | [optional] 

### Return type

[**List[MarginGetMarginIsolatedMarginTierV1RespItem]**](MarginGetMarginIsolatedMarginTierV1RespItem.md)

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

# **margin_get_margin_leverage_bracket_v1**
> List[MarginGetMarginLeverageBracketV1RespItem] margin_get_margin_leverage_bracket_v1()

Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)

Liability Coin Leverage Bracket in Cross Margin Pro Mode

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_leverage_bracket_v1_resp_item import MarginGetMarginLeverageBracketV1RespItem
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)

    try:
        # Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
        api_response = api_instance.margin_get_margin_leverage_bracket_v1()
        print("The response of MarketDataApi->margin_get_margin_leverage_bracket_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_leverage_bracket_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MarginGetMarginLeverageBracketV1RespItem]**](MarginGetMarginLeverageBracketV1RespItem.md)

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

# **margin_get_margin_price_index_v1**
> MarginGetMarginPriceIndexV1Resp margin_get_margin_price_index_v1(symbol)

Query Margin PriceIndex (MARKET_DATA)

Query Margin PriceIndex

### Example


```python
import binance.margin
from binance.margin.models.margin_get_margin_price_index_v1_resp import MarginGetMarginPriceIndexV1Resp
from binance.margin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.margin.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.margin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.margin.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Margin PriceIndex (MARKET_DATA)
        api_response = api_instance.margin_get_margin_price_index_v1(symbol)
        print("The response of MarketDataApi->margin_get_margin_price_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->margin_get_margin_price_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**MarginGetMarginPriceIndexV1Resp**](MarginGetMarginPriceIndexV1Resp.md)

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

