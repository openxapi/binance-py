# GetMiningPaymentOtherV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**GetMiningPaymentOtherV1RespData**](GetMiningPaymentOtherV1RespData.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_payment_other_v1_resp import GetMiningPaymentOtherV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningPaymentOtherV1Resp from a JSON string
get_mining_payment_other_v1_resp_instance = GetMiningPaymentOtherV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMiningPaymentOtherV1Resp.to_json())

# convert the object into a dict
get_mining_payment_other_v1_resp_dict = get_mining_payment_other_v1_resp_instance.to_dict()
# create an instance of GetMiningPaymentOtherV1Resp from a dict
get_mining_payment_other_v1_resp_from_dict = GetMiningPaymentOtherV1Resp.from_dict(get_mining_payment_other_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


