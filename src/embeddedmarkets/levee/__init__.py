"""LeveeBacktest(TM): multiverse agent-based simulation engine.

This submodule exposes the planned public API for running strategy simulations
through thousands of heterogeneous, network-connected AI-agent histories. In
the pre-alpha release, ``run`` validates arguments and raises
:class:`embeddedmarkets.BetaUnavailableError`; the full backend ships with the
private-preview engine.
"""

from . import agents
from .agents import AgentPopulation
from .core import run, SimulationResult, TailRisk, TailRiskSummary

__all__ = (
    "agents",
    "AgentPopulation",
    "run",
    "SimulationResult",
    "TailRisk",
    "TailRiskSummary",
)

