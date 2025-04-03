# SpotGetExchangeInfoV3RespSorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | **str** |  | [optional] 
**symbols** | **List[str]** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_exchange_info_v3_resp_sors_inner import SpotGetExchangeInfoV3RespSorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetExchangeInfoV3RespSorsInner from a JSON string
spot_get_exchange_info_v3_resp_sors_inner_instance = SpotGetExchangeInfoV3RespSorsInner.from_json(json)
# print the JSON string representation of the object
print(SpotGetExchangeInfoV3RespSorsInner.to_json())

# convert the object into a dict
spot_get_exchange_info_v3_resp_sors_inner_dict = spot_get_exchange_info_v3_resp_sors_inner_instance.to_dict()
# create an instance of SpotGetExchangeInfoV3RespSorsInner from a dict
spot_get_exchange_info_v3_resp_sors_inner_from_dict = SpotGetExchangeInfoV3RespSorsInner.from_dict(spot_get_exchange_info_v3_resp_sors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


