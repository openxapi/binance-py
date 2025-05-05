# GetExerciseHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **int** |  | [optional] 
**real_strike_price** | **str** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**strike_result** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_exercise_history_v1_resp_item import GetExerciseHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetExerciseHistoryV1RespItem from a JSON string
get_exercise_history_v1_resp_item_instance = GetExerciseHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetExerciseHistoryV1RespItem.to_json())

# convert the object into a dict
get_exercise_history_v1_resp_item_dict = get_exercise_history_v1_resp_item_instance.to_dict()
# create an instance of GetExerciseHistoryV1RespItem from a dict
get_exercise_history_v1_resp_item_from_dict = GetExerciseHistoryV1RespItem.from_dict(get_exercise_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


