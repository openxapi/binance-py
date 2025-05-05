# GetUmAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetCmAccountV1RespAssetsInner]**](GetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[GetUmAccountV2RespPositionsInner]**](GetUmAccountV2RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_account_v2_resp import GetUmAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmAccountV2Resp from a JSON string
get_um_account_v2_resp_instance = GetUmAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmAccountV2Resp.to_json())

# convert the object into a dict
get_um_account_v2_resp_dict = get_um_account_v2_resp_instance.to_dict()
# create an instance of GetUmAccountV2Resp from a dict
get_um_account_v2_resp_from_dict = GetUmAccountV2Resp.from_dict(get_um_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


