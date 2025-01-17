""" Includes custom types used in schemas
"""
import datetime
import sys
from enum import Enum
from typing import Any, Dict, List, Literal, Tuple, Union

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from eolearn.core import EONode, FeatureType
from sentinelhub import BBox

PatchList: TypeAlias = List[Tuple[str, BBox]]
ExecKwargs: TypeAlias = Dict[str, Dict[EONode, Dict[str, object]]]

ImportPath: TypeAlias = str
TimePeriod: TypeAlias = Tuple[datetime.date, datetime.date]

Feature: TypeAlias = Tuple[FeatureType, str]
FeatureSpec: TypeAlias = Union[Tuple[FeatureType, str], FeatureType]

BoolOrAuto: TypeAlias = Union[Literal["auto"], bool]

JsonDict: TypeAlias = Dict[str, Any]
RawSchemaDict: TypeAlias = Dict[str, Any]

AwsAclType: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
    "log-delivery-write",
]


class ProcessingType(Enum):
    RAY = "ray"
    SINGLE = "single"
    MULTI = "multi"
