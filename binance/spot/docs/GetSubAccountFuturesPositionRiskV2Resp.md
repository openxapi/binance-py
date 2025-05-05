# GetSubAccountFuturesPositionRiskV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_position_risk_vos** | [**List[GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner]**](GetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_position_risk_v2_resp import GetSubAccountFuturesPositionRiskV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesPositionRiskV2Resp from a JSON string
get_sub_account_futures_position_risk_v2_resp_instance = GetSubAccountFuturesPositionRiskV2Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesPositionRiskV2Resp.to_json())

# convert the object into a dict
get_sub_account_futures_position_risk_v2_resp_dict = get_sub_account_futures_position_risk_v2_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesPositionRiskV2Resp from a dict
get_sub_account_futures_position_risk_v2_resp_from_dict = GetSubAccountFuturesPositionRiskV2Resp.from_dict(get_sub_account_futures_position_risk_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


