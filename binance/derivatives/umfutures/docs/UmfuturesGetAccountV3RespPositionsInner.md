# UmfuturesGetAccountV3RespPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_margin** | **str** |  | [optional] 
**isolated_margin** | **str** |  | [optional] 
**isolated_wallet** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**notional** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_account_v3_resp_positions_inner import UmfuturesGetAccountV3RespPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAccountV3RespPositionsInner from a JSON string
umfutures_get_account_v3_resp_positions_inner_instance = UmfuturesGetAccountV3RespPositionsInner.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAccountV3RespPositionsInner.to_json())

# convert the object into a dict
umfutures_get_account_v3_resp_positions_inner_dict = umfutures_get_account_v3_resp_positions_inner_instance.to_dict()
# create an instance of UmfuturesGetAccountV3RespPositionsInner from a dict
umfutures_get_account_v3_resp_positions_inner_from_dict = UmfuturesGetAccountV3RespPositionsInner.from_dict(umfutures_get_account_v3_resp_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


