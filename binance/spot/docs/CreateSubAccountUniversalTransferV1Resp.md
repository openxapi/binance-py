# CreateSubAccountUniversalTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_tran_id** | **str** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_sub_account_universal_transfer_v1_resp import CreateSubAccountUniversalTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountUniversalTransferV1Resp from a JSON string
create_sub_account_universal_transfer_v1_resp_instance = CreateSubAccountUniversalTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountUniversalTransferV1Resp.to_json())

# convert the object into a dict
create_sub_account_universal_transfer_v1_resp_dict = create_sub_account_universal_transfer_v1_resp_instance.to_dict()
# create an instance of CreateSubAccountUniversalTransferV1Resp from a dict
create_sub_account_universal_transfer_v1_resp_from_dict = CreateSubAccountUniversalTransferV1Resp.from_dict(create_sub_account_universal_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


