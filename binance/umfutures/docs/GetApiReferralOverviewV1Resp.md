# GetApiReferralOverviewV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker_id** | **str** |  | [optional] 
**new_trader_rebate_commission** | **str** |  | [optional] 
**old_trader_rebate_commission** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**total_rebate_vol** | **str** |  | [optional] 
**total_trade_user** | **int** |  | [optional] 
**total_trade_vol** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_api_referral_overview_v1_resp import GetApiReferralOverviewV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralOverviewV1Resp from a JSON string
get_api_referral_overview_v1_resp_instance = GetApiReferralOverviewV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralOverviewV1Resp.to_json())

# convert the object into a dict
get_api_referral_overview_v1_resp_dict = get_api_referral_overview_v1_resp_instance.to_dict()
# create an instance of GetApiReferralOverviewV1Resp from a dict
get_api_referral_overview_v1_resp_from_dict = GetApiReferralOverviewV1Resp.from_dict(get_api_referral_overview_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


