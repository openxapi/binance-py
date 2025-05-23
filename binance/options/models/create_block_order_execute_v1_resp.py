# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

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
from binance.options.models.create_block_order_execute_v1_resp_legs_inner import CreateBlockOrderExecuteV1RespLegsInner
from typing import Optional, Set
from typing_extensions import Self

class CreateBlockOrderExecuteV1Resp(BaseModel):
    """
    CreateBlockOrderExecuteV1Resp
    """ # noqa: E501
    block_trade_settlement_key: Optional[StrictStr] = Field(default=None, alias="blockTradeSettlementKey")
    create_time: Optional[StrictInt] = Field(default=None, alias="createTime")
    expire_time: Optional[StrictInt] = Field(default=None, alias="expireTime")
    legs: Optional[List[CreateBlockOrderExecuteV1RespLegsInner]] = None
    liquidity: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["blockTradeSettlementKey", "createTime", "expireTime", "legs", "liquidity", "status"]

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
        """Create an instance of CreateBlockOrderExecuteV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item_legs in self.legs:
                if _item_legs:
                    _items.append(_item_legs.to_dict())
            _dict['legs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateBlockOrderExecuteV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blockTradeSettlementKey": obj.get("blockTradeSettlementKey"),
            "createTime": obj.get("createTime"),
            "expireTime": obj.get("expireTime"),
            "legs": [CreateBlockOrderExecuteV1RespLegsInner.from_dict(_item) for _item in obj["legs"]] if obj.get("legs") is not None else None,
            "liquidity": obj.get("liquidity"),
            "status": obj.get("status")
        })
        return _obj


