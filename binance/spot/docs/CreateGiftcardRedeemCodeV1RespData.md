# CreateGiftcardRedeemCodeV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**identity_no** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_giftcard_redeem_code_v1_resp_data import CreateGiftcardRedeemCodeV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGiftcardRedeemCodeV1RespData from a JSON string
create_giftcard_redeem_code_v1_resp_data_instance = CreateGiftcardRedeemCodeV1RespData.from_json(json)
# print the JSON string representation of the object
print(CreateGiftcardRedeemCodeV1RespData.to_json())

# convert the object into a dict
create_giftcard_redeem_code_v1_resp_data_dict = create_giftcard_redeem_code_v1_resp_data_instance.to_dict()
# create an instance of CreateGiftcardRedeemCodeV1RespData from a dict
create_giftcard_redeem_code_v1_resp_data_from_dict = CreateGiftcardRedeemCodeV1RespData.from_dict(create_giftcard_redeem_code_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


