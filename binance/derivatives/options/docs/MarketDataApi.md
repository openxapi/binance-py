# binance.derivatives.options.MarketDataApi

All URIs are relative to *https://eapi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**options_get_block_trades_v1**](MarketDataApi.md#options_get_block_trades_v1) | **GET** /eapi/v1/blockTrades | Recent Block Trades List
[**options_get_depth_v1**](MarketDataApi.md#options_get_depth_v1) | **GET** /eapi/v1/depth | Order Book
[**options_get_exchange_info_v1**](MarketDataApi.md#options_get_exchange_info_v1) | **GET** /eapi/v1/exchangeInfo | Exchange Information
[**options_get_exercise_history_v1**](MarketDataApi.md#options_get_exercise_history_v1) | **GET** /eapi/v1/exerciseHistory | Historical Exercise Records
[**options_get_historical_trades_v1**](MarketDataApi.md#options_get_historical_trades_v1) | **GET** /eapi/v1/historicalTrades | Old Trades Lookup (MARKET_DATA)
[**options_get_index_v1**](MarketDataApi.md#options_get_index_v1) | **GET** /eapi/v1/index | Symbol Price Ticker
[**options_get_klines_v1**](MarketDataApi.md#options_get_klines_v1) | **GET** /eapi/v1/klines | Kline/Candlestick Data
[**options_get_mark_v1**](MarketDataApi.md#options_get_mark_v1) | **GET** /eapi/v1/mark | Option Mark Price
[**options_get_open_interest_v1**](MarketDataApi.md#options_get_open_interest_v1) | **GET** /eapi/v1/openInterest | Open Interest
[**options_get_ping_v1**](MarketDataApi.md#options_get_ping_v1) | **GET** /eapi/v1/ping | Test Connectivity
[**options_get_ticker_v1**](MarketDataApi.md#options_get_ticker_v1) | **GET** /eapi/v1/ticker | 24hr Ticker Price Change Statistics
[**options_get_time_v1**](MarketDataApi.md#options_get_time_v1) | **GET** /eapi/v1/time | Check Server Time
[**options_get_trades_v1**](MarketDataApi.md#options_get_trades_v1) | **GET** /eapi/v1/trades | Recent Trades List


# **options_get_block_trades_v1**
> List[OptionsGetBlockTradesV1RespItem] options_get_block_trades_v1(symbol=symbol, limit=limit)

Recent Block Trades List

Get recent block trades

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_block_trades_v1_resp_item import OptionsGetBlockTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g. BTC-200730-9000-C (optional) (default to '')
    limit = 100 # int | Number of records; Default: 100 and Max: 500 (optional) (default to 100)

    try:
        # Recent Block Trades List
        api_response = api_instance.options_get_block_trades_v1(symbol=symbol, limit=limit)
        print("The response of MarketDataApi->options_get_block_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_block_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g. BTC-200730-9000-C | [optional] [default to &#39;&#39;]
 **limit** | **int**| Number of records; Default: 100 and Max: 500 | [optional] [default to 100]

### Return type

[**List[OptionsGetBlockTradesV1RespItem]**](OptionsGetBlockTradesV1RespItem.md)

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

# **options_get_depth_v1**
> OptionsGetDepthV1Resp options_get_depth_v1(symbol, limit=limit)

Order Book

Check orderbook depth on specific symbol

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_depth_v1_resp import OptionsGetDepthV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] (optional)

    try:
        # Order Book
        api_response = api_instance.options_get_depth_v1(symbol, limit=limit)
        print("The response of MarketDataApi->options_get_depth_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_depth_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] | [optional] 

### Return type

[**OptionsGetDepthV1Resp**](OptionsGetDepthV1Resp.md)

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

# **options_get_exchange_info_v1**
> OptionsGetExchangeInfoV1Resp options_get_exchange_info_v1()

Exchange Information

Current exchange trading rules and symbol information

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_exchange_info_v1_resp import OptionsGetExchangeInfoV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)

    try:
        # Exchange Information
        api_response = api_instance.options_get_exchange_info_v1()
        print("The response of MarketDataApi->options_get_exchange_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_exchange_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetExchangeInfoV1Resp**](OptionsGetExchangeInfoV1Resp.md)

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

# **options_get_exercise_history_v1**
> List[OptionsGetExerciseHistoryV1RespItem] options_get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)

Historical Exercise Records

Get historical exercise records.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_exercise_history_v1_resp_item import OptionsGetExerciseHistoryV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    underlying = '' # str | Underlying index like BTCUSDT (optional) (default to '')
    start_time = 56 # int | Start Time (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:100 Max:100 (optional)

    try:
        # Historical Exercise Records
        api_response = api_instance.options_get_exercise_history_v1(underlying=underlying, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->options_get_exercise_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_exercise_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying index like BTCUSDT | [optional] [default to &#39;&#39;]
 **start_time** | **int**| Start Time | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of records Default:100 Max:100 | [optional] 

### Return type

[**List[OptionsGetExerciseHistoryV1RespItem]**](OptionsGetExerciseHistoryV1RespItem.md)

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

# **options_get_historical_trades_v1**
> List[OptionsGetHistoricalTradesV1RespItem] options_get_historical_trades_v1(symbol, from_id=from_id, limit=limit)

Old Trades Lookup (MARKET_DATA)

Get older market historical trades.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_historical_trades_v1_resp_item import OptionsGetHistoricalTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    from_id = 56 # int | The UniqueId ID from which to return. The latest deal record is returned by default (optional)
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Old Trades Lookup (MARKET_DATA)
        api_response = api_instance.options_get_historical_trades_v1(symbol, from_id=from_id, limit=limit)
        print("The response of MarketDataApi->options_get_historical_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_historical_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **from_id** | **int**| The UniqueId ID from which to return. The latest deal record is returned by default | [optional] 
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[OptionsGetHistoricalTradesV1RespItem]**](OptionsGetHistoricalTradesV1RespItem.md)

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

# **options_get_index_v1**
> OptionsGetIndexV1Resp options_get_index_v1(underlying)

Symbol Price Ticker

Get spot index price for option underlying.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_index_v1_resp import OptionsGetIndexV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    underlying = '' # str | Spot pair（Option contract underlying asset, e.g BTCUSDT) (default to '')

    try:
        # Symbol Price Ticker
        api_response = api_instance.options_get_index_v1(underlying)
        print("The response of MarketDataApi->options_get_index_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_index_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Spot pair（Option contract underlying asset, e.g BTCUSDT) | [default to &#39;&#39;]

### Return type

[**OptionsGetIndexV1Resp**](OptionsGetIndexV1Resp.md)

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

# **options_get_klines_v1**
> List[OptionsGetKlinesV1RespItem] options_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for an option symbol.
Klines are uniquely identified by their open time.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_klines_v1_resp_item import OptionsGetKlinesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    interval = '' # str | Time interval (default to '')
    start_time = 56 # int | Start Time  1592317127349 (optional)
    end_time = 56 # int | End Time (optional)
    limit = 56 # int | Number of records Default:500 Max:1500 (optional)

    try:
        # Kline/Candlestick Data
        api_response = api_instance.options_get_klines_v1(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
        print("The response of MarketDataApi->options_get_klines_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_klines_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **interval** | **str**| Time interval | [default to &#39;&#39;]
 **start_time** | **int**| Start Time  1592317127349 | [optional] 
 **end_time** | **int**| End Time | [optional] 
 **limit** | **int**| Number of records Default:500 Max:1500 | [optional] 

### Return type

[**List[OptionsGetKlinesV1RespItem]**](OptionsGetKlinesV1RespItem.md)

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

# **options_get_mark_v1**
> List[OptionsGetMarkV1RespItem] options_get_mark_v1(symbol=symbol)

Option Mark Price

Option mark price and greek info.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_mark_v1_resp_item import OptionsGetMarkV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # Option Mark Price
        api_response = api_instance.options_get_mark_v1(symbol=symbol)
        print("The response of MarketDataApi->options_get_mark_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_mark_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[OptionsGetMarkV1RespItem]**](OptionsGetMarkV1RespItem.md)

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

# **options_get_open_interest_v1**
> List[OptionsGetOpenInterestV1RespItem] options_get_open_interest_v1(underlying_asset, expiration)

Open Interest

Get open interest for specific underlying asset on specific expiration date.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_open_interest_v1_resp_item import OptionsGetOpenInterestV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    underlying_asset = '' # str | underlying asset, e.g ETH/BTC (default to '')
    expiration = '' # str | expiration date, e.g 221225 (default to '')

    try:
        # Open Interest
        api_response = api_instance.options_get_open_interest_v1(underlying_asset, expiration)
        print("The response of MarketDataApi->options_get_open_interest_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_open_interest_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying_asset** | **str**| underlying asset, e.g ETH/BTC | [default to &#39;&#39;]
 **expiration** | **str**| expiration date, e.g 221225 | [default to &#39;&#39;]

### Return type

[**List[OptionsGetOpenInterestV1RespItem]**](OptionsGetOpenInterestV1RespItem.md)

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

# **options_get_ping_v1**
> object options_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.options_get_ping_v1()
        print("The response of MarketDataApi->options_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_ping_v1: %s\n" % e)
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

# **options_get_ticker_v1**
> List[OptionsGetTickerV1RespItem] options_get_ticker_v1(symbol=symbol)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_ticker_v1_resp_item import OptionsGetTickerV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (optional) (default to '')

    try:
        # 24hr Ticker Price Change Statistics
        api_response = api_instance.options_get_ticker_v1(symbol=symbol)
        print("The response of MarketDataApi->options_get_ticker_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_ticker_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [optional] [default to &#39;&#39;]

### Return type

[**List[OptionsGetTickerV1RespItem]**](OptionsGetTickerV1RespItem.md)

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

# **options_get_time_v1**
> OptionsGetTimeV1Resp options_get_time_v1()

Check Server Time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_time_v1_resp import OptionsGetTimeV1Resp
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)

    try:
        # Check Server Time
        api_response = api_instance.options_get_time_v1()
        print("The response of MarketDataApi->options_get_time_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_time_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsGetTimeV1Resp**](OptionsGetTimeV1Resp.md)

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

# **options_get_trades_v1**
> List[OptionsGetTradesV1RespItem] options_get_trades_v1(symbol, limit=limit)

Recent Trades List

Get recent market trades

### Example


```python
import binance.derivatives.options
from binance.derivatives.options.models.options_get_trades_v1_resp_item import OptionsGetTradesV1RespItem
from binance.derivatives.options.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eapi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.options.Configuration(
    host = "https://eapi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.options.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.options.MarketDataApi(api_client)
    symbol = '' # str | Option trading pair, e.g BTC-200730-9000-C (default to '')
    limit = 56 # int | Number of records Default:100 Max:500 (optional)

    try:
        # Recent Trades List
        api_response = api_instance.options_get_trades_v1(symbol, limit=limit)
        print("The response of MarketDataApi->options_get_trades_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->options_get_trades_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option trading pair, e.g BTC-200730-9000-C | [default to &#39;&#39;]
 **limit** | **int**| Number of records Default:100 Max:500 | [optional] 

### Return type

[**List[OptionsGetTradesV1RespItem]**](OptionsGetTradesV1RespItem.md)

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

