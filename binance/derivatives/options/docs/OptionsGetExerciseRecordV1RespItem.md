# OptionsGetExerciseRecordV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**create_date** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**exercise_price** | **str** |  | [optional] 
**fee** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**option_side** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price_scale** | **int** |  | [optional] 
**quantity** | **str** |  | [optional] 
**quantity_scale** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_exercise_record_v1_resp_item import OptionsGetExerciseRecordV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetExerciseRecordV1RespItem from a JSON string
options_get_exercise_record_v1_resp_item_instance = OptionsGetExerciseRecordV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetExerciseRecordV1RespItem.to_json())

# convert the object into a dict
options_get_exercise_record_v1_resp_item_dict = options_get_exercise_record_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetExerciseRecordV1RespItem from a dict
options_get_exercise_record_v1_resp_item_from_dict = OptionsGetExerciseRecordV1RespItem.from_dict(options_get_exercise_record_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


