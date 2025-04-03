# CmfuturesGetAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[CmfuturesGetAccountV1RespAssetsInner]**](CmfuturesGetAccountV1RespAssetsInner.md) |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**fee_tier** | **int** |  | [optional] 
**positions** | [**List[CmfuturesGetAccountV1RespPositionsInner]**](CmfuturesGetAccountV1RespPositionsInner.md) |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp import CmfuturesGetAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetAccountV1Resp from a JSON string
cmfutures_get_account_v1_resp_instance = CmfuturesGetAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetAccountV1Resp.to_json())

# convert the object into a dict
cmfutures_get_account_v1_resp_dict = cmfutures_get_account_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetAccountV1Resp from a dict
cmfutures_get_account_v1_resp_from_dict = CmfuturesGetAccountV1Resp.from_dict(cmfutures_get_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


