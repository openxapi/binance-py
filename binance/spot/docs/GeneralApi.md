# binance.spot.GeneralApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spot_get_exchange_info_v3**](GeneralApi.md#spot_get_exchange_info_v3) | **GET** /api/v3/exchangeInfo | Exchange information
[**spot_get_ping_v3**](GeneralApi.md#spot_get_ping_v3) | **GET** /api/v3/ping | Test connectivity
[**spot_get_time_v3**](GeneralApi.md#spot_get_time_v3) | **GET** /api/v3/time | Check server time


# **spot_get_exchange_info_v3**
> SpotGetExchangeInfoV3Resp spot_get_exchange_info_v3(symbol=symbol, symbols=symbols, permissions=permissions, show_permission_sets=show_permission_sets, symbol_status=symbol_status)

Exchange information

Current exchange trading rules and symbol information

### Example


```python
import binance.spot
from binance.spot.models.spot_get_exchange_info_v3_resp import SpotGetExchangeInfoV3Resp
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
    api_instance = binance.spot.GeneralApi(api_client)
    symbol = '' # str | Example: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC</a>&#34; (optional) (default to '')
    symbols = ['symbols_example'] # List[str] | Examples: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D</a>&#34; <br/> or <br/> curl -g -X  GET &#39;<a href=\"https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BTCUSDT%22,%22BNBBTC\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?symbols=[&#34;BTCUSDT&#34;,&#34;BNBBTC</a>&#34;]&#39; (optional)
    permissions = '' # str | Examples: curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT</a>&#34; <br/> or <br/> curl -X GET &#34;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D</a>&#34; <br/> or <br/> curl -g -X GET &#39;<a href=\"https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22,%22LEVERAGED\" target=\"_blank\" rel=\"noopener noreferrer\">https://api.binance.com/api/v3/exchangeInfo?permissions=[&#34;MARGIN&#34;,&#34;LEVERAGED</a>&#34;]&#39; (optional) (default to '')
    show_permission_sets = True # bool | Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true` (optional)
    symbol_status =  # str | Filters symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK` <br/> Cannot be used in combination with `symbols` or `symbol`. (optional) (default to )

    try:
        # Exchange information
        api_response = api_instance.spot_get_exchange_info_v3(symbol=symbol, symbols=symbols, permissions=permissions, show_permission_sets=show_permission_sets, symbol_status=symbol_status)
        print("The response of GeneralApi->spot_get_exchange_info_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->spot_get_exchange_info_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Example: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbol&#x3D;BNBBTC\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbol&#x3D;BNBBTC&lt;/a&gt;&amp;#34; | [optional] [default to &#39;&#39;]
 **symbols** | [**List[str]**](str.md)| Examples: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BNBBTC%22,%22BTCUSDT%22%5D\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BNBBTC%22,%22BTCUSDT%22%5D&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -g -X  GET &amp;#39;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;%5B%22BTCUSDT%22,%22BNBBTC\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?symbols&#x3D;[&amp;#34;BTCUSDT&amp;#34;,&amp;#34;BNBBTC&lt;/a&gt;&amp;#34;]&amp;#39; | [optional] 
 **permissions** | **str**| Examples: curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;SPOT\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;SPOT&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -X GET &amp;#34;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22%2C%22LEVERAGED%22%5D\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22%2C%22LEVERAGED%22%5D&lt;/a&gt;&amp;#34; &lt;br/&gt; or &lt;br/&gt; curl -g -X GET &amp;#39;&lt;a href&#x3D;\&quot;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;%5B%22MARGIN%22,%22LEVERAGED\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://api.binance.com/api/v3/exchangeInfo?permissions&#x3D;[&amp;#34;MARGIN&amp;#34;,&amp;#34;LEVERAGED&lt;/a&gt;&amp;#34;]&amp;#39; | [optional] [default to &#39;&#39;]
 **show_permission_sets** | **bool**| Controls whether the content of the &#x60;permissionSets&#x60; field is populated or not. Defaults to &#x60;true&#x60; | [optional] 
 **symbol_status** | **str**| Filters symbols that have this &#x60;tradingStatus&#x60;. Valid values: &#x60;TRADING&#x60;, &#x60;HALT&#x60;, &#x60;BREAK&#x60; &lt;br/&gt; Cannot be used in combination with &#x60;symbols&#x60; or &#x60;symbol&#x60;. | [optional] [default to ]

### Return type

[**SpotGetExchangeInfoV3Resp**](SpotGetExchangeInfoV3Resp.md)

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

# **spot_get_ping_v3**
> object spot_get_ping_v3()

Test connectivity

Test connectivity to the Rest API.

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
    api_instance = binance.spot.GeneralApi(api_client)

    try:
        # Test connectivity
        api_response = api_instance.spot_get_ping_v3()
        print("The response of GeneralApi->spot_get_ping_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->spot_get_ping_v3: %s\n" % e)
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

# **spot_get_time_v3**
> SpotGetTimeV3Resp spot_get_time_v3()

Check server time

Test connectivity to the Rest API and get the current server time.

### Example


```python
import binance.spot
from binance.spot.models.spot_get_time_v3_resp import SpotGetTimeV3Resp
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
    api_instance = binance.spot.GeneralApi(api_client)

    try:
        # Check server time
        api_response = api_instance.spot_get_time_v3()
        print("The response of GeneralApi->spot_get_time_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->spot_get_time_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpotGetTimeV3Resp**](SpotGetTimeV3Resp.md)

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

