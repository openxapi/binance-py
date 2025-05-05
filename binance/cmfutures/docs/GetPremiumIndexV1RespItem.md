# GetPremiumIndexV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_settle_price** | **str** |  | [optional] 
**index_price** | **str** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**last_funding_rate** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**next_funding_time** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_premium_index_v1_resp_item import GetPremiumIndexV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPremiumIndexV1RespItem from a JSON string
get_premium_index_v1_resp_item_instance = GetPremiumIndexV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPremiumIndexV1RespItem.to_json())

# convert the object into a dict
get_premium_index_v1_resp_item_dict = get_premium_index_v1_resp_item_instance.to_dict()
# create an instance of GetPremiumIndexV1RespItem from a dict
get_premium_index_v1_resp_item_from_dict = GetPremiumIndexV1RespItem.from_dict(get_premium_index_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


