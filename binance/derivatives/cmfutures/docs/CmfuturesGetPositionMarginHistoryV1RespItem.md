# CmfuturesGetPositionMarginHistoryV1RespItem


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
from binance.derivatives.cmfutures.models.cmfutures_get_position_margin_history_v1_resp_item import CmfuturesGetPositionMarginHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetPositionMarginHistoryV1RespItem from a JSON string
cmfutures_get_position_margin_history_v1_resp_item_instance = CmfuturesGetPositionMarginHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetPositionMarginHistoryV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_position_margin_history_v1_resp_item_dict = cmfutures_get_position_margin_history_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetPositionMarginHistoryV1RespItem from a dict
cmfutures_get_position_margin_history_v1_resp_item_from_dict = CmfuturesGetPositionMarginHistoryV1RespItem.from_dict(cmfutures_get_position_margin_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


