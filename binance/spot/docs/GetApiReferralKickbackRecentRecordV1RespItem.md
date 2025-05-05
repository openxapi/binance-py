# GetApiReferralKickbackRecentRecordV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_api_referral_kickback_recent_record_v1_resp_item import GetApiReferralKickbackRecentRecordV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralKickbackRecentRecordV1RespItem from a JSON string
get_api_referral_kickback_recent_record_v1_resp_item_instance = GetApiReferralKickbackRecentRecordV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralKickbackRecentRecordV1RespItem.to_json())

# convert the object into a dict
get_api_referral_kickback_recent_record_v1_resp_item_dict = get_api_referral_kickback_recent_record_v1_resp_item_instance.to_dict()
# create an instance of GetApiReferralKickbackRecentRecordV1RespItem from a dict
get_api_referral_kickback_recent_record_v1_resp_item_from_dict = GetApiReferralKickbackRecentRecordV1RespItem.from_dict(get_api_referral_kickback_recent_record_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


