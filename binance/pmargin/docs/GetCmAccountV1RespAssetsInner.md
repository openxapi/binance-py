# GetCmAccountV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**cross_un_pnl** | **str** |  | [optional] 
**cross_wallet_balance** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_account_v1_resp_assets_inner import GetCmAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmAccountV1RespAssetsInner from a JSON string
get_cm_account_v1_resp_assets_inner_instance = GetCmAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(GetCmAccountV1RespAssetsInner.to_json())

# convert the object into a dict
get_cm_account_v1_resp_assets_inner_dict = get_cm_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of GetCmAccountV1RespAssetsInner from a dict
get_cm_account_v1_resp_assets_inner_from_dict = GetCmAccountV1RespAssetsInner.from_dict(get_cm_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


