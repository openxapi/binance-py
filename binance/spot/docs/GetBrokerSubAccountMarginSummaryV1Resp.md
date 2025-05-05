# GetBrokerSubAccountMarginSummaryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetBrokerSubAccountMarginSummaryV1RespDataInner]**](GetBrokerSubAccountMarginSummaryV1RespDataInner.md) |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_margin_summary_v1_resp import GetBrokerSubAccountMarginSummaryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountMarginSummaryV1Resp from a JSON string
get_broker_sub_account_margin_summary_v1_resp_instance = GetBrokerSubAccountMarginSummaryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountMarginSummaryV1Resp.to_json())

# convert the object into a dict
get_broker_sub_account_margin_summary_v1_resp_dict = get_broker_sub_account_margin_summary_v1_resp_instance.to_dict()
# create an instance of GetBrokerSubAccountMarginSummaryV1Resp from a dict
get_broker_sub_account_margin_summary_v1_resp_from_dict = GetBrokerSubAccountMarginSummaryV1Resp.from_dict(get_broker_sub_account_margin_summary_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


