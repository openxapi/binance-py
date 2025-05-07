# GetSimpleEarnLockedListV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**GetSimpleEarnLockedListV1RespRowsInnerDetail**](GetSimpleEarnLockedListV1RespRowsInnerDetail.md) |  | [optional] 
**project_id** | **str** |  | [optional] 
**quota** | [**GetSimpleEarnLockedListV1RespRowsInnerQuota**](GetSimpleEarnLockedListV1RespRowsInnerQuota.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_locked_list_v1_resp_rows_inner import GetSimpleEarnLockedListV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnLockedListV1RespRowsInner from a JSON string
get_simple_earn_locked_list_v1_resp_rows_inner_instance = GetSimpleEarnLockedListV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnLockedListV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_locked_list_v1_resp_rows_inner_dict = get_simple_earn_locked_list_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnLockedListV1RespRowsInner from a dict
get_simple_earn_locked_list_v1_resp_rows_inner_from_dict = GetSimpleEarnLockedListV1RespRowsInner.from_dict(get_simple_earn_locked_list_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


