# CreateCmLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_cm_leverage_v1_resp import CreateCmLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCmLeverageV1Resp from a JSON string
create_cm_leverage_v1_resp_instance = CreateCmLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateCmLeverageV1Resp.to_json())

# convert the object into a dict
create_cm_leverage_v1_resp_dict = create_cm_leverage_v1_resp_instance.to_dict()
# create an instance of CreateCmLeverageV1Resp from a dict
create_cm_leverage_v1_resp_from_dict = CreateCmLeverageV1Resp.from_dict(create_cm_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


