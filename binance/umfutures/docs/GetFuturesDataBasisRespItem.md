# GetFuturesDataBasisRespItem


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
from binance.umfutures.models.get_futures_data_basis_resp_item import GetFuturesDataBasisRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFuturesDataBasisRespItem from a JSON string
get_futures_data_basis_resp_item_instance = GetFuturesDataBasisRespItem.from_json(json)
# print the JSON string representation of the object
print(GetFuturesDataBasisRespItem.to_json())

# convert the object into a dict
get_futures_data_basis_resp_item_dict = get_futures_data_basis_resp_item_instance.to_dict()
# create an instance of GetFuturesDataBasisRespItem from a dict
get_futures_data_basis_resp_item_from_dict = GetFuturesDataBasisRespItem.from_dict(get_futures_data_basis_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


