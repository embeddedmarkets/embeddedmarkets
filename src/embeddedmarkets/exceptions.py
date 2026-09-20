"""Exceptions for the pre-alpha build."""


_PRE_ALPHA_MSG = (
    "This is a pre-alpha developer build of 'embeddedmarkets' (v0.1.0a1). "
    "LeveeBacktest(TM) and emPortfolioAnalyzer(TM) are currently in private preview; "
    "this feature will be available once the beta opens. Join the beta notification list at "
    "https://www.embeddedmarkets.com/."
)


class BetaUnavailableError(NotImplementedError):
    """Raised when a feature is not yet available in this pre-alpha build."""

    def __init__(self, msg=None) -> None:
        super().__init__(msg or _PRE_ALPHA_MSG)

