# GetSubAccountFuturesMovePositionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_move_position_order_vo_list** | [**List[GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner]**](GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_move_position_v1_resp import GetSubAccountFuturesMovePositionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesMovePositionV1Resp from a JSON string
get_sub_account_futures_move_position_v1_resp_instance = GetSubAccountFuturesMovePositionV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesMovePositionV1Resp.to_json())

# convert the object into a dict
get_sub_account_futures_move_position_v1_resp_dict = get_sub_account_futures_move_position_v1_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesMovePositionV1Resp from a dict
get_sub_account_futures_move_position_v1_resp_from_dict = GetSubAccountFuturesMovePositionV1Resp.from_dict(get_sub_account_futures_move_position_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


