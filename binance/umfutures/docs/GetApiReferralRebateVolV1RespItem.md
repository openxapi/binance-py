# GetApiReferralRebateVolV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rebate_vol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_api_referral_rebate_vol_v1_resp_item import GetApiReferralRebateVolV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralRebateVolV1RespItem from a JSON string
get_api_referral_rebate_vol_v1_resp_item_instance = GetApiReferralRebateVolV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralRebateVolV1RespItem.to_json())

# convert the object into a dict
get_api_referral_rebate_vol_v1_resp_item_dict = get_api_referral_rebate_vol_v1_resp_item_instance.to_dict()
# create an instance of GetApiReferralRebateVolV1RespItem from a dict
get_api_referral_rebate_vol_v1_resp_item_from_dict = GetApiReferralRebateVolV1RespItem.from_dict(get_api_referral_rebate_vol_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


