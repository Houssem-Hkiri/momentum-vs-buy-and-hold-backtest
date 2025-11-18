import pandas as pd
import numpy as np

def compute_cagr(returns: pd.Series, periods_per_year: int = 252) -> float:
    """
    Calcule le rendement annualisé (CAGR) à partir d'une série de rendements périodiques.
    """
    cumulative_return = (1 + returns).prod()
    n_periods = returns.shape[0]
    if n_periods == 0:
        return np.nan
    years = n_periods / periods_per_year
    if years == 0:
        return np.nan
    cagr = cumulative_return ** (1 / years) - 1
    return cagr


def compute_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """
    Volatilité annualisée des rendements.
    """
    return returns.std() * np.sqrt(periods_per_year)


def compute_max_drawdown(portfolio_values: pd.Series) -> float:
    """
    Calcule le drawdown maximal d'une courbe de portefeuille.
    """
    running_max = portfolio_values.cummax()
    drawdowns = portfolio_values / running_max - 1
    return drawdowns.min()


def compute_sharpe(returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    """
    Calcule le ratio de Sharpe annualisé.
    returns : rendements périodiques (par ex. journaliers).
    risk_free_rate : taux sans risque annualisé.
    """
    # On convertit le taux sans risque annualisé en taux périodique
    rf_periodic = (1 + risk_free_rate) ** (1 / periods_per_year) - 1
    excess_returns = returns - rf_periodic
    vol = compute_volatility(returns, periods_per_year=periods_per_year)
    if vol == 0:
        return np.nan
    sharpe = excess_returns.mean() / vol * np.sqrt(periods_per_year)
    return sharpe
