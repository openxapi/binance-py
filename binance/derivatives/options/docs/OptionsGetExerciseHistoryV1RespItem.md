# OptionsGetExerciseHistoryV1RespItem


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
from binance.derivatives.options.models.options_get_exercise_history_v1_resp_item import OptionsGetExerciseHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExerciseHistoryV1RespItem from a JSON string
options_get_exercise_history_v1_resp_item_instance = OptionsGetExerciseHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExerciseHistoryV1RespItem.to_json())

# convert the object into a dict
options_get_exercise_history_v1_resp_item_dict = options_get_exercise_history_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetExerciseHistoryV1RespItem from a dict
options_get_exercise_history_v1_resp_item_from_dict = OptionsGetExerciseHistoryV1RespItem.from_dict(options_get_exercise_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


