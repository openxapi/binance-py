# CreateSubAccountBlvtEnableV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**enable_blvt** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_blvt_enable_v1_resp import CreateSubAccountBlvtEnableV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountBlvtEnableV1Resp from a JSON string
create_sub_account_blvt_enable_v1_resp_instance = CreateSubAccountBlvtEnableV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountBlvtEnableV1Resp.to_json())

# convert the object into a dict
create_sub_account_blvt_enable_v1_resp_dict = create_sub_account_blvt_enable_v1_resp_instance.to_dict()
# create an instance of CreateSubAccountBlvtEnableV1Resp from a dict
create_sub_account_blvt_enable_v1_resp_from_dict = CreateSubAccountBlvtEnableV1Resp.from_dict(create_sub_account_blvt_enable_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


