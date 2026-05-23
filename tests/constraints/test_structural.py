"""Tests for structural constraints."""

from ai_project.constraints.structural import (
    ForbiddenWordConstraint,
    MaxWordsConstraint,
    MinWordsConstraint,
    RequiredWordConstraint,
)

# Tests for Max Words Constraint


def test_max_words_constraint_less():
    """Message under limit satisfies the constraint."""
    constraint = MaxWordsConstraint(max_words=5)
    assert constraint.is_satisfied("hello world")


def test_max_words_constraint_equal():
    """Message equal to limit satisfies the constraint."""
    constraint = MaxWordsConstraint(max_words=2)
    assert constraint.is_satisfied("hello world")


def test_max_words_constraint_more():
    """Message over limit does not satisfy the constraint."""
    constraint = MaxWordsConstraint(max_words=2)
    assert not constraint.is_satisfied("hello world again")


# Tests for Min Words Constraint


def test_min_words_constraint_more():
    """Message over limit satisfies the constraint."""
    constraint = MinWordsConstraint(min_words=2)
    assert constraint.is_satisfied("hello world again")


def test_min_words_constraint_equal():
    """Message equal to limit satisfies the constraint."""
    constraint = MinWordsConstraint(min_words=2)
    assert constraint.is_satisfied("hello world")


def test_min_words_constraint_less():
    """Message under limit does not satisfy the constraint."""
    constraint = MinWordsConstraint(min_words=3)
    assert not constraint.is_satisfied("hello world")


# Tests for Forbidden Words Constraint


def test_forbidden_word_constraint_present():
    """Message containing a forbidden word does not satisfy the constraint."""
    constraint = ForbiddenWordConstraint(forbidden_words=["sorry"])
    assert not constraint.is_satisfied("I am sorry")


def test_forbidden_word_constraint_absent():
    """Message without a forbidden word satisfies the constraint."""
    constraint = ForbiddenWordConstraint(forbidden_words=["sorry"])
    assert constraint.is_satisfied("I am happy")


def test_forbidden_word_constraint_punctuation():
    """Forbidden words adjacent to punctuation are still detected."""
    constraint = ForbiddenWordConstraint(forbidden_words=["sorry"])
    assert not constraint.is_satisfied("sorry.")


# Tests for Required Words Constraint


def test_required_word_constraint_present():
    """Message containing a required word satisfies the constraint."""
    constraint = RequiredWordConstraint(required_words=["hello"])
    assert constraint.is_satisfied("hello there")


def test_required_word_constraint_absent():
    """Message without a required word does not satisfy the constraint."""
    constraint = RequiredWordConstraint(required_words=["hello"])
    assert not constraint.is_satisfied("goodbye there")


def test_required_word_constraint_case():
    """Required words match regardless of case."""
    constraint = RequiredWordConstraint(required_words=["hello"])
    assert constraint.is_satisfied("Hello")


# Tests for describe()


def test_max_words_constraint_describe():
    """MaxWordsConstraint.describe should include the maximum word limit."""
    constraint = MaxWordsConstraint(10)

    assert "10" in constraint.describe()


def test_min_words_constraint_describe():
    """MinWordsConstraint.describe should include the minimum word limit."""
    constraint = MinWordsConstraint(5)

    assert "5" in constraint.describe()


def test_forbidden_word_constraint_describe():
    """ForbiddenWordConstraint.describe should include forbidden words."""
    constraint = ForbiddenWordConstraint(["sorry"])

    assert "sorry" in constraint.describe()


def test_required_word_constraint_describe():
    """RequiredWordConstraint.describe should include required words."""
    constraint = RequiredWordConstraint(["help"])

    assert "help" in constraint.describe()
