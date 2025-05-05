# GetRateLimitOrderV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_rate_limit_order_v3_resp_item import GetRateLimitOrderV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimitOrderV3RespItem from a JSON string
get_rate_limit_order_v3_resp_item_instance = GetRateLimitOrderV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetRateLimitOrderV3RespItem.to_json())

# convert the object into a dict
get_rate_limit_order_v3_resp_item_dict = get_rate_limit_order_v3_resp_item_instance.to_dict()
# create an instance of GetRateLimitOrderV3RespItem from a dict
get_rate_limit_order_v3_resp_item_from_dict = GetRateLimitOrderV3RespItem.from_dict(get_rate_limit_order_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


