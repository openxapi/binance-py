# GetSubAccountMarginAccountV1RespMarginTradeCoeffVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_liquidation_bar** | **str** |  | [optional] 
**margin_call_bar** | **str** |  | [optional] 
**normal_bar** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo import GetSubAccountMarginAccountV1RespMarginTradeCoeffVo

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountMarginAccountV1RespMarginTradeCoeffVo from a JSON string
get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo_instance = GetSubAccountMarginAccountV1RespMarginTradeCoeffVo.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountMarginAccountV1RespMarginTradeCoeffVo.to_json())

# convert the object into a dict
get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo_dict = get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo_instance.to_dict()
# create an instance of GetSubAccountMarginAccountV1RespMarginTradeCoeffVo from a dict
get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo_from_dict = GetSubAccountMarginAccountV1RespMarginTradeCoeffVo.from_dict(get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


