# SubaccountGetManagedSubaccountDepositAddressV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_deposit_address_v1_resp import SubaccountGetManagedSubaccountDepositAddressV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountDepositAddressV1Resp from a JSON string
subaccount_get_managed_subaccount_deposit_address_v1_resp_instance = SubaccountGetManagedSubaccountDepositAddressV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountDepositAddressV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_deposit_address_v1_resp_dict = subaccount_get_managed_subaccount_deposit_address_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountDepositAddressV1Resp from a dict
subaccount_get_managed_subaccount_deposit_address_v1_resp_from_dict = SubaccountGetManagedSubaccountDepositAddressV1Resp.from_dict(subaccount_get_managed_subaccount_deposit_address_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


