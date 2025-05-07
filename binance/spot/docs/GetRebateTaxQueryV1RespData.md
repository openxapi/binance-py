# GetRebateTaxQueryV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetRebateTaxQueryV1RespDataDataInner]**](GetRebateTaxQueryV1RespDataDataInner.md) |  | [optional] 
**page** | **int** |  | [optional] 
**total_page_num** | **int** |  | [optional] 
**total_records** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_rebate_tax_query_v1_resp_data import GetRebateTaxQueryV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRebateTaxQueryV1RespData from a JSON string
get_rebate_tax_query_v1_resp_data_instance = GetRebateTaxQueryV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetRebateTaxQueryV1RespData.to_json())

# convert the object into a dict
get_rebate_tax_query_v1_resp_data_dict = get_rebate_tax_query_v1_resp_data_instance.to_dict()
# create an instance of GetRebateTaxQueryV1RespData from a dict
get_rebate_tax_query_v1_resp_data_from_dict = GetRebateTaxQueryV1RespData.from_dict(get_rebate_tax_query_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


