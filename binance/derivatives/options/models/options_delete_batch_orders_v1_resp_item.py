# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

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

class OptionsDeleteBatchOrdersV1RespItem(BaseModel):
    """
    OptionsDeleteBatchOrdersV1RespItem
    """ # noqa: E501
    avg_price: Optional[StrictStr] = Field(default=None, alias="avgPrice")
    client_order_id: Optional[StrictStr] = Field(default=None, alias="clientOrderId")
    create_time: Optional[StrictInt] = Field(default=None, alias="createTime")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    fee: Optional[StrictInt] = None
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    price: Optional[StrictStr] = None
    quantity: Optional[StrictStr] = None
    reduce_only: Optional[StrictBool] = Field(default=None, alias="reduceOnly")
    side: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    type: Optional[StrictStr] = None
    update_time: Optional[StrictInt] = Field(default=None, alias="updateTime")
    __properties: ClassVar[List[str]] = ["avgPrice", "clientOrderId", "createTime", "executedQty", "fee", "orderId", "price", "quantity", "reduceOnly", "side", "status", "symbol", "timeInForce", "type", "updateTime"]

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
        """Create an instance of OptionsDeleteBatchOrdersV1RespItem from a JSON string"""
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
        """Create an instance of OptionsDeleteBatchOrdersV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgPrice": obj.get("avgPrice"),
            "clientOrderId": obj.get("clientOrderId"),
            "createTime": obj.get("createTime"),
            "executedQty": obj.get("executedQty"),
            "fee": obj.get("fee"),
            "orderId": obj.get("orderId"),
            "price": obj.get("price"),
            "quantity": obj.get("quantity"),
            "reduceOnly": obj.get("reduceOnly"),
            "side": obj.get("side"),
            "status": obj.get("status"),
            "symbol": obj.get("symbol"),
            "timeInForce": obj.get("timeInForce"),
            "type": obj.get("type"),
            "updateTime": obj.get("updateTime")
        })
        return _obj


