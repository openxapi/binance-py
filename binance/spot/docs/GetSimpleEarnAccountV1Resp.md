# GetSimpleEarnAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount_in_btc** | **str** |  | [optional] 
**total_amount_in_usdt** | **str** |  | [optional] 
**total_flexible_amount_in_btc** | **str** |  | [optional] 
**total_flexible_amount_in_usdt** | **str** |  | [optional] 
**total_locked_in_btc** | **str** |  | [optional] 
**total_locked_in_usdt** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_account_v1_resp import GetSimpleEarnAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnAccountV1Resp from a JSON string
get_simple_earn_account_v1_resp_instance = GetSimpleEarnAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnAccountV1Resp.to_json())

# convert the object into a dict
get_simple_earn_account_v1_resp_dict = get_simple_earn_account_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnAccountV1Resp from a dict
get_simple_earn_account_v1_resp_from_dict = GetSimpleEarnAccountV1Resp.from_dict(get_simple_earn_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


