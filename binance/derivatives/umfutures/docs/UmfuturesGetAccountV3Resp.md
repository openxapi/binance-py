# UmfuturesGetAccountV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[UmfuturesGetAccountV3RespAssetsInner]**](UmfuturesGetAccountV3RespAssetsInner.md) |  | [optional] 
**available_balance** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**positions** | [**List[UmfuturesGetAccountV3RespPositionsInner]**](UmfuturesGetAccountV3RespPositionsInner.md) |  | [optional] 
**total_cross_un_pnl** | **str** |  | [optional] 
**total_cross_wallet_balance** | **str** |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maint_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp import UmfuturesGetAccountV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAccountV3Resp from a JSON string
umfutures_get_account_v3_resp_instance = UmfuturesGetAccountV3Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAccountV3Resp.to_json())

# convert the object into a dict
umfutures_get_account_v3_resp_dict = umfutures_get_account_v3_resp_instance.to_dict()
# create an instance of UmfuturesGetAccountV3Resp from a dict
umfutures_get_account_v3_resp_from_dict = UmfuturesGetAccountV3Resp.from_dict(umfutures_get_account_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


