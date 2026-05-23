"""Public interface for the generator package."""

from .base import Generator
from .ollama import OllamaGenerator

__all__ = [
    "Generator",
    "OllamaGenerator",
]
