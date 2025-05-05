# GetBrokerSubAccountApiV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**futures_trade** | **bool** |  | [optional] 
**margin_trade** | **bool** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_api_v1_resp_item import GetBrokerSubAccountApiV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountApiV1RespItem from a JSON string
get_broker_sub_account_api_v1_resp_item_instance = GetBrokerSubAccountApiV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountApiV1RespItem.to_json())

# convert the object into a dict
get_broker_sub_account_api_v1_resp_item_dict = get_broker_sub_account_api_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerSubAccountApiV1RespItem from a dict
get_broker_sub_account_api_v1_resp_item_from_dict = GetBrokerSubAccountApiV1RespItem.from_dict(get_broker_sub_account_api_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


