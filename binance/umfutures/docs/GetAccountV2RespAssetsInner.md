# GetAccountV2RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**available_balance** | **str** |  | [optional] 
**cross_un_pnl** | **str** |  | [optional] 
**cross_wallet_balance** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**margin_available** | **bool** |  | [optional] 
**margin_balance** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_account_v2_resp_assets_inner import GetAccountV2RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV2RespAssetsInner from a JSON string
get_account_v2_resp_assets_inner_instance = GetAccountV2RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountV2RespAssetsInner.to_json())

# convert the object into a dict
get_account_v2_resp_assets_inner_dict = get_account_v2_resp_assets_inner_instance.to_dict()
# create an instance of GetAccountV2RespAssetsInner from a dict
get_account_v2_resp_assets_inner_from_dict = GetAccountV2RespAssetsInner.from_dict(get_account_v2_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


