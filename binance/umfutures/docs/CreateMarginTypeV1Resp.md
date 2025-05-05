# CreateMarginTypeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.create_margin_type_v1_resp import CreateMarginTypeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginTypeV1Resp from a JSON string
create_margin_type_v1_resp_instance = CreateMarginTypeV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginTypeV1Resp.to_json())

# convert the object into a dict
create_margin_type_v1_resp_dict = create_margin_type_v1_resp_instance.to_dict()
# create an instance of CreateMarginTypeV1Resp from a dict
create_margin_type_v1_resp_from_dict = CreateMarginTypeV1Resp.from_dict(create_margin_type_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


