# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MarginGetMarginAllOrdersV1RespItem(BaseModel):
    """
    MarginGetMarginAllOrdersV1RespItem
    """ # noqa: E501
    client_order_id: Optional[StrictStr] = Field(default=None, alias="clientOrderId")
    cummulative_quote_qty: Optional[StrictStr] = Field(default=None, alias="cummulativeQuoteQty")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    iceberg_qty: Optional[StrictStr] = Field(default=None, alias="icebergQty")
    is_isolated: Optional[StrictBool] = Field(default=None, alias="isIsolated")
    is_working: Optional[StrictBool] = Field(default=None, alias="isWorking")
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    orig_qty: Optional[StrictStr] = Field(default=None, alias="origQty")
    price: Optional[StrictStr] = None
    self_trade_prevention_mode: Optional[StrictStr] = Field(default=None, alias="selfTradePreventionMode")
    side: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    stop_price: Optional[StrictStr] = Field(default=None, alias="stopPrice")
    symbol: Optional[StrictStr] = None
    time: Optional[StrictInt] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    type: Optional[StrictStr] = None
    update_time: Optional[StrictInt] = Field(default=None, alias="updateTime")
    __properties: ClassVar[List[str]] = ["clientOrderId", "cummulativeQuoteQty", "executedQty", "icebergQty", "isIsolated", "isWorking", "orderId", "origQty", "price", "selfTradePreventionMode", "side", "status", "stopPrice", "symbol", "time", "timeInForce", "type", "updateTime"]

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
        """Create an instance of MarginGetMarginAllOrdersV1RespItem from a JSON string"""
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
        """Create an instance of MarginGetMarginAllOrdersV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientOrderId": obj.get("clientOrderId"),
            "cummulativeQuoteQty": obj.get("cummulativeQuoteQty"),
            "executedQty": obj.get("executedQty"),
            "icebergQty": obj.get("icebergQty"),
            "isIsolated": obj.get("isIsolated"),
            "isWorking": obj.get("isWorking"),
            "orderId": obj.get("orderId"),
            "origQty": obj.get("origQty"),
            "price": obj.get("price"),
            "selfTradePreventionMode": obj.get("selfTradePreventionMode"),
            "side": obj.get("side"),
            "status": obj.get("status"),
            "stopPrice": obj.get("stopPrice"),
            "symbol": obj.get("symbol"),
            "time": obj.get("time"),
            "timeInForce": obj.get("timeInForce"),
            "type": obj.get("type"),
            "updateTime": obj.get("updateTime")
        })
        return _obj


