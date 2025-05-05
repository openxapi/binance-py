# GetPortfolioCollateralRateV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**collateral_info** | [**List[GetPortfolioCollateralRateV2RespItemCollateralInfoInner]**](GetPortfolioCollateralRateV2RespItemCollateralInfoInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_portfolio_collateral_rate_v2_resp_item import GetPortfolioCollateralRateV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioCollateralRateV2RespItem from a JSON string
get_portfolio_collateral_rate_v2_resp_item_instance = GetPortfolioCollateralRateV2RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioCollateralRateV2RespItem.to_json())

# convert the object into a dict
get_portfolio_collateral_rate_v2_resp_item_dict = get_portfolio_collateral_rate_v2_resp_item_instance.to_dict()
# create an instance of GetPortfolioCollateralRateV2RespItem from a dict
get_portfolio_collateral_rate_v2_resp_item_from_dict = GetPortfolioCollateralRateV2RespItem.from_dict(get_portfolio_collateral_rate_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


