# MarginGetMarginForceLiquidationRecV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**updated_time** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_force_liquidation_rec_v1_resp_rows_inner import MarginGetMarginForceLiquidationRecV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginForceLiquidationRecV1RespRowsInner from a JSON string
margin_get_margin_force_liquidation_rec_v1_resp_rows_inner_instance = MarginGetMarginForceLiquidationRecV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginForceLiquidationRecV1RespRowsInner.to_json())

# convert the object into a dict
margin_get_margin_force_liquidation_rec_v1_resp_rows_inner_dict = margin_get_margin_force_liquidation_rec_v1_resp_rows_inner_instance.to_dict()
# create an instance of MarginGetMarginForceLiquidationRecV1RespRowsInner from a dict
margin_get_margin_force_liquidation_rec_v1_resp_rows_inner_from_dict = MarginGetMarginForceLiquidationRecV1RespRowsInner.from_dict(margin_get_margin_force_liquidation_rec_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


