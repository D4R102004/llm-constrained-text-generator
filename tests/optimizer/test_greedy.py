"""Tests for the GreedyOptimizer implementation."""

from unittest.mock import Mock

from ai_project.optimizer.greedy import GreedyOptimizer


def test_returns_best_message_found() -> None:
    """Returns the highest-scoring message generated during optimization."""
    generator = Mock()
    evaluator = Mock()

    generator.generate.side_effect = [
        "first message",
        "best message",
        "third message",
    ]
    evaluator.evaluate.side_effect = [0.2, 0.8, 0.5]

    optimizer = GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=3,
    )

    result = optimizer.optimize("topic", [])

    assert result.message == "best message"
    assert result.iterations_used == 3
    assert result.score_history == (0.2, 0.8, 0.5)


def test_keeps_previous_best_message_when_score_decreases() -> None:
    """Preserves the current best message when a lower score is obtained."""
    generator = Mock()
    evaluator = Mock()

    generator.generate.side_effect = [
        "best message",
        "worse message",
    ]
    evaluator.evaluate.side_effect = [0.8, 0.4]

    optimizer = GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=2,
    )

    result = optimizer.optimize("topic", [])

    assert result.message == "best message"
    assert result.iterations_used == 2
    assert result.score_history == (0.8, 0.4)


def test_stops_early_when_perfect_score_is_reached() -> None:
    """Stops iterating when a candidate achieves a perfect score."""
    generator = Mock()
    evaluator = Mock()

    generator.generate.side_effect = [
        "good message",
        "perfect message",
        "unused message",
    ]
    evaluator.evaluate.side_effect = [0.7, 1.0, 0.5]

    optimizer = GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=10,
    )

    result = optimizer.optimize("topic", [])

    assert result.message == "perfect message"
    assert result.iterations_used == 2
    assert result.score_history == (0.7, 1.0)

    assert generator.generate.call_count == 2
    assert evaluator.evaluate.call_count == 2


def test_respects_max_iterations() -> None:
    """Performs at most the configured number of iterations."""
    generator = Mock()
    evaluator = Mock()

    generator.generate.return_value = "message"
    evaluator.evaluate.return_value = 0.5

    optimizer = GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=3,
    )

    result = optimizer.optimize("topic", [])

    assert result.iterations_used == 3
    assert result.score_history == (0.5, 0.5, 0.5)

    assert generator.generate.call_count == 3
    assert evaluator.evaluate.call_count == 3


def test_passes_failed_constraints_as_feedback() -> None:
    """Provides failed constraints from the current best message as feedback."""
    generator = Mock()
    evaluator = Mock()

    failed_constraint = Mock()
    failed_constraint.is_satisfied.return_value = False

    satisfied_constraint = Mock()
    satisfied_constraint.is_satisfied.return_value = True

    generator.generate.return_value = "candidate"
    evaluator.evaluate.return_value = 0.5

    optimizer = GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=1,
    )

    result = optimizer.optimize(
        "topic",
        [failed_constraint, satisfied_constraint],
    )

    assert result.message == "candidate"
    assert result.iterations_used == 1
    assert result.score_history == (0.5,)

    generator.generate.assert_called_once_with(
        topic="topic",
        constraints=[failed_constraint, satisfied_constraint],
        feedback=[failed_constraint],
    )
