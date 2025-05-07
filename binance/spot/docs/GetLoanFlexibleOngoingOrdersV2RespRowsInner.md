# GetLoanFlexibleOngoingOrdersV2RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_amount** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**current_ltv** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**total_debt** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_flexible_ongoing_orders_v2_resp_rows_inner import GetLoanFlexibleOngoingOrdersV2RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFlexibleOngoingOrdersV2RespRowsInner from a JSON string
get_loan_flexible_ongoing_orders_v2_resp_rows_inner_instance = GetLoanFlexibleOngoingOrdersV2RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanFlexibleOngoingOrdersV2RespRowsInner.to_json())

# convert the object into a dict
get_loan_flexible_ongoing_orders_v2_resp_rows_inner_dict = get_loan_flexible_ongoing_orders_v2_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanFlexibleOngoingOrdersV2RespRowsInner from a dict
get_loan_flexible_ongoing_orders_v2_resp_rows_inner_from_dict = GetLoanFlexibleOngoingOrdersV2RespRowsInner.from_dict(get_loan_flexible_ongoing_orders_v2_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


