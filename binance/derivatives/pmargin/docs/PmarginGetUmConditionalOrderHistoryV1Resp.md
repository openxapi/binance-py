# PmarginGetUmConditionalOrderHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**good_till_date** | **int** |  | [optional] 
**new_client_strategy_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
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
**working_type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_conditional_order_history_v1_resp import PmarginGetUmConditionalOrderHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmConditionalOrderHistoryV1Resp from a JSON string
pmargin_get_um_conditional_order_history_v1_resp_instance = PmarginGetUmConditionalOrderHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmConditionalOrderHistoryV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_conditional_order_history_v1_resp_dict = pmargin_get_um_conditional_order_history_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmConditionalOrderHistoryV1Resp from a dict
pmargin_get_um_conditional_order_history_v1_resp_from_dict = PmarginGetUmConditionalOrderHistoryV1Resp.from_dict(pmargin_get_um_conditional_order_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


