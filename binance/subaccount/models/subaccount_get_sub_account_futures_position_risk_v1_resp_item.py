# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SubaccountGetSubAccountFuturesPositionRiskV1RespItem(BaseModel):
    """
    SubaccountGetSubAccountFuturesPositionRiskV1RespItem
    """ # noqa: E501
    entry_price: Optional[StrictStr] = Field(default=None, alias="entryPrice")
    leverage: Optional[StrictStr] = None
    liquidation_price: Optional[StrictStr] = Field(default=None, alias="liquidationPrice")
    mark_price: Optional[StrictStr] = Field(default=None, alias="markPrice")
    max_notional: Optional[StrictStr] = Field(default=None, alias="maxNotional")
    position_amount: Optional[StrictStr] = Field(default=None, alias="positionAmount")
    symbol: Optional[StrictStr] = None
    unrealized_profit: Optional[StrictStr] = Field(default=None, alias="unrealizedProfit")
    __properties: ClassVar[List[str]] = ["entryPrice", "leverage", "liquidationPrice", "markPrice", "maxNotional", "positionAmount", "symbol", "unrealizedProfit"]

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
        """Create an instance of SubaccountGetSubAccountFuturesPositionRiskV1RespItem from a JSON string"""
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
        """Create an instance of SubaccountGetSubAccountFuturesPositionRiskV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entryPrice": obj.get("entryPrice"),
            "leverage": obj.get("leverage"),
            "liquidationPrice": obj.get("liquidationPrice"),
            "markPrice": obj.get("markPrice"),
            "maxNotional": obj.get("maxNotional"),
            "positionAmount": obj.get("positionAmount"),
            "symbol": obj.get("symbol"),
            "unrealizedProfit": obj.get("unrealizedProfit")
        })
        return _obj


