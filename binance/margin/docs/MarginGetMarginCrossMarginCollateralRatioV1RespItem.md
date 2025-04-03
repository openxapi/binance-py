# MarginGetMarginCrossMarginCollateralRatioV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_names** | **List[str]** |  | [optional] 
**collaterals** | [**List[MarginGetMarginCrossMarginCollateralRatioV1RespItemCollateralsInner]**](MarginGetMarginCrossMarginCollateralRatioV1RespItemCollateralsInner.md) |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_cross_margin_collateral_ratio_v1_resp_item import MarginGetMarginCrossMarginCollateralRatioV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginCrossMarginCollateralRatioV1RespItem from a JSON string
margin_get_margin_cross_margin_collateral_ratio_v1_resp_item_instance = MarginGetMarginCrossMarginCollateralRatioV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginCrossMarginCollateralRatioV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_cross_margin_collateral_ratio_v1_resp_item_dict = margin_get_margin_cross_margin_collateral_ratio_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginCrossMarginCollateralRatioV1RespItem from a dict
margin_get_margin_cross_margin_collateral_ratio_v1_resp_item_from_dict = MarginGetMarginCrossMarginCollateralRatioV1RespItem.from_dict(margin_get_margin_cross_margin_collateral_ratio_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


