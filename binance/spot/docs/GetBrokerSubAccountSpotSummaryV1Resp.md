# GetBrokerSubAccountSpotSummaryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetBrokerSubAccountSpotSummaryV1RespDataInner]**](GetBrokerSubAccountSpotSummaryV1RespDataInner.md) |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_spot_summary_v1_resp import GetBrokerSubAccountSpotSummaryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountSpotSummaryV1Resp from a JSON string
get_broker_sub_account_spot_summary_v1_resp_instance = GetBrokerSubAccountSpotSummaryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountSpotSummaryV1Resp.to_json())

# convert the object into a dict
get_broker_sub_account_spot_summary_v1_resp_dict = get_broker_sub_account_spot_summary_v1_resp_instance.to_dict()
# create an instance of GetBrokerSubAccountSpotSummaryV1Resp from a dict
get_broker_sub_account_spot_summary_v1_resp_from_dict = GetBrokerSubAccountSpotSummaryV1Resp.from_dict(get_broker_sub_account_spot_summary_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


