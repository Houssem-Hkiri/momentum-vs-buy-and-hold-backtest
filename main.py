from src.data_loader import load_index_data
from src.strategies import buy_and_hold, momentum_strategy
import matplotlib.pyplot as plt

def main():
    data = load_index_data("^GSPC", "2010-01-01", "2025-01-01")

    bh = buy_and_hold(data["Price"], initial_capital=1_000.0)
    mom = momentum_strategy(data["Price"], initial_capital=1_000.0, lookback=126)

    plt.figure()
    plt.plot(bh.index, bh["PortfolioValue"], label="Buy & Hold")
    plt.plot(mom.index, mom["PortfolioValue"], label="Momentum (126j)")
    plt.xlabel("Date")
    plt.ylabel("Valeur du portefeuille")
    plt.title("Momentum vs Buy & Hold – S&P 500")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
