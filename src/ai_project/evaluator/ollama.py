"""Ollama-based semantic evaluator for constraint satisfaction."""

import ollama

from ai_project.constraints.base import Constraint
from ai_project.evaluator.base import Evaluator
from ai_project.evaluator.prompt import build_eval_prompt


class OllamaEvaluator(Evaluator):
    """Semantic evaluator that uses an Ollama LLM to score constraints."""

    def __init__(self, model: str, base_url: str) -> None:
        """Initialize the Ollama-based semantic evaluator.

        Args:
            model:
                Name of the Ollama model used for semantic evaluation.
            base_url:
                Base URL of the Ollama server (e.g., http://localhost:11434).
        """
        self.model = model
        self.client = ollama.Client(host=base_url)

    def evaluate(self, message: str, constraints: list[Constraint]) -> float:
        """Evaluate a message against semantic constraints using an LLM.

        Args:
            message:
                The generated message to evaluate.
            constraints:
                List of semantic constraints.

        Returns:
            A float between 0.0 and 1.0 representing semantic satisfaction.
        """
        if not constraints:
            return 1.0

        scores: list[float] = []

        for constraint in constraints:
            prompt = build_eval_prompt(message, constraint)
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            raw_output = (response.message.content or "").strip()
            try:
                score = float(raw_output)
            except (ValueError, TypeError, AttributeError):
                score = 0.0
            scores.append(score)

        return sum(scores) / len(scores)
