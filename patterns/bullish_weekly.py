
class bullish_weekly():
    
    import pandas as pd
    import numpy as np
    import yfinance as yf

    

    final = []
    # cryptos = ['BTC-USD','ETH-USD','USDT-USD','ADA-USD','BNB-USD','XRP-USD','DOGE-USD',
    #         'USDC-USD','MATIC-USD','ETC-USD','EOS-USD','LTC-USD']
    stocks = ['SEYAIND.NS']
    # intervals = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    for i in stocks:
        tickerData = yf.Ticker(i)
        tickerDf = tickerData.history(period = '100d',interval='1wk')
        df = tickerDf
        df = df.drop(['Volume','Dividends','Stock Splits'],axis=1)
        df = df.round(2)
        df['Name'] = i
        data = df.copy()
    #     df = df.iloc[-2:,:]
        bullish = df[(df['Close'].shift(1) < df['Open'].shift(1)) &
                (df['Close'] > df['Open'].shift(1))          &
                (df['Open'] < df['Close'].shift(1))          &
                (df['High'] > df['High'].shift(1))           &
                (df['Low'] < df['Low'].shift(1))
                    ]

        final.append(bullish)
            
    final = pd.concat(final)
    final['Pattern'] = 'Bullish Engulfing'
    bullish_engulfing = final.copy()  