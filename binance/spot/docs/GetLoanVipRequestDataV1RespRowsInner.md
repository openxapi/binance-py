# GetLoanVipRequestDataV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_account_id** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**loan_account_id** | **str** |  | [optional] 
**loan_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_date** | **str** |  | [optional] 
**loan_term** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_request_data_v1_resp_rows_inner import GetLoanVipRequestDataV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipRequestDataV1RespRowsInner from a JSON string
get_loan_vip_request_data_v1_resp_rows_inner_instance = GetLoanVipRequestDataV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipRequestDataV1RespRowsInner.to_json())

# convert the object into a dict
get_loan_vip_request_data_v1_resp_rows_inner_dict = get_loan_vip_request_data_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetLoanVipRequestDataV1RespRowsInner from a dict
get_loan_vip_request_data_v1_resp_rows_inner_from_dict = GetLoanVipRequestDataV1RespRowsInner.from_dict(get_loan_vip_request_data_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


