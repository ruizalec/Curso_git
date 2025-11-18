# bot_mexc_prueba.py
import ccxt
import pandas as pd
import pandas_ta as ta
import time
import requests

# =========================
# CONFIGURACIÓN MEXC
# =========================
api_key = ''
api_secret = ''

symbol = 'BTC/USDT'
timeframe = '15m'       # Intervalo corto para pruebas
capital = 100
portion = 0.2
stop_loss_pct = 0.05
take_profit_pct = 0.1

exchange = ccxt.mexc({
    'apiKey': api_key,
    'secret': api_secret,
})

# =========================
# CONFIGURACIÓN TELEGRAM
# =========================
telegram_token = ''
telegram_chat_id = 'Mexc_AlexIA'

def enviar_alerta_telegram(mensaje):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {'chat_id': telegram_chat_id, 'text': mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Error enviando mensaje a Telegram:", e)

# =========================
# FUNCIONES DE TRADING
# =========================
def obtener_datos():
    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calcular_indicadores(df):
    df['EMA10'] = ta.ema(df['close'], length=10)
    df['EMA30'] = ta.ema(df['close'], length=30)
    df['RSI'] = ta.rsi(df['close'], length=14)
    return df

def verificar_senal(df):
    if df['EMA10'].iloc[-2] < df['EMA30'].iloc[-2] and df['EMA10'].iloc[-1] > df['EMA30'].iloc[-1]:
        if df['RSI'].iloc[-1] < 50:
            return 'buy'
    if df['EMA10'].iloc[-2] > df['EMA30'].iloc[-2] and df['EMA10'].iloc[-1] < df['EMA30'].iloc[-1]:
        if df['RSI'].iloc[-1] > 50:
            return 'sell'
    return 'hold'

def gestionar_posicion(open_price, current_price, tipo):
    if tipo == 'buy':
        if current_price <= open_price * (1 - stop_loss_pct):
            return 'stop_loss'
        if current_price >= open_price * (1 + take_profit_pct):
            return 'take_profit'
    elif tipo == 'sell':
        if current_price >= open_price * (1 + stop_loss_pct):
            return 'stop_loss'
        if current_price <= open_price * (1 - take_profit_pct):
            return 'take_profit'
    return 'hold'

# =========================
# LOOP PRINCIPAL
# =========================
posicion_abierta = None
precio_apertura = 0
cantidad = 0

while True:
    try:
        df = obtener_datos()
        df = calcular_indicadores(df)
        signal = verificar_senal(df)
        precio_actual = df['close'].iloc[-1]

        if posicion_abierta is None:
            if signal == 'buy':
                cantidad = (capital * portion) / precio_actual
                # exchange.create_market_buy_order(symbol, cantidad)
                precio_apertura = precio_actual
                posicion_abierta = 'buy'
                enviar_alerta_telegram(f"💚 COMPRA abierta: {cantidad:.6f} {symbol} a {precio_actual}")
            elif signal == 'sell':
                cantidad = (capital * portion) / precio_actual
                # exchange.create_market_sell_order(symbol, cantidad)
                precio_apertura = precio_actual
                posicion_abierta = 'sell'
                enviar_alerta_telegram(f"❤️ VENTA abierta: {cantidad:.6f} {symbol} a {precio_actual}")

        else:
            estado = gestionar_posicion(precio_apertura, precio_actual, posicion_abierta)
            if estado in ['stop_loss', 'take_profit']:
                if posicion_abierta == 'buy':
                    # exchange.create_market_sell_order(symbol, cantidad)
                    enviar_alerta_telegram(f"💔 COMPRA cerrada ({estado}): {cantidad:.6f} {symbol} a {precio_actual}")
                elif posicion_abierta == 'sell':
                    # exchange.create_market_buy_order(symbol, cantidad)
                    enviar_alerta_telegram(f"💔 VENTA cerrada ({estado}): {cantidad:.6f} {symbol} a {precio_actual}")
                posicion_abierta = None
                precio_apertura = 0
                cantidad = 0

    except Exception as e:
        print("Error:", e)
        enviar_alerta_telegram(f"⚠️ Error en bot: {e}")

    time.sleep(900)  # Espera 15 minutos
