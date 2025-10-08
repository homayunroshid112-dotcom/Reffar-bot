import telebot
from telebot import types

# আপনার BotFather থেকে পাওয়া টোকেন বসান
TOKEN = "8276456405:AAGTG2ec-4h5iCsIiXR2Je996Ly3j9IdGJI"
bot = telebot.TeleBot(TOKEN)

# আপনার অ্যাডমিন আইডি (Withdraw রিকোয়েস্ট যাবে এখানে)
ADMIN_ID = 8287786713  

# /start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # এখানে Signup বাটনে সরাসরি লিংক বসানো হলো
    signup_button = types.InlineKeyboardButton("✅ Signup & Earn", url="https://www.revenuecpmgate.com/ntmaiyqqv?key=c170e6d189f42ac05b9ea6fdec5fcbaf")
    support_button = types.InlineKeyboardButton("📢 Support Channel", url="https://t.me/Sapurt_channel_1")
    youtube_button = types.InlineKeyboardButton("▶️ YouTube", url="https://youtube.com/@HSOfficialsChannel")
    refer_button = types.InlineKeyboardButton("👥 My_Refar", callback_data="refer")
    wallet_button = types.InlineKeyboardButton("💼 My Wallet", callback_data="wallet")
    withdraw_button = types.InlineKeyboardButton("💵 Withdraw", callback_data="withdraw")
    
    markup.add(signup_button)
    markup.add(support_button, youtube_button)
    markup.add(refer_button)
    markup.add(wallet_button, withdraw_button)

    bot.send_message(message.chat.id, 
        "👋 স্বাগতম!\n\nআপনি এখান থেকে রেফার করে ইনকাম করতে চাইলে প্রথমে Signup করুন, "
        "তারপর YouTube সাবস্ক্রাইব করুন এবং Support Channel এ জয়েন হোন।",
        reply_markup=markup
    )

# Refer
@bot.callback_query_handler(func=lambda call: call.data == "refer")
def refer(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "১টা রেফার করলে পাবেন ১০০ টাকা।১৫ টা রেফার করা পর টাকা উত্তোলন করতে পারবেন🔗 আপনার রেফারেল লিঙ্ক:\nhttps://t.me/YourBotName?start=" + str(call.from_user.id))

# Wallet
@bot.callback_query_handler(func=lambda call: call.data == "wallet")
def wallet(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "💼 আপনার ব্যালেন্স: 0.00৳")

# Withdraw
@bot.callback_query_handler(func=lambda call: call.data == "withdraw")
def withdraw(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "💵 Withdraw এর জন্য কমপক্ষে 1500৳ থাকতে হবে।\n\nরিকোয়েস্ট অ্যাডমিনকে পাঠানো হবে।")

    # Withdraw request admin এ পাঠানো হবে
    bot.send_message(ADMIN_ID, f"📢 New Withdraw Request\n\nUser: {call.from_user.first_name}\nUser ID: {call.from_user.id}")

print("🤖 Bot is running...")
bot.polling()
