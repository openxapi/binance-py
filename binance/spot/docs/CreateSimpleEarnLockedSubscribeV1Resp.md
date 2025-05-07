# CreateSimpleEarnLockedSubscribeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** |  | [optional] 
**purchase_id** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_simple_earn_locked_subscribe_v1_resp import CreateSimpleEarnLockedSubscribeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSimpleEarnLockedSubscribeV1Resp from a JSON string
create_simple_earn_locked_subscribe_v1_resp_instance = CreateSimpleEarnLockedSubscribeV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSimpleEarnLockedSubscribeV1Resp.to_json())

# convert the object into a dict
create_simple_earn_locked_subscribe_v1_resp_dict = create_simple_earn_locked_subscribe_v1_resp_instance.to_dict()
# create an instance of CreateSimpleEarnLockedSubscribeV1Resp from a dict
create_simple_earn_locked_subscribe_v1_resp_from_dict = CreateSimpleEarnLockedSubscribeV1Resp.from_dict(create_simple_earn_locked_subscribe_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


