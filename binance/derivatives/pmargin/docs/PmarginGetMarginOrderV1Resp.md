# PmarginGetMarginOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**iceberg_qty** | **str** |  | [optional] 
**is_working** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**prevented_match_id** | **object** |  | [optional] 
**prevented_quantity** | **object** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_order_v1_resp import PmarginGetMarginOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginOrderV1Resp from a JSON string
pmargin_get_margin_order_v1_resp_instance = PmarginGetMarginOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginOrderV1Resp.to_json())

# convert the object into a dict
pmargin_get_margin_order_v1_resp_dict = pmargin_get_margin_order_v1_resp_instance.to_dict()
# create an instance of PmarginGetMarginOrderV1Resp from a dict
pmargin_get_margin_order_v1_resp_from_dict = PmarginGetMarginOrderV1Resp.from_dict(pmargin_get_margin_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


