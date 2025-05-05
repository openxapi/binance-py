# GetUmAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetCmAccountV1RespAssetsInner]**](GetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[GetUmAccountV1RespPositionsInner]**](GetUmAccountV1RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_account_v1_resp import GetUmAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmAccountV1Resp from a JSON string
get_um_account_v1_resp_instance = GetUmAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmAccountV1Resp.to_json())

# convert the object into a dict
get_um_account_v1_resp_dict = get_um_account_v1_resp_instance.to_dict()
# create an instance of GetUmAccountV1Resp from a dict
get_um_account_v1_resp_from_dict = GetUmAccountV1Resp.from_dict(get_um_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


