# GetMarginCapitalFlowV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**tran_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_capital_flow_v1_resp_item import GetMarginCapitalFlowV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginCapitalFlowV1RespItem from a JSON string
get_margin_capital_flow_v1_resp_item_instance = GetMarginCapitalFlowV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginCapitalFlowV1RespItem.to_json())

# convert the object into a dict
get_margin_capital_flow_v1_resp_item_dict = get_margin_capital_flow_v1_resp_item_instance.to_dict()
# create an instance of GetMarginCapitalFlowV1RespItem from a dict
get_margin_capital_flow_v1_resp_item_from_dict = GetMarginCapitalFlowV1RespItem.from_dict(get_margin_capital_flow_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


