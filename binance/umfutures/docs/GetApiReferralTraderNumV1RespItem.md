# GetApiReferralTraderNumV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_trader** | **str** |  | [optional] 
**old_trader** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_api_referral_trader_num_v1_resp_item import GetApiReferralTraderNumV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiReferralTraderNumV1RespItem from a JSON string
get_api_referral_trader_num_v1_resp_item_instance = GetApiReferralTraderNumV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetApiReferralTraderNumV1RespItem.to_json())

# convert the object into a dict
get_api_referral_trader_num_v1_resp_item_dict = get_api_referral_trader_num_v1_resp_item_instance.to_dict()
# create an instance of GetApiReferralTraderNumV1RespItem from a dict
get_api_referral_trader_num_v1_resp_item_from_dict = GetApiReferralTraderNumV1RespItem.from_dict(get_api_referral_trader_num_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


