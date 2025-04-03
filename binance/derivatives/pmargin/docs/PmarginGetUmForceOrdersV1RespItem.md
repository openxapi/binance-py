# PmarginGetUmForceOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cum_quote** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_force_orders_v1_resp_item import PmarginGetUmForceOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmForceOrdersV1RespItem from a JSON string
pmargin_get_um_force_orders_v1_resp_item_instance = PmarginGetUmForceOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmForceOrdersV1RespItem.to_json())

# convert the object into a dict
pmargin_get_um_force_orders_v1_resp_item_dict = pmargin_get_um_force_orders_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetUmForceOrdersV1RespItem from a dict
pmargin_get_um_force_orders_v1_resp_item_from_dict = PmarginGetUmForceOrdersV1RespItem.from_dict(pmargin_get_um_force_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


