# PmarginGetCmOrderAmendmentV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment** | [**PmarginGetCmOrderAmendmentV1RespItemAmendment**](PmarginGetCmOrderAmendmentV1RespItemAmendment.md) |  | [optional] 
**amendment_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item import PmarginGetCmOrderAmendmentV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmOrderAmendmentV1RespItem from a JSON string
pmargin_get_cm_order_amendment_v1_resp_item_instance = PmarginGetCmOrderAmendmentV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmOrderAmendmentV1RespItem.to_json())

# convert the object into a dict
pmargin_get_cm_order_amendment_v1_resp_item_dict = pmargin_get_cm_order_amendment_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetCmOrderAmendmentV1RespItem from a dict
pmargin_get_cm_order_amendment_v1_resp_item_from_dict = PmarginGetCmOrderAmendmentV1RespItem.from_dict(pmargin_get_cm_order_amendment_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


