# SpotGetTimeV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_time_v3_resp import SpotGetTimeV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTimeV3Resp from a JSON string
spot_get_time_v3_resp_instance = SpotGetTimeV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetTimeV3Resp.to_json())

# convert the object into a dict
spot_get_time_v3_resp_dict = spot_get_time_v3_resp_instance.to_dict()
# create an instance of SpotGetTimeV3Resp from a dict
spot_get_time_v3_resp_from_dict = SpotGetTimeV3Resp.from_dict(spot_get_time_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


