# GetBrokerSubAccountSpotSummaryV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account_id** | **str** |  | [optional] 
**total_balance_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_spot_summary_v1_resp_data_inner import GetBrokerSubAccountSpotSummaryV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountSpotSummaryV1RespDataInner from a JSON string
get_broker_sub_account_spot_summary_v1_resp_data_inner_instance = GetBrokerSubAccountSpotSummaryV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountSpotSummaryV1RespDataInner.to_json())

# convert the object into a dict
get_broker_sub_account_spot_summary_v1_resp_data_inner_dict = get_broker_sub_account_spot_summary_v1_resp_data_inner_instance.to_dict()
# create an instance of GetBrokerSubAccountSpotSummaryV1RespDataInner from a dict
get_broker_sub_account_spot_summary_v1_resp_data_inner_from_dict = GetBrokerSubAccountSpotSummaryV1RespDataInner.from_dict(get_broker_sub_account_spot_summary_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


