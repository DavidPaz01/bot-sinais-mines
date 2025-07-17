import random
import asyncio
import time
from datetime import datetime, timedelta
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = '7989005994:AAGCZGrvyF1lvMY_OtsAgcQ_NHQl4-uGecE'
CHANNEL_ID = -1002809117020
LINK_AFILIADO = 'https://ganhowin.fun/?ref=seunome'
IMAGEM_SINAL = 'https://static.sambafoot.com/br/apostas/wp//Imagem-destaque-mines.jpg'


def gerar_sinal():
    bombas = random.choice([2, 3, 4])
    chance = random.randint(95, 98)

    mapa = [['🔲' for _ in range(5)] for _ in range(5)]

    posicoes = [(i, j) for i in range(5) for j in range(5)]
    bombas_colocadas = 0
    while bombas_colocadas < bombas:
        x, y = random.choice(posicoes)
        if mapa[x][y] != '💥':
            mapa[x][y] = '💥'
            bombas_colocadas += 1

    mapa_str = '\n'.join(' '.join(linha) for linha in mapa)

    # Corrige o horário para UTC-3 (horário de Brasília)
    horario_brasilia = (datetime.utcnow() -
                        timedelta(hours=3)).strftime("%H:%M:%S")

    mensagem = f"""💣 SINAL DE MINES - Ganhawin 💥

🎯 Minas: {bombas}   |   💹 Chance de Acerto: {chance}%

{mapa_str}

🕒 Horário: {horario_brasilia}

🎯 Link para jogar agora:
👉 {LINK_AFILIADO}

🚀 A consistência vence o jogo. Entre agora e aproveite sua vantagem! 🔥
CANAL NOVO DE SINAIS DE MINES!
"""
    return mensagem


async def enviar_sinais_periodicos(app):
    while True:
        try:
            sinal = gerar_sinal()
            await app.bot.send_photo(chat_id=CHANNEL_ID,
                                     photo=IMAGEM_SINAL,
                                     caption=sinal,
                                     parse_mode='Markdown')
            print(f"✅ Sinal enviado!")
        except Exception as e:
            print(f"❌ Erro ao enviar sinal: {e}")
        await asyncio.sleep(90)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot ativo e enviando sinais automáticos!")


async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    asyncio.create_task(enviar_sinais_periodicos(app))
    print("🤖 Bot iniciado!")
    await app.run_polling()


if __name__ == "__main__":
    import nest_asyncio
    import asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
