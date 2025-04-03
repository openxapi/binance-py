# PmarginproGetPortfolioInterestHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**interest_accrued_time** | **int** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_interest_history_v1_resp_item import PmarginproGetPortfolioInterestHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginproGetPortfolioInterestHistoryV1RespItem from a JSON string
pmarginpro_get_portfolio_interest_history_v1_resp_item_instance = PmarginproGetPortfolioInterestHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginproGetPortfolioInterestHistoryV1RespItem.to_json())

# convert the object into a dict
pmarginpro_get_portfolio_interest_history_v1_resp_item_dict = pmarginpro_get_portfolio_interest_history_v1_resp_item_instance.to_dict()
# create an instance of PmarginproGetPortfolioInterestHistoryV1RespItem from a dict
pmarginpro_get_portfolio_interest_history_v1_resp_item_from_dict = PmarginproGetPortfolioInterestHistoryV1RespItem.from_dict(pmarginpro_get_portfolio_interest_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


