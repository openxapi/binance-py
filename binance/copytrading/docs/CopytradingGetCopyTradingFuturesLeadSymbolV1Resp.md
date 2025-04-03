# CopytradingGetCopyTradingFuturesLeadSymbolV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**List[CopytradingGetCopyTradingFuturesLeadSymbolV1RespDataInner]**](CopytradingGetCopyTradingFuturesLeadSymbolV1RespDataInner.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp import CopytradingGetCopyTradingFuturesLeadSymbolV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CopytradingGetCopyTradingFuturesLeadSymbolV1Resp from a JSON string
copytrading_get_copy_trading_futures_lead_symbol_v1_resp_instance = CopytradingGetCopyTradingFuturesLeadSymbolV1Resp.from_json(json)
# print the JSON string representation of the object
print(CopytradingGetCopyTradingFuturesLeadSymbolV1Resp.to_json())

# convert the object into a dict
copytrading_get_copy_trading_futures_lead_symbol_v1_resp_dict = copytrading_get_copy_trading_futures_lead_symbol_v1_resp_instance.to_dict()
# create an instance of CopytradingGetCopyTradingFuturesLeadSymbolV1Resp from a dict
copytrading_get_copy_trading_futures_lead_symbol_v1_resp_from_dict = CopytradingGetCopyTradingFuturesLeadSymbolV1Resp.from_dict(copytrading_get_copy_trading_futures_lead_symbol_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


