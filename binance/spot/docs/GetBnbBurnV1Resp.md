# GetBnbBurnV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_bnb_burn** | **bool** |  | [optional] 
**spot_bnb_burn** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_bnb_burn_v1_resp import GetBnbBurnV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBnbBurnV1Resp from a JSON string
get_bnb_burn_v1_resp_instance = GetBnbBurnV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBnbBurnV1Resp.to_json())

# convert the object into a dict
get_bnb_burn_v1_resp_dict = get_bnb_burn_v1_resp_instance.to_dict()
# create an instance of GetBnbBurnV1Resp from a dict
get_bnb_burn_v1_resp_from_dict = GetBnbBurnV1Resp.from_dict(get_bnb_burn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


