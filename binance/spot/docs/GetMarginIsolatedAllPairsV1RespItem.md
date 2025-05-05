# GetMarginIsolatedAllPairsV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | [optional] 
**is_buy_allowed** | **bool** |  | [optional] 
**is_margin_trade** | **bool** |  | [optional] 
**is_sell_allowed** | **bool** |  | [optional] 
**quote** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_all_pairs_v1_resp_item import GetMarginIsolatedAllPairsV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedAllPairsV1RespItem from a JSON string
get_margin_isolated_all_pairs_v1_resp_item_instance = GetMarginIsolatedAllPairsV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedAllPairsV1RespItem.to_json())

# convert the object into a dict
get_margin_isolated_all_pairs_v1_resp_item_dict = get_margin_isolated_all_pairs_v1_resp_item_instance.to_dict()
# create an instance of GetMarginIsolatedAllPairsV1RespItem from a dict
get_margin_isolated_all_pairs_v1_resp_item_from_dict = GetMarginIsolatedAllPairsV1RespItem.from_dict(get_margin_isolated_all_pairs_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


