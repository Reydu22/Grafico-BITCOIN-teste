from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.offline
import plotly.graph_objects as go

cg = CoinGeckoAPI()

bitcoin_infos = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency='brl',days=30)

bitcoindf = pd.DataFrame(bitcoin_infos['prices'],columns=['TimeStamp','Price'])
bitcoindf['Data'] = pd.to_datetime(bitcoindf['TimeStamp'],unit='ms')

candlestick_data = bitcoindf.groupby(bitcoindf.Data.dt.date).agg({'Price': ['min','max','first','last']})

fig = go.Figure(data=[go.Candlestick(x = candlestick_data.index,
        open= candlestick_data['Price']['first'],
        high= candlestick_data['Price']['max'],
        low = candlestick_data['Price']['min'],
        close = candlestick_data['Price']['last'])
])

fig.update_layout(xaxis_rangeslider_visible = False,xaxis_title = 'Data',yaxis_title = 'Preco (REAL R$)', title= 'Grafico Candlestick  BITCOIN')

plotly.offline.plot(fig, filename='./bitcoingrafico.html',auto_open=False)