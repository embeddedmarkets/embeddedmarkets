"""Portfolio loading and analysis (pre-alpha).

``load_portfolio`` is functional in this pre-alpha developer release.
``PortfolioAnalyzer`` exposes the planned public API and will become fully
functional once the private-preview engine is integrated into the package.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from typing import Optional

from .exceptions import BetaUnavailableError


@dataclass(frozen=True)
class Portfolio:
    """A container for parsed portfolio holdings.

    Attributes:
        holdings: mapping of ticker/asset name to quantity or value (as parsed).
        source:   path the portfolio was loaded from.
    """

    holdings: dict[str, float] = field(default_factory=dict)
    source: str = ""

    @property
    def total(self) -> float:
        """Return the sum of all holding values/quantities."""
        return sum(self.holdings.values())

    def __bool__(self) -> bool:
        """A portfolio is truthy if it contains at least one holding."""
        return bool(self.holdings)


_NAME_HEADERS = frozenset({"ticker", "symbol", "asset"})
_VALUE_HEADERS = frozenset({"quantity", "shares", "weight", "value"})


def load_portfolio(path: str) -> Portfolio:
    """Load holdings from a CSV file.

    Expected columns (case-insensitive): ``ticker``/``symbol``/``asset`` plus
    ``quantity``/``shares``/``weight``/``value``. If headers are absent or
    unrecognized, the first two columns are used as name and amount respectively.

    Args:
        path: filesystem path to the CSV file.

    Returns:
        A :class:`Portfolio` containing the parsed holdings.

    Raises:
        ValueError: if the CSV has only one column and no recognizable headers.
    """
    holdings: dict[str, float] = {}

    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.reader(fh)
        header_row = next(reader, None)

        if header_row is None or not any(h.strip() for h in header_row):
            return Portfolio(holdings=holdings, source=path)

        lowered = [h.strip().lower() for h in header_row]

        try:
            name_idx = next(i for i, h in enumerate(lowered) if h in _NAME_HEADERS)
        except StopIteration:
            name_idx = 0

        try:
            amt_idx = next(
                i for i, h in enumerate(lowered)
                if h in _VALUE_HEADERS and i != name_idx
            )
        except StopIteration:
            amt_idx = 1 if len(lowered) > 1 else None

        if amt_idx is None or amt_idx == name_idx:
            raise ValueError(
                f"Could not resolve ticker and quantity columns in {path!r}. "
                "Expected headers such as 'ticker'/'symbol' and 'quantity'/'shares'."
            )

        for row_number, row in enumerate(reader, start=2):
            if not any(cell.strip() for cell in row):
                continue
            try:
                key = row[name_idx].strip()
                amt = float(row[amt_idx])
            except (IndexError, ValueError):
                continue
            if key:
                holdings[key] = amt

    return Portfolio(holdings=holdings, source=path)


class PortfolioAnalyzer:
    """Evaluate a portfolio's risk/return tradeoff and implied position sizes.

    This class exposes the planned public API for emPortfolioAnalyzer(TM).
    In the pre-alpha release, :meth:`evaluate` raises
    :class:`embeddedmarkets.BetaUnavailableError`; it will return computed
    weights once the private-preview engine is available.
    """

    def __init__(
        self,
        portfolio: Optional[Portfolio] = None,
        objective: str = "max_sortino_ratio",
        max_drawdown: float = 0.15,
        stress_distribution=None,
    ) -> None:
        """Initialize the analyzer.

        Args:
            portfolio: holdings to analyze.
            objective: optimization objective (e.g., ``"max_sortino_ratio"``).
            max_drawdown: maximum acceptable drawdown over the horizon, as a
                fraction in ``(0, 1]``.
            stress_distribution: optional tail-risk distribution from a
                LeveeBacktest(TM) simulation.
        """
        if not (0 < max_drawdown <= 1):
            raise ValueError("max_drawdown must be in (0, 1].")
        self.portfolio = portfolio
        self.objective = objective
        self.max_drawdown = max_drawdown
        self.stress_distribution = stress_distribution

    def evaluate(self) -> dict[str, float]:
        """Return implied position weights.

        Raises:
            BetaUnavailableError: until the private-preview engine is released.
        """
        raise BetaUnavailableError()


__all__ = (
    "Portfolio",
    "PortfolioAnalyzer",
    "load_portfolio",
)

