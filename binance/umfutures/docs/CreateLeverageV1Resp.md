# CreateLeverageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **int** |  | [optional] 
**max_notional_value** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.create_leverage_v1_resp import CreateLeverageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLeverageV1Resp from a JSON string
create_leverage_v1_resp_instance = CreateLeverageV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateLeverageV1Resp.to_json())

# convert the object into a dict
create_leverage_v1_resp_dict = create_leverage_v1_resp_instance.to_dict()
# create an instance of CreateLeverageV1Resp from a dict
create_leverage_v1_resp_from_dict = CreateLeverageV1Resp.from_dict(create_leverage_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


