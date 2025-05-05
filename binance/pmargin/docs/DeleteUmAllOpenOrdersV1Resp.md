# DeleteUmAllOpenOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.delete_um_all_open_orders_v1_resp import DeleteUmAllOpenOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUmAllOpenOrdersV1Resp from a JSON string
delete_um_all_open_orders_v1_resp_instance = DeleteUmAllOpenOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteUmAllOpenOrdersV1Resp.to_json())

# convert the object into a dict
delete_um_all_open_orders_v1_resp_dict = delete_um_all_open_orders_v1_resp_instance.to_dict()
# create an instance of DeleteUmAllOpenOrdersV1Resp from a dict
delete_um_all_open_orders_v1_resp_from_dict = DeleteUmAllOpenOrdersV1Resp.from_dict(delete_um_all_open_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


