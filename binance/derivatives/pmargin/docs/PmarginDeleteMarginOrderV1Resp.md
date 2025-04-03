# PmarginDeleteMarginOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_delete_margin_order_v1_resp import PmarginDeleteMarginOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginDeleteMarginOrderV1Resp from a JSON string
pmargin_delete_margin_order_v1_resp_instance = PmarginDeleteMarginOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginDeleteMarginOrderV1Resp.to_json())

# convert the object into a dict
pmargin_delete_margin_order_v1_resp_dict = pmargin_delete_margin_order_v1_resp_instance.to_dict()
# create an instance of PmarginDeleteMarginOrderV1Resp from a dict
pmargin_delete_margin_order_v1_resp_from_dict = PmarginDeleteMarginOrderV1Resp.from_dict(pmargin_delete_margin_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


