# GetPayTransactionsV1RespDataInnerReceiverInfoExtend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** |  | [optional] 
**digital_wallet_id** | **str** |  | [optional] 
**institution_name** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp_data_inner_receiver_info_extend import GetPayTransactionsV1RespDataInnerReceiverInfoExtend

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1RespDataInnerReceiverInfoExtend from a JSON string
get_pay_transactions_v1_resp_data_inner_receiver_info_extend_instance = GetPayTransactionsV1RespDataInnerReceiverInfoExtend.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1RespDataInnerReceiverInfoExtend.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_data_inner_receiver_info_extend_dict = get_pay_transactions_v1_resp_data_inner_receiver_info_extend_instance.to_dict()
# create an instance of GetPayTransactionsV1RespDataInnerReceiverInfoExtend from a dict
get_pay_transactions_v1_resp_data_inner_receiver_info_extend_from_dict = GetPayTransactionsV1RespDataInnerReceiverInfoExtend.from_dict(get_pay_transactions_v1_resp_data_inner_receiver_info_extend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


