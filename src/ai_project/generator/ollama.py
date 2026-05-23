"""Ollama-based implementation of the text generator interface."""

# Third-party
import ollama

# Local
from ai_project.constraints.base import Constraint
from ai_project.generator.base import Generator
from ai_project.generator.prompt import build_prompt


class OllamaGenerator(Generator):
    """Text generator powered by an Ollama language model."""

    def __init__(
        self,
        model: str,
        base_url: str,
    ) -> None:
        """Initialize the Ollama generator.

        Args:
            model: Name of the Ollama model to use.
            base_url: Base URL of the Ollama server.
        """
        self.model = model
        self.client = ollama.Client(host=base_url)

    def generate(
        self,
        topic: str,
        constraints: list[Constraint],
    ) -> str:
        """Generate a message that satisfies the given constraints.

        Builds a prompt from the topic and constraints, sends it
        to the Ollama model, and returns the generated message.

        Args:
            topic: The topic or subject for the generated message.
            constraints: Constraints the generated message must satisfy.

        Returns:
            The generated message as a string.
        """
        prompt = build_prompt(topic, constraints)

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content
