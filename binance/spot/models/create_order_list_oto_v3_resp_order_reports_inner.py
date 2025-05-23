# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateOrderListOtoV3RespOrderReportsInner(BaseModel):
    """
    CreateOrderListOtoV3RespOrderReportsInner
    """ # noqa: E501
    client_order_id: Optional[StrictStr] = Field(default=None, alias="clientOrderId")
    cummulative_quote_qty: Optional[StrictStr] = Field(default=None, alias="cummulativeQuoteQty")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    order_list_id: Optional[StrictInt] = Field(default=None, alias="orderListId")
    orig_qty: Optional[StrictStr] = Field(default=None, alias="origQty")
    orig_quote_order_qty: Optional[StrictStr] = Field(default=None, alias="origQuoteOrderQty")
    price: Optional[StrictStr] = None
    self_trade_prevention_mode: Optional[StrictStr] = Field(default=None, alias="selfTradePreventionMode")
    side: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    transact_time: Optional[StrictInt] = Field(default=None, alias="transactTime")
    type: Optional[StrictStr] = None
    working_time: Optional[StrictInt] = Field(default=None, alias="workingTime")
    __properties: ClassVar[List[str]] = ["clientOrderId", "cummulativeQuoteQty", "executedQty", "orderId", "orderListId", "origQty", "origQuoteOrderQty", "price", "selfTradePreventionMode", "side", "status", "symbol", "timeInForce", "transactTime", "type", "workingTime"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOrderListOtoV3RespOrderReportsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderListOtoV3RespOrderReportsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientOrderId": obj.get("clientOrderId"),
            "cummulativeQuoteQty": obj.get("cummulativeQuoteQty"),
            "executedQty": obj.get("executedQty"),
            "orderId": obj.get("orderId"),
            "orderListId": obj.get("orderListId"),
            "origQty": obj.get("origQty"),
            "origQuoteOrderQty": obj.get("origQuoteOrderQty"),
            "price": obj.get("price"),
            "selfTradePreventionMode": obj.get("selfTradePreventionMode"),
            "side": obj.get("side"),
            "status": obj.get("status"),
            "symbol": obj.get("symbol"),
            "timeInForce": obj.get("timeInForce"),
            "transactTime": obj.get("transactTime"),
            "type": obj.get("type"),
            "workingTime": obj.get("workingTime")
        })
        return _obj


