# CreateCountdownCancelAllV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countdown_time** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.create_countdown_cancel_all_v1_resp import CreateCountdownCancelAllV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCountdownCancelAllV1Resp from a JSON string
create_countdown_cancel_all_v1_resp_instance = CreateCountdownCancelAllV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateCountdownCancelAllV1Resp.to_json())

# convert the object into a dict
create_countdown_cancel_all_v1_resp_dict = create_countdown_cancel_all_v1_resp_instance.to_dict()
# create an instance of CreateCountdownCancelAllV1Resp from a dict
create_countdown_cancel_all_v1_resp_from_dict = CreateCountdownCancelAllV1Resp.from_dict(create_countdown_cancel_all_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


