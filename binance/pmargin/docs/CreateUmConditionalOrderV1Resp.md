# CreateUmConditionalOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**good_till_date** | **int** |  | [optional] 
**new_client_strategy_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_match** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**strategy_id** | **int** |  | [optional] 
**strategy_status** | **str** |  | [optional] 
**strategy_type** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_type** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_um_conditional_order_v1_resp import CreateUmConditionalOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUmConditionalOrderV1Resp from a JSON string
create_um_conditional_order_v1_resp_instance = CreateUmConditionalOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateUmConditionalOrderV1Resp.to_json())

# convert the object into a dict
create_um_conditional_order_v1_resp_dict = create_um_conditional_order_v1_resp_instance.to_dict()
# create an instance of CreateUmConditionalOrderV1Resp from a dict
create_um_conditional_order_v1_resp_from_dict = CreateUmConditionalOrderV1Resp.from_dict(create_um_conditional_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


