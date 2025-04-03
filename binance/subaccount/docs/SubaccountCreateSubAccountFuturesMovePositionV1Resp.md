# SubaccountCreateSubAccountFuturesMovePositionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_position_orders** | [**List[SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner]**](SubaccountCreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_create_sub_account_futures_move_position_v1_resp import SubaccountCreateSubAccountFuturesMovePositionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateSubAccountFuturesMovePositionV1Resp from a JSON string
subaccount_create_sub_account_futures_move_position_v1_resp_instance = SubaccountCreateSubAccountFuturesMovePositionV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountCreateSubAccountFuturesMovePositionV1Resp.to_json())

# convert the object into a dict
subaccount_create_sub_account_futures_move_position_v1_resp_dict = subaccount_create_sub_account_futures_move_position_v1_resp_instance.to_dict()
# create an instance of SubaccountCreateSubAccountFuturesMovePositionV1Resp from a dict
subaccount_create_sub_account_futures_move_position_v1_resp_from_dict = SubaccountCreateSubAccountFuturesMovePositionV1Resp.from_dict(subaccount_create_sub_account_futures_move_position_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


