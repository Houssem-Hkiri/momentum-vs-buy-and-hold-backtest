import pandas as pd


def buy_and_hold(prices: pd.Series, initial_capital: float = 1000.0) -> pd.DataFrame:
    df = pd.DataFrame(index=prices.index)
    df["Price"] = prices
    df["Returns"] = df["Price"].pct_change().fillna(0.0)
    df["PortfolioValue"] = initial_capital * (1 + df["Returns"]).cumprod()
    return df


def momentum_strategy(prices: pd.Series, initial_capital: float = 1000.0, lookback: int = 126) -> pd.DataFrame:
    df = pd.DataFrame(index=prices.index)
    df["Price"] = prices
    df["Returns"] = df["Price"].pct_change().fillna(0.0)
    df["RollingReturn"] = df["Price"].pct_change(lookback)
    df["Position"] = (df["RollingReturn"] > 0).astype(float)
    df["Position"] = df["Position"].shift(1).fillna(0.0)
    df["StrategyReturns"] = df["Position"] * df["Returns"]
    df["PortfolioValue"] = initial_capital * (1 + df["StrategyReturns"]).cumprod()
    return df

