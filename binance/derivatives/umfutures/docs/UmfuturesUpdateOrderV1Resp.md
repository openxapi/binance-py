# UmfuturesUpdateOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**close_position** | **bool** |  | [optional] 
**cum_base** | **str** |  | [optional] 
**cum_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**good_till_date** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_match** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_update_order_v1_resp import UmfuturesUpdateOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesUpdateOrderV1Resp from a JSON string
umfutures_update_order_v1_resp_instance = UmfuturesUpdateOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesUpdateOrderV1Resp.to_json())

# convert the object into a dict
umfutures_update_order_v1_resp_dict = umfutures_update_order_v1_resp_instance.to_dict()
# create an instance of UmfuturesUpdateOrderV1Resp from a dict
umfutures_update_order_v1_resp_from_dict = UmfuturesUpdateOrderV1Resp.from_dict(umfutures_update_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


