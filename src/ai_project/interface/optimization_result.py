"""Defines result models produced by the optimization pipeline.

This module contains immutable data structures used to represent the
outcome of message optimization. These models are intended to transfer
results between application layers without exposing implementation
details of the optimization process.
"""

from dataclasses import dataclass

from ai_project.dataset import Instance


@dataclass(frozen=True)
class OptimizationResult:
    """Represents the outcome of optimizing a dataset instance.

    An optimization result associates a dataset instance with the
    highest-scoring message generated for that instance. The object is
    immutable to ensure that optimization results remain consistent
    after they have been produced.

    Attributes:
        instance: Dataset instance that was optimized, including its
            topic and associated constraints.
        message: Best message generated for the instance according to
            the optimization strategy and evaluation criteria.
    """

    instance: Instance
    message: str
