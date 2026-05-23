"""Abstract base class for evaluators."""

from abc import ABC, abstractmethod

from ai_project.constraints import Constraint


class Evaluator(ABC):
    """Abstract base class for message evaluators."""

    @abstractmethod
    def evaluate(
        self,
        message: str,
        constraints: list[Constraint],
    ) -> float:
        """Evaluate how well a message satisfies a list of constraints.

        Return a normalized score between 0.0 and 1.0.

        Args:
            message:
                The generated message to evaluate.
            constraints:
                The constraints applied to the message.

        Returns:
            A normalized constraint satisfaction score between
            0.0 and 1.0.
        """
        pass
