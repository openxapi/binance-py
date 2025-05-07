# GetPayTransactionsV1RespDataInnerReceiverInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**binance_id** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**extend** | [**GetPayTransactionsV1RespDataInnerReceiverInfoExtend**](GetPayTransactionsV1RespDataInnerReceiverInfoExtend.md) |  | [optional] 
**mobile_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp_data_inner_receiver_info import GetPayTransactionsV1RespDataInnerReceiverInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1RespDataInnerReceiverInfo from a JSON string
get_pay_transactions_v1_resp_data_inner_receiver_info_instance = GetPayTransactionsV1RespDataInnerReceiverInfo.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1RespDataInnerReceiverInfo.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_data_inner_receiver_info_dict = get_pay_transactions_v1_resp_data_inner_receiver_info_instance.to_dict()
# create an instance of GetPayTransactionsV1RespDataInnerReceiverInfo from a dict
get_pay_transactions_v1_resp_data_inner_receiver_info_from_dict = GetPayTransactionsV1RespDataInnerReceiverInfo.from_dict(get_pay_transactions_v1_resp_data_inner_receiver_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


