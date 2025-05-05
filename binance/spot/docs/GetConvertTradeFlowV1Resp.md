# GetConvertTradeFlowV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**list** | [**List[GetConvertTradeFlowV1RespListInner]**](GetConvertTradeFlowV1RespListInner.md) |  | [optional] 
**more_data** | **bool** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_convert_trade_flow_v1_resp import GetConvertTradeFlowV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertTradeFlowV1Resp from a JSON string
get_convert_trade_flow_v1_resp_instance = GetConvertTradeFlowV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetConvertTradeFlowV1Resp.to_json())

# convert the object into a dict
get_convert_trade_flow_v1_resp_dict = get_convert_trade_flow_v1_resp_instance.to_dict()
# create an instance of GetConvertTradeFlowV1Resp from a dict
get_convert_trade_flow_v1_resp_from_dict = GetConvertTradeFlowV1Resp.from_dict(get_convert_trade_flow_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


