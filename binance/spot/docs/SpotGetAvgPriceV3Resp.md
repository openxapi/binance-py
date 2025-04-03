# SpotGetAvgPriceV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_time** | **int** |  | [optional] 
**mins** | **int** |  | [optional] 
**price** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_avg_price_v3_resp import SpotGetAvgPriceV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAvgPriceV3Resp from a JSON string
spot_get_avg_price_v3_resp_instance = SpotGetAvgPriceV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetAvgPriceV3Resp.to_json())

# convert the object into a dict
spot_get_avg_price_v3_resp_dict = spot_get_avg_price_v3_resp_instance.to_dict()
# create an instance of SpotGetAvgPriceV3Resp from a dict
spot_get_avg_price_v3_resp_from_dict = SpotGetAvgPriceV3Resp.from_dict(spot_get_avg_price_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


