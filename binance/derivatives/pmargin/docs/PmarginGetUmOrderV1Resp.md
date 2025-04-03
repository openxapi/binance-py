# PmarginGetUmOrderV1Resp


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
from binance.derivatives.pmargin.models.pmargin_get_um_order_v1_resp import PmarginGetUmOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmOrderV1Resp from a JSON string
pmargin_get_um_order_v1_resp_instance = PmarginGetUmOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmOrderV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_order_v1_resp_dict = pmargin_get_um_order_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmOrderV1Resp from a dict
pmargin_get_um_order_v1_resp_from_dict = PmarginGetUmOrderV1Resp.from_dict(pmargin_get_um_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


