# GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_user_email** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_stamp** | **int** |  | [optional] 
**to_user_email** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner import GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner from a JSON string
get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner_instance = GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner.to_json())

# convert the object into a dict
get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner_dict = get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner_instance.to_dict()
# create an instance of GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner from a dict
get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner_from_dict = GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner.from_dict(get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


