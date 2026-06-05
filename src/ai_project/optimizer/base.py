"""Abstract base class for message optimizers."""

from abc import ABC, abstractmethod

from ai_project.constraints.base import Constraint


class Optimizer(ABC):
    """Defines the contract for message optimization strategies."""

    @abstractmethod
    def optimize(self, topic: str, constraints: list[Constraint]) -> str:
        """Optimizes a message according to the provided constraints.

        Args:
            topic: Topic or subject for which the message is being optimized.
            constraints: Collection of constraints that the optimized message
                must satisfy.

        Returns:
            The best optimized message that satisfies the given constraints.
        """
        pass
