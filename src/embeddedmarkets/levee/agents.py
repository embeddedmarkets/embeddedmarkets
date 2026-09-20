"""Agent-population configuration for LeveeBacktest(TM).

``from_config`` validates arguments in this pre-alpha release; fully populated
agent objects ship with the private-preview engine.
"""

from __future__ import annotations

from typing import Optional

from ..exceptions import BetaUnavailableError


INTERACTION_MODELS = (
    "belief_similarity",
    "transaction_network",
    "herding_correlation",
)


class AgentPopulation:
    """A heterogeneous population of AI agents for multiverse simulation.

    This is a pre-alpha placeholder class. Instances will be produced by
    ``from_config`` once the private-preview engine is integrated.
    """

    def __init__(self, path: Optional[str] = None, interaction_model: str = "") -> None:
        self.path = path
        self.interaction_model = interaction_model


def from_config(
    path: Optional[str] = None,
    interaction_model: str = "belief_similarity",
) -> AgentPopulation:
    """Load a heterogeneous agent population from a configuration file.

    Args:
        path: filesystem path to an agent-archetype configuration file.
            Optional during pre-alpha argument validation.
        interaction_model: how agents influence one another. Must be one of
            ``"belief_similarity"``, ``"transaction_network"``, or
            ``"herding_correlation"``.

    Returns:
        An :class:`AgentPopulation` instance.

    Raises:
        TypeError: if ``path`` is not a string or ``None``.
        ValueError: if ``interaction_model`` is not recognized.
        BetaUnavailableError: until the private-preview engine is released.
    """
    if path is not None and not isinstance(path, str):
        raise TypeError("path must be a string or None.")
    if interaction_model not in INTERACTION_MODELS:
        raise ValueError(
            f"interaction_model must be one of {INTERACTION_MODELS}; "
            f"got {interaction_model!r}."
        )
    raise BetaUnavailableError()


__all__ = (
    "AgentPopulation",
    "INTERACTION_MODELS",
    "from_config",
)

