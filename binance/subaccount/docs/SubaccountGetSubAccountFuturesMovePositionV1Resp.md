# SubaccountGetSubAccountFuturesMovePositionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_move_position_order_vo_list** | [**List[SubaccountGetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner]**](SubaccountGetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_sub_account_futures_move_position_v1_resp import SubaccountGetSubAccountFuturesMovePositionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetSubAccountFuturesMovePositionV1Resp from a JSON string
subaccount_get_sub_account_futures_move_position_v1_resp_instance = SubaccountGetSubAccountFuturesMovePositionV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetSubAccountFuturesMovePositionV1Resp.to_json())

# convert the object into a dict
subaccount_get_sub_account_futures_move_position_v1_resp_dict = subaccount_get_sub_account_futures_move_position_v1_resp_instance.to_dict()
# create an instance of SubaccountGetSubAccountFuturesMovePositionV1Resp from a dict
subaccount_get_sub_account_futures_move_position_v1_resp_from_dict = SubaccountGetSubAccountFuturesMovePositionV1Resp.from_dict(subaccount_get_sub_account_futures_move_position_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


