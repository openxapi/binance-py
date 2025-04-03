# MarginGetMarginCapitalFlowV1RespItem


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
from binance.margin.models.margin_get_margin_capital_flow_v1_resp_item import MarginGetMarginCapitalFlowV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginCapitalFlowV1RespItem from a JSON string
margin_get_margin_capital_flow_v1_resp_item_instance = MarginGetMarginCapitalFlowV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginCapitalFlowV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_capital_flow_v1_resp_item_dict = margin_get_margin_capital_flow_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginCapitalFlowV1RespItem from a dict
margin_get_margin_capital_flow_v1_resp_item_from_dict = MarginGetMarginCapitalFlowV1RespItem.from_dict(margin_get_margin_capital_flow_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


