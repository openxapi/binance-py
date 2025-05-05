# GetFuturesDataTakerBuySellVolRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**taker_buy_vol** | **str** |  | [optional] 
**taker_buy_vol_value** | **str** |  | [optional] 
**taker_sell_vol** | **str** |  | [optional] 
**taker_sell_vol_value** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_futures_data_taker_buy_sell_vol_resp_item import GetFuturesDataTakerBuySellVolRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataTakerBuySellVolRespItem from a JSON string
get_futures_data_taker_buy_sell_vol_resp_item_instance = GetFuturesDataTakerBuySellVolRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataTakerBuySellVolRespItem.to_json())

# convert the object into a dict
get_futures_data_taker_buy_sell_vol_resp_item_dict = get_futures_data_taker_buy_sell_vol_resp_item_instance.to_dict()
# create an instance of GetFuturesDataTakerBuySellVolRespItem from a dict
get_futures_data_taker_buy_sell_vol_resp_item_from_dict = GetFuturesDataTakerBuySellVolRespItem.from_dict(get_futures_data_taker_buy_sell_vol_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


