from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 Начать оценку", callback_data="start")]
    ])


# 📱 ТВОИ УСТРОЙСТВА (СДАЁШЬ)
def model_kb():
    models = [
        "iPhone 11", "iPhone 11 Pro", "iPhone 11 Pro Max",
        "iPhone 12", "iPhone 12 mini", "iPhone 12 Pro", "iPhone 12 Pro Max",
        "iPhone 13", "iPhone 13 mini", "iPhone 13 Pro", "iPhone 13 Pro Max",
        "iPhone 14", "iPhone 14 Plus", "iPhone 14 Pro", "iPhone 14 Pro Max",
        "iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max",
        "iPhone 16", "iPhone 16 Plus", "iPhone 16 Pro", "iPhone 16 Pro Max",
        "iPhone 17", "iPhone 17 Air", "iPhone 17 Pro", "iPhone 17 Pro Max",
    ]

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=m, callback_data=f"m|{m}")]
            for m in models
        ]
    )


# 🔁 МОДЕЛИ ДЛЯ ОБМЕНА (ЦЕЛЬ)
def target_kb():
    models = [
        "iPhone 14", "iPhone 14 Plus", "iPhone 14 Pro", "iPhone 14 Pro Max",
        "iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max",
        "iPhone 16", "iPhone 16 Plus", "iPhone 16 Pro", "iPhone 16 Pro Max",
        "iPhone 17", "iPhone 17 Air", "iPhone 17 Pro", "iPhone 17 Pro Max",
    ]

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=m, callback_data=f"t|{m}")]
            for m in models
        ]
    )


# 📊 состояние (1–5)
def condition_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="c|1"),
            InlineKeyboardButton(text="2", callback_data="c|2"),
            InlineKeyboardButton(text="3", callback_data="c|3"),
            InlineKeyboardButton(text="4", callback_data="c|4"),
            InlineKeyboardButton(text="5", callback_data="c|5"),
        ]
    ])


# 🔋 батарея
def battery_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="100%", callback_data="b|100"),
            InlineKeyboardButton(text="95%", callback_data="b|95"),
            InlineKeyboardButton(text="90%", callback_data="b|90"),
        ],
        [
            InlineKeyboardButton(text="85%", callback_data="b|85"),
            InlineKeyboardButton(text="80%", callback_data="b|80"),
            InlineKeyboardButton(text="<80%", callback_data="b|low"),
        ]
    ])


def result_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Зафиксировать цену", callback_data="take")],
        [InlineKeyboardButton(text="💬 Менеджер", callback_data="manager")]
    ])