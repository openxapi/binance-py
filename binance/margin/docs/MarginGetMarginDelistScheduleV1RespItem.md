# MarginGetMarginDelistScheduleV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cross_margin_assets** | **List[str]** |  | [optional] 
**delist_time** | **int** |  | [optional] 
**isolated_margin_symbols** | **List[str]** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_delist_schedule_v1_resp_item import MarginGetMarginDelistScheduleV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginDelistScheduleV1RespItem from a JSON string
margin_get_margin_delist_schedule_v1_resp_item_instance = MarginGetMarginDelistScheduleV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginDelistScheduleV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_delist_schedule_v1_resp_item_dict = margin_get_margin_delist_schedule_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginDelistScheduleV1RespItem from a dict
margin_get_margin_delist_schedule_v1_resp_item_from_dict = MarginGetMarginDelistScheduleV1RespItem.from_dict(margin_get_margin_delist_schedule_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


