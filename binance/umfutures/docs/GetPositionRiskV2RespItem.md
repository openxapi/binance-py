# GetPositionRiskV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_even_price** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**is_auto_add_margin** | **str** |  | [optional] 
**isolated_margin** | **str** |  | [optional] 
**isolated_wallet** | **str** |  | [optional] 
**leverage** | **str** |  | [optional] 
**liquidation_price** | **str** |  | [optional] 
**margin_type** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**notional** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**un_realized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_position_risk_v2_resp_item import GetPositionRiskV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPositionRiskV2RespItem from a JSON string
get_position_risk_v2_resp_item_instance = GetPositionRiskV2RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPositionRiskV2RespItem.to_json())

# convert the object into a dict
get_position_risk_v2_resp_item_dict = get_position_risk_v2_resp_item_instance.to_dict()
# create an instance of GetPositionRiskV2RespItem from a dict
get_position_risk_v2_resp_item_from_dict = GetPositionRiskV2RespItem.from_dict(get_position_risk_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


