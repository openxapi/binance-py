# UmfuturesGetLeverageBracketV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brackets** | [**List[UmfuturesGetLeverageBracketV1RespItemBracketsInner]**](UmfuturesGetLeverageBracketV1RespItemBracketsInner.md) |  | [optional] 
**notional_coef** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp_item import UmfuturesGetLeverageBracketV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetLeverageBracketV1RespItem from a JSON string
umfutures_get_leverage_bracket_v1_resp_item_instance = UmfuturesGetLeverageBracketV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetLeverageBracketV1RespItem.to_json())

# convert the object into a dict
umfutures_get_leverage_bracket_v1_resp_item_dict = umfutures_get_leverage_bracket_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetLeverageBracketV1RespItem from a dict
umfutures_get_leverage_bracket_v1_resp_item_from_dict = UmfuturesGetLeverageBracketV1RespItem.from_dict(umfutures_get_leverage_bracket_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


