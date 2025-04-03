# PmarginGetPortfolioInterestHistoryV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**interest_accured_time** | **int** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_portfolio_interest_history_v1_resp_item import PmarginGetPortfolioInterestHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetPortfolioInterestHistoryV1RespItem from a JSON string
pmargin_get_portfolio_interest_history_v1_resp_item_instance = PmarginGetPortfolioInterestHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetPortfolioInterestHistoryV1RespItem.to_json())

# convert the object into a dict
pmargin_get_portfolio_interest_history_v1_resp_item_dict = pmargin_get_portfolio_interest_history_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetPortfolioInterestHistoryV1RespItem from a dict
pmargin_get_portfolio_interest_history_v1_resp_item_from_dict = PmarginGetPortfolioInterestHistoryV1RespItem.from_dict(pmargin_get_portfolio_interest_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


