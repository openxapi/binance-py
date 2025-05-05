# GetMarginCrossMarginCollateralRatioV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_names** | **List[str]** |  | [optional] 
**collaterals** | [**List[GetMarginCrossMarginCollateralRatioV1RespItemCollateralsInner]**](GetMarginCrossMarginCollateralRatioV1RespItemCollateralsInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_cross_margin_collateral_ratio_v1_resp_item import GetMarginCrossMarginCollateralRatioV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginCrossMarginCollateralRatioV1RespItem from a JSON string
get_margin_cross_margin_collateral_ratio_v1_resp_item_instance = GetMarginCrossMarginCollateralRatioV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginCrossMarginCollateralRatioV1RespItem.to_json())

# convert the object into a dict
get_margin_cross_margin_collateral_ratio_v1_resp_item_dict = get_margin_cross_margin_collateral_ratio_v1_resp_item_instance.to_dict()
# create an instance of GetMarginCrossMarginCollateralRatioV1RespItem from a dict
get_margin_cross_margin_collateral_ratio_v1_resp_item_from_dict = GetMarginCrossMarginCollateralRatioV1RespItem.from_dict(get_margin_cross_margin_collateral_ratio_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


