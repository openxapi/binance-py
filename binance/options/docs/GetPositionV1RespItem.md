# GetPositionV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_price** | **str** |  | [optional] 
**expiry_date** | **int** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**mark_value** | **str** |  | [optional] 
**option_side** | **str** |  | [optional] 
**position_cost** | **str** |  | [optional] 
**price_scale** | **int** |  | [optional] 
**quantity** | **str** |  | [optional] 
**quantity_scale** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**reducible_qty** | **str** |  | [optional] 
**ror** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_pnl** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_position_v1_resp_item import GetPositionV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetPositionV1RespItem from a JSON string
get_position_v1_resp_item_instance = GetPositionV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetPositionV1RespItem.to_json())

# convert the object into a dict
get_position_v1_resp_item_dict = get_position_v1_resp_item_instance.to_dict()
# create an instance of GetPositionV1RespItem from a dict
get_position_v1_resp_item_from_dict = GetPositionV1RespItem.from_dict(get_position_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


