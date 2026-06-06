"""Abstract base class for message optimizers."""

from abc import ABC, abstractmethod

from ai_project.constraints.base import Constraint
from ai_project.optimizer.run import OptimizationRun


class Optimizer(ABC):
    """Defines the contract for message optimization strategies."""

    @abstractmethod
    def optimize(
        self,
        topic: str,
        constraints: list[Constraint],
    ) -> OptimizationRun:
        """Optimizes a message according to the provided constraints.

        Args:
            topic: Topic or subject for which the message is being
                optimized.
            constraints: Collection of constraints that the optimized
                message must satisfy.

        Returns:
            An OptimizationRun containing the best message found and
            metadata describing the optimization process.
        """
        pass
