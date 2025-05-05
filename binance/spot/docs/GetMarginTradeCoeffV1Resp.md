# GetMarginTradeCoeffV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_liquidation_bar** | **str** |  | [optional] 
**margin_call_bar** | **str** |  | [optional] 
**normal_bar** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_trade_coeff_v1_resp import GetMarginTradeCoeffV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginTradeCoeffV1Resp from a JSON string
get_margin_trade_coeff_v1_resp_instance = GetMarginTradeCoeffV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginTradeCoeffV1Resp.to_json())

# convert the object into a dict
get_margin_trade_coeff_v1_resp_dict = get_margin_trade_coeff_v1_resp_instance.to_dict()
# create an instance of GetMarginTradeCoeffV1Resp from a dict
get_margin_trade_coeff_v1_resp_from_dict = GetMarginTradeCoeffV1Resp.from_dict(get_margin_trade_coeff_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


