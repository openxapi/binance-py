# GetApiReferralIfNewUserV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker_id** | **str** |  | [optional] 
**if_new_user** | **bool** |  | [optional] 
**rebate_working** | **bool** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_api_referral_if_new_user_v1_resp import GetApiReferralIfNewUserV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralIfNewUserV1Resp from a JSON string
get_api_referral_if_new_user_v1_resp_instance = GetApiReferralIfNewUserV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralIfNewUserV1Resp.to_json())

# convert the object into a dict
get_api_referral_if_new_user_v1_resp_dict = get_api_referral_if_new_user_v1_resp_instance.to_dict()
# create an instance of GetApiReferralIfNewUserV1Resp from a dict
get_api_referral_if_new_user_v1_resp_from_dict = GetApiReferralIfNewUserV1Resp.from_dict(get_api_referral_if_new_user_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


