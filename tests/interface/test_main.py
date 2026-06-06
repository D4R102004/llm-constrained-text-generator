"""Tests for the application entry point."""

from unittest.mock import Mock, patch

from ai_project.constraints import MinWordsConstraint
from ai_project.dataset.models import Instance
from ai_project.interface.main import OptimizationResult, run_instances
from ai_project.optimizer.run import OptimizationRun


@patch("ai_project.interface.main.INSTANCES")
def test_run_instances_returns_results_for_all_instances(
    mock_instances: Mock,
) -> None:
    """Run optimization for all dataset instances and collect results.

    The test verifies that:
    - The optimizer is invoked once per instance.
    - Each invocation receives the correct topic and constraints.
    - The returned results contain the expected instance-message pairs.
    """
    constraint = MinWordsConstraint(10)

    instances = [
        Instance(
            name="instance_1",
            difficulty="easy",
            topic="Topic 1",
            constraints=[constraint],
        ),
        Instance(
            name="instance_2",
            difficulty="medium",
            topic="Topic 2",
            constraints=[constraint],
        ),
    ]

    mock_instances.__iter__.return_value = iter(instances)

    optimizer = Mock()
    optimizer.optimize.side_effect = [
        OptimizationRun(
            message="Generated message 1",
            iterations_used=1,
            score_history=(1.0,),
        ),
        OptimizationRun(
            message="Generated message 2",
            iterations_used=1,
            score_history=(1.0,),
        ),
    ]

    results = run_instances(optimizer)

    assert results == [
        OptimizationResult(
            instance=instances[0],
            message="Generated message 1",
        ),
        OptimizationResult(
            instance=instances[1],
            message="Generated message 2",
        ),
    ]

    assert optimizer.optimize.call_count == len(instances)

    optimizer.optimize.assert_any_call(
        topic=instances[0].topic,
        constraints=instances[0].constraints,
    )

    optimizer.optimize.assert_any_call(
        topic=instances[1].topic,
        constraints=instances[1].constraints,
    )
