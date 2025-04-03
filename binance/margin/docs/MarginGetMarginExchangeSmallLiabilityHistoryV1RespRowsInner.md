# MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**biz_type** | **str** |  | [optional] 
**target_amount** | **str** |  | [optional] 
**target_asset** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner import MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner from a JSON string
margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner_instance = MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.to_json())

# convert the object into a dict
margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner_dict = margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner from a dict
margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner_from_dict = MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.from_dict(margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


