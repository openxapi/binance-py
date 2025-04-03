# UmfuturesGetPositionRiskV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adl** | **int** |  | [optional] 
**ask_notional** | **str** |  | [optional] 
**bid_notional** | **str** |  | [optional] 
**break_even_price** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**isolated_margin** | **str** |  | [optional] 
**isolated_wallet** | **str** |  | [optional] 
**liquidation_price** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**margin_asset** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**notional** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**un_realized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_position_risk_v3_resp_item import UmfuturesGetPositionRiskV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetPositionRiskV3RespItem from a JSON string
umfutures_get_position_risk_v3_resp_item_instance = UmfuturesGetPositionRiskV3RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetPositionRiskV3RespItem.to_json())

# convert the object into a dict
umfutures_get_position_risk_v3_resp_item_dict = umfutures_get_position_risk_v3_resp_item_instance.to_dict()
# create an instance of UmfuturesGetPositionRiskV3RespItem from a dict
umfutures_get_position_risk_v3_resp_item_from_dict = UmfuturesGetPositionRiskV3RespItem.from_dict(umfutures_get_position_risk_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


