# GetBrokerInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_maker_commission** | **float** |  | [optional] 
**max_sub_account_qty** | **int** |  | [optional] 
**max_taker_commission** | **float** |  | [optional] 
**min_maker_commission** | **float** |  | [optional] 
**min_taker_commission** | **float** |  | [optional] 
**sub_account_qty** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_info_v1_resp import GetBrokerInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerInfoV1Resp from a JSON string
get_broker_info_v1_resp_instance = GetBrokerInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerInfoV1Resp.to_json())

# convert the object into a dict
get_broker_info_v1_resp_dict = get_broker_info_v1_resp_instance.to_dict()
# create an instance of GetBrokerInfoV1Resp from a dict
get_broker_info_v1_resp_from_dict = GetBrokerInfoV1Resp.from_dict(get_broker_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


