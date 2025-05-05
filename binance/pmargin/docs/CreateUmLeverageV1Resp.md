# CreateUmLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_um_leverage_v1_resp import CreateUmLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUmLeverageV1Resp from a JSON string
create_um_leverage_v1_resp_instance = CreateUmLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateUmLeverageV1Resp.to_json())

# convert the object into a dict
create_um_leverage_v1_resp_dict = create_um_leverage_v1_resp_instance.to_dict()
# create an instance of CreateUmLeverageV1Resp from a dict
create_um_leverage_v1_resp_from_dict = CreateUmLeverageV1Resp.from_dict(create_um_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


