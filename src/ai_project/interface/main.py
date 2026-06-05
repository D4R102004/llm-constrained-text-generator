"""Command-line entry point for the application.

This module assembles the application's components, executes the
optimization process for predefined dataset instances, and displays
the generated results.
"""

from ai_project.config import settings
from ai_project.dataset import INSTANCES
from ai_project.evaluator.ollama import OllamaEvaluator
from ai_project.generator.ollama import OllamaGenerator
from ai_project.interface.optimization_result import OptimizationResult
from ai_project.optimizer import GreedyOptimizer, Optimizer


def build_optimizer() -> Optimizer:
    """Build and configure the optimizer and its dependencies.

    Returns:
        A fully configured optimizer instance.
    """
    generator = OllamaGenerator(
        model=settings.llm_model,
        base_url=settings.ollama_base_url,
    )
    evaluator = OllamaEvaluator(
        model=settings.llm_model,
        base_url=settings.ollama_base_url,
    )
    return GreedyOptimizer(
        generator=generator,
        evaluator=evaluator,
        max_iterations=settings.max_iterations,
    )


def run_instances(optimizer: Optimizer) -> list[OptimizationResult]:
    """Run the optimization process for all predefined instances.

    Args:
        optimizer: Optimizer used to generate messages.

    Returns:
        A list containing the optimization result for each dataset
        instance.
    """
    results: list[OptimizationResult] = []
    for instance in INSTANCES:
        message = optimizer.optimize(
            topic=instance.topic,
            constraints=instance.constraints,
        )
        results.append(
            OptimizationResult(
                instance=instance,
                message=message,
            )
        )
    return results


def display_results(results: list[OptimizationResult]) -> None:
    """Display optimization results in a human-readable format.

    Args:
        results: Results to display.
    """
    for result in results:
        print("=" * 80)
        print(f"Topic: {result.instance.topic}")
        print("Constraints:")
        for constraint in result.instance.constraints:
            print(f"  - {constraint.describe()}")
        print("\nGenerated Message:")
        print(result.message)
        print()
    print("=" * 80)


def main() -> None:
    """Execute the application workflow."""
    optimizer = build_optimizer()
    results = run_instances(optimizer)
    display_results(results)


if __name__ == "__main__":
    main()
