# GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner


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
from binance.spot.models.get_margin_exchange_small_liability_history_v1_resp_rows_inner import GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner from a JSON string
get_margin_exchange_small_liability_history_v1_resp_rows_inner_instance = GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_margin_exchange_small_liability_history_v1_resp_rows_inner_dict = get_margin_exchange_small_liability_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner from a dict
get_margin_exchange_small_liability_history_v1_resp_rows_inner_from_dict = GetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.from_dict(get_margin_exchange_small_liability_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


