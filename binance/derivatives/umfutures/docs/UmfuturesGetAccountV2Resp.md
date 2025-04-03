# UmfuturesGetAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[UmfuturesGetAccountV2RespAssetsInner]**](UmfuturesGetAccountV2RespAssetsInner.md) |  | [optional] 
**available_balance** | **str** |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**fee_burn** | **bool** |  | [optional] 
**fee_tier** | **int** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**multi_assets_margin** | **bool** |  | [optional] 
**positions** | [**List[UmfuturesGetAccountV2RespPositionsInner]**](UmfuturesGetAccountV2RespPositionsInner.md) |  | [optional] 
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
from binance.derivatives.umfutures.models.umfutures_get_account_v2_resp import UmfuturesGetAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAccountV2Resp from a JSON string
umfutures_get_account_v2_resp_instance = UmfuturesGetAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAccountV2Resp.to_json())

# convert the object into a dict
umfutures_get_account_v2_resp_dict = umfutures_get_account_v2_resp_instance.to_dict()
# create an instance of UmfuturesGetAccountV2Resp from a dict
umfutures_get_account_v2_resp_from_dict = UmfuturesGetAccountV2Resp.from_dict(umfutures_get_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


