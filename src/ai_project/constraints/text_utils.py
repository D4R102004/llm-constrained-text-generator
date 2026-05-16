"""Module for text normalization used in constraints."""

import string


def normalize_words(message: str) -> set[str]:
    """Normalize the input text by converting to lowercase and removing punctuation.

    Args:
        message: The input message to normalize.

    Returns:
        A set of normalized words from the input message.
    """
    return set(word.strip(string.punctuation).lower() for word in message.split())
