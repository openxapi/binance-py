# GetSubAccountAssetsV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[GetSubAccountAssetsV3RespBalancesInner]**](GetSubAccountAssetsV3RespBalancesInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_assets_v3_resp import GetSubAccountAssetsV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountAssetsV3Resp from a JSON string
get_sub_account_assets_v3_resp_instance = GetSubAccountAssetsV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountAssetsV3Resp.to_json())

# convert the object into a dict
get_sub_account_assets_v3_resp_dict = get_sub_account_assets_v3_resp_instance.to_dict()
# create an instance of GetSubAccountAssetsV3Resp from a dict
get_sub_account_assets_v3_resp_from_dict = GetSubAccountAssetsV3Resp.from_dict(get_sub_account_assets_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


