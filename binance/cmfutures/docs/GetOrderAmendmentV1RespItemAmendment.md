# GetOrderAmendmentV1RespItemAmendment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**orig_qty** | [**GetOrderAmendmentV1RespItemAmendmentOrigQty**](GetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 
**price** | [**GetOrderAmendmentV1RespItemAmendmentOrigQty**](GetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_order_amendment_v1_resp_item_amendment import GetOrderAmendmentV1RespItemAmendment

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderAmendmentV1RespItemAmendment from a JSON string
get_order_amendment_v1_resp_item_amendment_instance = GetOrderAmendmentV1RespItemAmendment.from_json(json)
# print the JSON string representation of the object
print(GetOrderAmendmentV1RespItemAmendment.to_json())

# convert the object into a dict
get_order_amendment_v1_resp_item_amendment_dict = get_order_amendment_v1_resp_item_amendment_instance.to_dict()
# create an instance of GetOrderAmendmentV1RespItemAmendment from a dict
get_order_amendment_v1_resp_item_amendment_from_dict = GetOrderAmendmentV1RespItemAmendment.from_dict(get_order_amendment_v1_resp_item_amendment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


