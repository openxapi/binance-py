# GetBrokerSubAccountApiCommissionFuturesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission** | **int** |  | [optional] 
**sub_account_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_api_commission_futures_v1_resp_item import GetBrokerSubAccountApiCommissionFuturesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountApiCommissionFuturesV1RespItem from a JSON string
get_broker_sub_account_api_commission_futures_v1_resp_item_instance = GetBrokerSubAccountApiCommissionFuturesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountApiCommissionFuturesV1RespItem.to_json())

# convert the object into a dict
get_broker_sub_account_api_commission_futures_v1_resp_item_dict = get_broker_sub_account_api_commission_futures_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerSubAccountApiCommissionFuturesV1RespItem from a dict
get_broker_sub_account_api_commission_futures_v1_resp_item_from_dict = GetBrokerSubAccountApiCommissionFuturesV1RespItem.from_dict(get_broker_sub_account_api_commission_futures_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


