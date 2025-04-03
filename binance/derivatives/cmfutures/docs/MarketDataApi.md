# binance.derivatives.cmfutures.MarketDataApi

All URIs are relative to *https://dapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmfutures_get_agg_trades_v1**](MarketDataApi.md#cmfutures_get_agg_trades_v1) | **GET** /dapi/v1/aggTrades | Compressed/Aggregate Trades List
[**cmfutures_get_constituents_v1**](MarketDataApi.md#cmfutures_get_constituents_v1) | **GET** /dapi/v1/constituents | Query Index Price Constituents
[**cmfutures_get_continuous_klines_v1**](MarketDataApi.md#cmfutures_get_continuous_klines_v1) | **GET** /dapi/v1/continuousKlines | Continuous Contract Kline/Candlestick Data
[**cmfutures_get_depth_v1**](MarketDataApi.md#cmfutures_get_depth_v1) | **GET** /dapi/v1/depth | Order Book
[**cmfutures_get_exchange_info_v1**](MarketDataApi.md#cmfutures_get_exchange_info_v1) | **GET** /dapi/v1/exchangeInfo | Exchange Information
[**cmfutures_get_funding_info_v1**](MarketDataApi.md#cmfutures_get_funding_info_v1) | **GET** /dapi/v1/fundingInfo | Get Funding Rate Info
[**cmfutures_get_funding_rate_v1**](MarketDataApi.md#cmfutures_get_funding_rate_v1) | **GET** /dapi/v1/fundingRate | Get Funding Rate History of Perpetual Futures
[**cmfutures_get_futures_data_basis**](MarketDataApi.md#cmfutures_get_futures_data_basis) | **GET** /futures/data/basis | Basis
[**cmfutures_get_futures_data_global_long_short_account_ratio**](MarketDataApi.md#cmfutures_get_futures_data_global_long_short_account_ratio) | **GET** /futures/data/globalLongShortAccountRatio | Long/Short Ratio
[**cmfutures_get_futures_data_open_interest_hist**](MarketDataApi.md#cmfutures_get_futures_data_open_interest_hist) | **GET** /futures/data/openInterestHist | Open Interest Statistics
[**cmfutures_get_futures_data_taker_buy_sell_vol**](MarketDataApi.md#cmfutures_get_futures_data_taker_buy_sell_vol) | **GET** /futures/data/takerBuySellVol | Taker Buy/Sell Volume
[**cmfutures_get_futures_data_top_long_short_account_ratio**](MarketDataApi.md#cmfutures_get_futures_data_top_long_short_account_ratio) | **GET** /futures/data/topLongShortAccountRatio | Top Trader Long/Short Ratio (Accounts)
[**cmfutures_get_futures_data_top_long_short_position_ratio**](MarketDataApi.md#cmfutures_get_futures_data_top_long_short_position_ratio) | **GET** /futures/data/topLongShortPositionRatio | Top Trader Long/Short Ratio (Positions)
[**cmfutures_get_historical_trades_v1**](MarketDataApi.md#cmfutures_get_historical_trades_v1) | **GET** /dapi/v1/historicalTrades | Old Trades Lookup(MARKET_DATA)
[**cmfutures_get_index_price_klines_v1**](MarketDataApi.md#cmfutures_get_index_price_klines_v1) | **GET** /dapi/v1/indexPriceKlines | Index Price Kline/Candlestick Data
[**cmfutures_get_klines_v1**](MarketDataApi.md#cmfutures_get_klines_v1) | **GET** /dapi/v1/klines | Kline/Candlestick Data
[**cmfutures_get_mark_price_klines_v1**](MarketDataApi.md#cmfutures_get_mark_price_klines_v1) | **GET** /dapi/v1/markPriceKlines | Mark Price Kline/Candlestick Data
[**cmfutures_get_open_interest_v1**](MarketDataApi.md#cmfutures_get_open_interest_v1) | **GET** /dapi/v1/openInterest | Open Interest
[**cmfutures_get_ping_v1**](MarketDataApi.md#cmfutures_get_ping_v1) | **GET** /dapi/v1/ping | Test Connectivity
[**cmfutures_get_premium_index_klines_v1**](MarketDataApi.md#cmfutures_get_premium_index_klines_v1) | **GET** /dapi/v1/premiumIndexKlines | Premium index Kline Data
[**cmfutures_get_premium_index_v1**](MarketDataApi.md#cmfutures_get_premium_index_v1) | **GET** /dapi/v1/premiumIndex | Index Price and Mark Price
[**cmfutures_get_ticker24hr_v1**](MarketDataApi.md#cmfutures_get_ticker24hr_v1) | **GET** /dapi/v1/ticker/24hr | 24hr Ticker Price Change Statistics
[**cmfutures_get_ticker_book_ticker_v1**](MarketDataApi.md#cmfutures_get_ticker_book_ticker_v1) | **GET** /dapi/v1/ticker/bookTicker | Symbol Order Book Ticker
[**cmfutures_get_ticker_price_v1**](MarketDataApi.md#cmfutures_get_ticker_price_v1) | **GET** /dapi/v1/ticker/price | Symbol Price Ticker
[**cmfutures_get_time_v1**](MarketDataApi.md#cmfutures_get_time_v1) | **GET** /dapi/v1/time | Check Server time
[**cmfutures_get_trades_v1**](MarketDataApi.md#cmfutures_get_trades_v1) | **GET** /dapi/v1/trades | Recent Trades List


# **cmfutures_get_agg_trades_v1**
> List[CmfuturesGetAggTradesV1RespItem] cmfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_agg_trades_v1_resp_item import CmfuturesGetAggTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate Trades List
        api_response = api_instance.cmfutures_get_agg_trades_v1(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_agg_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_agg_trades_v1: %s\n" % e)
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

[**List[CmfuturesGetAggTradesV1RespItem]**](CmfuturesGetAggTradesV1RespItem.md)

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

# **cmfutures_get_constituents_v1**
> CmfuturesGetConstituentsV1Resp cmfutures_get_constituents_v1(symbol)

Query Index Price Constituents

Query index price constituents

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_constituents_v1_resp import CmfuturesGetConstituentsV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Query Index Price Constituents
        api_response = api_instance.cmfutures_get_constituents_v1(symbol)
        print("The response of MarketDataApi->cmfutures_get_constituents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_constituents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**CmfuturesGetConstituentsV1Resp**](CmfuturesGetConstituentsV1Resp.md)

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

# **cmfutures_get_continuous_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)

Continuous Contract Kline/Candlestick Data

Kline/candlestick bars for a specific contract type.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str |  (default to '')
    contract_type = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Continuous Contract Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_continuous_klines_v1(pair, contract_type, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_continuous_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_continuous_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_depth_v1**
> CmfuturesGetDepthV1Resp cmfutures_get_depth_v1(symbol, limit=limit)

Order Book

Query orderbook on specific symbol

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_depth_v1_resp import CmfuturesGetDepthV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] (optional) (default to 500)

    try:
        # Order Book
        api_response = api_instance.cmfutures_get_depth_v1(symbol, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] | [optional] [default to 500]

### Return type

[**CmfuturesGetDepthV1Resp**](CmfuturesGetDepthV1Resp.md)

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

# **cmfutures_get_exchange_info_v1**
> CmfuturesGetExchangeInfoV1Resp cmfutures_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_exchange_info_v1_resp import CmfuturesGetExchangeInfoV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.cmfutures_get_exchange_info_v1()
        print("The response of MarketDataApi->cmfutures_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesGetExchangeInfoV1Resp**](CmfuturesGetExchangeInfoV1Resp.md)

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

# **cmfutures_get_funding_info_v1**
> List[CmfuturesGetFundingInfoV1RespItem] cmfutures_get_funding_info_v1()

Get Funding Rate Info

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_funding_info_v1_resp_item import CmfuturesGetFundingInfoV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)

    try:
        # Get Funding Rate Info
        api_response = api_instance.cmfutures_get_funding_info_v1()
        print("The response of MarketDataApi->cmfutures_get_funding_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_funding_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CmfuturesGetFundingInfoV1RespItem]**](CmfuturesGetFundingInfoV1RespItem.md)

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

# **cmfutures_get_funding_rate_v1**
> List[CmfuturesGetFundingRateV1RespItem] cmfutures_get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)

Get Funding Rate History of Perpetual Futures

Get Funding Rate History of Perpetual Futures

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_funding_rate_v1_resp_item import CmfuturesGetFundingRateV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    start_time = 56 # int | Timestamp in ms to get funding rate from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get funding rate  until INCLUSIVE. (optional)
    limit = 100 # int | Default 100; max 1000 (optional) (default to 100)

    try:
        # Get Funding Rate History of Perpetual Futures
        api_response = api_instance.cmfutures_get_funding_rate_v1(symbol, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_funding_rate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_funding_rate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**| Timestamp in ms to get funding rate from INCLUSIVE. | [optional] 
 **end_time** | **int**| Timestamp in ms to get funding rate  until INCLUSIVE. | [optional] 
 **limit** | **int**| Default 100; max 1000 | [optional] [default to 100]

### Return type

[**List[CmfuturesGetFundingRateV1RespItem]**](CmfuturesGetFundingRateV1RespItem.md)

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

# **cmfutures_get_futures_data_basis**
> List[CmfuturesGetFuturesDataBasisRespItem] cmfutures_get_futures_data_basis(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Basis

Query basis

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_basis_resp_item import CmfuturesGetFuturesDataBasisRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Basis
        api_response = api_instance.cmfutures_get_futures_data_basis(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_basis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_basis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetFuturesDataBasisRespItem]**](CmfuturesGetFuturesDataBasisRespItem.md)

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

# **cmfutures_get_futures_data_global_long_short_account_ratio**
> List[CmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem] cmfutures_get_futures_data_global_long_short_account_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)

Long/Short Ratio

Query symbol Long/Short Ratio

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_global_long_short_account_ratio_resp_item import CmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Long/Short Ratio
        api_response = api_instance.cmfutures_get_futures_data_global_long_short_account_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_global_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_global_long_short_account_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem]**](CmfuturesGetFuturesDataGlobalLongShortAccountRatioRespItem.md)

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

# **cmfutures_get_futures_data_open_interest_hist**
> List[CmfuturesGetFuturesDataOpenInterestHistRespItem] cmfutures_get_futures_data_open_interest_hist(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Open Interest Statistics

Query open interest stats

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_open_interest_hist_resp_item import CmfuturesGetFuturesDataOpenInterestHistRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Open Interest Statistics
        api_response = api_instance.cmfutures_get_futures_data_open_interest_hist(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_open_interest_hist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_open_interest_hist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetFuturesDataOpenInterestHistRespItem]**](CmfuturesGetFuturesDataOpenInterestHistRespItem.md)

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

# **cmfutures_get_futures_data_taker_buy_sell_vol**
> List[CmfuturesGetFuturesDataTakerBuySellVolRespItem] cmfutures_get_futures_data_taker_buy_sell_vol(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)

Taker Buy/Sell Volume

Taker Buy Volume: the total volume of buy orders filled by takers within the period.
Taker Sell Volume: the total volume of sell orders filled by takers within the period.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_taker_buy_sell_vol_resp_item import CmfuturesGetFuturesDataTakerBuySellVolRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    contract_type = '' # str | ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Taker Buy/Sell Volume
        api_response = api_instance.cmfutures_get_futures_data_taker_buy_sell_vol(pair, contract_type, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_taker_buy_sell_vol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_taker_buy_sell_vol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **contract_type** | **str**| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetFuturesDataTakerBuySellVolRespItem]**](CmfuturesGetFuturesDataTakerBuySellVolRespItem.md)

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

# **cmfutures_get_futures_data_top_long_short_account_ratio**
> List[CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem] cmfutures_get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Accounts)

The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only.
Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions
Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions
Long/Short Ratio (Accounts) = Long Account % / Short Account %

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_top_long_short_account_ratio_resp_item import CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | default 30, max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Accounts)
        api_response = api_instance.cmfutures_get_futures_data_top_long_short_account_ratio(symbol, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_top_long_short_account_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_top_long_short_account_ratio: %s\n" % e)
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

[**List[CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem]**](CmfuturesGetFuturesDataTopLongShortAccountRatioRespItem.md)

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

# **cmfutures_get_futures_data_top_long_short_position_ratio**
> List[CmfuturesGetFuturesDataTopLongShortPositionRatioRespItem] cmfutures_get_futures_data_top_long_short_position_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)

Top Trader Long/Short Ratio (Positions)

The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance.
Long Position % = Long positions of top traders / Total open positions of top traders
Short Position % = Short positions of top traders / Total open positions of top traders
Long/Short Ratio (Positions) = Long Position % / Short Position %

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_top_long_short_position_ratio_resp_item import CmfuturesGetFuturesDataTopLongShortPositionRatioRespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str | BTCUSD (default to '')
    period = '' # str | &#34;5m&#34;,&#34;15m&#34;,&#34;30m&#34;,&#34;1h&#34;,&#34;2h&#34;,&#34;4h&#34;,&#34;6h&#34;,&#34;12h&#34;,&#34;1d&#34; (default to '')
    limit = 30 # int | Default 30,Max 500 (optional) (default to 30)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        # Top Trader Long/Short Ratio (Positions)
        api_response = api_instance.cmfutures_get_futures_data_top_long_short_position_ratio(pair, period, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of MarketDataApi->cmfutures_get_futures_data_top_long_short_position_ratio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_futures_data_top_long_short_position_ratio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| BTCUSD | [default to &#39;&#39;]
 **period** | **str**| &amp;#34;5m&amp;#34;,&amp;#34;15m&amp;#34;,&amp;#34;30m&amp;#34;,&amp;#34;1h&amp;#34;,&amp;#34;2h&amp;#34;,&amp;#34;4h&amp;#34;,&amp;#34;6h&amp;#34;,&amp;#34;12h&amp;#34;,&amp;#34;1d&amp;#34; | [default to &#39;&#39;]
 **limit** | **int**| Default 30,Max 500 | [optional] [default to 30]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

[**List[CmfuturesGetFuturesDataTopLongShortPositionRatioRespItem]**](CmfuturesGetFuturesDataTopLongShortPositionRatioRespItem.md)

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

# **cmfutures_get_historical_trades_v1**
> List[CmfuturesGetHistoricalTradesV1RespItem] cmfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)

Old Trades Lookup(MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_historical_trades_v1_resp_item import CmfuturesGetHistoricalTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 500. (optional) (default to 100)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old Trades Lookup(MARKET_DATA)
        api_response = api_instance.cmfutures_get_historical_trades_v1(symbol, limit=limit, from_id=from_id)
        print("The response of MarketDataApi->cmfutures_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 500. | [optional] [default to 100]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[CmfuturesGetHistoricalTradesV1RespItem]**](CmfuturesGetHistoricalTradesV1RespItem.md)

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

# **cmfutures_get_index_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)

Index Price Kline/Candlestick Data

Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    pair = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Index Price Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_index_price_klines_v1(pair, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_index_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_index_price_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_mark_price_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Mark Price Kline/Candlestick Data

Kline/candlestick bars for the mark price of a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Mark Price Kline/Candlestick Data
        api_response = api_instance.cmfutures_get_mark_price_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_mark_price_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_mark_price_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_open_interest_v1**
> CmfuturesGetOpenInterestV1Resp cmfutures_get_open_interest_v1(symbol)

Open Interest

Get present open interest of a specific symbol.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_open_interest_v1_resp import CmfuturesGetOpenInterestV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Open Interest
        api_response = api_instance.cmfutures_get_open_interest_v1(symbol)
        print("The response of MarketDataApi->cmfutures_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**CmfuturesGetOpenInterestV1Resp**](CmfuturesGetOpenInterestV1Resp.md)

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

# **cmfutures_get_ping_v1**
> object cmfutures_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.cmfutures_get_ping_v1()
        print("The response of MarketDataApi->cmfutures_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_ping_v1: %s\n" % e)
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

# **cmfutures_get_premium_index_klines_v1**
> List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]] cmfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Premium index Kline Data

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_continuous_klines_v1_resp_inner_inner import CmfuturesGetContinuousKlinesV1RespInnerInner
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    limit = 500 # int | Default 500; max 1500. (optional) (default to 500)

    try:
        # Premium index Kline Data
        api_response = api_instance.cmfutures_get_premium_index_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_premium_index_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_premium_index_klines_v1: %s\n" % e)
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

**List[List[CmfuturesGetContinuousKlinesV1RespInnerInner]]**

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

# **cmfutures_get_premium_index_v1**
> List[CmfuturesGetPremiumIndexV1RespItem] cmfutures_get_premium_index_v1(symbol=symbol, pair=pair)

Index Price and Mark Price

Query index price and mark price

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_premium_index_v1_resp_item import CmfuturesGetPremiumIndexV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Index Price and Mark Price
        api_response = api_instance.cmfutures_get_premium_index_v1(symbol=symbol, pair=pair)
        print("The response of MarketDataApi->cmfutures_get_premium_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_premium_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetPremiumIndexV1RespItem]**](CmfuturesGetPremiumIndexV1RespItem.md)

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

# **cmfutures_get_ticker24hr_v1**
> List[CmfuturesGetTicker24hrV1RespItem] cmfutures_get_ticker24hr_v1(symbol=symbol, pair=pair)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker24hr_v1_resp_item import CmfuturesGetTicker24hrV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.cmfutures_get_ticker24hr_v1(symbol=symbol, pair=pair)
        print("The response of MarketDataApi->cmfutures_get_ticker24hr_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_ticker24hr_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTicker24hrV1RespItem]**](CmfuturesGetTicker24hrV1RespItem.md)

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

# **cmfutures_get_ticker_book_ticker_v1**
> List[CmfuturesGetTickerBookTickerV1RespItem] cmfutures_get_ticker_book_ticker_v1(symbol=symbol, pair=pair)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker_book_ticker_v1_resp_item import CmfuturesGetTickerBookTickerV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Order Book Ticker
        api_response = api_instance.cmfutures_get_ticker_book_ticker_v1(symbol=symbol, pair=pair)
        print("The response of MarketDataApi->cmfutures_get_ticker_book_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_ticker_book_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTickerBookTickerV1RespItem]**](CmfuturesGetTickerBookTickerV1RespItem.md)

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

# **cmfutures_get_ticker_price_v1**
> List[CmfuturesGetTickerPriceV1RespItem] cmfutures_get_ticker_price_v1(symbol=symbol, pair=pair)

Symbol Price Ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_ticker_price_v1_resp_item import CmfuturesGetTickerPriceV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (optional) (default to '')
    pair = '' # str |  (optional) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.cmfutures_get_ticker_price_v1(symbol=symbol, pair=pair)
        print("The response of MarketDataApi->cmfutures_get_ticker_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_ticker_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] [default to &#39;&#39;]
 **pair** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[CmfuturesGetTickerPriceV1RespItem]**](CmfuturesGetTickerPriceV1RespItem.md)

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

# **cmfutures_get_time_v1**
> CmfuturesGetTimeV1Resp cmfutures_get_time_v1()

Check Server time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_time_v1_resp import CmfuturesGetTimeV1Resp
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)

    try:
        # Check Server time
        api_response = api_instance.cmfutures_get_time_v1()
        print("The response of MarketDataApi->cmfutures_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CmfuturesGetTimeV1Resp**](CmfuturesGetTimeV1Resp.md)

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

# **cmfutures_get_trades_v1**
> List[CmfuturesGetTradesV1RespItem] cmfutures_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.cmfutures
from binance.derivatives.cmfutures.models.cmfutures_get_trades_v1_resp_item import CmfuturesGetTradesV1RespItem
from binance.derivatives.cmfutures.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.cmfutures.Configuration(
    host = "https://dapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.cmfutures.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.cmfutures.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent Trades List
        api_response = api_instance.cmfutures_get_trades_v1(symbol, limit=limit)
        print("The response of MarketDataApi->cmfutures_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->cmfutures_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[CmfuturesGetTradesV1RespItem]**](CmfuturesGetTradesV1RespItem.md)

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

