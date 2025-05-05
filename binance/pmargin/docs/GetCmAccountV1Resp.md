# GetCmAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetCmAccountV1RespAssetsInner]**](GetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[GetCmAccountV1RespPositionsInner]**](GetCmAccountV1RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_account_v1_resp import GetCmAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmAccountV1Resp from a JSON string
get_cm_account_v1_resp_instance = GetCmAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetCmAccountV1Resp.to_json())

# convert the object into a dict
get_cm_account_v1_resp_dict = get_cm_account_v1_resp_instance.to_dict()
# create an instance of GetCmAccountV1Resp from a dict
get_cm_account_v1_resp_from_dict = GetCmAccountV1Resp.from_dict(get_cm_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


