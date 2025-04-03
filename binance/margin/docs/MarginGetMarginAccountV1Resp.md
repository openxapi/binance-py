# MarginGetMarginAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_collateral_value_in_usdt** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**borrow_enabled** | **bool** |  | [optional] 
**collateral_margin_level** | **str** |  | [optional] 
**created** | **bool** |  | [optional] 
**margin_level** | **str** |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 
**total_open_order_loss_in_usdt** | **str** |  | [optional] 
**trade_enabled** | **bool** |  | [optional] 
**transfer_in_enabled** | **bool** |  | [optional] 
**transfer_out_enabled** | **bool** |  | [optional] 
**user_assets** | [**List[MarginGetMarginAccountV1RespUserAssetsInner]**](MarginGetMarginAccountV1RespUserAssetsInner.md) |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_account_v1_resp import MarginGetMarginAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAccountV1Resp from a JSON string
margin_get_margin_account_v1_resp_instance = MarginGetMarginAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAccountV1Resp.to_json())

# convert the object into a dict
margin_get_margin_account_v1_resp_dict = margin_get_margin_account_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginAccountV1Resp from a dict
margin_get_margin_account_v1_resp_from_dict = MarginGetMarginAccountV1Resp.from_dict(margin_get_margin_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


