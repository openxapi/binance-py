# GetMarginInterestHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**interest_accured_time** | **int** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**isolated_symbol** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**raw_asset** | **str** |  | [optional] 
**tx_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_interest_history_v1_resp_rows_inner import GetMarginInterestHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginInterestHistoryV1RespRowsInner from a JSON string
get_margin_interest_history_v1_resp_rows_inner_instance = GetMarginInterestHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginInterestHistoryV1RespRowsInner.to_json())

# convert the object into a dict
get_margin_interest_history_v1_resp_rows_inner_dict = get_margin_interest_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetMarginInterestHistoryV1RespRowsInner from a dict
get_margin_interest_history_v1_resp_rows_inner_from_dict = GetMarginInterestHistoryV1RespRowsInner.from_dict(get_margin_interest_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


