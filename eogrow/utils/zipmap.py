"""A collection of functions to be used with the ZipMapPipeline."""

from typing import Dict, Optional

import numpy as np

from ..core.schemas import BaseSchema
from .validators import optional_field_validator, parse_dtype


class MapParams(BaseSchema):
    mapping: Dict[int, int]
    default: Optional[int]
    dtype: np.dtype
    _parse_dtype = optional_field_validator("dtype", parse_dtype, pre=True)


def map_values(
    array: np.ndarray,
    *,
    mapping: Dict[int, int],
    default: Optional[int] = None,
    dtype: Optional[np.dtype] = None,
) -> np.ndarray:
    """Maps all values from `array` according to a dictionary. A default value can be given, which is assigned to
    values without a corresponding key in the mapping dictionary.

    Vectorizing the `.get` method is faster, but difficult to do with a default (and also loses speed advantage)."""

    if default is not None:
        flat_mapped_array = np.array([mapping.get(x, default) for x in array.ravel()], dtype=dtype)
        return flat_mapped_array.reshape(array.shape)

    mapped_array = np.vectorize(mapping.get)(array)
    return mapped_array.astype(dtype)
