# SpotRateLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**interval_num** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**rate_limit_type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_rate_limit import SpotRateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SpotRateLimit from a JSON string
spot_rate_limit_instance = SpotRateLimit.from_json(json)
# print the JSON string representation of the object
print(SpotRateLimit.to_json())

# convert the object into a dict
spot_rate_limit_dict = spot_rate_limit_instance.to_dict()
# create an instance of SpotRateLimit from a dict
spot_rate_limit_from_dict = SpotRateLimit.from_dict(spot_rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


