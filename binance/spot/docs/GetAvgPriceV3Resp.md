# GetAvgPriceV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_time** | **int** |  | [optional] 
**mins** | **int** |  | [optional] 
**price** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_avg_price_v3_resp import GetAvgPriceV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvgPriceV3Resp from a JSON string
get_avg_price_v3_resp_instance = GetAvgPriceV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetAvgPriceV3Resp.to_json())

# convert the object into a dict
get_avg_price_v3_resp_dict = get_avg_price_v3_resp_instance.to_dict()
# create an instance of GetAvgPriceV3Resp from a dict
get_avg_price_v3_resp_from_dict = GetAvgPriceV3Resp.from_dict(get_avg_price_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


