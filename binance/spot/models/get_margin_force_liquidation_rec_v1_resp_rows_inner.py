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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetMarginForceLiquidationRecV1RespRowsInner(BaseModel):
    """
    GetMarginForceLiquidationRecV1RespRowsInner
    """ # noqa: E501
    avg_price: Optional[StrictStr] = Field(default=None, alias="avgPrice")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    is_isolated: Optional[StrictBool] = Field(default=None, alias="isIsolated")
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    price: Optional[StrictStr] = None
    qty: Optional[StrictStr] = None
    side: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    updated_time: Optional[StrictInt] = Field(default=None, alias="updatedTime")
    __properties: ClassVar[List[str]] = ["avgPrice", "executedQty", "isIsolated", "orderId", "price", "qty", "side", "symbol", "timeInForce", "updatedTime"]

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
        """Create an instance of GetMarginForceLiquidationRecV1RespRowsInner from a JSON string"""
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
        """Create an instance of GetMarginForceLiquidationRecV1RespRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgPrice": obj.get("avgPrice"),
            "executedQty": obj.get("executedQty"),
            "isIsolated": obj.get("isIsolated"),
            "orderId": obj.get("orderId"),
            "price": obj.get("price"),
            "qty": obj.get("qty"),
            "side": obj.get("side"),
            "symbol": obj.get("symbol"),
            "timeInForce": obj.get("timeInForce"),
            "updatedTime": obj.get("updatedTime")
        })
        return _obj


