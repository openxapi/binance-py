# GetDciProductPositionsV1RespListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **str** |  | [optional] 
**auto_compound_plan** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**exercised_coin** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invest_coin** | **str** |  | [optional] 
**option_type** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**purchase_end_time** | **int** |  | [optional] 
**purchase_status** | **str** |  | [optional] 
**settle_date** | **int** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**subscription_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_dci_product_positions_v1_resp_list_inner import GetDciProductPositionsV1RespListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDciProductPositionsV1RespListInner from a JSON string
get_dci_product_positions_v1_resp_list_inner_instance = GetDciProductPositionsV1RespListInner.from_json(json)
# print the JSON string representation of the object
print(GetDciProductPositionsV1RespListInner.to_json())

# convert the object into a dict
get_dci_product_positions_v1_resp_list_inner_dict = get_dci_product_positions_v1_resp_list_inner_instance.to_dict()
# create an instance of GetDciProductPositionsV1RespListInner from a dict
get_dci_product_positions_v1_resp_list_inner_from_dict = GetDciProductPositionsV1RespListInner.from_dict(get_dci_product_positions_v1_resp_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


