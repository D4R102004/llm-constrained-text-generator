"""Tests for dataset models."""

import pytest
from pydantic import ValidationError

from ai_project.constraints.structural import MaxWordsConstraint
from ai_project.dataset.models import Instance


def test_creates_instance_with_valid_data() -> None:
    """Creates an instance when all required fields are provided."""
    constraint = MaxWordsConstraint(10)
    instance = Instance(topic="Artificial Intelligence", constraints=[constraint])
    assert instance.topic == "Artificial Intelligence"
    assert instance.constraints == [constraint]


def test_raises_validation_error_when_topic_is_missing() -> None:
    """Raises a validation error when topic is not provided."""
    with pytest.raises(ValidationError):
        Instance(
            constraints=[],
        )
