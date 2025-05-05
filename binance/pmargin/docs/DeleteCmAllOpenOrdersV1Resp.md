# DeleteCmAllOpenOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.delete_cm_all_open_orders_v1_resp import DeleteCmAllOpenOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCmAllOpenOrdersV1Resp from a JSON string
delete_cm_all_open_orders_v1_resp_instance = DeleteCmAllOpenOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteCmAllOpenOrdersV1Resp.to_json())

# convert the object into a dict
delete_cm_all_open_orders_v1_resp_dict = delete_cm_all_open_orders_v1_resp_instance.to_dict()
# create an instance of DeleteCmAllOpenOrdersV1Resp from a dict
delete_cm_all_open_orders_v1_resp_from_dict = DeleteCmAllOpenOrdersV1Resp.from_dict(delete_cm_all_open_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


