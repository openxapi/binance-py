# PmarginproGetPortfolioCollateralRateV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**collateral_info** | [**List[PmarginproGetPortfolioCollateralRateV2RespItemCollateralInfoInner]**](PmarginproGetPortfolioCollateralRateV2RespItemCollateralInfoInner.md) |  | [optional] 

## Example

```python
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_collateral_rate_v2_resp_item import PmarginproGetPortfolioCollateralRateV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginproGetPortfolioCollateralRateV2RespItem from a JSON string
pmarginpro_get_portfolio_collateral_rate_v2_resp_item_instance = PmarginproGetPortfolioCollateralRateV2RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginproGetPortfolioCollateralRateV2RespItem.to_json())

# convert the object into a dict
pmarginpro_get_portfolio_collateral_rate_v2_resp_item_dict = pmarginpro_get_portfolio_collateral_rate_v2_resp_item_instance.to_dict()
# create an instance of PmarginproGetPortfolioCollateralRateV2RespItem from a dict
pmarginpro_get_portfolio_collateral_rate_v2_resp_item_from_dict = PmarginproGetPortfolioCollateralRateV2RespItem.from_dict(pmarginpro_get_portfolio_collateral_rate_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


