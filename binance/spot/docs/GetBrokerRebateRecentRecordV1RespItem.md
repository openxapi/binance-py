# GetBrokerRebateRecentRecordV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_rebate_recent_record_v1_resp_item import GetBrokerRebateRecentRecordV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerRebateRecentRecordV1RespItem from a JSON string
get_broker_rebate_recent_record_v1_resp_item_instance = GetBrokerRebateRecentRecordV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerRebateRecentRecordV1RespItem.to_json())

# convert the object into a dict
get_broker_rebate_recent_record_v1_resp_item_dict = get_broker_rebate_recent_record_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerRebateRecentRecordV1RespItem from a dict
get_broker_rebate_recent_record_v1_resp_item_from_dict = GetBrokerRebateRecentRecordV1RespItem.from_dict(get_broker_rebate_recent_record_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


