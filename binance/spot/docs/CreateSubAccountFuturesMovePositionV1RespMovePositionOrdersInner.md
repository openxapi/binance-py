# CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_user_email** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_type** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 
**to_user_email** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_futures_move_position_v1_resp_move_position_orders_inner import CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner from a JSON string
create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_instance = CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.to_json())

# convert the object into a dict
create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_dict = create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_instance.to_dict()
# create an instance of CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner from a dict
create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_from_dict = CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.from_dict(create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


