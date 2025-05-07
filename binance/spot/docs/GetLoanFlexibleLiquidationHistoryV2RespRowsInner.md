# GetLoanFlexibleLiquidationHistoryV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_coin** | **str** |  | [optional] 
**liquidation_collateral_amount** | **str** |  | [optional] 
**liquidation_debt** | **str** |  | [optional] 
**liquidation_fee** | **str** |  | [optional] 
**liquidation_starting_price** | **str** |  | [optional] 
**liquidation_starting_time** | **int** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**return_collateral_amount** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_liquidation_history_v2_resp_rows_inner import GetLoanFlexibleLiquidationHistoryV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleLiquidationHistoryV2RespRowsInner from a JSON string
get_loan_flexible_liquidation_history_v2_resp_rows_inner_instance = GetLoanFlexibleLiquidationHistoryV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleLiquidationHistoryV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_liquidation_history_v2_resp_rows_inner_dict = get_loan_flexible_liquidation_history_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleLiquidationHistoryV2RespRowsInner from a dict
get_loan_flexible_liquidation_history_v2_resp_rows_inner_from_dict = GetLoanFlexibleLiquidationHistoryV2RespRowsInner.from_dict(get_loan_flexible_liquidation_history_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


