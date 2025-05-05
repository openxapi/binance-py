# GetKlinesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**close** | **str** |  | [optional] 
**close_time** | **int** |  | [optional] 
**high** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**low** | **str** |  | [optional] 
**open** | **str** |  | [optional] 
**open_time** | **int** |  | [optional] 
**taker_amount** | **str** |  | [optional] 
**taker_volume** | **str** |  | [optional] 
**trade_count** | **int** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_klines_v1_resp_item import GetKlinesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetKlinesV1RespItem from a JSON string
get_klines_v1_resp_item_instance = GetKlinesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetKlinesV1RespItem.to_json())

# convert the object into a dict
get_klines_v1_resp_item_dict = get_klines_v1_resp_item_instance.to_dict()
# create an instance of GetKlinesV1RespItem from a dict
get_klines_v1_resp_item_from_dict = GetKlinesV1RespItem.from_dict(get_klines_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


