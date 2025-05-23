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

class GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner(BaseModel):
    """
    GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner
    """ # noqa: E501
    bind_parent_email: Optional[StrictStr] = Field(default=None, alias="bindParentEmail")
    bind_parent_user_id: Optional[StrictInt] = Field(default=None, alias="bindParentUserId")
    email: Optional[StrictStr] = None
    insert_time_stamp: Optional[StrictInt] = Field(default=None, alias="insertTimeStamp")
    is_future_enabled: Optional[StrictBool] = Field(default=None, alias="isFutureEnabled")
    is_margin_enabled: Optional[StrictBool] = Field(default=None, alias="isMarginEnabled")
    is_signed_lvt_risk_agreement: Optional[StrictBool] = Field(default=None, alias="isSignedLVTRiskAgreement")
    is_sub_user_enabled: Optional[StrictBool] = Field(default=None, alias="isSubUserEnabled")
    is_user_active: Optional[StrictBool] = Field(default=None, alias="isUserActive")
    managersub_user_id: Optional[StrictInt] = Field(default=None, alias="managersubUserId")
    root_user_id: Optional[StrictInt] = Field(default=None, alias="rootUserId")
    __properties: ClassVar[List[str]] = ["bindParentEmail", "bindParentUserId", "email", "insertTimeStamp", "isFutureEnabled", "isMarginEnabled", "isSignedLVTRiskAgreement", "isSubUserEnabled", "isUserActive", "managersubUserId", "rootUserId"]

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
        """Create an instance of GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner from a JSON string"""
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
        """Create an instance of GetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bindParentEmail": obj.get("bindParentEmail"),
            "bindParentUserId": obj.get("bindParentUserId"),
            "email": obj.get("email"),
            "insertTimeStamp": obj.get("insertTimeStamp"),
            "isFutureEnabled": obj.get("isFutureEnabled"),
            "isMarginEnabled": obj.get("isMarginEnabled"),
            "isSignedLVTRiskAgreement": obj.get("isSignedLVTRiskAgreement"),
            "isSubUserEnabled": obj.get("isSubUserEnabled"),
            "isUserActive": obj.get("isUserActive"),
            "managersubUserId": obj.get("managersubUserId"),
            "rootUserId": obj.get("rootUserId")
        })
        return _obj


