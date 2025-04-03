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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from binance.subaccount.models.subaccount_get_managed_subaccount_info_v1_resp_manager_sub_user_info_vo_list_inner import SubaccountGetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner
from typing import Optional, Set
from typing_extensions import Self

class SubaccountGetManagedSubaccountInfoV1Resp(BaseModel):
    """
    SubaccountGetManagedSubaccountInfoV1Resp
    """ # noqa: E501
    manager_sub_user_info_vo_list: Optional[List[SubaccountGetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner]] = Field(default=None, alias="managerSubUserInfoVoList")
    total: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["managerSubUserInfoVoList", "total"]

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
        """Create an instance of SubaccountGetManagedSubaccountInfoV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in manager_sub_user_info_vo_list (list)
        _items = []
        if self.manager_sub_user_info_vo_list:
            for _item_manager_sub_user_info_vo_list in self.manager_sub_user_info_vo_list:
                if _item_manager_sub_user_info_vo_list:
                    _items.append(_item_manager_sub_user_info_vo_list.to_dict())
            _dict['managerSubUserInfoVoList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubaccountGetManagedSubaccountInfoV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "managerSubUserInfoVoList": [SubaccountGetManagedSubaccountInfoV1RespManagerSubUserInfoVoListInner.from_dict(_item) for _item in obj["managerSubUserInfoVoList"]] if obj.get("managerSubUserInfoVoList") is not None else None,
            "total": obj.get("total")
        })
        return _obj


