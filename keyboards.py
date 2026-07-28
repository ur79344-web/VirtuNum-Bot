 from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# =========================
# ASOSIY MENU
# =========================

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰 Mening hisobim"),
            KeyboardButton(text="📞 Nomer olish")
        ],
        [
            KeyboardButton(text="📦 Boshqa xizmatlar"),
            KeyboardButton(text="💳 Hisobni to'ldirish")
        ],
        [
            KeyboardButton(text="☎️ Qo'llab-quvvatlash"),
            KeyboardButton(text="🎁 Pul ishlash")
        ],
        [
            KeyboardButton(text="📖 Qo'llanma")
        ]
    ],
    resize_keyboard=True
)

# =========================
# MAJBURIY OBUNA
# =========================

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 VirtuNum News",
                url="https://t.me/VirtuNum_News"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Havola Nakrutka",
                url="https://t.me/havola_nakrutka"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Tekshirish",
                callback_data="check_sub"
            )
        ]
    ]
)