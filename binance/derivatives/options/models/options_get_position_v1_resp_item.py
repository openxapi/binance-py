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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OptionsGetPositionV1RespItem(BaseModel):
    """
    OptionsGetPositionV1RespItem
    """ # noqa: E501
    entry_price: Optional[StrictStr] = Field(default=None, alias="entryPrice")
    expiry_date: Optional[StrictInt] = Field(default=None, alias="expiryDate")
    mark_price: Optional[StrictStr] = Field(default=None, alias="markPrice")
    mark_value: Optional[StrictStr] = Field(default=None, alias="markValue")
    option_side: Optional[StrictStr] = Field(default=None, alias="optionSide")
    position_cost: Optional[StrictStr] = Field(default=None, alias="positionCost")
    price_scale: Optional[StrictInt] = Field(default=None, alias="priceScale")
    quantity: Optional[StrictStr] = None
    quantity_scale: Optional[StrictInt] = Field(default=None, alias="quantityScale")
    quote_asset: Optional[StrictStr] = Field(default=None, alias="quoteAsset")
    reducible_qty: Optional[StrictStr] = Field(default=None, alias="reducibleQty")
    ror: Optional[StrictStr] = None
    side: Optional[StrictStr] = None
    strike_price: Optional[StrictStr] = Field(default=None, alias="strikePrice")
    symbol: Optional[StrictStr] = None
    unrealized_pnl: Optional[StrictStr] = Field(default=None, alias="unrealizedPNL")
    __properties: ClassVar[List[str]] = ["entryPrice", "expiryDate", "markPrice", "markValue", "optionSide", "positionCost", "priceScale", "quantity", "quantityScale", "quoteAsset", "reducibleQty", "ror", "side", "strikePrice", "symbol", "unrealizedPNL"]

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
        """Create an instance of OptionsGetPositionV1RespItem from a JSON string"""
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
        """Create an instance of OptionsGetPositionV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entryPrice": obj.get("entryPrice"),
            "expiryDate": obj.get("expiryDate"),
            "markPrice": obj.get("markPrice"),
            "markValue": obj.get("markValue"),
            "optionSide": obj.get("optionSide"),
            "positionCost": obj.get("positionCost"),
            "priceScale": obj.get("priceScale"),
            "quantity": obj.get("quantity"),
            "quantityScale": obj.get("quantityScale"),
            "quoteAsset": obj.get("quoteAsset"),
            "reducibleQty": obj.get("reducibleQty"),
            "ror": obj.get("ror"),
            "side": obj.get("side"),
            "strikePrice": obj.get("strikePrice"),
            "symbol": obj.get("symbol"),
            "unrealizedPNL": obj.get("unrealizedPNL")
        })
        return _obj


