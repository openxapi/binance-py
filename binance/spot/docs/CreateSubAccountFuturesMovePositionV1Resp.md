# CreateSubAccountFuturesMovePositionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_position_orders** | [**List[CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner]**](CreateSubAccountFuturesMovePositionV1RespMovePositionOrdersInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_futures_move_position_v1_resp import CreateSubAccountFuturesMovePositionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountFuturesMovePositionV1Resp from a JSON string
create_sub_account_futures_move_position_v1_resp_instance = CreateSubAccountFuturesMovePositionV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountFuturesMovePositionV1Resp.to_json())

# convert the object into a dict
create_sub_account_futures_move_position_v1_resp_dict = create_sub_account_futures_move_position_v1_resp_instance.to_dict()
# create an instance of CreateSubAccountFuturesMovePositionV1Resp from a dict
create_sub_account_futures_move_position_v1_resp_from_dict = CreateSubAccountFuturesMovePositionV1Resp.from_dict(create_sub_account_futures_move_position_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


