# GetSubAccountAssetsV4Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[GetSubAccountAssetsV4RespBalancesInner]**](GetSubAccountAssetsV4RespBalancesInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_assets_v4_resp import GetSubAccountAssetsV4Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountAssetsV4Resp from a JSON string
get_sub_account_assets_v4_resp_instance = GetSubAccountAssetsV4Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountAssetsV4Resp.to_json())

# convert the object into a dict
get_sub_account_assets_v4_resp_dict = get_sub_account_assets_v4_resp_instance.to_dict()
# create an instance of GetSubAccountAssetsV4Resp from a dict
get_sub_account_assets_v4_resp_from_dict = GetSubAccountAssetsV4Resp.from_dict(get_sub_account_assets_v4_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


