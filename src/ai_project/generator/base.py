"""Abstract base class for text generators."""

from abc import ABC, abstractmethod

from ai_project.constraints.base import Constraint


class Generator(ABC):
    """Abstract interface for all text generators."""

    @abstractmethod
    def generate(
        self,
        topic: str,
        constraints: list[Constraint],
    ) -> str:
        """Generate a message that satisfies the given constraints.

        Args:
            topic: The topic or subject for the message.
            constraints: Constraints the generated message must satisfy.

        Returns:
            A generated message as a string.
        """
