# GetIncomeAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_income_asyn_v1_resp import GetIncomeAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomeAsynV1Resp from a JSON string
get_income_asyn_v1_resp_instance = GetIncomeAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetIncomeAsynV1Resp.to_json())

# convert the object into a dict
get_income_asyn_v1_resp_dict = get_income_asyn_v1_resp_instance.to_dict()
# create an instance of GetIncomeAsynV1Resp from a dict
get_income_asyn_v1_resp_from_dict = GetIncomeAsynV1Resp.from_dict(get_income_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


