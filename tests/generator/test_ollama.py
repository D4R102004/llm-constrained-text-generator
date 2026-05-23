"""Tests for the OllamaGenerator."""

from unittest.mock import MagicMock

from ai_project.constraints.structural import MaxWordsConstraint
from ai_project.generator.ollama import OllamaGenerator


def test_generate_returns_llm_response():
    """OllamaGenerator returns the message from the LLM."""
    # Arrange
    mock_response = MagicMock()
    mock_response.message.content = "I can help you."

    mock_client = MagicMock()
    mock_client.chat.return_value = mock_response

    generator = OllamaGenerator(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
    )

    generator.client = mock_client

    constraints = [
        MaxWordsConstraint(10),
    ]

    # Act
    result = generator.generate(
        topic="customer support",
        constraints=constraints,
    )

    # Assert
    assert result == "I can help you."


def test_generate_sends_prompt_with_constraints():
    """OllamaGenerator sends topic and constraints in the prompt."""
    # Arrange
    mock_response = MagicMock()
    mock_response.message.content = "I can help you."

    mock_client = MagicMock()
    mock_client.chat.return_value = mock_response

    generator = OllamaGenerator(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
    )

    generator.client = mock_client

    constraints = [
        MaxWordsConstraint(10),
    ]

    # Act
    generator.generate(
        topic="customer support",
        constraints=constraints,
    )

    # Assert
    mock_client.chat.assert_called_once()

    prompt = mock_client.chat.call_args.kwargs["messages"][0]["content"]

    assert "customer support" in prompt
    assert "at most 10 words" in prompt
