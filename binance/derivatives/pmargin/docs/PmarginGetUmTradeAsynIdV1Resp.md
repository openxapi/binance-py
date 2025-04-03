# PmarginGetUmTradeAsynIdV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** |  | [optional] 
**expiration_timestamp** | **int** |  | [optional] 
**is_expired** | **object** |  | [optional] 
**notified** | **bool** |  | [optional] 
**s3_link** | **object** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_trade_asyn_id_v1_resp import PmarginGetUmTradeAsynIdV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmTradeAsynIdV1Resp from a JSON string
pmargin_get_um_trade_asyn_id_v1_resp_instance = PmarginGetUmTradeAsynIdV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmTradeAsynIdV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_trade_asyn_id_v1_resp_dict = pmargin_get_um_trade_asyn_id_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmTradeAsynIdV1Resp from a dict
pmargin_get_um_trade_asyn_id_v1_resp_from_dict = PmarginGetUmTradeAsynIdV1Resp.from_dict(pmargin_get_um_trade_asyn_id_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


