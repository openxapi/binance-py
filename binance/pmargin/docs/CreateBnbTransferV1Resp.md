# CreateBnbTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.create_bnb_transfer_v1_resp import CreateBnbTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBnbTransferV1Resp from a JSON string
create_bnb_transfer_v1_resp_instance = CreateBnbTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBnbTransferV1Resp.to_json())

# convert the object into a dict
create_bnb_transfer_v1_resp_dict = create_bnb_transfer_v1_resp_instance.to_dict()
# create an instance of CreateBnbTransferV1Resp from a dict
create_bnb_transfer_v1_resp_from_dict = CreateBnbTransferV1Resp.from_dict(create_bnb_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


