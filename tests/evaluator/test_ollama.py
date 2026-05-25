from unittest.mock import MagicMock

from ai_project.constraints.base import Constraint
from ai_project.evaluator.ollama import OllamaEvaluator


class TestOllamaEvaluator:
    """Test suite for OllamaEvaluator semantic scoring."""

    def setup_method(self):
        """Set up evaluator with mocked LLM client."""
        self.client = MagicMock()
        self.evaluator = OllamaEvaluator(
            model="llama3", base_url="http://localhost:11434"
        )
        self.evaluator.client = self.client

    def test_all_constraints_satisfied_returns_one(self):
        """Return 1.0 when all constraints return perfect score."""
        # Arrange
        message = "hello world"

        c1 = MagicMock(spec=Constraint)
        c1.describe.return_value = "constraint 1"
        c2 = MagicMock(spec=Constraint)
        c2.describe.return_value = "constraint 2"

        self.client.chat.return_value.message.content = "1.0"

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 1.0
        assert self.client.chat.call_count == 2

    def test_no_constraints_satisfied_returns_zero(self):
        """Return 0.0 when all constraints return zero score."""
        # Arrange
        message = "hello world"

        c1 = MagicMock(spec=Constraint)
        c1.describe.return_value = "constraint 1"
        c2 = MagicMock(spec=Constraint)
        c2.describe.return_value = "constraint 2"

        self.client.chat.return_value.message.content = "0.0"

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 0.0
        assert self.client.chat.call_count == 2

    def test_half_constraints_satisfied_returns_half(self):
        """Return 0.5 when half of constraints are satisfied."""
        # Arrange
        message = "hello world"

        c1 = MagicMock(spec=Constraint)
        c1.describe.return_value = "constraint 1"
        c2 = MagicMock(spec=Constraint)
        c2.describe.return_value = "constraint 2"

        # first call 1.0, second call 0.0
        self.client.chat.side_effect = [
            MagicMock(message=MagicMock(content="1.0")),
            MagicMock(message=MagicMock(content="0.0")),
        ]

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 0.5
        assert self.client.chat.call_count == 2

    def test_empty_constraints_returns_one(self):
        """Return 1.0 when no constraints are provided."""
        # Arrange
        message = "hello world"
        constraints = []

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 1.0
        self.client.chat.assert_not_called()

    def test_invalid_llm_output_returns_zero_fallback(self):
        """Return 0.0 when LLM output cannot be parsed as float."""
        # Arrange
        message = "hello world"

        c1 = MagicMock(spec=Constraint)
        c1.describe.return_value = "constraint 1"

        self.client.chat.return_value.message.content = "this is not a number"

        constraints = [c1]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 0.0
        self.client.chat.assert_called_once()
