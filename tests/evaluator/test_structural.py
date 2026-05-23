from unittest.mock import MagicMock

from ai_project.evaluator import StructuralEvaluator


class TestStructuralEvaluator:
    """Test suite for StructuralEvaluator CSR computation."""

    def setup_method(self):
        """Set up a fresh evaluator instance for each test."""
        self.evaluator = StructuralEvaluator()

    def test_all_constraints_satisfied_returns_one(self):
        """Return 1.0 when all constraints are satisfied by the message."""
        # Arrange
        message = "hello world"

        c1 = MagicMock()
        c1.is_satisfied.return_value = True

        c2 = MagicMock()
        c2.is_satisfied.return_value = True

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 1.0
        c1.is_satisfied.assert_called_once_with(message)
        c2.is_satisfied.assert_called_once_with(message)

    def test_no_constraints_satisfied_returns_zero(self):
        """Return 0.0 when no constraints are satisfied by the message."""
        # Arrange
        message = "hello world"

        c1 = MagicMock()
        c1.is_satisfied.return_value = False

        c2 = MagicMock()
        c2.is_satisfied.return_value = False

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 0.0

    def test_half_constraints_satisfied_returns_half(self):
        """Return 0.5 when half of the constraints are satisfied."""
        # Arrange
        message = "hello world"

        c1 = MagicMock()
        c1.is_satisfied.return_value = True

        c2 = MagicMock()
        c2.is_satisfied.return_value = False

        constraints = [c1, c2]

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 0.5

    def test_empty_constraints_returns_one(self):
        """Return 1.0 when no constraints are provided."""
        # Arrange
        message = "hello world"
        constraints = []

        # Act
        result = self.evaluator.evaluate(message, constraints)

        # Assert
        assert result == 1.0
