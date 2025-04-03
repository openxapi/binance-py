# PmarginCreateCmLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_cm_leverage_v1_resp import PmarginCreateCmLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateCmLeverageV1Resp from a JSON string
pmargin_create_cm_leverage_v1_resp_instance = PmarginCreateCmLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateCmLeverageV1Resp.to_json())

# convert the object into a dict
pmargin_create_cm_leverage_v1_resp_dict = pmargin_create_cm_leverage_v1_resp_instance.to_dict()
# create an instance of PmarginCreateCmLeverageV1Resp from a dict
pmargin_create_cm_leverage_v1_resp_from_dict = PmarginCreateCmLeverageV1Resp.from_dict(pmargin_create_cm_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


