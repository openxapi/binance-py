# GetMiningPaymentListV1RespDataAccountProfitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coin_name** | **str** |  | [optional] 
**day_hash_rate** | **int** |  | [optional] 
**hash_transfer** | **object** |  | [optional] 
**profit_amount** | **float** |  | [optional] 
**status** | **int** |  | [optional] 
**time** | **int** |  | [optional] 
**transfer_amount** | **object** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_payment_list_v1_resp_data_account_profits_inner import GetMiningPaymentListV1RespDataAccountProfitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPaymentListV1RespDataAccountProfitsInner from a JSON string
get_mining_payment_list_v1_resp_data_account_profits_inner_instance = GetMiningPaymentListV1RespDataAccountProfitsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningPaymentListV1RespDataAccountProfitsInner.to_json())

# convert the object into a dict
get_mining_payment_list_v1_resp_data_account_profits_inner_dict = get_mining_payment_list_v1_resp_data_account_profits_inner_instance.to_dict()
# create an instance of GetMiningPaymentListV1RespDataAccountProfitsInner from a dict
get_mining_payment_list_v1_resp_data_account_profits_inner_from_dict = GetMiningPaymentListV1RespDataAccountProfitsInner.from_dict(get_mining_payment_list_v1_resp_data_account_profits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


