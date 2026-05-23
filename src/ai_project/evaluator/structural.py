"""Structural evaluator implementation."""

from ai_project.constraints import Constraint
from ai_project.evaluator.base import Evaluator


class StructuralEvaluator(Evaluator):
    """Evaluate messages using constraint satisfaction rate (CSR)."""

    def evaluate(
        self,
        message: str,
        constraints: list[Constraint],
    ) -> float:
        """Evaluate how well a message satisfies a list of constraints.

        Args:
            message:
                The generated message to evaluate.
            constraints:
                The constraints applied to the message.

        Returns:
            A normalized constraint satisfaction score between
            0.0 and 1.0.
        """
        if not constraints:
            return 1.0

        satisfied_constraints = sum(
            constraint.is_satisfied(message) for constraint in constraints
        )

        return satisfied_constraints / len(constraints)
