# WalletCreateCapitalDepositCreditApplyV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_create_capital_deposit_credit_apply_v1_resp import WalletCreateCapitalDepositCreditApplyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateCapitalDepositCreditApplyV1Resp from a JSON string
wallet_create_capital_deposit_credit_apply_v1_resp_instance = WalletCreateCapitalDepositCreditApplyV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletCreateCapitalDepositCreditApplyV1Resp.to_json())

# convert the object into a dict
wallet_create_capital_deposit_credit_apply_v1_resp_dict = wallet_create_capital_deposit_credit_apply_v1_resp_instance.to_dict()
# create an instance of WalletCreateCapitalDepositCreditApplyV1Resp from a dict
wallet_create_capital_deposit_credit_apply_v1_resp_from_dict = WalletCreateCapitalDepositCreditApplyV1Resp.from_dict(wallet_create_capital_deposit_credit_apply_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


