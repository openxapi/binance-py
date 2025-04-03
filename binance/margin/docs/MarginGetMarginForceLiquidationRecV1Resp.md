# MarginGetMarginForceLiquidationRecV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[MarginGetMarginForceLiquidationRecV1RespRowsInner]**](MarginGetMarginForceLiquidationRecV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_force_liquidation_rec_v1_resp import MarginGetMarginForceLiquidationRecV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginForceLiquidationRecV1Resp from a JSON string
margin_get_margin_force_liquidation_rec_v1_resp_instance = MarginGetMarginForceLiquidationRecV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginForceLiquidationRecV1Resp.to_json())

# convert the object into a dict
margin_get_margin_force_liquidation_rec_v1_resp_dict = margin_get_margin_force_liquidation_rec_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginForceLiquidationRecV1Resp from a dict
margin_get_margin_force_liquidation_rec_v1_resp_from_dict = MarginGetMarginForceLiquidationRecV1Resp.from_dict(margin_get_margin_force_liquidation_rec_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


