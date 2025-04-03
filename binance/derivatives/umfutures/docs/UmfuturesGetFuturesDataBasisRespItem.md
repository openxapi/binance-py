# UmfuturesGetFuturesDataBasisRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualized_basis_rate** | **str** |  | [optional] 
**basis** | **str** |  | [optional] 
**basis_rate** | **str** |  | [optional] 
**contract_type** | **str** |  | [optional] 
**futures_price** | **str** |  | [optional] 
**index_price** | **str** |  | [optional] 
**pair** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_futures_data_basis_resp_item import UmfuturesGetFuturesDataBasisRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFuturesDataBasisRespItem from a JSON string
umfutures_get_futures_data_basis_resp_item_instance = UmfuturesGetFuturesDataBasisRespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFuturesDataBasisRespItem.to_json())

# convert the object into a dict
umfutures_get_futures_data_basis_resp_item_dict = umfutures_get_futures_data_basis_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFuturesDataBasisRespItem from a dict
umfutures_get_futures_data_basis_resp_item_from_dict = UmfuturesGetFuturesDataBasisRespItem.from_dict(umfutures_get_futures_data_basis_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


