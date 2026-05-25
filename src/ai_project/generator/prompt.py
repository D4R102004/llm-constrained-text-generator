"""Prompt construction utilities for text generators."""

from ai_project.constraints.base import Constraint


def build_prompt(
    topic: str,
    constraints: list[Constraint],
    feedback: list[Constraint] | None = None,
) -> str:
    """Build a prompt for the language model.

    The prompt includes the target topic, all constraint
    descriptions, and optional feedback from failed constraints.

    Args:
        topic:
            The topic or subject for the generated message.
        constraints:
            Constraints the generated message must satisfy.
        feedback:
            Constraints that failed in a previous generation attempt.

    Returns:
        A formatted prompt string ready to send to the LLM.
    """
    rules = "\n".join(f"- {constraint.describe()}" for constraint in constraints)
    prompt = (
        f"Generate a message about: {topic}.\n\n"
        f"The message must follow these rules:\n"
        f"{rules}\n\n"
    )
    if feedback:
        feedback_rules = "\n".join(
            f"- {constraint.describe()}" for constraint in feedback
        )
        prompt += (
            "Previous attempts failed to satisfy these constraints:\n"
            f"{feedback_rules}\n\n"
            "Improve the next response to satisfy them.\n\n"
        )
    prompt += "Respond with the message only. No explanations, no extra text."
    return prompt
