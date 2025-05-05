# GetMarginTransferV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**trans_from** | **str** |  | [optional] 
**trans_to** | **str** |  | [optional] 
**tx_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_transfer_v1_resp_rows_inner import GetMarginTransferV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginTransferV1RespRowsInner from a JSON string
get_margin_transfer_v1_resp_rows_inner_instance = GetMarginTransferV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginTransferV1RespRowsInner.to_json())

# convert the object into a dict
get_margin_transfer_v1_resp_rows_inner_dict = get_margin_transfer_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetMarginTransferV1RespRowsInner from a dict
get_margin_transfer_v1_resp_rows_inner_from_dict = GetMarginTransferV1RespRowsInner.from_dict(get_margin_transfer_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


