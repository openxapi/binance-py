# GetPayTransactionsV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**funds_detail** | [**List[GetPayTransactionsV1RespDataInnerFundsDetailInner]**](GetPayTransactionsV1RespDataInnerFundsDetailInner.md) |  | [optional] 
**order_type** | **str** |  | [optional] 
**payer_info** | [**GetPayTransactionsV1RespDataInnerPayerInfo**](GetPayTransactionsV1RespDataInnerPayerInfo.md) |  | [optional] 
**receiver_info** | [**GetPayTransactionsV1RespDataInnerReceiverInfo**](GetPayTransactionsV1RespDataInnerReceiverInfo.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 
**wallet_type** | **int** |  | [optional] 
**wallet_types** | **List[int]** |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp_data_inner import GetPayTransactionsV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1RespDataInner from a JSON string
get_pay_transactions_v1_resp_data_inner_instance = GetPayTransactionsV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1RespDataInner.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_data_inner_dict = get_pay_transactions_v1_resp_data_inner_instance.to_dict()
# create an instance of GetPayTransactionsV1RespDataInner from a dict
get_pay_transactions_v1_resp_data_inner_from_dict = GetPayTransactionsV1RespDataInner.from_dict(get_pay_transactions_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


