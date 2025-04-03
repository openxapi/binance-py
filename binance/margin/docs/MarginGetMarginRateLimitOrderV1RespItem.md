# MarginGetMarginRateLimitOrderV1RespItem


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
from binance.margin.models.margin_get_margin_rate_limit_order_v1_resp_item import MarginGetMarginRateLimitOrderV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginRateLimitOrderV1RespItem from a JSON string
margin_get_margin_rate_limit_order_v1_resp_item_instance = MarginGetMarginRateLimitOrderV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginRateLimitOrderV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_rate_limit_order_v1_resp_item_dict = margin_get_margin_rate_limit_order_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginRateLimitOrderV1RespItem from a dict
margin_get_margin_rate_limit_order_v1_resp_item_from_dict = MarginGetMarginRateLimitOrderV1RespItem.from_dict(margin_get_margin_rate_limit_order_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


