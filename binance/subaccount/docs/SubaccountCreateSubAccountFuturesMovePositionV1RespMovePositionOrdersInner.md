# SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner


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
from binance.subaccount.models.subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner import SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner from a JSON string
subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_instance = SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.from_json(json)
# print the JSON string representation of the object
print(SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.to_json())

# convert the object into a dict
subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_dict = subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_instance.to_dict()
# create an instance of SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner from a dict
subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_from_dict = SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.from_dict(subaccount_create_sub_account_futures_move_position_v1_resp_move_position_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


