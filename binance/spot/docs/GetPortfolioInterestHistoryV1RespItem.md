# GetPortfolioInterestHistoryV1RespItem


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
from binance.spot.models.get_portfolio_interest_history_v1_resp_item import GetPortfolioInterestHistoryV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioInterestHistoryV1RespItem from a JSON string
get_portfolio_interest_history_v1_resp_item_instance = GetPortfolioInterestHistoryV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioInterestHistoryV1RespItem.to_json())

# convert the object into a dict
get_portfolio_interest_history_v1_resp_item_dict = get_portfolio_interest_history_v1_resp_item_instance.to_dict()
# create an instance of GetPortfolioInterestHistoryV1RespItem from a dict
get_portfolio_interest_history_v1_resp_item_from_dict = GetPortfolioInterestHistoryV1RespItem.from_dict(get_portfolio_interest_history_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


