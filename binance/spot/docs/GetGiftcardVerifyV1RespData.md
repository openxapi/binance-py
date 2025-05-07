# GetGiftcardVerifyV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_giftcard_verify_v1_resp_data import GetGiftcardVerifyV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftcardVerifyV1RespData from a JSON string
get_giftcard_verify_v1_resp_data_instance = GetGiftcardVerifyV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetGiftcardVerifyV1RespData.to_json())

# convert the object into a dict
get_giftcard_verify_v1_resp_data_dict = get_giftcard_verify_v1_resp_data_instance.to_dict()
# create an instance of GetGiftcardVerifyV1RespData from a dict
get_giftcard_verify_v1_resp_data_from_dict = GetGiftcardVerifyV1RespData.from_dict(get_giftcard_verify_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


