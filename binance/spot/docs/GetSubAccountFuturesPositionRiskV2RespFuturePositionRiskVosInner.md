# GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_price** | **str** |  | [optional] 
**leverage** | **str** |  | [optional] 
**liquidation_price** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**max_notional** | **str** |  | [optional] 
**position_amount** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner import GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner from a JSON string
get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner_instance = GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner.to_json())

# convert the object into a dict
get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner_dict = get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner_instance.to_dict()
# create an instance of GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner from a dict
get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner_from_dict = GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner.from_dict(get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


