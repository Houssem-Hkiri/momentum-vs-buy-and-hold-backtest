import pandas as pd
from src.metrics import (
    compute_cagr,
    compute_volatility,
    compute_max_drawdown,
    compute_sharpe
)
import matplotlib.pyplot as plt



def evaluate_strategy(portfolio_df: pd.DataFrame) -> dict:
    """
    Calcule les métriques d'une stratégie à partir d'un DataFrame
    contenant une colonne 'PortfolioValue'.
    """
    returns = portfolio_df["PortfolioValue"].pct_change().dropna()

    metrics = {
        "CAGR": compute_cagr(returns),
        "Volatility": compute_volatility(returns),
        "Max Drawdown": compute_max_drawdown(portfolio_df["PortfolioValue"]),
        "Sharpe Ratio": compute_sharpe(returns),
    }

    return metrics


def compare_strategies(strategies: dict) -> pd.DataFrame:
    """
    Compare plusieurs stratégies et renvoie un tableau récapitulatif.

    strategies : dict
        {"Nom de stratégie": DataFrame, ...}
    """
    results = {}

    for name, df in strategies.items():
        results[name] = evaluate_strategy(df)

    return pd.DataFrame(results).T

def plot_strategies(strategies: dict, title: str = "Comparaison des stratégies"):
    """
    Trace la valeur de portefeuille de plusieurs stratégies sur un même graphique.

    strategies : dict
        {"Nom de stratégie": DataFrame avec 'PortfolioValue', ...}
    """
    plt.figure(figsize=(10, 6))

    for name, df in strategies.items():
        if "PortfolioValue" not in df.columns:
            continue
        plt.plot(df.index, df["PortfolioValue"], label=name)

    plt.xlabel("Date")
    plt.ylabel("Valeur du portefeuille")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.yscale("log")  # échelle logarithmique (option pro)
    plt.tight_layout()
    plt.savefig("results/strategies_plot.png", dpi=300)

    plt.show()
