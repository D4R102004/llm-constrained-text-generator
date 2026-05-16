"""Public interface for the constraints package."""

from ia_proyecto.constraints.base import Constraint
from ia_proyecto.constraints.structural import (
    ForbiddenWordConstraint,
    MaxWordsConstraint,
    MinWordsConstraint,
    RequiredWordConstraint,
)

__all__ = [
    "Constraint",
    "ForbiddenWordConstraint",
    "MaxWordsConstraint",
    "MinWordsConstraint",
    "RequiredWordConstraint",
]
