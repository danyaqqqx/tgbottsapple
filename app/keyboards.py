from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 Начать оценку", callback_data="start")]
    ])


def model_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="iPhone 15 Pro Max", callback_data="m_15pm")],
        [InlineKeyboardButton(text="iPhone 15 Pro", callback_data="m_15p")],
        [InlineKeyboardButton(text="iPhone 14 Pro Max", callback_data="m_14pm")],
    ])


def target_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="iPhone 15 Pro Max", callback_data="t_15pm")],
        [InlineKeyboardButton(text="iPhone 15 Pro", callback_data="t_15p")],
    ])


def condition_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="c_1"),
            InlineKeyboardButton(text="2", callback_data="c_2"),
            InlineKeyboardButton(text="3", callback_data="c_3"),
            InlineKeyboardButton(text="4", callback_data="c_4"),
            InlineKeyboardButton(text="5", callback_data="c_5"),
        ]
    ])


def battery_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="100%", callback_data="b_100"),
            InlineKeyboardButton(text="95%", callback_data="b_95"),
            InlineKeyboardButton(text="90%", callback_data="b_90"),
        ],
        [
            InlineKeyboardButton(text="85%", callback_data="b_85"),
            InlineKeyboardButton(text="80%", callback_data="b_80"),
            InlineKeyboardButton(text="<80%", callback_data="b_low"),
        ]
    ])


def result_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Зафиксировать цену", callback_data="take")],
        [InlineKeyboardButton(text="💬 Менеджер", callback_data="manager")]
    ])