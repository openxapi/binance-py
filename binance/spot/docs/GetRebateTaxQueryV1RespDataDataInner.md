# GetRebateTaxQueryV1RespDataDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_rebate_tax_query_v1_resp_data_data_inner import GetRebateTaxQueryV1RespDataDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRebateTaxQueryV1RespDataDataInner from a JSON string
get_rebate_tax_query_v1_resp_data_data_inner_instance = GetRebateTaxQueryV1RespDataDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRebateTaxQueryV1RespDataDataInner.to_json())

# convert the object into a dict
get_rebate_tax_query_v1_resp_data_data_inner_dict = get_rebate_tax_query_v1_resp_data_data_inner_instance.to_dict()
# create an instance of GetRebateTaxQueryV1RespDataDataInner from a dict
get_rebate_tax_query_v1_resp_data_data_inner_from_dict = GetRebateTaxQueryV1RespDataDataInner.from_dict(get_rebate_tax_query_v1_resp_data_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


