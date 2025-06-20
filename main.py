from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = "8006623960:AAHbVLtKObGeSqASOuLoV1mV8EWX5uvNPxQ"

async def start(update, context):
    await update.message.reply_text("🧠 Welcome to Lazy Yeti Bot! Use /latest, /elite, or /og...")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
