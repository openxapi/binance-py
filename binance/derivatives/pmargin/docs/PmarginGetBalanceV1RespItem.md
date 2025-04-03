# PmarginGetBalanceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**cm_unrealized_pnl** | **str** |  | [optional] 
**cm_wallet_balance** | **str** |  | [optional] 
**cross_margin_asset** | **str** |  | [optional] 
**cross_margin_borrowed** | **str** |  | [optional] 
**cross_margin_free** | **str** |  | [optional] 
**cross_margin_interest** | **str** |  | [optional] 
**cross_margin_locked** | **str** |  | [optional] 
**negative_balance** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 
**um_unrealized_pnl** | **str** |  | [optional] 
**um_wallet_balance** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_balance_v1_resp_item import PmarginGetBalanceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetBalanceV1RespItem from a JSON string
pmargin_get_balance_v1_resp_item_instance = PmarginGetBalanceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetBalanceV1RespItem.to_json())

# convert the object into a dict
pmargin_get_balance_v1_resp_item_dict = pmargin_get_balance_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetBalanceV1RespItem from a dict
pmargin_get_balance_v1_resp_item_from_dict = PmarginGetBalanceV1RespItem.from_dict(pmargin_get_balance_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


