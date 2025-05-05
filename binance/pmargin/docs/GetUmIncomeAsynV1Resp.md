# GetUmIncomeAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_income_asyn_v1_resp import GetUmIncomeAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmIncomeAsynV1Resp from a JSON string
get_um_income_asyn_v1_resp_instance = GetUmIncomeAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmIncomeAsynV1Resp.to_json())

# convert the object into a dict
get_um_income_asyn_v1_resp_dict = get_um_income_asyn_v1_resp_instance.to_dict()
# create an instance of GetUmIncomeAsynV1Resp from a dict
get_um_income_asyn_v1_resp_from_dict = GetUmIncomeAsynV1Resp.from_dict(get_um_income_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


