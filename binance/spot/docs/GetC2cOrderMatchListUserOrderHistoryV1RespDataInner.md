# GetC2cOrderMatchListUserOrderHistoryV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adv_no** | **str** |  | [optional] 
**advertisement_role** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**commission** | **str** |  | [optional] 
**counter_part_nick_name** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**fiat** | **str** |  | [optional] 
**fiat_symbol** | **str** |  | [optional] 
**order_number** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**total_price** | **str** |  | [optional] 
**trade_type** | **str** |  | [optional] 
**unit_price** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_c2c_order_match_list_user_order_history_v1_resp_data_inner import GetC2cOrderMatchListUserOrderHistoryV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetC2cOrderMatchListUserOrderHistoryV1RespDataInner from a JSON string
get_c2c_order_match_list_user_order_history_v1_resp_data_inner_instance = GetC2cOrderMatchListUserOrderHistoryV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetC2cOrderMatchListUserOrderHistoryV1RespDataInner.to_json())

# convert the object into a dict
get_c2c_order_match_list_user_order_history_v1_resp_data_inner_dict = get_c2c_order_match_list_user_order_history_v1_resp_data_inner_instance.to_dict()
# create an instance of GetC2cOrderMatchListUserOrderHistoryV1RespDataInner from a dict
get_c2c_order_match_list_user_order_history_v1_resp_data_inner_from_dict = GetC2cOrderMatchListUserOrderHistoryV1RespDataInner.from_dict(get_c2c_order_match_list_user_order_history_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


