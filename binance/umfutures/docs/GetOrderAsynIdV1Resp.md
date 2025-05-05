# GetOrderAsynIdV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** |  | [optional] 
**expiration_timestamp** | **int** |  | [optional] 
**is_expired** | **object** |  | [optional] 
**notified** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_order_asyn_id_v1_resp import GetOrderAsynIdV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderAsynIdV1Resp from a JSON string
get_order_asyn_id_v1_resp_instance = GetOrderAsynIdV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetOrderAsynIdV1Resp.to_json())

# convert the object into a dict
get_order_asyn_id_v1_resp_dict = get_order_asyn_id_v1_resp_instance.to_dict()
# create an instance of GetOrderAsynIdV1Resp from a dict
get_order_asyn_id_v1_resp_from_dict = GetOrderAsynIdV1Resp.from_dict(get_order_asyn_id_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


