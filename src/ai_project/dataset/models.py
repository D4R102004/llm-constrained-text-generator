"""Defines dataset models used throughout the application.

This module contains data structures that represent benchmark
instances used for message generation and optimization tasks.
"""

from pydantic import BaseModel, ConfigDict

from ai_project.constraints.base import Constraint


class Instance(BaseModel):
    """Represents a message generation instance.

    An instance consists of a topic and a collection of constraints
    that the generated message must satisfy.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    topic: str
    constraints: list[Constraint]
