# MarginGetMarginBorrowRepayV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[MarginGetMarginBorrowRepayV1RespRowsInner]**](MarginGetMarginBorrowRepayV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_borrow_repay_v1_resp import MarginGetMarginBorrowRepayV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginBorrowRepayV1Resp from a JSON string
margin_get_margin_borrow_repay_v1_resp_instance = MarginGetMarginBorrowRepayV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginBorrowRepayV1Resp.to_json())

# convert the object into a dict
margin_get_margin_borrow_repay_v1_resp_dict = margin_get_margin_borrow_repay_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginBorrowRepayV1Resp from a dict
margin_get_margin_borrow_repay_v1_resp_from_dict = MarginGetMarginBorrowRepayV1Resp.from_dict(margin_get_margin_borrow_repay_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


