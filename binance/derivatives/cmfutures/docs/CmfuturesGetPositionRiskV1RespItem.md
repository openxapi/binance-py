# CmfuturesGetPositionRiskV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_even_price** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**is_auto_add_margin** | **str** |  | [optional] 
**isolated_margin** | **str** |  | [optional] 
**leverage** | **str** |  | [optional] 
**liquidation_price** | **str** |  | [optional] 
**margin_type** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**un_realized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_position_risk_v1_resp_item import CmfuturesGetPositionRiskV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetPositionRiskV1RespItem from a JSON string
cmfutures_get_position_risk_v1_resp_item_instance = CmfuturesGetPositionRiskV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetPositionRiskV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_position_risk_v1_resp_item_dict = cmfutures_get_position_risk_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetPositionRiskV1RespItem from a dict
cmfutures_get_position_risk_v1_resp_item_from_dict = CmfuturesGetPositionRiskV1RespItem.from_dict(cmfutures_get_position_risk_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


