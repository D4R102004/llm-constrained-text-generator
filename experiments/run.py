"""Run benchmark experiments and persist results to disk.

This script executes all benchmark instances against each evaluator
variant, collects optimization metrics, and stores the results as a
JSON file for subsequent analysis.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from ai_project.config import settings
from ai_project.dataset import INSTANCES
from ai_project.evaluator import OllamaEvaluator, StructuralEvaluator
from ai_project.generator import OllamaGenerator
from ai_project.optimizer import GreedyOptimizer


def main() -> None:
    """Execute all experiment configurations and save their results."""
    generator = OllamaGenerator(
        model=settings.llm_model,
        base_url=settings.ollama_base_url,
    )

    reference_evaluator = StructuralEvaluator()

    evaluators = [
        ("structural", StructuralEvaluator()),
        (
            "ollama",
            OllamaEvaluator(
                model=settings.llm_model,
                base_url=settings.ollama_base_url,
            ),
        ),
    ]

    results: list[dict] = []

    for evaluator_name, evaluator in evaluators:
        for instance in INSTANCES:
            optimizer = GreedyOptimizer(
                generator=generator,
                evaluator=evaluator,
                max_iterations=settings.max_iterations,
            )

            start_time = time.perf_counter()

            run = optimizer.optimize(
                topic=instance.topic,
                constraints=instance.constraints,
            )

            elapsed_seconds = time.perf_counter() - start_time

            optimization_score = run.score_history[-1]

            final_score = reference_evaluator.evaluate(
                run.message,
                instance.constraints,
            )

            results.append(
                {
                    "evaluator": evaluator_name,
                    "instance_name": instance.name,
                    "difficulty": instance.difficulty,
                    "topic": instance.topic,
                    "optimization_score": optimization_score,
                    "final_score": final_score,
                    "iterations_used": run.iterations_used,
                    "elapsed_seconds": elapsed_seconds,
                    "score_history": list(run.score_history),
                    "final_message": run.message,
                    "constraints": [
                        {
                            "description": constraint.describe(),
                            "satisfied": constraint.is_satisfied(
                                run.message,
                            ),
                        }
                        for constraint in instance.constraints
                    ],
                }
            )

    output_path = Path(__file__).parent / "results" / "results.json"

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        mode="w",
        encoding="utf-8",
    ) as file:
        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    main()
