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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from binance.spot.models.get_sub_account_futures_account_summary_v2_resp_future_account_summary_resp import GetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp
from typing import Optional, Set
from typing_extensions import Self

class GetSubAccountFuturesAccountSummaryV2Resp(BaseModel):
    """
    GetSubAccountFuturesAccountSummaryV2Resp
    """ # noqa: E501
    future_account_summary_resp: Optional[GetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp] = Field(default=None, alias="futureAccountSummaryResp")
    __properties: ClassVar[List[str]] = ["futureAccountSummaryResp"]

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
        """Create an instance of GetSubAccountFuturesAccountSummaryV2Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of future_account_summary_resp
        if self.future_account_summary_resp:
            _dict['futureAccountSummaryResp'] = self.future_account_summary_resp.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSubAccountFuturesAccountSummaryV2Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "futureAccountSummaryResp": GetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp.from_dict(obj["futureAccountSummaryResp"]) if obj.get("futureAccountSummaryResp") is not None else None
        })
        return _obj


