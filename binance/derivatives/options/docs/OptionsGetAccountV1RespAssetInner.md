# OptionsGetAccountV1RespAssetInner


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
from binance.derivatives.options.models.options_get_account_v1_resp_asset_inner import OptionsGetAccountV1RespAssetInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetAccountV1RespAssetInner from a JSON string
options_get_account_v1_resp_asset_inner_instance = OptionsGetAccountV1RespAssetInner.from_json(json)
# print the JSON string representation of the object
print(OptionsGetAccountV1RespAssetInner.to_json())

# convert the object into a dict
options_get_account_v1_resp_asset_inner_dict = options_get_account_v1_resp_asset_inner_instance.to_dict()
# create an instance of OptionsGetAccountV1RespAssetInner from a dict
options_get_account_v1_resp_asset_inner_from_dict = OptionsGetAccountV1RespAssetInner.from_dict(options_get_account_v1_resp_asset_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


