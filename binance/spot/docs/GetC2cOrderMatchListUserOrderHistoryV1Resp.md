# GetC2cOrderMatchListUserOrderHistoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**List[GetC2cOrderMatchListUserOrderHistoryV1RespDataInner]**](GetC2cOrderMatchListUserOrderHistoryV1RespDataInner.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_c2c_order_match_list_user_order_history_v1_resp import GetC2cOrderMatchListUserOrderHistoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetC2cOrderMatchListUserOrderHistoryV1Resp from a JSON string
get_c2c_order_match_list_user_order_history_v1_resp_instance = GetC2cOrderMatchListUserOrderHistoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetC2cOrderMatchListUserOrderHistoryV1Resp.to_json())

# convert the object into a dict
get_c2c_order_match_list_user_order_history_v1_resp_dict = get_c2c_order_match_list_user_order_history_v1_resp_instance.to_dict()
# create an instance of GetC2cOrderMatchListUserOrderHistoryV1Resp from a dict
get_c2c_order_match_list_user_order_history_v1_resp_from_dict = GetC2cOrderMatchListUserOrderHistoryV1Resp.from_dict(get_c2c_order_match_list_user_order_history_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


