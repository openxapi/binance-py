# MarginGetMarginApiKeyV1Resp


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
from binance.margin.models.margin_get_margin_api_key_v1_resp import MarginGetMarginApiKeyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginApiKeyV1Resp from a JSON string
margin_get_margin_api_key_v1_resp_instance = MarginGetMarginApiKeyV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginApiKeyV1Resp.to_json())

# convert the object into a dict
margin_get_margin_api_key_v1_resp_dict = margin_get_margin_api_key_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginApiKeyV1Resp from a dict
margin_get_margin_api_key_v1_resp_from_dict = MarginGetMarginApiKeyV1Resp.from_dict(margin_get_margin_api_key_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


