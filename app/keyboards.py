from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 Оценить iPhone", callback_data="start")]
    ])

def models_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="iPhone 15 Pro Max", callback_data="m_15pm")],
        [InlineKeyboardButton(text="iPhone 15 Pro", callback_data="m_15p")],
        [InlineKeyboardButton(text="iPhone 14 Pro Max", callback_data="m_14pm")],
        [InlineKeyboardButton(text="iPhone 14 Pro", callback_data="m_14p")],
    ])

def yes_no(prefix):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Есть проблема", callback_data=f"{prefix}_yes"),
            InlineKeyboardButton(text="✅ Всё ок", callback_data=f"{prefix}_no"),
        ]
    ])

def result_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Зафиксировать цену", callback_data="take")],
        [InlineKeyboardButton(text="💬 Хочу выше цену", callback_data="manager")],
        [InlineKeyboardButton(text="📞 Связаться", callback_data="contact")]
    ])