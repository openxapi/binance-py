# OptionsGetIncomeAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_income_asyn_v1_resp import OptionsGetIncomeAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetIncomeAsynV1Resp from a JSON string
options_get_income_asyn_v1_resp_instance = OptionsGetIncomeAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetIncomeAsynV1Resp.to_json())

# convert the object into a dict
options_get_income_asyn_v1_resp_dict = options_get_income_asyn_v1_resp_instance.to_dict()
# create an instance of OptionsGetIncomeAsynV1Resp from a dict
options_get_income_asyn_v1_resp_from_dict = OptionsGetIncomeAsynV1Resp.from_dict(options_get_income_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


