# GetCmPositionRiskV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_price** | **str** |  | [optional] 
**leverage** | **str** |  | [optional] 
**liquidation_price** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**notional_value** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**un_realized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_position_risk_v1_resp_item import GetCmPositionRiskV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmPositionRiskV1RespItem from a JSON string
get_cm_position_risk_v1_resp_item_instance = GetCmPositionRiskV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCmPositionRiskV1RespItem.to_json())

# convert the object into a dict
get_cm_position_risk_v1_resp_item_dict = get_cm_position_risk_v1_resp_item_instance.to_dict()
# create an instance of GetCmPositionRiskV1RespItem from a dict
get_cm_position_risk_v1_resp_item_from_dict = GetCmPositionRiskV1RespItem.from_dict(get_cm_position_risk_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


