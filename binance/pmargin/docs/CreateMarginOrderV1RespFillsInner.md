# CreateMarginOrderV1RespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_margin_order_v1_resp_fills_inner import CreateMarginOrderV1RespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginOrderV1RespFillsInner from a JSON string
create_margin_order_v1_resp_fills_inner_instance = CreateMarginOrderV1RespFillsInner.from_json(json)
# print the JSON string representation of the object
print(CreateMarginOrderV1RespFillsInner.to_json())

# convert the object into a dict
create_margin_order_v1_resp_fills_inner_dict = create_margin_order_v1_resp_fills_inner_instance.to_dict()
# create an instance of CreateMarginOrderV1RespFillsInner from a dict
create_margin_order_v1_resp_fills_inner_from_dict = CreateMarginOrderV1RespFillsInner.from_dict(create_margin_order_v1_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


