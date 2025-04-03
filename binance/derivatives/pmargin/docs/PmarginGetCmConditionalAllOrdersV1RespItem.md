# PmarginGetCmConditionalAllOrdersV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**new_client_strategy_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**strategy_id** | **int** |  | [optional] 
**strategy_status** | **str** |  | [optional] 
**strategy_type** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**trigger_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_all_orders_v1_resp_item import PmarginGetCmConditionalAllOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmConditionalAllOrdersV1RespItem from a JSON string
pmargin_get_cm_conditional_all_orders_v1_resp_item_instance = PmarginGetCmConditionalAllOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmConditionalAllOrdersV1RespItem.to_json())

# convert the object into a dict
pmargin_get_cm_conditional_all_orders_v1_resp_item_dict = pmargin_get_cm_conditional_all_orders_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetCmConditionalAllOrdersV1RespItem from a dict
pmargin_get_cm_conditional_all_orders_v1_resp_item_from_dict = PmarginGetCmConditionalAllOrdersV1RespItem.from_dict(pmargin_get_cm_conditional_all_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


