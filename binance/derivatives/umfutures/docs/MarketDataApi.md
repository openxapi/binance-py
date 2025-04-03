# binance.derivatives.umfutures.MarketDataApi

All URIs are relative to *https://fapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**umfutures_get_agg_trades_v1**](MarketDataApi.md#umfutures_get_agg_trades_v1) | **GET** /fapi/v1/aggTrades | Compressed/Aggregate Trades List
[**umfutures_get_asset_index_v1**](MarketDataApi.md#umfutures_get_asset_index_v1) | **GET** /fapi/v1/assetIndex | Multi-Assets Mode Asset Index
[**umfutures_get_constituents_v1**](MarketDataApi.md#umfutures_get_constituents_v1) | **GET** /fapi/v1/constituents | Query Index Price Constituents
[**umfutures_get_continuous_klines_v1**](MarketDataApi.md#umfutures_get_continuous_klines_v1) | **GET** /fapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**umfutures_get_depth_v1**](MarketDataApi.md#umfutures_get_depth_v1) | **GET** /fapi/v1/depth | Order Book
[**umfutures_get_exchange_info_v1**](MarketDataApi.md#umfutures_get_exchange_info_v1) | **GET** /fapi/v1/exchangeInfo | Exchange Information
[**umfutures_get_funding_info_v1**](MarketDataApi.md#umfutures_get_funding_info_v1) | **GET** /fapi/v1/fundingInfo | Get Funding Rate Info
[**umfutures_get_funding_rate_v1**](MarketDataApi.md#umfutures_get_funding_rate_v1) | **GET** /fapi/v1/fundingRate | Get Funding Rate History
[**umfutures_get_futures_data_basis**](MarketDataApi.md#umfutures_get_futures_data_basis) | **GET** /futures/data/basis | Basis
[**umfutures_get_futures_data_delivery_price**](MarketDataApi.md#umfutures_get_futures_data_delivery_price) | **GET** /futures/data/delivery-price | Quarterly Contract Settlement Price
[**umfutures_get_futures_data_global_long_short_account_ratio**](MarketDataApi.md#umfutures_get_futures_data_global_long_short_account_ratio) | **GET** /futures/data/globalLongShortAccountRatio | Long/Short Ratio
[**umfutures_get_futures_data_open_interest_hist**](MarketDataApi.md#umfutures_get_futures_data_open_interest_hist) | **GET** /futures/data/openInterestHist | Open Interest Statistics
[**umfutures_get_futures_data_takerlongshort_ratio**](MarketDataApi.md#umfutures_get_futures_data_takerlongshort_ratio) | **GET** /futures/data/takerlongshortRatio | Taker Buy/Sell Volume
[**umfutures_get_futures_data_top_long_short_account_ratio**](MarketDataApi.md#umfutures_get_futures_data_top_long_short_account_ratio) | **GET** /futures/data/topLongShortAccountRatio | Top Trader Long/Short Ratio (Accounts)
[**umfutures_get_futures_data_top_long_short_position_ratio**](MarketDataApi.md#umfutures_get_futures_data_top_long_short_position_ratio) | **GET** /futures/data/topLongShortPositionRatio | Top Trader Long/Short Ratio (Positions)
[**umfutures_get_historical_trades_v1**](MarketDataApi.md#umfutures_get_historical_trades_v1) | **GET** /fapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**umfutures_get_index_info_v1**](MarketDataApi.md#umfutures_get_index_info_v1) | **GET** /fapi/v1/indexInfo | Composite Index Symbol Information
[**umfutures_get_index_price_klines_v1**](MarketDataApi.md#umfutures_get_index_price_klines_v1) | **GET** /fapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**umfutures_get_klines_v1**](MarketDataApi.md#umfutures_get_klines_v1) | **GET** /fapi/v1/klines | Kline/Candlestick Data
[**umfutures_get_mark_price_klines_v1**](MarketDataApi.md#umfutures_get_mark_price_klines_v1) | **GET** /fapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**umfutures_get_open_interest_v1**](MarketDataApi.md#umfutures_get_open_interest_v1) | **GET** /fapi/v1/openInterest | Open Interest
[**umfutures_get_ping_v1**](MarketDataApi.md#umfutures_get_ping_v1) | **GET** /fapi/v1/ping | Test Connectivity
[**umfutures_get_premium_index_klines_v1**](MarketDataApi.md#umfutures_get_premium_index_klines_v1) | **GET** /fapi/v1/premiumIndexKlines | Premium index Kline Data
[**umfutures_get_premium_index_v1**](MarketDataApi.md#umfutures_get_premium_index_v1) | **GET** /fapi/v1/premiumIndex | Mark Price
[**umfutures_get_ticker24hr_v1**](MarketDataApi.md#umfutures_get_ticker24hr_v1) | **GET** /fapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**umfutures_get_ticker_book_ticker_v1**](MarketDataApi.md#umfutures_get_ticker_book_ticker_v1) | **GET** /fapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**umfutures_get_ticker_price_v1**](MarketDataApi.md#umfutures_get_ticker_price_v1) | **GET** /fapi/v1/ticker/price | Symbol Price Ticker
[**umfutures_get_ticker_price_v2**](MarketDataApi.md#umfutures_get_ticker_price_v2) | **GET** /fapi/v2/ticker/price | Symbol Price Ticker V2
[**umfutures_get_time_v1**](MarketDataApi.md#umfutures_get_time_v1) | **GET** /fapi/v1/time | Check Server Time
[**umfutures_get_trades_v1**](MarketDataApi.md#umfutures_get_trades_v1) | **GET** /fapi/v1/trades | Recent Trades List


# **umfutures_get_agg_trades_v1**
> List[UmfuturesGetAggTradesV1RespItem] umfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate market trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_agg_trades_v1_resp_item import UmfuturesGetAggTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.umfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_agg_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **from_id** | **int**| ID to get aggregate trades from INCLUSIVE. | [optional] 
 **start_time** | **int**| Timestamp in ms to get aggregate trades from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get aggregate trades until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[UmfuturesGetAggTradesV1RespItem]**](UmfuturesGetAggTradesV1RespItem.md)

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

# **umfutures_get_asset_index_v1**
> UmfuturesGetAssetIndexV1Resp umfutures_get_asset_index_v1(symbol=symbol)

Multi-Assets Mode Asset Index

asset index for Multi-Assets mode

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_asset_index_v1_resp import UmfuturesGetAssetIndexV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str | Asset pair (optional) (default to '')

    try:
        # Multi-Assets Mode Asset Index
        api_response = api_instance.umfutures_get_asset_index_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_asset_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_asset_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Asset pair | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetAssetIndexV1Resp**](UmfuturesGetAssetIndexV1Resp.md)

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

# **umfutures_get_constituents_v1**
> UmfuturesGetConstituentsV1Resp umfutures_get_constituents_v1(symbol)

Query Index Price Constituents

Query index price constituents

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_constituents_v1_resp import UmfuturesGetConstituentsV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.umfutures_get_constituents_v1(symbol)
        print("The response of MarketDataApi->umfutures_get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_constituents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**UmfuturesGetConstituentsV1Resp**](UmfuturesGetConstituentsV1Resp.md)

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

# **umfutures_get_continuous_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.umfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_continuous_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **contract_type** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **umfutures_get_depth_v1**
> UmfuturesGetDepthV1Resp umfutures_get_depth_v1(symbol, limit=limit)

Order Book

Query symbol orderbook

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_depth_v1_resp import UmfuturesGetDepthV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.umfutures_get_depth_v1(symbol, limit=limit)
        print("The response of MarketDataApi->umfutures_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] | [optional] [default to 500]

### Return type

[**UmfuturesGetDepthV1Resp**](UmfuturesGetDepthV1Resp.md)

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

# **umfutures_get_exchange_info_v1**
> UmfuturesGetExchangeInfoV1Resp umfutures_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp import UmfuturesGetExchangeInfoV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.umfutures_get_exchange_info_v1()
        print("The response of MarketDataApi->umfutures_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesGetExchangeInfoV1Resp**](UmfuturesGetExchangeInfoV1Resp.md)

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

# **umfutures_get_funding_info_v1**
> List[UmfuturesGetFundingInfoV1RespItem] umfutures_get_funding_info_v1()

Get Funding Rate Info

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_funding_info_v1_resp_item import UmfuturesGetFundingInfoV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.umfutures_get_funding_info_v1()
        print("The response of MarketDataApi->umfutures_get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_funding_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UmfuturesGetFundingInfoV1RespItem]**](UmfuturesGetFundingInfoV1RespItem.md)

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

# **umfutures_get_funding_rate_v1**
> List[UmfuturesGetFundingRateV1RespItem] umfutures_get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History

Get Funding Rate History

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_funding_rate_v1_resp_item import UmfuturesGetFundingRateV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History
        api_response = api_instance.umfutures_get_funding_rate_v1(symbol=symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding rate from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding rate  until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]

### Return type

[**List[UmfuturesGetFundingRateV1RespItem]**](UmfuturesGetFundingRateV1RespItem.md)

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

# **umfutures_get_futures_data_basis**
> List[UmfuturesGetFuturesDataBasisRespItem] umfutures_get_futures_data_basis(pair, contract_type, period, limit, start_time=start_time, end_time=end_time)

Basis

Query future basis

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_basis_resp_item import UmfuturesGetFuturesDataBasisRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSDT (default to '')
    contract_type = '' # str | CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Basis
        api_response = api_instance.umfutures_get_futures_data_basis(pair, contract_type, period, limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_basis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_basis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSDT | [default to &#39;&#39;]
 **contract_type** | **str**| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataBasisRespItem]**](UmfuturesGetFuturesDataBasisRespItem.md)

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

# **umfutures_get_futures_data_delivery_price**
> List[UmfuturesGetFuturesDataDeliveryPriceRespItem] umfutures_get_futures_data_delivery_price(pair)

Quarterly Contract Settlement Price

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_delivery_price_resp_item import UmfuturesGetFuturesDataDeliveryPriceRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    pair = '' # str | e.g BTCUSDT (default to '')

    try:
        # Quarterly Contract Settlement Price
        api_response = api_instance.umfutures_get_futures_data_delivery_price(pair)
        print("The response of MarketDataApi->umfutures_get_futures_data_delivery_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_delivery_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| e.g BTCUSDT | [default to &#39;&#39;]

### Return type

[**List[UmfuturesGetFuturesDataDeliveryPriceRespItem]**](UmfuturesGetFuturesDataDeliveryPriceRespItem.md)

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

# **umfutures_get_futures_data_global_long_short_account_ratio**
> List[UmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem] umfutures_get_futures_data_global_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Long/Short Ratio

Query symbol Long/Short Ratio

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_global_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Long/Short Ratio
        api_response = api_instance.umfutures_get_futures_data_global_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_global_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_global_long_short_account_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem]**](UmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem.md)

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

# **umfutures_get_futures_data_open_interest_hist**
> List[UmfuturesGetFuturesDataOpenInterestHistRespItem] umfutures_get_futures_data_open_interest_hist(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Open Interest Statistics

Open Interest Statistics

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_open_interest_hist_resp_item import UmfuturesGetFuturesDataOpenInterestHistRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Open Interest Statistics
        api_response = api_instance.umfutures_get_futures_data_open_interest_hist(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_open_interest_hist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_open_interest_hist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataOpenInterestHistRespItem]**](UmfuturesGetFuturesDataOpenInterestHistRespItem.md)

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

# **umfutures_get_futures_data_takerlongshort_ratio**
> List[UmfuturesGetFuturesDataTakerlongshortRatioRespItem] umfutures_get_futures_data_takerlongshort_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Taker Buy/Sell Volume

Taker Buy/Sell Volume

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_takerlongshort_ratio_resp_item import UmfuturesGetFuturesDataTakerlongshortRatioRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Taker Buy/Sell Volume
        api_response = api_instance.umfutures_get_futures_data_takerlongshort_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_takerlongshort_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_takerlongshort_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataTakerlongshortRatioRespItem]**](UmfuturesGetFuturesDataTakerlongshortRatioRespItem.md)

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

# **umfutures_get_futures_data_top_long_short_account_ratio**
> List[UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem] umfutures_get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Accounts)

The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only.
Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions
Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions
Long/Short Ratio (Accounts) = Long Account % / Short Account %

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Accounts)
        api_response = api_instance.umfutures_get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_top_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_top_long_short_account_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem]**](UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.md)

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

# **umfutures_get_futures_data_top_long_short_position_ratio**
> List[UmfuturesGetFuturesDataTopLongShortPositionRatioRespItem] umfutures_get_futures_data_top_long_short_position_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Positions)

The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance.
Long Position % = Long positions of top traders / Total open positions of top traders
Short Position % = Short positions of top traders / Total open positions of top traders
Long/Short Ratio (Positions) = Long Position % / Short Position %

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_position_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortPositionRatioRespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Positions)
        api_response = api_instance.umfutures_get_futures_data_top_long_short_position_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->umfutures_get_futures_data_top_long_short_position_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_futures_data_top_long_short_position_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| default 30, max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[UmfuturesGetFuturesDataTopLongShortPositionRatioRespItem]**](UmfuturesGetFuturesDataTopLongShortPositionRatioRespItem.md)

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

# **umfutures_get_historical_trades_v1**
> List[UmfuturesGetHistoricalTradesV1RespItem] umfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_historical_trades_v1_resp_item import UmfuturesGetHistoricalTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.umfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of MarketDataApi->umfutures_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 500. | [optional] [default to 100]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[UmfuturesGetHistoricalTradesV1RespItem]**](UmfuturesGetHistoricalTradesV1RespItem.md)

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

# **umfutures_get_index_info_v1**
> List[UmfuturesGetIndexInfoV1RespItem] umfutures_get_index_info_v1(symbol=symbol)

Composite Index Symbol Information

Query composite index symbol information

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_index_info_v1_resp_item import UmfuturesGetIndexInfoV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Composite Index Symbol Information
        api_response = api_instance.umfutures_get_index_info_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_index_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_index_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[UmfuturesGetIndexInfoV1RespItem]**](UmfuturesGetIndexInfoV1RespItem.md)

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

# **umfutures_get_index_price_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.umfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_index_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **umfutures_get_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.umfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **umfutures_get_mark_price_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.umfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_mark_price_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **umfutures_get_open_interest_v1**
> UmfuturesGetOpenInterestV1Resp umfutures_get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_open_interest_v1_resp import UmfuturesGetOpenInterestV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.umfutures_get_open_interest_v1(symbol)
        print("The response of MarketDataApi->umfutures_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**UmfuturesGetOpenInterestV1Resp**](UmfuturesGetOpenInterestV1Resp.md)

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

# **umfutures_get_ping_v1**
> object umfutures_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.umfutures_get_ping_v1()
        print("The response of MarketDataApi->umfutures_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_ping_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **umfutures_get_premium_index_klines_v1**
> List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]] umfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_continuous_klines_v1_resp_inner_inner import UmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.umfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->umfutures_get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_premium_index_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1500. | [optional] [default to 500]

### Return type

**List[List[UmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **umfutures_get_premium_index_v1**
> UmfuturesGetPremiumIndexV1Resp umfutures_get_premium_index_v1(symbol=symbol)

Mark Price

Mark Price and Funding Rate

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_premium_index_v1_resp import UmfuturesGetPremiumIndexV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Mark Price
        api_response = api_instance.umfutures_get_premium_index_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetPremiumIndexV1Resp**](UmfuturesGetPremiumIndexV1Resp.md)

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

# **umfutures_get_ticker24hr_v1**
> UmfuturesGetTicker24hrV1Resp umfutures_get_ticker24hr_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.
Careful when accessing this with no symbol.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker24hr_v1_resp import UmfuturesGetTicker24hrV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.umfutures_get_ticker24hr_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTicker24hrV1Resp**](UmfuturesGetTicker24hrV1Resp.md)

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

# **umfutures_get_ticker_book_ticker_v1**
> UmfuturesGetTickerBookTickerV1Resp umfutures_get_ticker_book_ticker_v1(symbol=symbol)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp import UmfuturesGetTickerBookTickerV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.umfutures_get_ticker_book_ticker_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerBookTickerV1Resp**](UmfuturesGetTickerBookTickerV1Resp.md)

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

# **umfutures_get_ticker_price_v1**
> UmfuturesGetTickerPriceV1Resp umfutures_get_ticker_price_v1(symbol=symbol)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v1_resp import UmfuturesGetTickerPriceV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.umfutures_get_ticker_price_v1(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerPriceV1Resp**](UmfuturesGetTickerPriceV1Resp.md)

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

# **umfutures_get_ticker_price_v2**
> UmfuturesGetTickerPriceV2Resp umfutures_get_ticker_price_v2(symbol=symbol)

Symbol Price Ticker V2

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_ticker_price_v2_resp import UmfuturesGetTickerPriceV2Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker V2
        api_response = api_instance.umfutures_get_ticker_price_v2(symbol=symbol)
        print("The response of MarketDataApi->umfutures_get_ticker_price_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_ticker_price_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UmfuturesGetTickerPriceV2Resp**](UmfuturesGetTickerPriceV2Resp.md)

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

# **umfutures_get_time_v1**
> UmfuturesGetTimeV1Resp umfutures_get_time_v1()

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_time_v1_resp import UmfuturesGetTimeV1Resp
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)

    try:
        # Check Server Time
        api_response = api_instance.umfutures_get_time_v1()
        print("The response of MarketDataApi->umfutures_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UmfuturesGetTimeV1Resp**](UmfuturesGetTimeV1Resp.md)

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

# **umfutures_get_trades_v1**
> List[UmfuturesGetTradesV1RespItem] umfutures_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.umfutures
from binance.derivatives.umfutures.models.umfutures_get_trades_v1_resp_item import UmfuturesGetTradesV1RespItem
from binance.derivatives.umfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.umfutures.Configuration(
    host = "https://fapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.umfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.umfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.umfutures_get_trades_v1(symbol, limit=limit)
        print("The response of MarketDataApi->umfutures_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->umfutures_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[UmfuturesGetTradesV1RespItem]**](UmfuturesGetTradesV1RespItem.md)

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

