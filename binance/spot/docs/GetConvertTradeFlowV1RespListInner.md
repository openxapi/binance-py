# GetConvertTradeFlowV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
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
from binance.spot.models.get_convert_trade_flow_v1_resp_list_inner import GetConvertTradeFlowV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertTradeFlowV1RespListInner from a JSON string
get_convert_trade_flow_v1_resp_list_inner_instance = GetConvertTradeFlowV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetConvertTradeFlowV1RespListInner.to_json())

# convert the object into a dict
get_convert_trade_flow_v1_resp_list_inner_dict = get_convert_trade_flow_v1_resp_list_inner_instance.to_dict()
# create an instance of GetConvertTradeFlowV1RespListInner from a dict
get_convert_trade_flow_v1_resp_list_inner_from_dict = GetConvertTradeFlowV1RespListInner.from_dict(get_convert_trade_flow_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


