# PmarginGetUmUserTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | **bool** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**maker** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**realized_pnl** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_user_trades_v1_resp_item import PmarginGetUmUserTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmUserTradesV1RespItem from a JSON string
pmargin_get_um_user_trades_v1_resp_item_instance = PmarginGetUmUserTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmUserTradesV1RespItem.to_json())

# convert the object into a dict
pmargin_get_um_user_trades_v1_resp_item_dict = pmargin_get_um_user_trades_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetUmUserTradesV1RespItem from a dict
pmargin_get_um_user_trades_v1_resp_item_from_dict = PmarginGetUmUserTradesV1RespItem.from_dict(pmargin_get_um_user_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


