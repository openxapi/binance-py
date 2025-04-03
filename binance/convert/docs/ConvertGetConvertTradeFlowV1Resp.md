# ConvertGetConvertTradeFlowV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**list** | [**List[ConvertGetConvertTradeFlowV1RespListInner]**](ConvertGetConvertTradeFlowV1RespListInner.md) |  | [optional] 
**more_data** | **bool** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from binance.convert.models.convert_get_convert_trade_flow_v1_resp import ConvertGetConvertTradeFlowV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGetConvertTradeFlowV1Resp from a JSON string
convert_get_convert_trade_flow_v1_resp_instance = ConvertGetConvertTradeFlowV1Resp.from_json(json)
# print the JSON string representation of the object
print(ConvertGetConvertTradeFlowV1Resp.to_json())

# convert the object into a dict
convert_get_convert_trade_flow_v1_resp_dict = convert_get_convert_trade_flow_v1_resp_instance.to_dict()
# create an instance of ConvertGetConvertTradeFlowV1Resp from a dict
convert_get_convert_trade_flow_v1_resp_from_dict = ConvertGetConvertTradeFlowV1Resp.from_dict(convert_get_convert_trade_flow_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


