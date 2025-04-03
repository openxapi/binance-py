# PmarginGetUmTradeAsynV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_cost_timestamp_of_last30d** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_trade_asyn_v1_resp import PmarginGetUmTradeAsynV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmTradeAsynV1Resp from a JSON string
pmargin_get_um_trade_asyn_v1_resp_instance = PmarginGetUmTradeAsynV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmTradeAsynV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_trade_asyn_v1_resp_dict = pmargin_get_um_trade_asyn_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmTradeAsynV1Resp from a dict
pmargin_get_um_trade_asyn_v1_resp_from_dict = PmarginGetUmTradeAsynV1Resp.from_dict(pmargin_get_um_trade_asyn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


