# PmarginCreateUmLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_um_leverage_v1_resp import PmarginCreateUmLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateUmLeverageV1Resp from a JSON string
pmargin_create_um_leverage_v1_resp_instance = PmarginCreateUmLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateUmLeverageV1Resp.to_json())

# convert the object into a dict
pmargin_create_um_leverage_v1_resp_dict = pmargin_create_um_leverage_v1_resp_instance.to_dict()
# create an instance of PmarginCreateUmLeverageV1Resp from a dict
pmargin_create_um_leverage_v1_resp_from_dict = PmarginCreateUmLeverageV1Resp.from_dict(pmargin_create_um_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


