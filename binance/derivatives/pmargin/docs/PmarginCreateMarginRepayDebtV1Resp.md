# PmarginCreateMarginRepayDebtV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**specify_repay_assets** | **List[str]** |  | [optional] 
**success** | **bool** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_create_margin_repay_debt_v1_resp import PmarginCreateMarginRepayDebtV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginCreateMarginRepayDebtV1Resp from a JSON string
pmargin_create_margin_repay_debt_v1_resp_instance = PmarginCreateMarginRepayDebtV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginCreateMarginRepayDebtV1Resp.to_json())

# convert the object into a dict
pmargin_create_margin_repay_debt_v1_resp_dict = pmargin_create_margin_repay_debt_v1_resp_instance.to_dict()
# create an instance of PmarginCreateMarginRepayDebtV1Resp from a dict
pmargin_create_margin_repay_debt_v1_resp_from_dict = PmarginCreateMarginRepayDebtV1Resp.from_dict(pmargin_create_margin_repay_debt_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


