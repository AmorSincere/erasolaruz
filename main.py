from aiogram.utils import executor
import handlers
from dispatch import dp

webhook_url = 'https://amorsincere.github.io/erasolaruz/'
await bot.setWebhook(webhook_url)



await dp.start_polling()

