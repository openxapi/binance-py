# GetLoanVipOngoingOrdersV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_account_id** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**current_ltv** | **str** |  | [optional] 
**expiration_time** | **int** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_date** | **str** |  | [optional] 
**loan_term** | **str** |  | [optional] 
**locked_collateral_value** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**residual_interest** | **str** |  | [optional] 
**total_collateral_value_after_haircut** | **str** |  | [optional] 
**total_debt** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_ongoing_orders_v1_resp_rows_inner import GetLoanVipOngoingOrdersV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipOngoingOrdersV1RespRowsInner from a JSON string
get_loan_vip_ongoing_orders_v1_resp_rows_inner_instance = GetLoanVipOngoingOrdersV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipOngoingOrdersV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_ongoing_orders_v1_resp_rows_inner_dict = get_loan_vip_ongoing_orders_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipOngoingOrdersV1RespRowsInner from a dict
get_loan_vip_ongoing_orders_v1_resp_rows_inner_from_dict = GetLoanVipOngoingOrdersV1RespRowsInner.from_dict(get_loan_vip_ongoing_orders_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


