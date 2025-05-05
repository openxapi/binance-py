# GetPositionMarginHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_position_margin_history_v1_resp_item import GetPositionMarginHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPositionMarginHistoryV1RespItem from a JSON string
get_position_margin_history_v1_resp_item_instance = GetPositionMarginHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPositionMarginHistoryV1RespItem.to_json())

# convert the object into a dict
get_position_margin_history_v1_resp_item_dict = get_position_margin_history_v1_resp_item_instance.to_dict()
# create an instance of GetPositionMarginHistoryV1RespItem from a dict
get_position_margin_history_v1_resp_item_from_dict = GetPositionMarginHistoryV1RespItem.from_dict(get_position_margin_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


