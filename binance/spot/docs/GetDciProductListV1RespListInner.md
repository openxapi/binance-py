# GetDciProductListV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **str** |  | [optional] 
**auto_compound_plan_list** | **List[str]** |  | [optional] 
**can_purchase** | **bool** |  | [optional] 
**create_timestamp** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**exercised_coin** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invest_coin** | **str** |  | [optional] 
**is_auto_compound_enable** | **bool** |  | [optional] 
**max_amount** | **str** |  | [optional] 
**min_amount** | **str** |  | [optional] 
**option_type** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**purchase_decimal** | **int** |  | [optional] 
**purchase_end_time** | **int** |  | [optional] 
**settle_date** | **int** |  | [optional] 
**strike_price** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_dci_product_list_v1_resp_list_inner import GetDciProductListV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDciProductListV1RespListInner from a JSON string
get_dci_product_list_v1_resp_list_inner_instance = GetDciProductListV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetDciProductListV1RespListInner.to_json())

# convert the object into a dict
get_dci_product_list_v1_resp_list_inner_dict = get_dci_product_list_v1_resp_list_inner_instance.to_dict()
# create an instance of GetDciProductListV1RespListInner from a dict
get_dci_product_list_v1_resp_list_inner_from_dict = GetDciProductListV1RespListInner.from_dict(get_dci_product_list_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


