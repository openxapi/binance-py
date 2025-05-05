# CreateConvertLimitQueryOpenOrdersV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**expired_timestamp** | **int** |  | [optional] 
**from_amount** | **str** |  | [optional] 
**from_asset** | **str** |  | [optional] 
**inverse_ratio** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_status** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**ratio** | **str** |  | [optional] 
**to_amount** | **str** |  | [optional] 
**to_asset** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_convert_limit_query_open_orders_v1_resp_list_inner import CreateConvertLimitQueryOpenOrdersV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConvertLimitQueryOpenOrdersV1RespListInner from a JSON string
create_convert_limit_query_open_orders_v1_resp_list_inner_instance = CreateConvertLimitQueryOpenOrdersV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(CreateConvertLimitQueryOpenOrdersV1RespListInner.to_json())

# convert the object into a dict
create_convert_limit_query_open_orders_v1_resp_list_inner_dict = create_convert_limit_query_open_orders_v1_resp_list_inner_instance.to_dict()
# create an instance of CreateConvertLimitQueryOpenOrdersV1RespListInner from a dict
create_convert_limit_query_open_orders_v1_resp_list_inner_from_dict = CreateConvertLimitQueryOpenOrdersV1RespListInner.from_dict(create_convert_limit_query_open_orders_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


