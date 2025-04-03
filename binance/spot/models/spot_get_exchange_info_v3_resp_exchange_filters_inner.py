# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from binance.spot.models.spot_exchange_filter_exchange_max_num_algo_orders import SpotExchangeFilterExchangeMaxNumAlgoOrders
from binance.spot.models.spot_exchange_filter_exchange_max_num_iceberg_orders import SpotExchangeFilterExchangeMaxNumIcebergOrders
from binance.spot.models.spot_exchange_filter_exchange_max_num_order import SpotExchangeFilterExchangeMaxNumOrder
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SPOTGETEXCHANGEINFOV3RESPEXCHANGEFILTERSINNER_ONE_OF_SCHEMAS = ["SpotExchangeFilterExchangeMaxNumAlgoOrders", "SpotExchangeFilterExchangeMaxNumIcebergOrders", "SpotExchangeFilterExchangeMaxNumOrder"]

class SpotGetExchangeInfoV3RespExchangeFiltersInner(BaseModel):
    """
    SpotGetExchangeInfoV3RespExchangeFiltersInner
    """
    # data type: SpotExchangeFilterExchangeMaxNumOrder
    oneof_schema_1_validator: Optional[SpotExchangeFilterExchangeMaxNumOrder] = None
    # data type: SpotExchangeFilterExchangeMaxNumAlgoOrders
    oneof_schema_2_validator: Optional[SpotExchangeFilterExchangeMaxNumAlgoOrders] = None
    # data type: SpotExchangeFilterExchangeMaxNumIcebergOrders
    oneof_schema_3_validator: Optional[SpotExchangeFilterExchangeMaxNumIcebergOrders] = None
    actual_instance: Optional[Union[SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder]] = None
    one_of_schemas: Set[str] = { "SpotExchangeFilterExchangeMaxNumAlgoOrders", "SpotExchangeFilterExchangeMaxNumIcebergOrders", "SpotExchangeFilterExchangeMaxNumOrder" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SpotGetExchangeInfoV3RespExchangeFiltersInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: SpotExchangeFilterExchangeMaxNumOrder
        if not isinstance(v, SpotExchangeFilterExchangeMaxNumOrder):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SpotExchangeFilterExchangeMaxNumOrder`")
        else:
            match += 1
        # validate data type: SpotExchangeFilterExchangeMaxNumAlgoOrders
        if not isinstance(v, SpotExchangeFilterExchangeMaxNumAlgoOrders):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SpotExchangeFilterExchangeMaxNumAlgoOrders`")
        else:
            match += 1
        # validate data type: SpotExchangeFilterExchangeMaxNumIcebergOrders
        if not isinstance(v, SpotExchangeFilterExchangeMaxNumIcebergOrders):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SpotExchangeFilterExchangeMaxNumIcebergOrders`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SpotGetExchangeInfoV3RespExchangeFiltersInner with oneOf schemas: SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SpotGetExchangeInfoV3RespExchangeFiltersInner with oneOf schemas: SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into SpotExchangeFilterExchangeMaxNumOrder
        try:
            instance.actual_instance = SpotExchangeFilterExchangeMaxNumOrder.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SpotExchangeFilterExchangeMaxNumAlgoOrders
        try:
            instance.actual_instance = SpotExchangeFilterExchangeMaxNumAlgoOrders.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SpotExchangeFilterExchangeMaxNumIcebergOrders
        try:
            instance.actual_instance = SpotExchangeFilterExchangeMaxNumIcebergOrders.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SpotGetExchangeInfoV3RespExchangeFiltersInner with oneOf schemas: SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SpotGetExchangeInfoV3RespExchangeFiltersInner with oneOf schemas: SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], SpotExchangeFilterExchangeMaxNumAlgoOrders, SpotExchangeFilterExchangeMaxNumIcebergOrders, SpotExchangeFilterExchangeMaxNumOrder]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


