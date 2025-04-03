# binance.derivatives.pmarginpro.MarketDataApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmarginpro_get_portfolio_asset_index_price_v1**](MarketDataApi.md#pmarginpro_get_portfolio_asset_index_price_v1) | **GET** /sapi/v1/portfolio/asset-index-price | Query Portfolio Margin Asset Index Price (MARKET_DATA)
[**pmarginpro_get_portfolio_collateral_rate_v1**](MarketDataApi.md#pmarginpro_get_portfolio_collateral_rate_v1) | **GET** /sapi/v1/portfolio/collateralRate | Portfolio Margin Collateral Rate(MARKET_DATA)
[**pmarginpro_get_portfolio_collateral_rate_v2**](MarketDataApi.md#pmarginpro_get_portfolio_collateral_rate_v2) | **GET** /sapi/v2/portfolio/collateralRate | Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)
[**pmarginpro_get_portfolio_margin_asset_leverage_v1**](MarketDataApi.md#pmarginpro_get_portfolio_margin_asset_leverage_v1) | **GET** /sapi/v1/portfolio/margin-asset-leverage | Get Portfolio Margin Asset Leverage(USER_DATA)


# **pmarginpro_get_portfolio_asset_index_price_v1**
> List[PmarginproGetPortfolioAssetIndexPriceV1RespItem] pmarginpro_get_portfolio_asset_index_price_v1(asset=asset)

Query Portfolio Margin Asset Index Price (MARKET_DATA)

Query Portfolio Margin Asset Index Price

### Example


```python
import binance.derivatives.pmarginpro
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_asset_index_price_v1_resp_item import PmarginproGetPortfolioAssetIndexPriceV1RespItem
from binance.derivatives.pmarginpro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmarginpro.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.pmarginpro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmarginpro.MarketDataApi(api_client)
    asset = '' # str |  (optional) (default to '')

    try:
        # Query Portfolio Margin Asset Index Price (MARKET_DATA)
        api_response = api_instance.pmarginpro_get_portfolio_asset_index_price_v1(asset=asset)
        print("The response of MarketDataApi->pmarginpro_get_portfolio_asset_index_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->pmarginpro_get_portfolio_asset_index_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[PmarginproGetPortfolioAssetIndexPriceV1RespItem]**](PmarginproGetPortfolioAssetIndexPriceV1RespItem.md)

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

# **pmarginpro_get_portfolio_collateral_rate_v1**
> List[PmarginproGetPortfolioCollateralRateV1RespItem] pmarginpro_get_portfolio_collateral_rate_v1()

Portfolio Margin Collateral Rate(MARKET_DATA)

Portfolio Margin Collateral Rate

### Example


```python
import binance.derivatives.pmarginpro
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_collateral_rate_v1_resp_item import PmarginproGetPortfolioCollateralRateV1RespItem
from binance.derivatives.pmarginpro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmarginpro.Configuration(
    host = "https://api.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.pmarginpro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmarginpro.MarketDataApi(api_client)

    try:
        # Portfolio Margin Collateral Rate(MARKET_DATA)
        api_response = api_instance.pmarginpro_get_portfolio_collateral_rate_v1()
        print("The response of MarketDataApi->pmarginpro_get_portfolio_collateral_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->pmarginpro_get_portfolio_collateral_rate_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PmarginproGetPortfolioCollateralRateV1RespItem]**](PmarginproGetPortfolioCollateralRateV1RespItem.md)

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

# **pmarginpro_get_portfolio_collateral_rate_v2**
> List[PmarginproGetPortfolioCollateralRateV2RespItem] pmarginpro_get_portfolio_collateral_rate_v2(timestamp, recv_window=recv_window)

Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)

Portfolio Margin PRO Tiered Collateral Rate

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmarginpro
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_collateral_rate_v2_resp_item import PmarginproGetPortfolioCollateralRateV2RespItem
from binance.derivatives.pmarginpro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmarginpro.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmarginpro.Configuration(
    auth=binance.derivatives.pmarginpro.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmarginpro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmarginpro.MarketDataApi(api_client)
    timestamp = 56 # int | 
    recv_window = 56 # int |  (optional)

    try:
        # Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)
        api_response = api_instance.pmarginpro_get_portfolio_collateral_rate_v2(timestamp, recv_window=recv_window)
        print("The response of MarketDataApi->pmarginpro_get_portfolio_collateral_rate_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->pmarginpro_get_portfolio_collateral_rate_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[PmarginproGetPortfolioCollateralRateV2RespItem]**](PmarginproGetPortfolioCollateralRateV2RespItem.md)

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

# **pmarginpro_get_portfolio_margin_asset_leverage_v1**
> List[PmarginproGetPortfolioMarginAssetLeverageV1RespItem] pmarginpro_get_portfolio_margin_asset_leverage_v1()

Get Portfolio Margin Asset Leverage(USER_DATA)

Get Portfolio Margin Asset Leverage

### Example

* Api Key Authentication (ApiKey):

```python
import binance.derivatives.pmarginpro
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_margin_asset_leverage_v1_resp_item import PmarginproGetPortfolioMarginAssetLeverageV1RespItem
from binance.derivatives.pmarginpro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmarginpro.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.derivatives.pmarginpro.Configuration(
    auth=binance.derivatives.pmarginpro.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.derivatives.pmarginpro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmarginpro.MarketDataApi(api_client)

    try:
        # Get Portfolio Margin Asset Leverage(USER_DATA)
        api_response = api_instance.pmarginpro_get_portfolio_margin_asset_leverage_v1()
        print("The response of MarketDataApi->pmarginpro_get_portfolio_margin_asset_leverage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->pmarginpro_get_portfolio_margin_asset_leverage_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PmarginproGetPortfolioMarginAssetLeverageV1RespItem]**](PmarginproGetPortfolioMarginAssetLeverageV1RespItem.md)

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

