# GetPortfolioCollateralRateV2RespItemCollateralInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_rate** | **str** |  | [optional] 
**cum** | **str** |  | [optional] 
**tier_cap** | **str** |  | [optional] 
**tier_floor** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner import GetPortfolioCollateralRateV2RespItemCollateralInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioCollateralRateV2RespItemCollateralInfoInner from a JSON string
get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner_instance = GetPortfolioCollateralRateV2RespItemCollateralInfoInner.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioCollateralRateV2RespItemCollateralInfoInner.to_json())

# convert the object into a dict
get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner_dict = get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner_instance.to_dict()
# create an instance of GetPortfolioCollateralRateV2RespItemCollateralInfoInner from a dict
get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner_from_dict = GetPortfolioCollateralRateV2RespItemCollateralInfoInner.from_dict(get_portfolio_collateral_rate_v2_resp_item_collateral_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


