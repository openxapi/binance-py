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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from binance.spot.models.get_algo_futures_historical_orders_v1_resp_orders_inner import GetAlgoFuturesHistoricalOrdersV1RespOrdersInner
from typing import Optional, Set
from typing_extensions import Self

class GetAlgoFuturesHistoricalOrdersV1Resp(BaseModel):
    """
    GetAlgoFuturesHistoricalOrdersV1Resp
    """ # noqa: E501
    orders: Optional[List[GetAlgoFuturesHistoricalOrdersV1RespOrdersInner]] = None
    total: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["orders", "total"]

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
        """Create an instance of GetAlgoFuturesHistoricalOrdersV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item_orders in self.orders:
                if _item_orders:
                    _items.append(_item_orders.to_dict())
            _dict['orders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAlgoFuturesHistoricalOrdersV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orders": [GetAlgoFuturesHistoricalOrdersV1RespOrdersInner.from_dict(_item) for _item in obj["orders"]] if obj.get("orders") is not None else None,
            "total": obj.get("total")
        })
        return _obj


