# CreatePortfolioMintV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** |  | [optional] 
**from_asset_qty** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 
**target_asset** | **str** |  | [optional] 
**target_asset_qty** | **float** |  | [optional] 

## Example

```python
from binance.spot.models.create_portfolio_mint_v1_resp import CreatePortfolioMintV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolioMintV1Resp from a JSON string
create_portfolio_mint_v1_resp_instance = CreatePortfolioMintV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreatePortfolioMintV1Resp.to_json())

# convert the object into a dict
create_portfolio_mint_v1_resp_dict = create_portfolio_mint_v1_resp_instance.to_dict()
# create an instance of CreatePortfolioMintV1Resp from a dict
create_portfolio_mint_v1_resp_from_dict = CreatePortfolioMintV1Resp.from_dict(create_portfolio_mint_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


