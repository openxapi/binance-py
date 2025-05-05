# GetUmOpenOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cum_quote** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**good_till_date** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_type** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_match** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_open_order_v1_resp import GetUmOpenOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmOpenOrderV1Resp from a JSON string
get_um_open_order_v1_resp_instance = GetUmOpenOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmOpenOrderV1Resp.to_json())

# convert the object into a dict
get_um_open_order_v1_resp_dict = get_um_open_order_v1_resp_instance.to_dict()
# create an instance of GetUmOpenOrderV1Resp from a dict
get_um_open_order_v1_resp_from_dict = GetUmOpenOrderV1Resp.from_dict(get_um_open_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


