# CreateMarginManualLiquidationV1Resp


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
from binance.spot.models.create_margin_manual_liquidation_v1_resp import CreateMarginManualLiquidationV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginManualLiquidationV1Resp from a JSON string
create_margin_manual_liquidation_v1_resp_instance = CreateMarginManualLiquidationV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginManualLiquidationV1Resp.to_json())

# convert the object into a dict
create_margin_manual_liquidation_v1_resp_dict = create_margin_manual_liquidation_v1_resp_instance.to_dict()
# create an instance of CreateMarginManualLiquidationV1Resp from a dict
create_margin_manual_liquidation_v1_resp_from_dict = CreateMarginManualLiquidationV1Resp.from_dict(create_margin_manual_liquidation_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


