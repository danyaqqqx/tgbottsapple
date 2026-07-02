from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states import Flow
from app.keyboards import *
from app.pricing import calc

router = Router()


# 📊 базовые цены (обновлённые до 17 серии)
BASE = {
    "iPhone 11": 30000,
    "iPhone 11 Pro": 35000,
    "iPhone 11 Pro Max": 40000,

    "iPhone 12": 40000,
    "iPhone 12 mini": 38000,
    "iPhone 12 Pro": 45000,
    "iPhone 12 Pro Max": 50000,

    "iPhone 13": 55000,
    "iPhone 13 mini": 52000,
    "iPhone 13 Pro": 65000,
    "iPhone 13 Pro Max": 70000,

    "iPhone 14": 70000,
    "iPhone 14 Plus": 75000,
    "iPhone 14 Pro": 85000,
    "iPhone 14 Pro Max": 90000,

    "iPhone 15": 90000,
    "iPhone 15 Plus": 95000,
    "iPhone 15 Pro": 105000,
    "iPhone 15 Pro Max": 115000,

    "iPhone 16": 105000,
    "iPhone 16 Plus": 110000,
    "iPhone 16 Pro": 125000,
    "iPhone 16 Pro Max": 140000,

    "iPhone 17": 120000,
    "iPhone 17 Air": 130000,
    "iPhone 17 Pro": 150000,
    "iPhone 17 Pro Max": 170000,
}


# 🚀 старт
@router.message(F.text == "/start")
async def start(m: Message):
    await m.answer(
        "Привет 👋\n"
        "Оценю твой iPhone и рассчитаю обмен за 1–2 минуты.",
        reply_markup=start_kb()
    )


# STEP 1
@router.callback_query(F.data == "start")
async def step1(c: CallbackQuery, state: FSMContext):
    await c.message.edit_text("📱 Выберите вашу модель:", reply_markup=model_kb())
    await state.set_state(Flow.model_from)


# STEP 2
@router.callback_query(F.data.startswith("m|"))
async def step2(c: CallbackQuery, state: FSMContext):
    model = c.data.split("|")[1]
    await state.update_data(model_from=model)

    await c.message.edit_text("🔁 Выберите модель для обмена:", reply_markup=target_kb())
    await state.set_state(Flow.model_to)


# STEP 3
@router.callback_query(F.data.startswith("t|"))
async def step3(c: CallbackQuery, state: FSMContext):
    model_to = c.data.split("|")[1]
    await state.update_data(model_to=model_to)

    await c.message.edit_text("📊 Оцените состояние (1–5):", reply_markup=condition_kb())
    await state.set_state(Flow.condition)


# STEP 4
@router.callback_query(F.data.startswith("c|"))
async def step4(c: CallbackQuery, state: FSMContext):
    condition = int(c.data.split("|")[1])
    await state.update_data(condition=condition)

    await c.message.edit_text("🔋 Батарея:", reply_markup=battery_kb())
    await state.set_state(Flow.battery)


# FINAL STEP
@router.callback_query(F.data.startswith("b|"))
async def step5(c: CallbackQuery, state: FSMContext):
    battery_raw = c.data.split("|")[1]
    data = await state.get_data()

    condition = data["condition"]
    battery = 75 if battery_raw == "low" else int(battery_raw)

    base = BASE.get(data["model_from"], 50000)

    price = calc(base, condition, battery)

    doplata = 129990 - price + 15000

    await c.message.edit_text(
        f"💰 Trade-in: ~{price} ₽\n"
        f"📱 Новый iPhone: 129 990 ₽\n"
        f"➕ Доплата: {doplata} ₽\n\n"
        f"⚡ Цена активна 2 часа",
        reply_markup=result_kb()
    )

    await state.clear()