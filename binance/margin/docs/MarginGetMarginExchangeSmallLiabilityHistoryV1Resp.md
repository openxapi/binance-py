# MarginGetMarginExchangeSmallLiabilityHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner]**](MarginGetMarginExchangeSmallLiabilityHistoryV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_exchange_small_liability_history_v1_resp import MarginGetMarginExchangeSmallLiabilityHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginExchangeSmallLiabilityHistoryV1Resp from a JSON string
margin_get_margin_exchange_small_liability_history_v1_resp_instance = MarginGetMarginExchangeSmallLiabilityHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginExchangeSmallLiabilityHistoryV1Resp.to_json())

# convert the object into a dict
margin_get_margin_exchange_small_liability_history_v1_resp_dict = margin_get_margin_exchange_small_liability_history_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginExchangeSmallLiabilityHistoryV1Resp from a dict
margin_get_margin_exchange_small_liability_history_v1_resp_from_dict = MarginGetMarginExchangeSmallLiabilityHistoryV1Resp.from_dict(margin_get_margin_exchange_small_liability_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


