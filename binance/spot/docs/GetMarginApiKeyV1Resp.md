# GetMarginApiKeyV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_name** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**permission_mode** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_api_key_v1_resp import GetMarginApiKeyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginApiKeyV1Resp from a JSON string
get_margin_api_key_v1_resp_instance = GetMarginApiKeyV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginApiKeyV1Resp.to_json())

# convert the object into a dict
get_margin_api_key_v1_resp_dict = get_margin_api_key_v1_resp_instance.to_dict()
# create an instance of GetMarginApiKeyV1Resp from a dict
get_margin_api_key_v1_resp_from_dict = GetMarginApiKeyV1Resp.from_dict(get_margin_api_key_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


