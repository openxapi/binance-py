# CmfuturesGetFuturesDataBasisRespItem


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
from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_basis_resp_item import CmfuturesGetFuturesDataBasisRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetFuturesDataBasisRespItem from a JSON string
cmfutures_get_futures_data_basis_resp_item_instance = CmfuturesGetFuturesDataBasisRespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetFuturesDataBasisRespItem.to_json())

# convert the object into a dict
cmfutures_get_futures_data_basis_resp_item_dict = cmfutures_get_futures_data_basis_resp_item_instance.to_dict()
# create an instance of CmfuturesGetFuturesDataBasisRespItem from a dict
cmfutures_get_futures_data_basis_resp_item_from_dict = CmfuturesGetFuturesDataBasisRespItem.from_dict(cmfutures_get_futures_data_basis_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


