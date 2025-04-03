# PmarginproGetPortfolioAssetIndexPriceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**asset_index_price** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_asset_index_price_v1_resp_item import PmarginproGetPortfolioAssetIndexPriceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginproGetPortfolioAssetIndexPriceV1RespItem from a JSON string
pmarginpro_get_portfolio_asset_index_price_v1_resp_item_instance = PmarginproGetPortfolioAssetIndexPriceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginproGetPortfolioAssetIndexPriceV1RespItem.to_json())

# convert the object into a dict
pmarginpro_get_portfolio_asset_index_price_v1_resp_item_dict = pmarginpro_get_portfolio_asset_index_price_v1_resp_item_instance.to_dict()
# create an instance of PmarginproGetPortfolioAssetIndexPriceV1RespItem from a dict
pmarginpro_get_portfolio_asset_index_price_v1_resp_item_from_dict = PmarginproGetPortfolioAssetIndexPriceV1RespItem.from_dict(pmarginpro_get_portfolio_asset_index_price_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


