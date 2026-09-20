# embeddedmarkets

**AI agent-based simulation and risk-management tools for professional traders.**

This is the pre-alpha developer release of the [Embedded Markets](https://www.embeddedmarkets.com)
Python toolkit. It exposes the planned public API surface for two products currently in
private preview:

- **LeveeBacktest™ Engine** — multiverse backtesting powered by LoRA-fine-tuned AI agents,
  network contagion, and fat-tailed CGMY shock models.
- **emPortfolioAnalyzer™** — regime-specific correlation analysis and hypothetical
  position-sizing aligned with return targets, drawdown tolerance, and risk budgets.

> **Pre-alpha status (v0.1.0a1).**
> This release is intended for early evaluation only. Most engine and analyzer methods raise
> `BetaUnavailableError` while the private preview matures toward a public beta in Q2 2027.
> You can load portfolio CSVs, inspect module structure, and import the documented API paths.
> [Join the beta notification list](https://www.embeddedmarkets.com/#pricing) to be notified when
> features become available.

## Why agent-based simulation?

Traditional walk-forward backtests replay a single historical path. Monte Carlo methods extend
that by resampling returns but still treat market participants as passive noise. Embedded Markets'
AI agent-based models (AABMs) go further: agents learn, imitate, herd, and adjust leverage
endogenously, producing emergent feedback loops that conventional backtests miss — including the
herding, model monoculture, and liquidity shocks introduced by autonomous AI trading agents.

## Installation

Install from PyPI:

bash
pip install embeddedmarkets

## Dependencies
Requires Python 3.9 or later. The following dependencies are installed automatically:

networkx
numpy
scipy
scikit-survival
statsmodels

To install the latest pre-alpha directly from the repository:

bash
pip install git+https://github.com/embeddedmarkets/embeddedmarkets.git
For development, clone the repo and install in editable mode:

bash
git clone https://github.com/embeddedmarkets/embeddedmarkets.git
cd embeddedmarkets
pip install -e .

## What works today
In v0.1.x you can explore package structure and load portfolio holdings from a CSV file. All other
engine and analyzer features are stubbed pending the private-preview integration.

python
import embeddedmarkets as em

print(em.__version__)
# 0.1.0a1

# Functional today: parse a holdings CSV into a Portfolio object.
portfolio = em.load_portfolio("holdings.csv")
print(portfolio.holdings)
# {'AAPL': 100.0, 'MSFT': 50.0, ...}
Calling preview-only features raises an informative error:

python
import embeddedmarkets as em

try:
    sim = em.levee.run(strategy=my_strategy, agents=agents, market_data=data)
except em.BetaUnavailableError as exc:
    print(exc)
Planned API
The snippets below show how the public API is expected to look once the beta opens. Method
signatures and behavior are subject to change.

LeveeBacktest™ Engine
python
import embeddedmarkets as em

agents = em.levee.agents.from_config(
    path="configs/agent_archetypes.json",
    interaction_model="belief_similarity",  # alternatives: "transaction_network", "herding_correlation"
)

sim = em.levee.run(
    strategy=my_strategy,
    agents=agents,
    market_data=price_series,       # sim extends it forward
    shock_model="cgmy",
    shock_params="configs/cgmy_baseline.toml",
    n_universes=100000,
    horizon="252D",                 # one trading year
    random_seed=42,
)

summary = sim.tail_risk.summary()
summary.plot_drawdown_distribution()
emPortfolioAnalyzer™
python
portfolio = em.load_portfolio("holdings.csv")   # functional today

analyzer = em.PortfolioAnalyzer(
    portfolio=portfolio,
    objective="max_sortino_ratio",
    max_drawdown=0.15,           # 15% max drawdown over the horizon
    stress_distribution=sim.tail_risk
)

implied_weights = analyzer.evaluate()   # raises BetaUnavailableError in pre-alpha
print(implied_weights)

## Target audience
Embedded Markets is designed for:

Proprietary trading firms and professional traders
Asset managers building tail-risk frameworks
Quantitative researchers studying agent-based market dynamics
Technically oriented individual investors who want to stress-test strategies under counterfactual regimes

## Roadmap
Milestone	Status	Description
Pre-alpha package release	Current — v0.1.0a1	Public API surface, portfolio loading, and informative stub errors
Private preview engine	In development	LoRA-fine-tuned agents, network contagion, CGMY shock models
Public beta	Targeted Q2 2027	Full LeveeBacktest™ Engine and emPortfolioAnalyzer™ functionality
Commercial & open-source tiers	Post-beta	Paid subscriptions plus select open-sourced components
Feedback, support, and contributing
This package will evolve rapidly as the private preview progresses toward beta. We welcome:

## Bug reports and API feedback via GitHub Issues
General inquiries through our contact page
Beta sign-ups at embeddedmarkets.com/#pricing
Select components will be open-sourced; announcements will be made on the website and in release notes.

## Important disclaimers
Embedded Markets is a software provider, not an investment adviser or broker-dealer. The Software
and any outputs — including simulations, backtests, risk metrics, correlation analyses,
position-sizing calculations, or hypothetical risk-adjusted position sizing suggestions — are for
analytical purposes only and do not constitute investment advice.

All simulation and backtest results are hypothetical, have inherent limitations, and may differ
materially from live-market outcomes. Do not use the Software's outputs as the sole basis for any
trading or investment decision without independent validation by qualified professionals.

## License
Use of this pre-alpha release is governed by the license included with the distribution and by the
Terms of Use and Privacy Policy of Embedded Markets, Inc.

Embedded Markets, its logo, LeveeBacktest™, emPortfolioAnalyzer™, and related product names are
trademarks of Embedded Markets, Inc.
