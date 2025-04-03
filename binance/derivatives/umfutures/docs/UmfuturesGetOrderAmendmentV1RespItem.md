# UmfuturesGetOrderAmendmentV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment** | [**UmfuturesGetOrderAmendmentV1RespItemAmendment**](UmfuturesGetOrderAmendmentV1RespItemAmendment.md) |  | [optional] 
**amendment_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item import UmfuturesGetOrderAmendmentV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetOrderAmendmentV1RespItem from a JSON string
umfutures_get_order_amendment_v1_resp_item_instance = UmfuturesGetOrderAmendmentV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetOrderAmendmentV1RespItem.to_json())

# convert the object into a dict
umfutures_get_order_amendment_v1_resp_item_dict = umfutures_get_order_amendment_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetOrderAmendmentV1RespItem from a dict
umfutures_get_order_amendment_v1_resp_item_from_dict = UmfuturesGetOrderAmendmentV1RespItem.from_dict(umfutures_get_order_amendment_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


