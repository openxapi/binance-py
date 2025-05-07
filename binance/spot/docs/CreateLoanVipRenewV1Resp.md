# CreateLoanVipRenewV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_account_id** | **str** |  | [optional] 
**collateral_coin** | **str** |  | [optional] 
**loan_account_id** | **str** |  | [optional] 
**loan_amount** | **str** |  | [optional] 
**loan_coin** | **str** |  | [optional] 
**loan_term** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_loan_vip_renew_v1_resp import CreateLoanVipRenewV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoanVipRenewV1Resp from a JSON string
create_loan_vip_renew_v1_resp_instance = CreateLoanVipRenewV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLoanVipRenewV1Resp.to_json())

# convert the object into a dict
create_loan_vip_renew_v1_resp_dict = create_loan_vip_renew_v1_resp_instance.to_dict()
# create an instance of CreateLoanVipRenewV1Resp from a dict
create_loan_vip_renew_v1_resp_from_dict = CreateLoanVipRenewV1Resp.from_dict(create_loan_vip_renew_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


