# PmarginGetMarginOrderListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orders** | [**List[PmarginCreateMarginOrderOcoV1RespOrdersInner]**](PmarginCreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_order_list_v1_resp import PmarginGetMarginOrderListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginOrderListV1Resp from a JSON string
pmargin_get_margin_order_list_v1_resp_instance = PmarginGetMarginOrderListV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginOrderListV1Resp.to_json())

# convert the object into a dict
pmargin_get_margin_order_list_v1_resp_dict = pmargin_get_margin_order_list_v1_resp_instance.to_dict()
# create an instance of PmarginGetMarginOrderListV1Resp from a dict
pmargin_get_margin_order_list_v1_resp_from_dict = PmarginGetMarginOrderListV1Resp.from_dict(pmargin_get_margin_order_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


