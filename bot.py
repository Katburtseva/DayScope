import logging
import random
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, InlineQueryHandler, CommandHandler, ContextTypes
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8611165698:AAH3CyPcn5g0uSf_Efa2qEAEA-9SJ8l6aCI"

DICK_PHRASES = [
    "🍆 Мой огурчик",
    "🌭 Моя сосиска",
    "🚀 Моя ракета",
    "🎸 Мой джойстик",
    "🐍 Мой питон",
    "🗼 Моя Эйфелева башня",
    "⚔️ Мой меч",
    "🎺 Моя труба",
    "🏒 Моя клюшка",
    "🌵 Мой кактус",
    "🔦 Мой фонарик",
    "🎻 Моя скрипочка",
    "🪄 Моя волшебная палочка",
    "🍌 Мой банан",
    "🛸 Моя летающая тарелка",
    "🎙️ Мой микрофон",
    "🏛️ Моя колонна",
    "🪝 Мой крючок",
    "🌶️ Мой перчик",
    "🎯 Мой дротик",
    "🧨 Моя петарда",
    "🪛 Моя отвёртка",
    "🏹 Моя стрела",
    "🧲 Мой магнит",
    "🌿 Мой стебелёк",
]

def generate_stats() -> str:
    dick_size = random.randint(3, 40)
    gay_percent = random.randint(0, 100)
    iq = random.randint(60, 180)
    mood = random.randint(0, 100)
    productivity = random.randint(0, 100)

    dick_phrase = random.choice(DICK_PHRASES)
    mood_emoji = "😄" if mood > 70 else "😐" if mood > 40 else "😞"
    prod_emoji = "🚀" if productivity > 70 else "💼" if productivity > 40 else "😴"
    gay_emoji = "🌈" if gay_percent > 50 else "🤔"
    iq_emoji = "🧠" if iq > 130 else "😊" if iq > 100 else "🐒"

    text = (
        f"📊 *Мои характеристики на сегодня:*\n\n"
        f"{dick_phrase}: *{dick_size} см*\n"
        f"{gay_emoji} Я гей на: *{gay_percent}%*\n"
        f"{iq_emoji} Мой IQ: *{iq}*\n"
        f"{mood_emoji} Настроение: *{mood}%*\n"
        f"{prod_emoji} Продуктивность: *{productivity}%*"
    )
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n\nЯ бот-генератор характеристик!\n"
        "Используй меня в инлайн-режиме: напиши *@имя_бота* в любом чате.",
        parse_mode="Markdown"
    )

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    results = []

    stats_text = generate_stats()

    results.append(
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="🎲 Сгенерировать мои характеристики",
            description="Нажми чтобы получить случайные характеристики!",
            input_message_content=InputTextMessageContent(
                message_text=stats_text,
                parse_mode="Markdown"
            ),
            thumbnail_url="https://i.imgur.com/placeholder.png"
        )
    )

    await update.inline_query.answer(results, cache_time=0)

def main():
 # Сначала стартует веб-сервер — Render видит порт и доволен
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    
    web_thread = threading.Thread(target=server.serve_forever, daemon=True)
    web_thread.start()
    logger.info(f"Веб-сервер запущен на порту {port}...")

    # Потом запускается бот
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    logger.info("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
```

Ключевое изменение — порт теперь `10000` (Render по умолчанию ждёт именно его), и веб-сервер стартует **до** `run_polling`.

---

if __name__ == "__main__":
    main()
