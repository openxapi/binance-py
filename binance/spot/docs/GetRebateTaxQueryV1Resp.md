# GetRebateTaxQueryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**GetRebateTaxQueryV1RespData**](GetRebateTaxQueryV1RespData.md) |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_rebate_tax_query_v1_resp import GetRebateTaxQueryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetRebateTaxQueryV1Resp from a JSON string
get_rebate_tax_query_v1_resp_instance = GetRebateTaxQueryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetRebateTaxQueryV1Resp.to_json())

# convert the object into a dict
get_rebate_tax_query_v1_resp_dict = get_rebate_tax_query_v1_resp_instance.to_dict()
# create an instance of GetRebateTaxQueryV1Resp from a dict
get_rebate_tax_query_v1_resp_from_dict = GetRebateTaxQueryV1Resp.from_dict(get_rebate_tax_query_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


