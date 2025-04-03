# CmfuturesGetOrderAmendmentV1RespItemAmendment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**orig_qty** | [**CmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty**](CmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 
**price** | [**CmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty**](CmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.md) |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_order_amendment_v1_resp_item_amendment import CmfuturesGetOrderAmendmentV1RespItemAmendment

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetOrderAmendmentV1RespItemAmendment from a JSON string
cmfutures_get_order_amendment_v1_resp_item_amendment_instance = CmfuturesGetOrderAmendmentV1RespItemAmendment.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetOrderAmendmentV1RespItemAmendment.to_json())

# convert the object into a dict
cmfutures_get_order_amendment_v1_resp_item_amendment_dict = cmfutures_get_order_amendment_v1_resp_item_amendment_instance.to_dict()
# create an instance of CmfuturesGetOrderAmendmentV1RespItemAmendment from a dict
cmfutures_get_order_amendment_v1_resp_item_amendment_from_dict = CmfuturesGetOrderAmendmentV1RespItemAmendment.from_dict(cmfutures_get_order_amendment_v1_resp_item_amendment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


