# GetMarginDelistScheduleV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cross_margin_assets** | **List[str]** |  | [optional] 
**delist_time** | **int** |  | [optional] 
**isolated_margin_symbols** | **List[str]** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_delist_schedule_v1_resp_item import GetMarginDelistScheduleV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginDelistScheduleV1RespItem from a JSON string
get_margin_delist_schedule_v1_resp_item_instance = GetMarginDelistScheduleV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginDelistScheduleV1RespItem.to_json())

# convert the object into a dict
get_margin_delist_schedule_v1_resp_item_dict = get_margin_delist_schedule_v1_resp_item_instance.to_dict()
# create an instance of GetMarginDelistScheduleV1RespItem from a dict
get_margin_delist_schedule_v1_resp_item_from_dict = GetMarginDelistScheduleV1RespItem.from_dict(get_margin_delist_schedule_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


