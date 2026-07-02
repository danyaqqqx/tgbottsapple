from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states import Flow
from app.keyboards import *

router = Router()


@router.message(F.text == "/start")
async def start(m: Message):
    await m.answer(
        "Привет 👋\n"
        "Оценю твой iPhone и рассчитаю обмен за 1 минуту.",
        reply_markup=start_kb()
    )


# START FLOW
@router.callback_query(F.data == "start")
async def step1(c: CallbackQuery, state: FSMContext):
    await c.message.edit_text("📱 Выберите вашу модель:", reply_markup=model_kb())
    await state.set_state(Flow.model_from)


# MODEL FROM
@router.callback_query(F.data.startswith("m_"))
async def step2(c: CallbackQuery, state: FSMContext):
    await state.update_data(model_from=c.data)

    await c.message.edit_text("🔁 На какую модель хотите обмен?", reply_markup=target_kb())
    await state.set_state(Flow.model_to)


# MODEL TO
@router.callback_query(F.data.startswith("t_"))
async def step3(c: CallbackQuery, state: FSMContext):
    await state.update_data(model_to=c.data)

    await c.message.edit_text("📊 Оцените состояние iPhone (1–5):", reply_markup=condition_kb())
    await state.set_state(Flow.condition)


# CONDITION 1-5
@router.callback_query(F.data.startswith("c_"))
async def step4(c: CallbackQuery, state: FSMContext):
    await state.update_data(condition=int(c.data.split("_")[1]))

    await c.message.edit_text("🔋 Какой процент батареи?", reply_markup=battery_kb())
    await state.set_state(Flow.battery)


# BATTERY (ФИНАЛ — БЕЗ ЗАВИСАНИЯ)
@router.callback_query(F.data.startswith("b_"))
async def step5(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    condition = data["condition"]
    battery = c.data.split("_")[1]

    # фиксация батареи
    if battery == "low":
        battery_val = 75
    else:
        battery_val = int(battery)

    # простая формула (можем потом усложнить)
    base = 100000

    price = base * (condition / 5)

    if battery_val < 85:
        price *= 0.85

    price = int(price)

    doplata = 129990 - price + 15000

    await c.message.edit_text(
        f"💰 Trade-in: ~{price} ₽\n"
        f"📱 Новый iPhone: 129 990 ₽\n"
        f"➕ Доплата: {doplata} ₽\n\n"
        f"⚡ Цена активна 2 часа",
        reply_markup=result_kb()
    )

    await state.clear()   # 🔥 ВОТ ЭТО УБИРАЕТ ЗАВИСАНИЯ