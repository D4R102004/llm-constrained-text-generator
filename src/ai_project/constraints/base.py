"""Abstract base class for all message constraints."""

from abc import ABC, abstractmethod


class Constraint(ABC):
    """Abstract base class for all message constraints."""

    @abstractmethod
    def is_satisfied(self, message: str) -> bool:
        """Check if the constraint is satisfied for the given message.

        Args:
            message: The candidate message to evaluate.

        Returns:
            bool: True if the constraint is satisfied, False otherwise.

        """
        pass

    @abstractmethod
    def describe(self) -> str:
        """Return a natural language description of this constraint.

        Returns:
            str: A human-readable description for use in LLM prompts.

        """
        pass
