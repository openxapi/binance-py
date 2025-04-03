# binance.derivatives.pmargin.MarketDataApi

All URIs are relative to *https://papi.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmargin_get_ping_v1**](MarketDataApi.md#pmargin_get_ping_v1) | **GET** /papi/v1/ping | Test Connectivity


# **pmargin_get_ping_v1**
> object pmargin_get_ping_v1()

Test Connectivity

Test connectivity to the Rest API.

### Example


```python
import binance.derivatives.pmargin
from binance.derivatives.pmargin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://papi.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.derivatives.pmargin.Configuration(
    host = "https://papi.binance.com"
)


# Enter a context with an instance of the API client
with binance.derivatives.pmargin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.derivatives.pmargin.MarketDataApi(api_client)

    try:
        # Test Connectivity
        api_response = api_instance.pmargin_get_ping_v1()
        print("The response of MarketDataApi->pmargin_get_ping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->pmargin_get_ping_v1: %s\n" % e)
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

