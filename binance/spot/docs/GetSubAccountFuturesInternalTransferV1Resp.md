# GetSubAccountFuturesInternalTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**futures_type** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**transfers** | [**List[GetSubAccountFuturesInternalTransferV1RespTransfersInner]**](GetSubAccountFuturesInternalTransferV1RespTransfersInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_internal_transfer_v1_resp import GetSubAccountFuturesInternalTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesInternalTransferV1Resp from a JSON string
get_sub_account_futures_internal_transfer_v1_resp_instance = GetSubAccountFuturesInternalTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesInternalTransferV1Resp.to_json())

# convert the object into a dict
get_sub_account_futures_internal_transfer_v1_resp_dict = get_sub_account_futures_internal_transfer_v1_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesInternalTransferV1Resp from a dict
get_sub_account_futures_internal_transfer_v1_resp_from_dict = GetSubAccountFuturesInternalTransferV1Resp.from_dict(get_sub_account_futures_internal_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


