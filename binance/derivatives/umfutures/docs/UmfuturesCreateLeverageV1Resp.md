# UmfuturesCreateLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_create_leverage_v1_resp import UmfuturesCreateLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesCreateLeverageV1Resp from a JSON string
umfutures_create_leverage_v1_resp_instance = UmfuturesCreateLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesCreateLeverageV1Resp.to_json())

# convert the object into a dict
umfutures_create_leverage_v1_resp_dict = umfutures_create_leverage_v1_resp_instance.to_dict()
# create an instance of UmfuturesCreateLeverageV1Resp from a dict
umfutures_create_leverage_v1_resp_from_dict = UmfuturesCreateLeverageV1Resp.from_dict(umfutures_create_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


