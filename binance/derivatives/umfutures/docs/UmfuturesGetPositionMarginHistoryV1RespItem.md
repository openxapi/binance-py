# UmfuturesGetPositionMarginHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**delta_type** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_position_margin_history_v1_resp_item import UmfuturesGetPositionMarginHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetPositionMarginHistoryV1RespItem from a JSON string
umfutures_get_position_margin_history_v1_resp_item_instance = UmfuturesGetPositionMarginHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetPositionMarginHistoryV1RespItem.to_json())

# convert the object into a dict
umfutures_get_position_margin_history_v1_resp_item_dict = umfutures_get_position_margin_history_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetPositionMarginHistoryV1RespItem from a dict
umfutures_get_position_margin_history_v1_resp_item_from_dict = UmfuturesGetPositionMarginHistoryV1RespItem.from_dict(umfutures_get_position_margin_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


