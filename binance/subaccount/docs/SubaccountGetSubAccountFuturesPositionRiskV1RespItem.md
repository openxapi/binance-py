# SubaccountGetSubAccountFuturesPositionRiskV1RespItem


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
from binance.subaccount.models.subaccount_get_sub_account_futures_position_risk_v1_resp_item import SubaccountGetSubAccountFuturesPositionRiskV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesPositionRiskV1RespItem from a JSON string
subaccount_get_sub_account_futures_position_risk_v1_resp_item_instance = SubaccountGetSubAccountFuturesPositionRiskV1RespItem.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesPositionRiskV1RespItem.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_position_risk_v1_resp_item_dict = subaccount_get_sub_account_futures_position_risk_v1_resp_item_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesPositionRiskV1RespItem from a dict
subaccount_get_sub_account_futures_position_risk_v1_resp_item_from_dict = SubaccountGetSubAccountFuturesPositionRiskV1RespItem.from_dict(subaccount_get_sub_account_futures_position_risk_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


