from src.data_loader import load_index_data
from src.strategies import buy_and_hold, momentum_strategy
from src.backtest import compare_strategies, plot_strategies

def main():
    data = load_index_data("^GSPC", "2010-01-01", "2025-01-01")

    bh = buy_and_hold(data["Price"], 1000)

    mom_20 = momentum_strategy(data["Price"], 1000, lookback=20)
    mom_63 = momentum_strategy(data["Price"], 1000, lookback=63)
    mom_126 = momentum_strategy(data["Price"], 1000, lookback=126)

    strategies = {
        "Buy & Hold": bh,
        "Momentum 20j": mom_20,
        "Momentum 63j": mom_63,
        "Momentum 126j": mom_126,
    }

    results = compare_strategies(strategies)
    print("\n=== RÉSUMÉ DU BACKTEST ===")
    print(results.round(4))
    try:
        import dataframe_image as dfi
        dfi.export(results.round(4), "results/metrics_table.png")
    except:
        # fallback : export en CSV
        results.round(4).to_csv("results/metrics_table.csv")
    plot_strategies(
        strategies,
        title="Buy & Hold vs Momentum (20j / 63j / 126j) – S&P 500"
    )


if __name__ == "__main__":
    main()
