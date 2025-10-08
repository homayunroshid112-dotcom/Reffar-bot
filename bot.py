import telebot
from telebot import types
import os

# ==============================
# 🔐 Bot Configuration
# ==============================

# আপনার BotFather থেকে পাওয়া টোকেন (Render-এ "Environment Variables" হিসেবে সেট করা ভালো)
TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ==============================
# ⚡ Bot Handlers
# ==============================

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    signup_button = types.InlineKeyboardButton(
        "✅ Signup & Earn",
        url="https://www.revenuecpmgate.com/ntmaiyqqv?key=c170e6d189f42ac05b9ea6fdec5fcbaf"
    )
    support_button = types.InlineKeyboardButton(
        "📢 Support Channel",
        url="https://t.me/Sapurt_channel_1"
    )
    youtube_button = types.InlineKeyboardButton(
        "▶️ YouTube",
        url="https://youtube.com/@HSOfficialsChannel"
    )
    refer_button = types.InlineKeyboardButton("👥 My_Refar", callback_data="refer")
    wallet_button = types.InlineKeyboardButton("💼 My Wallet", callback_data="wallet")
    withdraw_button = types.InlineKeyboardButton("💵 Withdraw", callback_data="withdraw")

    markup.add(signup_button)
    markup.add(support_button, youtube_button)
    markup.add(refer_button)
    markup.add(wallet_button, withdraw_button)

    bot.send_message(
        message.chat.id,
        (
            "👋 স্বাগতম!\n\n"
            "আপনি এখান থেকে রেফার করে ইনকাম করতে চাইলে প্রথমে Signup করুন, "
            "তারপর YouTube সাবস্ক্রাইব করুন এবং Support Channel এ জয়েন হোন।"
        ),
        reply_markup=markup
    )


# ==============================
# 🔗 Callback Handlers
# ==============================

@bot.callback_query_handler(func=lambda call: call.data == "refer")
def refer(call):
    bot.answer_callback_query(call.id)
    ref_link = f"https://t.me/YourBotName?start={call.from_user.id}"
    bot.send_message(call.message.chat.id,
        f"১টা রেফার করলে পাবেন ১০০ টাকা। "
        f"১৫ টা রেফার করা পর টাকা উত্তোলন করতে পারবেন।\n\n"
        f"🔗 আপনার রেফারেল লিঙ্ক:\n{ref_link}"
    )

@bot.callback_query_handler(func=lambda call: call.data == "wallet")
def wallet(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "💼 আপনার ব্যালেন্স: 0.00৳")

@bot.callback_query_handler(func=lambda call: call.data == "withdraw")
def withdraw(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "💵 Withdraw এর জন্য কমপক্ষে 1500৳ থাকতে হবে।\n\nরিকোয়েস্ট অ্যাডমিনকে পাঠানো হবে।"
    )
    bot.send_message(
        ADMIN_ID,
        f"📢 New Withdraw Request\n\nUser: {call.from_user.first_name}\nUser ID: {call.from_user.id}"
    )

# ==============================
# 🚀 Run the bot (Render friendly)
# ==============================

if __name__ == "__main__":
    print("🤖 Bot is running on Render...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
