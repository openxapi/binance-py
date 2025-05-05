# CreateBnbBurnV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_bnb_burn** | **bool** |  | [optional] 
**spot_bnb_burn** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.create_bnb_burn_v1_resp import CreateBnbBurnV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBnbBurnV1Resp from a JSON string
create_bnb_burn_v1_resp_instance = CreateBnbBurnV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBnbBurnV1Resp.to_json())

# convert the object into a dict
create_bnb_burn_v1_resp_dict = create_bnb_burn_v1_resp_instance.to_dict()
# create an instance of CreateBnbBurnV1Resp from a dict
create_bnb_burn_v1_resp_from_dict = CreateBnbBurnV1Resp.from_dict(create_bnb_burn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


