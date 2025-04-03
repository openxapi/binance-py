# UmfuturesGetLeverageBracketV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[UmfuturesGetLeverageBracketV1RespItemBracketsInner]**](UmfuturesGetLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetLeverageBracketV1Resp from a JSON string
umfutures_get_leverage_bracket_v1_resp_instance = UmfuturesGetLeverageBracketV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetLeverageBracketV1Resp.to_json())

# convert the object into a dict
umfutures_get_leverage_bracket_v1_resp_dict = umfutures_get_leverage_bracket_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetLeverageBracketV1Resp from a dict
umfutures_get_leverage_bracket_v1_resp_from_dict = UmfuturesGetLeverageBracketV1Resp.from_dict(umfutures_get_leverage_bracket_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


