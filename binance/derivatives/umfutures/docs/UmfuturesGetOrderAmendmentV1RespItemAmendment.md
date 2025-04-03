# UmfuturesGetOrderAmendmentV1RespItemAmendment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**orig_qty** | [**UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty**](UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 
**price** | [**UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty**](UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item_amendment import UmfuturesGetOrderAmendmentV1RespItemAmendment

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetOrderAmendmentV1RespItemAmendment from a JSON string
umfutures_get_order_amendment_v1_resp_item_amendment_instance = UmfuturesGetOrderAmendmentV1RespItemAmendment.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetOrderAmendmentV1RespItemAmendment.to_json())

# convert the object into a dict
umfutures_get_order_amendment_v1_resp_item_amendment_dict = umfutures_get_order_amendment_v1_resp_item_amendment_instance.to_dict()
# create an instance of UmfuturesGetOrderAmendmentV1RespItemAmendment from a dict
umfutures_get_order_amendment_v1_resp_item_amendment_from_dict = UmfuturesGetOrderAmendmentV1RespItemAmendment.from_dict(umfutures_get_order_amendment_v1_resp_item_amendment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


