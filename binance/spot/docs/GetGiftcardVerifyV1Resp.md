# GetGiftcardVerifyV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**GetGiftcardVerifyV1RespData**](GetGiftcardVerifyV1RespData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_giftcard_verify_v1_resp import GetGiftcardVerifyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftcardVerifyV1Resp from a JSON string
get_giftcard_verify_v1_resp_instance = GetGiftcardVerifyV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetGiftcardVerifyV1Resp.to_json())

# convert the object into a dict
get_giftcard_verify_v1_resp_dict = get_giftcard_verify_v1_resp_instance.to_dict()
# create an instance of GetGiftcardVerifyV1Resp from a dict
get_giftcard_verify_v1_resp_from_dict = GetGiftcardVerifyV1Resp.from_dict(get_giftcard_verify_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


