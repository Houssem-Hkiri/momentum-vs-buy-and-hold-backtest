import yfinance as yf
import pandas as pd

def load_index_data(ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Charge les données historiques d'un indice via yfinance
    et renvoie un DataFrame avec une colonne 'Price'.
    """

    data = yf.download(
        ticker,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=True  # prix déjà ajustés
    )

    if data is None or data.empty:
        raise ValueError(f"Aucune donnée téléchargée pour {ticker} entre {start} et {end}")

    # Aplatir les colonnes si MultiIndex (cas que tu as actuellement)
    if isinstance(data.columns, pd.MultiIndex):
        # on garde seulement le premier niveau (Open, High, Low, Close, etc.)
        data.columns = data.columns.get_level_values(0)

    # Normalisation de l'index
    data = data.rename_axis("Date").reset_index()
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.set_index("Date")

    # On vérifie la colonne de prix
    possible_price_cols = ["Adj Close", "Close", "Price"]
    price_col = None
    for col in possible_price_cols:
        if col in data.columns:
            price_col = col
            break

    if price_col is None:
        raise ValueError(f"Aucune colonne de prix trouvée dans les colonnes : {list(data.columns)}")

    out = data[[price_col]].copy()
    out = out.dropna()
    out = out.rename(columns={price_col: "Price"})

    return out
