# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

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

class PmarginDeleteCmOrderV1Resp(BaseModel):
    """
    PmarginDeleteCmOrderV1Resp
    """ # noqa: E501
    avg_price: Optional[StrictStr] = Field(default=None, alias="avgPrice")
    client_order_id: Optional[StrictStr] = Field(default=None, alias="clientOrderId")
    cum_base: Optional[StrictStr] = Field(default=None, alias="cumBase")
    cum_qty: Optional[StrictStr] = Field(default=None, alias="cumQty")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    orig_qty: Optional[StrictStr] = Field(default=None, alias="origQty")
    pair: Optional[StrictStr] = None
    position_side: Optional[StrictStr] = Field(default=None, alias="positionSide")
    price: Optional[StrictStr] = None
    reduce_only: Optional[StrictBool] = Field(default=None, alias="reduceOnly")
    side: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    type: Optional[StrictStr] = None
    update_time: Optional[StrictInt] = Field(default=None, alias="updateTime")
    __properties: ClassVar[List[str]] = ["avgPrice", "clientOrderId", "cumBase", "cumQty", "executedQty", "orderId", "origQty", "pair", "positionSide", "price", "reduceOnly", "side", "status", "symbol", "timeInForce", "type", "updateTime"]

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
        """Create an instance of PmarginDeleteCmOrderV1Resp from a JSON string"""
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
        """Create an instance of PmarginDeleteCmOrderV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgPrice": obj.get("avgPrice"),
            "clientOrderId": obj.get("clientOrderId"),
            "cumBase": obj.get("cumBase"),
            "cumQty": obj.get("cumQty"),
            "executedQty": obj.get("executedQty"),
            "orderId": obj.get("orderId"),
            "origQty": obj.get("origQty"),
            "pair": obj.get("pair"),
            "positionSide": obj.get("positionSide"),
            "price": obj.get("price"),
            "reduceOnly": obj.get("reduceOnly"),
            "side": obj.get("side"),
            "status": obj.get("status"),
            "symbol": obj.get("symbol"),
            "timeInForce": obj.get("timeInForce"),
            "type": obj.get("type"),
            "updateTime": obj.get("updateTime")
        })
        return _obj


