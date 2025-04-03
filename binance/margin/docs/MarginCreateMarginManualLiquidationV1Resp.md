# MarginCreateMarginManualLiquidationV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**liability_asset** | **str** |  | [optional] 
**liability_qty** | **float** |  | [optional] 
**principal** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_create_margin_manual_liquidation_v1_resp import MarginCreateMarginManualLiquidationV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginCreateMarginManualLiquidationV1Resp from a JSON string
margin_create_margin_manual_liquidation_v1_resp_instance = MarginCreateMarginManualLiquidationV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginCreateMarginManualLiquidationV1Resp.to_json())

# convert the object into a dict
margin_create_margin_manual_liquidation_v1_resp_dict = margin_create_margin_manual_liquidation_v1_resp_instance.to_dict()
# create an instance of MarginCreateMarginManualLiquidationV1Resp from a dict
margin_create_margin_manual_liquidation_v1_resp_from_dict = MarginCreateMarginManualLiquidationV1Resp.from_dict(margin_create_margin_manual_liquidation_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


