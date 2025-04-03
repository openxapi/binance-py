# PmarginGetUmAccountV2Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[PmarginGetCmAccountV1RespAssetsInner]**](PmarginGetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[PmarginGetUmAccountV2RespPositionsInner]**](PmarginGetUmAccountV2RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp import PmarginGetUmAccountV2Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmAccountV2Resp from a JSON string
pmargin_get_um_account_v2_resp_instance = PmarginGetUmAccountV2Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmAccountV2Resp.to_json())

# convert the object into a dict
pmargin_get_um_account_v2_resp_dict = pmargin_get_um_account_v2_resp_instance.to_dict()
# create an instance of PmarginGetUmAccountV2Resp from a dict
pmargin_get_um_account_v2_resp_from_dict = PmarginGetUmAccountV2Resp.from_dict(pmargin_get_um_account_v2_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


