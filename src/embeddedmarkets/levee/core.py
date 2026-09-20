"""LeveeBacktest(TM) multiverse simulation engine (pre-alpha).

``run`` validates arguments in this pre-alpha release; the actual multiverse
simulation backend ships with the private-preview engine.
"""

from __future__ import annotations

import re
from typing import Any, Optional

from ..exceptions import BetaUnavailableError


_VALID_SHOCK_MODELS = frozenset({"cgmy"})
_HORIZON_RE = re.compile(r"^\d+D$")


class TailRisk:
    """Container for tail-risk metrics derived from a simulation.

    Pre-alpha placeholder: ``summary`` raises :class:`BetaUnavailableError`
    until the private-preview engine is integrated.
    """

    def summary(self) -> "TailRiskSummary":
        """Return a tail-risk summary."""
        raise BetaUnavailableError()


class TailRiskSummary:
    """Summary statistics for tail risk.

    Pre-alpha placeholder: ``plot_drawdown_distribution`` raises
    :class:`BetaUnavailableError`.
    """

    def plot_drawdown_distribution(self) -> None:
        """Plot the simulated drawdown distribution."""
        raise BetaUnavailableError()


class SimulationResult:
    """Result of a LeveeBacktest(TM) multiverse simulation.

    Pre-alpha placeholder class exposing the API surface documented at
    https://www.embeddedmarkets.com.
    """

    def __init__(
        self,
        strategy: Any = None,
        agents: Any = None,
        market_data: Any = None,
        shock_model: str = "cgmy",
        n_universes: int = 100_000,
        horizon: str = "252D",
        random_seed: Optional[int] = None,
    ) -> None:
        self.strategy = strategy
        self.agents = agents
        self.market_data = market_data
        self.shock_model = shock_model
        self.n_universes = n_universes
        self.horizon = horizon
        self.random_seed = random_seed

    @property
    def tail_risk(self) -> TailRisk:
        """Tail-risk metrics for the simulation."""
        return TailRisk()


def run(
    strategy: Any = None,
    agents: Any = None,
    market_data: Any = None,
    shock_model: str = "cgmy",
    shock_params: Optional[str] = None,
    n_universes: int = 100_000,
    horizon: str = "252D",
    random_seed: Optional[int] = None,
) -> SimulationResult:
    """Propagate a strategy through agent-driven counterfactual histories.

    Args:
        strategy: trading strategy to evaluate.
        agents: agent population produced by ``em.levee.agents.from_config``.
        market_data: historical price series used as the simulation seed.
        shock_model: stochastic shock model; currently only ``"cgmy"`` is
            recognized in pre-alpha validation.
        shock_params: path to calibrated CGMY parameters, or ``None``.
        n_universes: number of simulated alternate histories. Must be positive.
        horizon: simulation horizon string such as ``"252D"``.
        random_seed: optional seed for reproducibility.

    Returns:
        A :class:`SimulationResult` instance (once the backend ships).

    Raises:
        TypeError: if argument types are invalid.
        ValueError: if numeric or enum arguments fail validation.
        BetaUnavailableError: until the private-preview engine is released.
    """
    if not isinstance(shock_model, str):
        raise TypeError("shock_model must be a string.")
    if shock_model.lower() not in _VALID_SHOCK_MODELS:
        raise ValueError(
            f"shock_model currently supports {_VALID_SHOCK_MODELS}; got {shock_model!r}."
        )

    if shock_params is not None and not isinstance(shock_params, str):
        raise TypeError("shock_params must be a string or None.")

    if not isinstance(n_universes, int) or n_universes <= 0:
        raise ValueError("n_universes must be a positive integer.")

    if not isinstance(horizon, str) or not _HORIZON_RE.match(horizon):
        raise ValueError("horizon must match the pattern '<days>D', e.g. '252D'.")

    if random_seed is not None and not isinstance(random_seed, int):
        raise TypeError("random_seed must be an integer or None.")

    raise BetaUnavailableError()


__all__ = (
    "SimulationResult",
    "TailRisk",
    "TailRiskSummary",
    "run",
)

