# CreateDciProductSubscribeV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **str** |  | [optional] 
**auto_compound_plan** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**exercised_coin** | **str** |  | [optional] 
**invest_coin** | **str** |  | [optional] 
**option_type** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**position_id** | **int** |  | [optional] 
**purchase_status** | **str** |  | [optional] 
**purchase_time** | **int** |  | [optional] 
**settle_date** | **int** |  | [optional] 
**strike_price** | **str** |  | [optional] 
**subscription_amount** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_dci_product_subscribe_v1_resp import CreateDciProductSubscribeV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDciProductSubscribeV1Resp from a JSON string
create_dci_product_subscribe_v1_resp_instance = CreateDciProductSubscribeV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateDciProductSubscribeV1Resp.to_json())

# convert the object into a dict
create_dci_product_subscribe_v1_resp_dict = create_dci_product_subscribe_v1_resp_instance.to_dict()
# create an instance of CreateDciProductSubscribeV1Resp from a dict
create_dci_product_subscribe_v1_resp_from_dict = CreateDciProductSubscribeV1Resp.from_dict(create_dci_product_subscribe_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


