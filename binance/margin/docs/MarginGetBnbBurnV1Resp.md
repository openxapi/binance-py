# MarginGetBnbBurnV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_bnb_burn** | **bool** |  | [optional] 
**spot_bnb_burn** | **bool** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_bnb_burn_v1_resp import MarginGetBnbBurnV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetBnbBurnV1Resp from a JSON string
margin_get_bnb_burn_v1_resp_instance = MarginGetBnbBurnV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetBnbBurnV1Resp.to_json())

# convert the object into a dict
margin_get_bnb_burn_v1_resp_dict = margin_get_bnb_burn_v1_resp_instance.to_dict()
# create an instance of MarginGetBnbBurnV1Resp from a dict
margin_get_bnb_burn_v1_resp_from_dict = MarginGetBnbBurnV1Resp.from_dict(margin_get_bnb_burn_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


