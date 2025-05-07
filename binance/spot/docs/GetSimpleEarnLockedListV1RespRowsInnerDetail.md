# GetSimpleEarnLockedListV1RespRowsInnerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**boost_apr** | **str** |  | [optional] 
**boost_end_time** | **str** |  | [optional] 
**boost_reward_asset** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**extra_reward_apr** | **str** |  | [optional] 
**extra_reward_asset** | **str** |  | [optional] 
**is_sold_out** | **bool** |  | [optional] 
**renewable** | **bool** |  | [optional] 
**reward_asset** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription_start_time** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_list_v1_resp_rows_inner_detail import GetSimpleEarnLockedListV1RespRowsInnerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedListV1RespRowsInnerDetail from a JSON string
get_simple_earn_locked_list_v1_resp_rows_inner_detail_instance = GetSimpleEarnLockedListV1RespRowsInnerDetail.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedListV1RespRowsInnerDetail.to_json())

# convert the object into a dict
get_simple_earn_locked_list_v1_resp_rows_inner_detail_dict = get_simple_earn_locked_list_v1_resp_rows_inner_detail_instance.to_dict()
# create an instance of GetSimpleEarnLockedListV1RespRowsInnerDetail from a dict
get_simple_earn_locked_list_v1_resp_rows_inner_detail_from_dict = GetSimpleEarnLockedListV1RespRowsInnerDetail.from_dict(get_simple_earn_locked_list_v1_resp_rows_inner_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


