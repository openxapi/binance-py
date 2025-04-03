# UmfuturesCreateCountdownCancelAllV1Req


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countdown_time** | **int** |  | 
**recv_window** | **int** |  | [optional] 
**symbol** | **str** |  | [default to '']
**timestamp** | **int** |  | 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesCreateCountdownCancelAllV1Req from a JSON string
umfutures_create_countdown_cancel_all_v1_req_instance = UmfuturesCreateCountdownCancelAllV1Req.from_json(json)
# print the JSON string representation of the object
print(UmfuturesCreateCountdownCancelAllV1Req.to_json())

# convert the object into a dict
umfutures_create_countdown_cancel_all_v1_req_dict = umfutures_create_countdown_cancel_all_v1_req_instance.to_dict()
# create an instance of UmfuturesCreateCountdownCancelAllV1Req from a dict
umfutures_create_countdown_cancel_all_v1_req_from_dict = UmfuturesCreateCountdownCancelAllV1Req.from_dict(umfutures_create_countdown_cancel_all_v1_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


