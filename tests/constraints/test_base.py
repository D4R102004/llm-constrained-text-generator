"""Tests for the constraint module."""

import pytest

from ia_proyecto.constraints.base import Constraint  # ✅


def test_constraint_instantiation_error():
    """Tests that Constraint cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Constraint()


def test_incomplete_subclass_instantiation_error():
    """Subclass without is_satisfied cannot be instantiated."""

    class IncompleteConstraint(Constraint):
        pass

    with pytest.raises(TypeError):
        IncompleteConstraint()
