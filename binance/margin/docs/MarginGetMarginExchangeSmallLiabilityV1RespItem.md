# MarginGetMarginExchangeSmallLiabilityV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**liability_asset** | **str** |  | [optional] 
**liability_qty** | **float** |  | [optional] 
**principal** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_exchange_small_liability_v1_resp_item import MarginGetMarginExchangeSmallLiabilityV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginExchangeSmallLiabilityV1RespItem from a JSON string
margin_get_margin_exchange_small_liability_v1_resp_item_instance = MarginGetMarginExchangeSmallLiabilityV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginExchangeSmallLiabilityV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_exchange_small_liability_v1_resp_item_dict = margin_get_margin_exchange_small_liability_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginExchangeSmallLiabilityV1RespItem from a dict
margin_get_margin_exchange_small_liability_v1_resp_item_from_dict = MarginGetMarginExchangeSmallLiabilityV1RespItem.from_dict(margin_get_margin_exchange_small_liability_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


