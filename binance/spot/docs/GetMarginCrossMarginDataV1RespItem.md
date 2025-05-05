# GetMarginCrossMarginDataV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrow_limit** | **str** |  | [optional] 
**borrowable** | **bool** |  | [optional] 
**coin** | **str** |  | [optional] 
**daily_interest** | **str** |  | [optional] 
**marginable_pairs** | **List[str]** |  | [optional] 
**transfer_in** | **bool** |  | [optional] 
**vip_level** | **int** |  | [optional] 
**yearly_interest** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_cross_margin_data_v1_resp_item import GetMarginCrossMarginDataV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginCrossMarginDataV1RespItem from a JSON string
get_margin_cross_margin_data_v1_resp_item_instance = GetMarginCrossMarginDataV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginCrossMarginDataV1RespItem.to_json())

# convert the object into a dict
get_margin_cross_margin_data_v1_resp_item_dict = get_margin_cross_margin_data_v1_resp_item_instance.to_dict()
# create an instance of GetMarginCrossMarginDataV1RespItem from a dict
get_margin_cross_margin_data_v1_resp_item_from_dict = GetMarginCrossMarginDataV1RespItem.from_dict(get_margin_cross_margin_data_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


