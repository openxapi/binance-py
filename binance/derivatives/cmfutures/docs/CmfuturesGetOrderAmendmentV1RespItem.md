# CmfuturesGetOrderAmendmentV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment** | [**CmfuturesGetOrderAmendmentV1RespItemAmendment**](CmfuturesGetOrderAmendmentV1RespItemAmendment.md) |  | [optional] 
**amendment_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_order_amendment_v1_resp_item import CmfuturesGetOrderAmendmentV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetOrderAmendmentV1RespItem from a JSON string
cmfutures_get_order_amendment_v1_resp_item_instance = CmfuturesGetOrderAmendmentV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetOrderAmendmentV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_order_amendment_v1_resp_item_dict = cmfutures_get_order_amendment_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetOrderAmendmentV1RespItem from a dict
cmfutures_get_order_amendment_v1_resp_item_from_dict = CmfuturesGetOrderAmendmentV1RespItem.from_dict(cmfutures_get_order_amendment_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


