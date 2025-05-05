# GetAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetAccountV2RespAssetsInner]**](GetAccountV2RespAssetsInner.md) |  | [optional] 
**available_balance** | **str** |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**fee_burn** | **bool** |  | [optional] 
**fee_tier** | **int** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**multi_assets_margin** | **bool** |  | [optional] 
**positions** | [**List[GetAccountV2RespPositionsInner]**](GetAccountV2RespPositionsInner.md) |  | [optional] 
**total_cross_un_pnl** | **str** |  | [optional] 
**total_cross_wallet_balance** | **str** |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maint_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 
**trade_group_id** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_account_v2_resp import GetAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV2Resp from a JSON string
get_account_v2_resp_instance = GetAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountV2Resp.to_json())

# convert the object into a dict
get_account_v2_resp_dict = get_account_v2_resp_instance.to_dict()
# create an instance of GetAccountV2Resp from a dict
get_account_v2_resp_from_dict = GetAccountV2Resp.from_dict(get_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


