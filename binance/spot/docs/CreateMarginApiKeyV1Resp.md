# CreateMarginApiKeyV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_margin_api_key_v1_resp import CreateMarginApiKeyV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginApiKeyV1Resp from a JSON string
create_margin_api_key_v1_resp_instance = CreateMarginApiKeyV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginApiKeyV1Resp.to_json())

# convert the object into a dict
create_margin_api_key_v1_resp_dict = create_margin_api_key_v1_resp_instance.to_dict()
# create an instance of CreateMarginApiKeyV1Resp from a dict
create_margin_api_key_v1_resp_from_dict = CreateMarginApiKeyV1Resp.from_dict(create_margin_api_key_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


