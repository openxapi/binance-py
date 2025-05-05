# GetAccountV1RespAssetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**available** | **str** |  | [optional] 
**equity** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**margin_balance** | **str** |  | [optional] 
**unrealized_pnl** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_account_v1_resp_asset_inner import GetAccountV1RespAssetInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV1RespAssetInner from a JSON string
get_account_v1_resp_asset_inner_instance = GetAccountV1RespAssetInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountV1RespAssetInner.to_json())

# convert the object into a dict
get_account_v1_resp_asset_inner_dict = get_account_v1_resp_asset_inner_instance.to_dict()
# create an instance of GetAccountV1RespAssetInner from a dict
get_account_v1_resp_asset_inner_from_dict = GetAccountV1RespAssetInner.from_dict(get_account_v1_resp_asset_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


