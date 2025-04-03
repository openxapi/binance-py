# PmarginGetRateLimitOrderV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_rate_limit_order_v1_resp_item import PmarginGetRateLimitOrderV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetRateLimitOrderV1RespItem from a JSON string
pmargin_get_rate_limit_order_v1_resp_item_instance = PmarginGetRateLimitOrderV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetRateLimitOrderV1RespItem.to_json())

# convert the object into a dict
pmargin_get_rate_limit_order_v1_resp_item_dict = pmargin_get_rate_limit_order_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetRateLimitOrderV1RespItem from a dict
pmargin_get_rate_limit_order_v1_resp_item_from_dict = PmarginGetRateLimitOrderV1RespItem.from_dict(pmargin_get_rate_limit_order_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


