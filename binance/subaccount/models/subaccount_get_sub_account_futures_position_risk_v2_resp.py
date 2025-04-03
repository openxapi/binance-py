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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from binance.subaccount.models.subaccount_get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner import SubaccountGetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner
from typing import Optional, Set
from typing_extensions import Self

class SubaccountGetSubAccountFuturesPositionRiskV2Resp(BaseModel):
    """
    SubaccountGetSubAccountFuturesPositionRiskV2Resp
    """ # noqa: E501
    future_position_risk_vos: Optional[List[SubaccountGetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner]] = Field(default=None, alias="futurePositionRiskVos")
    __properties: ClassVar[List[str]] = ["futurePositionRiskVos"]

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
        """Create an instance of SubaccountGetSubAccountFuturesPositionRiskV2Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in future_position_risk_vos (list)
        _items = []
        if self.future_position_risk_vos:
            for _item_future_position_risk_vos in self.future_position_risk_vos:
                if _item_future_position_risk_vos:
                    _items.append(_item_future_position_risk_vos.to_dict())
            _dict['futurePositionRiskVos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubaccountGetSubAccountFuturesPositionRiskV2Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "futurePositionRiskVos": [SubaccountGetSubAccountFuturesPositionRiskV2RespFuturePositionRiskVosInner.from_dict(_item) for _item in obj["futurePositionRiskVos"]] if obj.get("futurePositionRiskVos") is not None else None
        })
        return _obj


