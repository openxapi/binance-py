# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from binance.derivatives.umfutures.models.umfutures_get_order_amendment_v1_resp_item_amendment_orig_qty import UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty
from typing import Optional, Set
from typing_extensions import Self

class UmfuturesGetOrderAmendmentV1RespItemAmendment(BaseModel):
    """
    UmfuturesGetOrderAmendmentV1RespItemAmendment
    """ # noqa: E501
    count: Optional[StrictInt] = None
    orig_qty: Optional[UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty] = Field(default=None, alias="origQty")
    price: Optional[UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty] = None
    __properties: ClassVar[List[str]] = ["count", "origQty", "price"]

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
        """Create an instance of UmfuturesGetOrderAmendmentV1RespItemAmendment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of orig_qty
        if self.orig_qty:
            _dict['origQty'] = self.orig_qty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UmfuturesGetOrderAmendmentV1RespItemAmendment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "origQty": UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.from_dict(obj["origQty"]) if obj.get("origQty") is not None else None,
            "price": UmfuturesGetOrderAmendmentV1RespItemAmendmentOrigQty.from_dict(obj["price"]) if obj.get("price") is not None else None
        })
        return _obj


