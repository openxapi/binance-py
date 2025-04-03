# binance.spot.MarketDataApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spot_get_agg_trades_v3**](MarketDataApi.md#spot_get_agg_trades_v3) | **GET** /api/v3/aggTrades | Compressed/Aggregate trades list
[**spot_get_avg_price_v3**](MarketDataApi.md#spot_get_avg_price_v3) | **GET** /api/v3/avgPrice | Current average price
[**spot_get_depth_v3**](MarketDataApi.md#spot_get_depth_v3) | **GET** /api/v3/depth | Order book
[**spot_get_historical_trades_v3**](MarketDataApi.md#spot_get_historical_trades_v3) | **GET** /api/v3/historicalTrades | Old trade lookup
[**spot_get_klines_v3**](MarketDataApi.md#spot_get_klines_v3) | **GET** /api/v3/klines | Kline/Candlestick data
[**spot_get_ticker24hr_v3**](MarketDataApi.md#spot_get_ticker24hr_v3) | **GET** /api/v3/ticker/24hr | 24hr ticker price change statistics
[**spot_get_ticker_book_ticker_v3**](MarketDataApi.md#spot_get_ticker_book_ticker_v3) | **GET** /api/v3/ticker/bookTicker | Symbol order book ticker
[**spot_get_ticker_price_v3**](MarketDataApi.md#spot_get_ticker_price_v3) | **GET** /api/v3/ticker/price | Symbol price ticker
[**spot_get_ticker_trading_day_v3**](MarketDataApi.md#spot_get_ticker_trading_day_v3) | **GET** /api/v3/ticker/tradingDay | Trading Day Ticker
[**spot_get_ticker_v3**](MarketDataApi.md#spot_get_ticker_v3) | **GET** /api/v3/ticker | Rolling window price change statistics
[**spot_get_trades_v3**](MarketDataApi.md#spot_get_trades_v3) | **GET** /api/v3/trades | Recent trades list
[**spot_get_ui_klines_v3**](MarketDataApi.md#spot_get_ui_klines_v3) | **GET** /api/v3/uiKlines | UIKlines


# **spot_get_agg_trades_v3**
> List[SpotGetAggTradesV3RespItem] spot_get_agg_trades_v3(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate trades list

Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_agg_trades_v3_resp_item import SpotGetAggTradesV3RespItem
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    from_id = 56 # int | ID to get aggregate trades from INCLUSIVE. (optional)
    start_time = 56 # int | Timestamp in ms to get aggregate trades from INCLUSIVE. (optional)
    end_time = 56 # int | Timestamp in ms to get aggregate trades until INCLUSIVE. (optional)
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Compressed/Aggregate trades list
        api_response = api_instance.spot_get_agg_trades_v3(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->spot_get_agg_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_agg_trades_v3: %s\n" % e)
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

[**List[SpotGetAggTradesV3RespItem]**](SpotGetAggTradesV3RespItem.md)

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

# **spot_get_avg_price_v3**
> SpotGetAvgPriceV3Resp spot_get_avg_price_v3(symbol)

Current average price

Current average price for a symbol.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_avg_price_v3_resp import SpotGetAvgPriceV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')

    try:
        # Current average price
        api_response = api_instance.spot_get_avg_price_v3(symbol)
        print("The response of MarketDataApi->spot_get_avg_price_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_avg_price_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]

### Return type

[**SpotGetAvgPriceV3Resp**](SpotGetAvgPriceV3Resp.md)

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

# **spot_get_depth_v3**
> SpotGetDepthV3Resp spot_get_depth_v3(symbol, limit=limit)

Order book

### Example


```python
import binance.spot
from binance.spot.models.spot_get_depth_v3_resp import SpotGetDepthV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 100 # int | Default 100; max 5000. <br/> If limit &gt; 5000. then the response will truncate to 5000. (optional) (default to 100)

    try:
        # Order book
        api_response = api_instance.spot_get_depth_v3(symbol, limit=limit)
        print("The response of MarketDataApi->spot_get_depth_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_depth_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 100; max 5000. &lt;br/&gt; If limit &amp;gt; 5000. then the response will truncate to 5000. | [optional] [default to 100]

### Return type

[**SpotGetDepthV3Resp**](SpotGetDepthV3Resp.md)

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

# **spot_get_historical_trades_v3**
> List[SpotGetHistoricalTradesV3RespItem] spot_get_historical_trades_v3(symbol, limit=limit, from_id=from_id)

Old trade lookup

Get older trades.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_historical_trades_v3_resp_item import SpotGetHistoricalTradesV3RespItem
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)
    from_id = 56 # int | TradeId to fetch from. Default gets most recent trades. (optional)

    try:
        # Old trade lookup
        api_response = api_instance.spot_get_historical_trades_v3(symbol, limit=limit, from_id=from_id)
        print("The response of MarketDataApi->spot_get_historical_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_historical_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]
 **from_id** | **int**| TradeId to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**List[SpotGetHistoricalTradesV3RespItem]**](SpotGetHistoricalTradesV3RespItem.md)

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

# **spot_get_klines_v3**
> List[List[SpotGetKlinesV3200ResponseInnerInner]] spot_get_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)

Kline/Candlestick data

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_klines_v3200_response_inner_inner import SpotGetKlinesV3200ResponseInnerInner
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str |  (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Kline/Candlestick data
        api_response = api_instance.spot_get_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)
        print("The response of MarketDataApi->spot_get_klines_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_klines_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**|  | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

**List[List[SpotGetKlinesV3200ResponseInnerInner]]**

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

# **spot_get_ticker24hr_v3**
> SpotGetTicker24hrV3Resp spot_get_ticker24hr_v3(symbol=symbol, symbols=symbols, type=type)

24hr ticker price change statistics

24 hour rolling window price change statistics. Careful when accessing this with no symbol.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker24hr_v3_resp import SpotGetTicker24hrV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, tickers for all symbols will be returned in an array. <br/><br/>          Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, tickers for all symbols will be returned in an array. <br/><br/>          Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # 24hr ticker price change statistics
        api_response = api_instance.spot_get_ticker24hr_v3(symbol=symbol, symbols=symbols, type=type)
        print("The response of MarketDataApi->spot_get_ticker24hr_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ticker24hr_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, tickers for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;          Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, tickers for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;          Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTicker24hrV3Resp**](SpotGetTicker24hrV3Resp.md)

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

# **spot_get_ticker_book_ticker_v3**
> SpotGetTickerBookTickerV3Resp spot_get_ticker_book_ticker_v3(symbol=symbol, symbols=symbols)

Symbol order book ticker

Best price/qty on the order book for a symbol or symbols.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_book_ticker_v3_resp import SpotGetTickerBookTickerV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, bookTickers for all symbols will be returned in an array.          <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, bookTickers for all symbols will be returned in an array.          <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')

    try:
        # Symbol order book ticker
        api_response = api_instance.spot_get_ticker_book_ticker_v3(symbol=symbol, symbols=symbols)
        print("The response of MarketDataApi->spot_get_ticker_book_ticker_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ticker_book_ticker_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, bookTickers for all symbols will be returned in an array.          &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, bookTickers for all symbols will be returned in an array.          &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]

### Return type

[**SpotGetTickerBookTickerV3Resp**](SpotGetTickerBookTickerV3Resp.md)

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

# **spot_get_ticker_price_v3**
> SpotGetTickerPriceV3Resp spot_get_ticker_price_v3(symbol=symbol, symbols=symbols)

Symbol price ticker

Latest price for a symbol or symbols.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_price_v3_resp import SpotGetTickerPriceV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, prices for all symbols will be returned in an array. <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')
    symbols = '' # str | Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, prices for all symbols will be returned in an array. <br/><br/>         Examples of accepted format for the symbols parameter:          [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>          or <br/>          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D (optional) (default to '')

    try:
        # Symbol price ticker
        api_response = api_instance.spot_get_ticker_price_v3(symbol=symbol, symbols=symbols)
        print("The response of MarketDataApi->spot_get_ticker_price_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ticker_price_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, prices for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]
 **symbols** | **str**| Parameter symbol and symbols cannot be used in combination. &lt;br/&gt; If neither parameter is sent, prices for all symbols will be returned in an array. &lt;br/&gt;&lt;br/&gt;         Examples of accepted format for the symbols parameter:          [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;          or &lt;br/&gt;          %5B%22BTCUSDT%22,%22BNBUSDT%22%5D | [optional] [default to &#39;&#39;]

### Return type

[**SpotGetTickerPriceV3Resp**](SpotGetTickerPriceV3Resp.md)

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

# **spot_get_ticker_trading_day_v3**
> SpotGetTickerTradingDayV3Resp spot_get_ticker_trading_day_v3(symbol, symbols, time_zone=time_zone, type=type)

Trading Day Ticker

Price change statistics for a trading day.
4 for each requested symbol.  The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_trading_day_v3_resp import SpotGetTickerTradingDayV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    symbols = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # Trading Day Ticker
        api_response = api_instance.spot_get_ticker_trading_day_v3(symbol, symbols, time_zone=time_zone, type=type)
        print("The response of MarketDataApi->spot_get_ticker_trading_day_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ticker_trading_day_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **symbols** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTickerTradingDayV3Resp**](SpotGetTickerTradingDayV3Resp.md)

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

# **spot_get_ticker_v3**
> SpotGetTickerV3Resp spot_get_ticker_v3(symbol, symbols, window_size=window_size, type=type)

Rolling window price change statistics

Note: This endpoint is different from the GET /api/v3/ticker/24hr endpoint.
The window used to compute statistics will be no more than 59999ms from the requested windowSize.
openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
As such, the effective window will be up to 59999ms wider than windowSize.
E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the openTime will be: 1641201420000 (January 3, 2022, 09:17:00)
4 for each requested symbol regardless of windowSize.  The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_ticker_v3_resp import SpotGetTickerV3Resp
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    symbols = '' # str | Either `symbol` or `symbols` must be provided <br/><br/> Examples of accepted format for the `symbols` parameter: <br/> [&#34;BTCUSDT&#34;,&#34;BNBUSDT&#34;] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of `symbols` allowed in a request is 100. (default to '')
    window_size = '' # str | Defaults to `1d` if no parameter provided <br/> Supported `windowSize` values: <br/> `1m`,`2m`....`59m` for minutes <br/> `1h`, `2h`....`23h` - for hours <br/> `1d`...`7d` - for days <br/><br/> Units cannot be combined (e.g. `1d2h` is not allowed) (optional) (default to '')
    type =  # str | Supported values: `FULL` or `MINI`. <br/>If none provided, the default is `FULL` (optional) (default to )

    try:
        # Rolling window price change statistics
        api_response = api_instance.spot_get_ticker_v3(symbol, symbols, window_size=window_size, type=type)
        print("The response of MarketDataApi->spot_get_ticker_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ticker_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **symbols** | **str**| Either &#x60;symbol&#x60; or &#x60;symbols&#x60; must be provided &lt;br/&gt;&lt;br/&gt; Examples of accepted format for the &#x60;symbols&#x60; parameter: &lt;br/&gt; [&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBUSDT&amp;#34;] &lt;br/&gt;or &lt;br/&gt;%5B%22BTCUSDT%22,%22BNBUSDT%22%5D &lt;br/&gt;&lt;br/&gt; The maximum number of &#x60;symbols&#x60; allowed in a request is 100. | [default to &#39;&#39;]
 **window_size** | **str**| Defaults to &#x60;1d&#x60; if no parameter provided &lt;br/&gt; Supported &#x60;windowSize&#x60; values: &lt;br/&gt; &#x60;1m&#x60;,&#x60;2m&#x60;....&#x60;59m&#x60; for minutes &lt;br/&gt; &#x60;1h&#x60;, &#x60;2h&#x60;....&#x60;23h&#x60; - for hours &lt;br/&gt; &#x60;1d&#x60;...&#x60;7d&#x60; - for days &lt;br/&gt;&lt;br/&gt; Units cannot be combined (e.g. &#x60;1d2h&#x60; is not allowed) | [optional] [default to &#39;&#39;]
 **type** | **str**| Supported values: &#x60;FULL&#x60; or &#x60;MINI&#x60;. &lt;br/&gt;If none provided, the default is &#x60;FULL&#x60; | [optional] [default to ]

### Return type

[**SpotGetTickerV3Resp**](SpotGetTickerV3Resp.md)

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

# **spot_get_trades_v3**
> List[SpotGetTradesV3RespItem] spot_get_trades_v3(symbol, limit=limit)

Recent trades list

Get recent trades.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_trades_v3_resp_item import SpotGetTradesV3RespItem
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # Recent trades list
        api_response = api_instance.spot_get_trades_v3(symbol, limit=limit)
        print("The response of MarketDataApi->spot_get_trades_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_trades_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

[**List[SpotGetTradesV3RespItem]**](SpotGetTradesV3RespItem.md)

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

# **spot_get_ui_klines_v3**
> List[List[SpotGetKlinesV3200ResponseInnerInner]] spot_get_ui_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)

UIKlines

The request is similar to klines having the same parameters and response.
uiKlines return modified kline data, optimized for presentation of candlestick charts.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_klines_v3200_response_inner_inner import SpotGetKlinesV3200ResponseInnerInner
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
    api_instance = binance.spot.MarketDataApi(api_client)
    symbol = '' # str |  (default to '')
    interval = '' # str | See <a href=\"/docs/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals\">`klines`</a> (default to '')
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    time_zone = '0' # str | Default: 0 (UTC) (optional) (default to '0')
    limit = 500 # int | Default 500; max 1000. (optional) (default to 500)

    try:
        # UIKlines
        api_response = api_instance.spot_get_ui_klines_v3(symbol, interval, start_time=start_time, end_time=end_time, time_zone=time_zone, limit=limit)
        print("The response of MarketDataApi->spot_get_ui_klines_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->spot_get_ui_klines_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [default to &#39;&#39;]
 **interval** | **str**| See &lt;a href&#x3D;\&quot;/docs/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals\&quot;&gt;&#x60;klines&#x60;&lt;/a&gt; | [default to &#39;&#39;]
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **time_zone** | **str**| Default: 0 (UTC) | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Default 500; max 1000. | [optional] [default to 500]

### Return type

**List[List[SpotGetKlinesV3200ResponseInnerInner]]**

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

