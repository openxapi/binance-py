# GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**dest_account** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**redeem_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner import GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner from a JSON string
get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner_instance = GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner.to_json())

# convert the object into a dict
get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner_dict = get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner from a dict
get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner_from_dict = GetSimpleEarnFlexibleHistoryRedemptionRecordV1RespRowsInner.from_dict(get_simple_earn_flexible_history_redemption_record_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


