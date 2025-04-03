# CmfuturesGetAccountV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**available_balance** | **str** |  | [optional] 
**cross_un_pnl** | **str** |  | [optional] 
**cross_wallet_balance** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**margin_balance** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp_assets_inner import CmfuturesGetAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetAccountV1RespAssetsInner from a JSON string
cmfutures_get_account_v1_resp_assets_inner_instance = CmfuturesGetAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetAccountV1RespAssetsInner.to_json())

# convert the object into a dict
cmfutures_get_account_v1_resp_assets_inner_dict = cmfutures_get_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of CmfuturesGetAccountV1RespAssetsInner from a dict
cmfutures_get_account_v1_resp_assets_inner_from_dict = CmfuturesGetAccountV1RespAssetsInner.from_dict(cmfutures_get_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


