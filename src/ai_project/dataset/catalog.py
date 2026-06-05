"""Provides predefined benchmark instances for evaluation and testing.

This module defines a collection of benchmark instances with varying
difficulty levels. Each instance combines a topic with a set of
constraints that generated messages must satisfy.
"""

from ai_project.constraints import (
    ForbiddenWordConstraint,
    MaxWordsConstraint,
    MinWordsConstraint,
    RequiredWordConstraint,
)
from ai_project.dataset.models import Instance

# ---------------------------------------------------------------------------
# Easy instances
# ---------------------------------------------------------------------------

AI_EDUCATION = Instance(
    topic="Benefits of artificial intelligence in education",
    constraints=[
        MinWordsConstraint(20),
        RequiredWordConstraint(["education"]),
    ],
)

HEALTHY_HABITS = Instance(
    topic="Healthy daily habits",
    constraints=[
        MinWordsConstraint(15),
        RequiredWordConstraint(["health"]),
    ],
)

RENEWABLE_ENERGY = Instance(
    topic="Importance of renewable energy",
    constraints=[
        MinWordsConstraint(20),
        RequiredWordConstraint(["energy"]),
    ],
)


# ---------------------------------------------------------------------------
# Medium instances
# ---------------------------------------------------------------------------

REMOTE_WORK = Instance(
    topic="Advantages and challenges of remote work",
    constraints=[
        MinWordsConstraint(30),
        MaxWordsConstraint(60),
        RequiredWordConstraint(["productivity"]),
    ],
)

CYBERSECURITY = Instance(
    topic="Cybersecurity best practices",
    constraints=[
        MinWordsConstraint(25),
        MaxWordsConstraint(50),
        RequiredWordConstraint(["security"]),
    ],
)

CLIMATE_CHANGE = Instance(
    topic="Actions to mitigate climate change",
    constraints=[
        MinWordsConstraint(30),
        RequiredWordConstraint(["climate", "sustainability"]),
        MaxWordsConstraint(70),
    ],
)

ONLINE_LEARNING = Instance(
    topic="The impact of online learning",
    constraints=[
        MaxWordsConstraint(50),
        RequiredWordConstraint(["learning"]),
        ForbiddenWordConstraint(["boring"]),
    ],
)


# ---------------------------------------------------------------------------
# Difficult instances
# ---------------------------------------------------------------------------

SPACE_EXPLORATION = Instance(
    topic="Future of space exploration",
    constraints=[
        MinWordsConstraint(40),
        MaxWordsConstraint(70),
        RequiredWordConstraint(["space", "innovation"]),
        ForbiddenWordConstraint(["impossible"]),
    ],
)

MENTAL_HEALTH = Instance(
    topic="Raising awareness about mental health",
    constraints=[
        MinWordsConstraint(35),
        MaxWordsConstraint(60),
        RequiredWordConstraint(["mental", "support"]),
        ForbiddenWordConstraint(["weakness"]),
    ],
)

SUSTAINABLE_CITIES = Instance(
    topic="Building sustainable cities",
    constraints=[
        MinWordsConstraint(40),
        MaxWordsConstraint(65),
        RequiredWordConstraint(["sustainable", "transportation"]),
        ForbiddenWordConstraint(["pollution"]),
    ],
)


INSTANCES = [
    AI_EDUCATION,
    HEALTHY_HABITS,
    RENEWABLE_ENERGY,
    REMOTE_WORK,
    CYBERSECURITY,
    CLIMATE_CHANGE,
    ONLINE_LEARNING,
    SPACE_EXPLORATION,
    MENTAL_HEALTH,
    SUSTAINABLE_CITIES,
]
