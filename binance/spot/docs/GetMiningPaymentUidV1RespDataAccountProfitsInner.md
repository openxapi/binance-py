# GetMiningPaymentUidV1RespDataAccountProfitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**coin_name** | **str** |  | [optional] 
**puid** | **int** |  | [optional] 
**sub_name** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_payment_uid_v1_resp_data_account_profits_inner import GetMiningPaymentUidV1RespDataAccountProfitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPaymentUidV1RespDataAccountProfitsInner from a JSON string
get_mining_payment_uid_v1_resp_data_account_profits_inner_instance = GetMiningPaymentUidV1RespDataAccountProfitsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningPaymentUidV1RespDataAccountProfitsInner.to_json())

# convert the object into a dict
get_mining_payment_uid_v1_resp_data_account_profits_inner_dict = get_mining_payment_uid_v1_resp_data_account_profits_inner_instance.to_dict()
# create an instance of GetMiningPaymentUidV1RespDataAccountProfitsInner from a dict
get_mining_payment_uid_v1_resp_data_account_profits_inner_from_dict = GetMiningPaymentUidV1RespDataAccountProfitsInner.from_dict(get_mining_payment_uid_v1_resp_data_account_profits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


