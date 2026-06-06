"""Defines result models produced by optimization strategies.

This module contains immutable data structures that capture the outcome
of an optimization run. These models are intended to transfer
optimization results and execution metadata between application layers
without exposing implementation details of the optimization algorithm.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OptimizationRun:
    """Represents the outcome of a single optimization run.

    An optimization run contains the best message found by the optimizer
    together with metadata describing how the optimization progressed.

    The class is implemented as an immutable value object. All fields
    use immutable types to ensure that optimization results cannot be
    modified after creation.

    Attributes:
        message: Best message produced during optimization.
        iterations_used: Number of iterations executed before the
            optimization terminated.
        score_history: Immutable sequence containing the evaluation
            score obtained at each optimization iteration.
    """

    message: str
    iterations_used: int
    score_history: tuple[float, ...]
