# GetMiningPaymentUidV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_profits** | [**List[GetMiningPaymentUidV1RespDataAccountProfitsInner]**](GetMiningPaymentUidV1RespDataAccountProfitsInner.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_num** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_payment_uid_v1_resp_data import GetMiningPaymentUidV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPaymentUidV1RespData from a JSON string
get_mining_payment_uid_v1_resp_data_instance = GetMiningPaymentUidV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetMiningPaymentUidV1RespData.to_json())

# convert the object into a dict
get_mining_payment_uid_v1_resp_data_dict = get_mining_payment_uid_v1_resp_data_instance.to_dict()
# create an instance of GetMiningPaymentUidV1RespData from a dict
get_mining_payment_uid_v1_resp_data_from_dict = GetMiningPaymentUidV1RespData.from_dict(get_mining_payment_uid_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


