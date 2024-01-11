import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from tradingview_ta import TA_Handler, Interval

"""
Trading View web = "https://tvdb.brianthe.dev/"
Mirar Tkinter con matplot
"""

print("Si no sabes a que exchage pertenece el ticker que vas a buscar, entra en https://tvdb.brianthe.dev/")
try:
    # Solicitar al usuario que ingrese el ticker, el screener y el exchange
    ticker_input = input("Ingrese el ticker: ").upper()
    screener = input("Ingrese el screener (e.g., 'america'): ").lower()
    exchange = input("Ingrese el exchange (e.g., 'NASDAQ'): ").upper()

    # Obtener datos de Yahoo Finance

    if screener == "crypto":
        ticker = ticker_input + 'USD'
        accion_yf = yf.Ticker(ticker_input + '-USD')
    else:
        ticker = ticker_input
        accion_yf = yf.Ticker(ticker)
    hist = accion_yf.history(period = "1y")
    hist.reset_index(inplace = True)
    
    """
        Parameters:
            period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval : str
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            start: str
                Download start date string (YYYY-MM-DD) or _datetime, inclusive.
                Default is 99 years ago
                E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
            end: str
                Download end date string (YYYY-MM-DD) or _datetime, exclusive.
                Default is now
                E.g. for end="2023-01-01", the last data point will be on "2022-12-31"
    """
    
    # Obtener análisis de TradingView
    handler_tradingv = TA_Handler(
        symbol = ticker,
        screener = screener,
        exchange = exchange,
        interval = Interval.INTERVAL_1_DAY
    )
    analysis_tradingv = handler_tradingv.get_analysis().summary
   
    # Obtener el precio más reciente y el precio inicial
    precio_reciente = hist["Close"].iloc[-1]
    precio_inicial = hist["Close"].iloc[0]

    # Obtener la variación de precio
    variacion = ((precio_reciente - precio_inicial) / precio_inicial) * 100

    # Determinar el color de la línea
    color = "green" if variacion > 0 else "red"
    texto_variacion = "El precio aumentó desde hace 1 año" if variacion > 0 else "El precio disminuyó desde hace 1 año"

    # Crear subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 6))

    # Subplot 1: Gráfico
    ax1.plot(hist["Date"], hist["Close"], color = color)
    ax1.set_ylabel('Precio')
    ax1.set_title(f'Precio de {ticker}', loc = 'center')

    # Subplot 2: Texto de variación y analysis_tradingv
    texto_completo = f'{texto_variacion}\n({variacion:.2f}%)\n\n{analysis_tradingv}'
    ax2.text(0.5, 0.5, texto_completo, ha = 'center', va = 'center', fontsize = 12, color = color, multialignment = 'center')
    ax2.axis('off')  # Oculta los ejes

    # Ajustar el diseño y mostrar la gráfica
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
