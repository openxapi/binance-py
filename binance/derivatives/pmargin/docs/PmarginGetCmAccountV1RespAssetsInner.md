# PmarginGetCmAccountV1RespAssetsInner


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
from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_assets_inner import PmarginGetCmAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmAccountV1RespAssetsInner from a JSON string
pmargin_get_cm_account_v1_resp_assets_inner_instance = PmarginGetCmAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmAccountV1RespAssetsInner.to_json())

# convert the object into a dict
pmargin_get_cm_account_v1_resp_assets_inner_dict = pmargin_get_cm_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of PmarginGetCmAccountV1RespAssetsInner from a dict
pmargin_get_cm_account_v1_resp_assets_inner_from_dict = PmarginGetCmAccountV1RespAssetsInner.from_dict(pmargin_get_cm_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


