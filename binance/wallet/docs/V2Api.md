# binance.wallet.V2Api

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_get_localentity_withdraw_history_v2**](V2Api.md#wallet_get_localentity_withdraw_history_v2) | **GET** /sapi/v2/localentity/withdraw/history | Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)


# **wallet_get_localentity_withdraw_history_v2**
> List[WalletGetLocalentityWithdrawHistoryV2RespItem] wallet_get_localentity_withdraw_history_v2(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)

Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)

Fetch withdraw history for local entities that required travel rule.

### Example

* Api Key Authentication (ApiKey):

```python
import binance.wallet
from binance.wallet.models.wallet_get_localentity_withdraw_history_v2_resp_item import WalletGetLocalentityWithdrawHistoryV2RespItem
from binance.wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.binance.com
# See configuration.py for a list of all supported configuration parameters.
configuration = binance.wallet.Configuration(
    host = "https://api.binance.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
configuration = binance.wallet.Configuration(
    auth=binance.wallet.BinanceAuth(
        api_key=os.getenv("BINANCE_API_KEY"),
        # secret_key=os.getenv("BINANCE_SECRET_KEY"), # if you want to use HMAC auth
        private_key_path="/path/to/private_key.pem", # Automatically detects RSA/Ed25519 private keys
    ),
)

# Enter a context with an instance of the API client
with binance.wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = binance.wallet.V2Api(api_client)
    timestamp = 56 # int | 
    tr_id = '' # str | Comma(,) separated list of travel rule record Ids. (optional) (default to '')
    tx_id = '' # str | Comma(,) separated list of transaction Ids. (optional) (default to '')
    withdraw_order_id = '' # str | Withdraw ID defined by the client (i.e. client&#39;s internal withdrawID). (optional) (default to '')
    network = '' # str |  (optional) (default to '')
    coin = '' # str |  (optional) (default to '')
    travel_rule_status = 56 # int | 0:Completed,1:Pending,2:Failed (optional)
    offset = 0 # int | Default: 0 (optional) (default to 0)
    limit = 1000 # int | Default: 1000, Max: 1000 (optional) (default to 1000)
    start_time = 56 # int | Default: 90 days from current timestamp (optional)
    end_time = 56 # int | Default: present timestamp (optional)
    recv_window = 56 # int |  (optional)

    try:
        # Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)
        api_response = api_instance.wallet_get_localentity_withdraw_history_v2(timestamp, tr_id=tr_id, tx_id=tx_id, withdraw_order_id=withdraw_order_id, network=network, coin=coin, travel_rule_status=travel_rule_status, offset=offset, limit=limit, start_time=start_time, end_time=end_time, recv_window=recv_window)
        print("The response of V2Api->wallet_get_localentity_withdraw_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2Api->wallet_get_localentity_withdraw_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**|  | 
 **tr_id** | **str**| Comma(,) separated list of travel rule record Ids. | [optional] [default to &#39;&#39;]
 **tx_id** | **str**| Comma(,) separated list of transaction Ids. | [optional] [default to &#39;&#39;]
 **withdraw_order_id** | **str**| Withdraw ID defined by the client (i.e. client&amp;#39;s internal withdrawID). | [optional] [default to &#39;&#39;]
 **network** | **str**|  | [optional] [default to &#39;&#39;]
 **coin** | **str**|  | [optional] [default to &#39;&#39;]
 **travel_rule_status** | **int**| 0:Completed,1:Pending,2:Failed | [optional] 
 **offset** | **int**| Default: 0 | [optional] [default to 0]
 **limit** | **int**| Default: 1000, Max: 1000 | [optional] [default to 1000]
 **start_time** | **int**| Default: 90 days from current timestamp | [optional] 
 **end_time** | **int**| Default: present timestamp | [optional] 
 **recv_window** | **int**|  | [optional] 

### Return type

[**List[WalletGetLocalentityWithdrawHistoryV2RespItem]**](WalletGetLocalentityWithdrawHistoryV2RespItem.md)

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

