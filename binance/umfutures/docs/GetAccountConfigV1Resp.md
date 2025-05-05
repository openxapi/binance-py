# GetAccountConfigV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_deposit** | **bool** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**dual_side_position** | **bool** |  | [optional] 
**fee_tier** | **int** |  | [optional] 
**multi_assets_margin** | **bool** |  | [optional] 
**trade_group_id** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_account_config_v1_resp import GetAccountConfigV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountConfigV1Resp from a JSON string
get_account_config_v1_resp_instance = GetAccountConfigV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountConfigV1Resp.to_json())

# convert the object into a dict
get_account_config_v1_resp_dict = get_account_config_v1_resp_instance.to_dict()
# create an instance of GetAccountConfigV1Resp from a dict
get_account_config_v1_resp_from_dict = GetAccountConfigV1Resp.from_dict(get_account_config_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


