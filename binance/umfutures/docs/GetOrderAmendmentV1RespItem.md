# GetOrderAmendmentV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment** | [**GetOrderAmendmentV1RespItemAmendment**](GetOrderAmendmentV1RespItemAmendment.md) |  | [optional] 
**amendment_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_order_amendment_v1_resp_item import GetOrderAmendmentV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderAmendmentV1RespItem from a JSON string
get_order_amendment_v1_resp_item_instance = GetOrderAmendmentV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetOrderAmendmentV1RespItem.to_json())

# convert the object into a dict
get_order_amendment_v1_resp_item_dict = get_order_amendment_v1_resp_item_instance.to_dict()
# create an instance of GetOrderAmendmentV1RespItem from a dict
get_order_amendment_v1_resp_item_from_dict = GetOrderAmendmentV1RespItem.from_dict(get_order_amendment_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


