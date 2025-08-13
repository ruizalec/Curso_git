import requests

# =========================
# CONFIGURACIÓN TELEGRAM
# =========================
telegram_token = '82763113:AAG_JG6JBGCzODUiDN64NBwTHSBukb7dgcs'       # Reemplaza con tu token
telegram_chat_id = 'Mexc_AlexIA'       # Reemplaza con tu chat ID

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {'chat_id': telegram_chat_id, 'text': mensaje}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensaje enviado correctamente ✅")
        else:
            print("Error al enviar mensaje:", response.text)
    except Exception as e:
        print("Excepción al enviar mensaje:", e)

# =========================
# EJEMPLO DE USO
# =========================
enviar_telegram("Hola desde Python! 🚀")
