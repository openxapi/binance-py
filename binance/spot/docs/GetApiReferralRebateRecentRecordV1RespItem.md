# GetApiReferralRebateRecentRecordV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_api_referral_rebate_recent_record_v1_resp_item import GetApiReferralRebateRecentRecordV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralRebateRecentRecordV1RespItem from a JSON string
get_api_referral_rebate_recent_record_v1_resp_item_instance = GetApiReferralRebateRecentRecordV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralRebateRecentRecordV1RespItem.to_json())

# convert the object into a dict
get_api_referral_rebate_recent_record_v1_resp_item_dict = get_api_referral_rebate_recent_record_v1_resp_item_instance.to_dict()
# create an instance of GetApiReferralRebateRecentRecordV1RespItem from a dict
get_api_referral_rebate_recent_record_v1_resp_item_from_dict = GetApiReferralRebateRecentRecordV1RespItem.from_dict(get_api_referral_rebate_recent_record_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


