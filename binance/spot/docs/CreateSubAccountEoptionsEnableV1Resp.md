# CreateSubAccountEoptionsEnableV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**is_e_options_enabled** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_eoptions_enable_v1_resp import CreateSubAccountEoptionsEnableV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountEoptionsEnableV1Resp from a JSON string
create_sub_account_eoptions_enable_v1_resp_instance = CreateSubAccountEoptionsEnableV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountEoptionsEnableV1Resp.to_json())

# convert the object into a dict
create_sub_account_eoptions_enable_v1_resp_dict = create_sub_account_eoptions_enable_v1_resp_instance.to_dict()
# create an instance of CreateSubAccountEoptionsEnableV1Resp from a dict
create_sub_account_eoptions_enable_v1_resp_from_dict = CreateSubAccountEoptionsEnableV1Resp.from_dict(create_sub_account_eoptions_enable_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


