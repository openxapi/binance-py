# GetPortfolioBalanceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**cm_unrealized_pnl** | **str** |  | [optional] 
**cm_wallet_balance** | **str** |  | [optional] 
**cross_margin_asset** | **str** |  | [optional] 
**cross_margin_borrowed** | **str** |  | [optional] 
**cross_margin_free** | **str** |  | [optional] 
**cross_margin_interest** | **str** |  | [optional] 
**cross_margin_locked** | **str** |  | [optional] 
**negative_balance** | **str** |  | [optional] 
**option_equity** | **str** |  | [optional] 
**option_wallet_balance** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 
**um_unrealized_pnl** | **str** |  | [optional] 
**um_wallet_balance** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_portfolio_balance_v1_resp_item import GetPortfolioBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioBalanceV1RespItem from a JSON string
get_portfolio_balance_v1_resp_item_instance = GetPortfolioBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioBalanceV1RespItem.to_json())

# convert the object into a dict
get_portfolio_balance_v1_resp_item_dict = get_portfolio_balance_v1_resp_item_instance.to_dict()
# create an instance of GetPortfolioBalanceV1RespItem from a dict
get_portfolio_balance_v1_resp_item_from_dict = GetPortfolioBalanceV1RespItem.from_dict(get_portfolio_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


