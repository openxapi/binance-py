# CreateFeeBurnV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.create_fee_burn_v1_resp import CreateFeeBurnV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeeBurnV1Resp from a JSON string
create_fee_burn_v1_resp_instance = CreateFeeBurnV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateFeeBurnV1Resp.to_json())

# convert the object into a dict
create_fee_burn_v1_resp_dict = create_fee_burn_v1_resp_instance.to_dict()
# create an instance of CreateFeeBurnV1Resp from a dict
create_fee_burn_v1_resp_from_dict = CreateFeeBurnV1Resp.from_dict(create_fee_burn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


