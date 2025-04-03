# PmarginGetCmPositionRiskV1RespItem


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
from binance.derivatives.pmargin.models.pmargin_get_cm_position_risk_v1_resp_item import PmarginGetCmPositionRiskV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmPositionRiskV1RespItem from a JSON string
pmargin_get_cm_position_risk_v1_resp_item_instance = PmarginGetCmPositionRiskV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmPositionRiskV1RespItem.to_json())

# convert the object into a dict
pmargin_get_cm_position_risk_v1_resp_item_dict = pmargin_get_cm_position_risk_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetCmPositionRiskV1RespItem from a dict
pmargin_get_cm_position_risk_v1_resp_item_from_dict = PmarginGetCmPositionRiskV1RespItem.from_dict(pmargin_get_cm_position_risk_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


