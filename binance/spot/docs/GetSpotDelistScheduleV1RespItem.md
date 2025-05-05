# GetSpotDelistScheduleV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delist_time** | **int** |  | [optional] 
**symbols** | **List[str]** |  | [optional] 

## Example

```python
from binance.spot.models.get_spot_delist_schedule_v1_resp_item import GetSpotDelistScheduleV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpotDelistScheduleV1RespItem from a JSON string
get_spot_delist_schedule_v1_resp_item_instance = GetSpotDelistScheduleV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetSpotDelistScheduleV1RespItem.to_json())

# convert the object into a dict
get_spot_delist_schedule_v1_resp_item_dict = get_spot_delist_schedule_v1_resp_item_instance.to_dict()
# create an instance of GetSpotDelistScheduleV1RespItem from a dict
get_spot_delist_schedule_v1_resp_item_from_dict = GetSpotDelistScheduleV1RespItem.from_dict(get_spot_delist_schedule_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


