# UmfuturesGetRateLimitOrderV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_rate_limit_order_v1_resp_item import UmfuturesGetRateLimitOrderV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetRateLimitOrderV1RespItem from a JSON string
umfutures_get_rate_limit_order_v1_resp_item_instance = UmfuturesGetRateLimitOrderV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetRateLimitOrderV1RespItem.to_json())

# convert the object into a dict
umfutures_get_rate_limit_order_v1_resp_item_dict = umfutures_get_rate_limit_order_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetRateLimitOrderV1RespItem from a dict
umfutures_get_rate_limit_order_v1_resp_item_from_dict = UmfuturesGetRateLimitOrderV1RespItem.from_dict(umfutures_get_rate_limit_order_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


