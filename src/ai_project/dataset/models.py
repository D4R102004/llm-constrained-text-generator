"""Defines dataset models used throughout the application.

This module contains data structures that represent benchmark
instances used for message generation and optimization tasks.
"""

from pydantic import BaseModel, ConfigDict

from ai_project.constraints.base import Constraint


class Instance(BaseModel):
    """Represents a benchmark message generation instance.

    An instance defines a generation task together with the
    constraints that the generated message must satisfy. Additional
    metadata such as the instance name and difficulty level can be
    used for experiment tracking and analysis.

    Attributes:
        name: Unique identifier for the benchmark instance.
        difficulty: Difficulty category of the instance.
        topic: Topic on which the message should be generated.
        constraints: Constraints that the generated message must
            satisfy.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    difficulty: str
    topic: str
    constraints: list[Constraint]
