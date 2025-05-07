# GetMiningPaymentUidV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**GetMiningPaymentUidV1RespData**](GetMiningPaymentUidV1RespData.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_payment_uid_v1_resp import GetMiningPaymentUidV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPaymentUidV1Resp from a JSON string
get_mining_payment_uid_v1_resp_instance = GetMiningPaymentUidV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMiningPaymentUidV1Resp.to_json())

# convert the object into a dict
get_mining_payment_uid_v1_resp_dict = get_mining_payment_uid_v1_resp_instance.to_dict()
# create an instance of GetMiningPaymentUidV1Resp from a dict
get_mining_payment_uid_v1_resp_from_dict = GetMiningPaymentUidV1Resp.from_dict(get_mining_payment_uid_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


