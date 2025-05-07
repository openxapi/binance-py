# GetPayTransactionsV1RespDataInnerPayerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**binance_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp_data_inner_payer_info import GetPayTransactionsV1RespDataInnerPayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1RespDataInnerPayerInfo from a JSON string
get_pay_transactions_v1_resp_data_inner_payer_info_instance = GetPayTransactionsV1RespDataInnerPayerInfo.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1RespDataInnerPayerInfo.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_data_inner_payer_info_dict = get_pay_transactions_v1_resp_data_inner_payer_info_instance.to_dict()
# create an instance of GetPayTransactionsV1RespDataInnerPayerInfo from a dict
get_pay_transactions_v1_resp_data_inner_payer_info_from_dict = GetPayTransactionsV1RespDataInnerPayerInfo.from_dict(get_pay_transactions_v1_resp_data_inner_payer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


