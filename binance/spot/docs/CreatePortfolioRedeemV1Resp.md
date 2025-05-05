# CreatePortfolioRedeemV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** |  | [optional] 
**from_asset_qty** | **float** |  | [optional] 
**rate** | **float** |  | [optional] 
**target_asset** | **str** |  | [optional] 
**target_asset_qty** | **float** |  | [optional] 

## Example

```python
from binance.spot.models.create_portfolio_redeem_v1_resp import CreatePortfolioRedeemV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolioRedeemV1Resp from a JSON string
create_portfolio_redeem_v1_resp_instance = CreatePortfolioRedeemV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreatePortfolioRedeemV1Resp.to_json())

# convert the object into a dict
create_portfolio_redeem_v1_resp_dict = create_portfolio_redeem_v1_resp_instance.to_dict()
# create an instance of CreatePortfolioRedeemV1Resp from a dict
create_portfolio_redeem_v1_resp_from_dict = CreatePortfolioRedeemV1Resp.from_dict(create_portfolio_redeem_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


