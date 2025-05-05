# GetMarginMarginInterestHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetMarginMarginInterestHistoryV1RespRowsInner]**](GetMarginMarginInterestHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_margin_margin_interest_history_v1_resp import GetMarginMarginInterestHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginMarginInterestHistoryV1Resp from a JSON string
get_margin_margin_interest_history_v1_resp_instance = GetMarginMarginInterestHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginMarginInterestHistoryV1Resp.to_json())

# convert the object into a dict
get_margin_margin_interest_history_v1_resp_dict = get_margin_margin_interest_history_v1_resp_instance.to_dict()
# create an instance of GetMarginMarginInterestHistoryV1Resp from a dict
get_margin_margin_interest_history_v1_resp_from_dict = GetMarginMarginInterestHistoryV1Resp.from_dict(get_margin_margin_interest_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


