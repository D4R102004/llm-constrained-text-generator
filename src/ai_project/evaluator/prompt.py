"""Prompt construction utilities for the semantic evaluator."""

from ai_project.constraints.base import Constraint


def build_eval_prompt(message: str, constraint: Constraint) -> str:
    """Build a prompt for semantic evaluation using an LLM judge.

    Args:
        message:
            The generated message to evaluate.
        constraint:
            The constraint to evaluate against.

    Returns:
        A formatted prompt instructing the LLM to return a numeric score.
    """
    return (
        f"You are a strict evaluation system.\n"
        f"Your task is to evaluate how well a given message satisfies a constraint.\n\n"
        f"Message:\n{message}\n\n"
        f"Constraint:\n{constraint.describe()}\n\n"
        f"Instructions:\n"
        f"- Return a single number between 0.0 and 1.0.\n"
        f"- 0.0 means the message does not satisfy the constraint at all.\n"
        f"- 1.0 means the message fully satisfies the constraint.\n"
        f"- You must not include explanations.\n"
        f"- You must not include any additional text.\n"
        f"- Output ONLY the number.\n"
    )
