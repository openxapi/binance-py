# GetAssetTradeFeeV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_trade_fee_v1_resp_item import GetAssetTradeFeeV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTradeFeeV1RespItem from a JSON string
get_asset_trade_fee_v1_resp_item_instance = GetAssetTradeFeeV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetAssetTradeFeeV1RespItem.to_json())

# convert the object into a dict
get_asset_trade_fee_v1_resp_item_dict = get_asset_trade_fee_v1_resp_item_instance.to_dict()
# create an instance of GetAssetTradeFeeV1RespItem from a dict
get_asset_trade_fee_v1_resp_item_from_dict = GetAssetTradeFeeV1RespItem.from_dict(get_asset_trade_fee_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


