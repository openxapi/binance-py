# DeleteAllOpenOrdersByUnderlyingV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.options.models.delete_all_open_orders_by_underlying_v1_resp import DeleteAllOpenOrdersByUnderlyingV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAllOpenOrdersByUnderlyingV1Resp from a JSON string
delete_all_open_orders_by_underlying_v1_resp_instance = DeleteAllOpenOrdersByUnderlyingV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteAllOpenOrdersByUnderlyingV1Resp.to_json())

# convert the object into a dict
delete_all_open_orders_by_underlying_v1_resp_dict = delete_all_open_orders_by_underlying_v1_resp_instance.to_dict()
# create an instance of DeleteAllOpenOrdersByUnderlyingV1Resp from a dict
delete_all_open_orders_by_underlying_v1_resp_from_dict = DeleteAllOpenOrdersByUnderlyingV1Resp.from_dict(delete_all_open_orders_by_underlying_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


