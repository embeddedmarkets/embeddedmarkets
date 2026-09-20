"""Embedded Markets: AI agent-based simulation and risk-management for traders.

This package is the pre-alpha developer release (v0.1.0a1) of the Embedded Markets
Python toolkit. It exposes the planned public API surface for two products in
private preview:

- LeveeBacktest(TM) Engine — multiverse backtesting with LoRA-fine-tuned AI agents.
- emPortfolioAnalyzer(TM) — regime-specific correlation and position sizing.

In this release you can inspect module structure, import documented API paths,
and load portfolio CSVs via ``load_portfolio``. Core simulation and analysis
methods raise :class:`embeddedmarkets.BetaUnavailableError` while the engine
remains in private preview; functionality will expand as the public beta opens.

Join the beta notification list: https://www.embeddedmarkets.com/#pricing
"""

from __future__ import annotations

from .exceptions import BetaUnavailableError
from .portfolio import Portfolio, PortfolioAnalyzer, load_portfolio
from . import levee  # noqa: F401  (exposes em.levee.run)

__version__ = "0.1.0a1"

__all__ = (
    "__version__",
    "BetaUnavailableError",
    "Portfolio",
    "PortfolioAnalyzer",
    "load_portfolio",
    "levee",
)

