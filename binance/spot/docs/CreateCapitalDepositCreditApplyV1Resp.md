# CreateCapitalDepositCreditApplyV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_capital_deposit_credit_apply_v1_resp import CreateCapitalDepositCreditApplyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCapitalDepositCreditApplyV1Resp from a JSON string
create_capital_deposit_credit_apply_v1_resp_instance = CreateCapitalDepositCreditApplyV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateCapitalDepositCreditApplyV1Resp.to_json())

# convert the object into a dict
create_capital_deposit_credit_apply_v1_resp_dict = create_capital_deposit_credit_apply_v1_resp_instance.to_dict()
# create an instance of CreateCapitalDepositCreditApplyV1Resp from a dict
create_capital_deposit_credit_apply_v1_resp_from_dict = CreateCapitalDepositCreditApplyV1Resp.from_dict(create_capital_deposit_credit_apply_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


