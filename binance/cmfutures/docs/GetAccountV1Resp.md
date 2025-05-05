# GetAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetAccountV1RespAssetsInner]**](GetAccountV1RespAssetsInner.md) |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**fee_tier** | **int** |  | [optional] 
**positions** | [**List[GetAccountV1RespPositionsInner]**](GetAccountV1RespPositionsInner.md) |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_account_v1_resp import GetAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV1Resp from a JSON string
get_account_v1_resp_instance = GetAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountV1Resp.to_json())

# convert the object into a dict
get_account_v1_resp_dict = get_account_v1_resp_instance.to_dict()
# create an instance of GetAccountV1Resp from a dict
get_account_v1_resp_from_dict = GetAccountV1Resp.from_dict(get_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


