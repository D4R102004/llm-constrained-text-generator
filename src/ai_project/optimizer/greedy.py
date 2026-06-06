"""Provides a greedy optimization strategy for message generation.

This module contains the GreedyOptimizer implementation, which
iteratively generates candidate messages, evaluates them against a
collection of constraints, and retains the highest-scoring result.
The optimization process terminates when a perfect score is achieved
or when the maximum number of iterations is reached.
"""

from ai_project.constraints.base import Constraint
from ai_project.evaluator.base import Evaluator
from ai_project.generator.base import Generator
from ai_project.optimizer.base import Optimizer
from ai_project.optimizer.run import OptimizationRun


class GreedyOptimizer(Optimizer):
    """Optimizes messages through iterative generation and evaluation.

    The optimizer follows a greedy search strategy in which each
    iteration produces a candidate message, evaluates it against the
    provided constraints, and keeps the best-scoring result found so
    far. The search may terminate early if a perfect score is reached.
    """

    def __init__(
        self,
        generator: Generator,
        evaluator: Evaluator,
        max_iterations: int = 10,
    ) -> None:
        """Initializes a GreedyOptimizer instance.

        Args:
            generator: Component responsible for generating candidate
                messages during each optimization iteration.
            evaluator: Component responsible for scoring candidate
                messages according to the provided constraints.
            max_iterations: Maximum number of optimization iterations
                to perform before stopping the search.
        """
        self.generator = generator
        self.evaluator = evaluator
        self.max_iterations = max_iterations

    def optimize(
        self,
        topic: str,
        constraints: list[Constraint],
    ) -> OptimizationRun:
        """Searches for the highest-scoring message for a topic.

        The method repeatedly generates candidate messages, evaluates
        their compliance with the provided constraints, and retains the
        best candidate found during the search process. Failed
        constraints from the current best message are provided as
        feedback to guide subsequent generations.

        The optimization terminates early when a perfect score is
        achieved or when the configured iteration limit is reached.

        Args:
            topic: Topic for which a message should be generated and
                optimized.
            constraints: Constraints that the generated message must
                satisfy.

        Returns:
            An OptimizationRun containing the best message found and
            metadata describing the optimization process.
        """
        best_message = ""
        best_score = 0.0
        score_history: list[float] = []
        iterations_used = 0

        for iteration in range(self.max_iterations):
            failed_constraints = [
                constraint
                for constraint in constraints
                if not constraint.is_satisfied(best_message)
            ]

            candidate = self.generator.generate(
                topic=topic,
                constraints=constraints,
                feedback=failed_constraints,
            )

            score = self.evaluator.evaluate(candidate, constraints)
            score_history.append(score)
            iterations_used = iteration + 1

            if score > best_score:
                best_message = candidate
                best_score = score

            if best_score == 1.0:
                break

        return OptimizationRun(
            message=best_message,
            iterations_used=iterations_used,
            score_history=tuple(score_history),
        )
