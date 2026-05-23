"""Prompt construction utilities for text generators."""

from ai_project.constraints.base import Constraint


def build_prompt(topic: str, constraints: list[Constraint]) -> str:
    """Build a prompt for the language model.

    The prompt includes the target topic and all constraint
    descriptions in natural language form.

    Args:
        topic: The topic or subject for the generated message.
        constraints: Constraints the generated message must satisfy.

    Returns:
        A formatted prompt string ready to send to the LLM.
    """
    rules = "\n".join(f"- {constraint.describe()}" for constraint in constraints)

    prompt = (
        f"Generate a message about: {topic}.\n\n"
        f"The message must follow these rules:\n"
        f"{rules}\n\n"
        f"Respond with the message only. "
        f"No explanations, no extra text."
    )

    return prompt
