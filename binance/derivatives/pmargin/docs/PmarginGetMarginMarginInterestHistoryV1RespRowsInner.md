# PmarginGetMarginMarginInterestHistoryV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**interest_accured_time** | **int** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**raw_asset** | **str** |  | [optional] 
**tx_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_margin_interest_history_v1_resp_rows_inner import PmarginGetMarginMarginInterestHistoryV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginMarginInterestHistoryV1RespRowsInner from a JSON string
pmargin_get_margin_margin_interest_history_v1_resp_rows_inner_instance = PmarginGetMarginMarginInterestHistoryV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginMarginInterestHistoryV1RespRowsInner.to_json())

# convert the object into a dict
pmargin_get_margin_margin_interest_history_v1_resp_rows_inner_dict = pmargin_get_margin_margin_interest_history_v1_resp_rows_inner_instance.to_dict()
# create an instance of PmarginGetMarginMarginInterestHistoryV1RespRowsInner from a dict
pmargin_get_margin_margin_interest_history_v1_resp_rows_inner_from_dict = PmarginGetMarginMarginInterestHistoryV1RespRowsInner.from_dict(pmargin_get_margin_margin_interest_history_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


