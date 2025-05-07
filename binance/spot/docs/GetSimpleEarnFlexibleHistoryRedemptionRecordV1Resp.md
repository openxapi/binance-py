# GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner]**](GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_history_redemption_record_v1_resp import GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp from a JSON string
get_simple_earn_flexible_history_redemption_record_v1_resp_instance = GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp.to_json())

# convert the object into a dict
get_simple_earn_flexible_history_redemption_record_v1_resp_dict = get_simple_earn_flexible_history_redemption_record_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp from a dict
get_simple_earn_flexible_history_redemption_record_v1_resp_from_dict = GetSimpleEarnFlexibleHistoryRedemptionRecordV1Resp.from_dict(get_simple_earn_flexible_history_redemption_record_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


