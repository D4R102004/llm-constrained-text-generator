"""Structural constraints for the text generator."""

from ai_project.constraints.text_utils import normalize_words

from .base import Constraint


class MaxWordsConstraint(Constraint):
    """Constraint that checks if the message does not exceed a maximum word count."""

    def __init__(self, max_words: int):
        """Initialize the MaxWordConstraint.

        Args:
            max_words: The maximum number of words allowed in the message.
        """
        self.max_words = max_words

    def is_satisfied(self, message: str) -> bool:
        """Check if the message does not exceed the maximum word count.

        Args:
            message: The candidate message to evaluate.

        Returns:
            True if the message has at most max_words words, False otherwise.
        """
        word_count = len(message.split())
        return word_count <= self.max_words


class MinWordsConstraint(Constraint):
    """Constraint that checks if the message meets a minimum word count."""

    def __init__(self, min_words: int):
        """Initialize the MinWordsConstraint.

        Args:
            min_words: The minimum number of words required in the message.
        """
        self.min_words = min_words

    def is_satisfied(self, message: str) -> bool:
        """Check if the message meets the minimum word count.

        Args:
            message: The candidate message to evaluate.

        Returns:
            True if the message has at least min_words words, False otherwise.
        """
        word_count = len(message.split())
        return word_count >= self.min_words


class ForbiddenWordConstraint(Constraint):
    """Constraint that checks if the message does not contain any forbidden words."""

    def __init__(self, forbidden_words: list[str]):
        """Initialize the ForbiddenWordConstraint.

        Args:
            forbidden_words: A list of words that are not allowed in the message.
        """
        self.forbidden_words = set(forbidden_words)

    def is_satisfied(self, message: str) -> bool:
        """Check if the message does not contain any forbidden words.

        Args:
            message: The candidate message to evaluate.

        Returns:
            True if the message does not contain any forbidden words, False otherwise.
        """
        words = normalize_words(message)
        return self.forbidden_words.isdisjoint(words)


class RequiredWordConstraint(Constraint):
    """Constraint that checks if the message contains all required words."""

    def __init__(self, required_words: list[str]):
        """Initialize the RequiredWordConstraint.

        Args:
            required_words: A list of words that must be present in the message.
        """
        self.required_words = set(required_words)

    def is_satisfied(self, message: str) -> bool:
        """Check if the message contains all required words.

        Args:
            message: The candidate message to evaluate.

        Returns:
            True if the message contains all required words, False otherwise.
        """
        words = normalize_words(message)
        return self.required_words.issubset(words)
