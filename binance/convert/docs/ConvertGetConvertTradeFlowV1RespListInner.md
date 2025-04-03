# ConvertGetConvertTradeFlowV1RespListInner


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
from binance.convert.models.convert_get_convert_trade_flow_v1_resp_list_inner import ConvertGetConvertTradeFlowV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGetConvertTradeFlowV1RespListInner from a JSON string
convert_get_convert_trade_flow_v1_resp_list_inner_instance = ConvertGetConvertTradeFlowV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(ConvertGetConvertTradeFlowV1RespListInner.to_json())

# convert the object into a dict
convert_get_convert_trade_flow_v1_resp_list_inner_dict = convert_get_convert_trade_flow_v1_resp_list_inner_instance.to_dict()
# create an instance of ConvertGetConvertTradeFlowV1RespListInner from a dict
convert_get_convert_trade_flow_v1_resp_list_inner_from_dict = ConvertGetConvertTradeFlowV1RespListInner.from_dict(convert_get_convert_trade_flow_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


