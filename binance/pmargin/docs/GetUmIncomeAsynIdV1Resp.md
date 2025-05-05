# GetUmIncomeAsynIdV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** |  | [optional] 
**expiration_timestamp** | **int** |  | [optional] 
**is_expired** | **object** |  | [optional] 
**notified** | **bool** |  | [optional] 
**s3_link** | **object** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_income_asyn_id_v1_resp import GetUmIncomeAsynIdV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmIncomeAsynIdV1Resp from a JSON string
get_um_income_asyn_id_v1_resp_instance = GetUmIncomeAsynIdV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmIncomeAsynIdV1Resp.to_json())

# convert the object into a dict
get_um_income_asyn_id_v1_resp_dict = get_um_income_asyn_id_v1_resp_instance.to_dict()
# create an instance of GetUmIncomeAsynIdV1Resp from a dict
get_um_income_asyn_id_v1_resp_from_dict = GetUmIncomeAsynIdV1Resp.from_dict(get_um_income_asyn_id_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


