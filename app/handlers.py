from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states import Flow
from app.keyboards import *
from app.pricing import calc
from app.db import save_lead
from app.scheduler import send_delayed

router = Router()

MODELS = {
    "m_15pm": 110000,
    "m_15p": 95000,
    "m_14pm": 80000,
    "m_14p": 70000
}


@router.message(F.text == "/start")
async def start(m: Message):
    await m.answer("Нажми кнопку:", reply_markup=start_kb())


@router.callback_query(F.data == "start")
async def model(c: CallbackQuery, state: FSMContext):
    await c.message.edit_text("Выбери модель:", reply_markup=models_kb())
    await state.set_state(Flow.model)


@router.callback_query(F.data.startswith("m_"))
async def model_set(c: CallbackQuery, state: FSMContext):
    await state.update_data(model=c.data)

    await c.message.edit_text("Есть проблемы с экраном?", reply_markup=yes_no("screen"))
    await state.set_state(Flow.screen)


@router.callback_query(F.data.startswith("screen_"))
async def screen(c: CallbackQuery, state: FSMContext):
    await state.update_data(screen=c.data.split("_")[1])

    await c.message.edit_text("Батарея норм?", reply_markup=yes_no("battery"))
    await state.set_state(Flow.battery)


@router.callback_query(F.data.startswith("battery_"))
async def battery(c: CallbackQuery, state: FSMContext):
    await state.update_data(battery=c.data.split("_")[1])

    await c.message.edit_text("Камера ок?", reply_markup=yes_no("camera"))
    await state.set_state(Flow.camera)


@router.callback_query(F.data.startswith("camera_"))
async def camera(c: CallbackQuery, state: FSMContext):
    await state.update_data(camera=c.data.split("_")[1])

    await c.message.edit_text("Face ID работает?", reply_markup=yes_no("faceid"))
    await state.set_state(Flow.faceid)


@router.callback_query(F.data.startswith("faceid_"))
async def faceid(c: CallbackQuery, state: FSMContext):
    await state.update_data(faceid=c.data.split("_")[1])

    await c.message.edit_text("Корпус в порядке?", reply_markup=yes_no("body"))
    await state.set_state(Flow.body)


@router.callback_query(F.data.startswith("body_"))
async def body(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    model = data["model"]
    price = calc(MODELS[model], data)

    doplata = 129990 - price + 15000

    text = (
        f"💰 Trade-in: ~{price} ₽\n"
        f"📱 Новый iPhone: 129 990 ₽\n"
        f"➕ Доплата: {doplata} ₽\n\n"
        f"⚡ Цена действует 2 часа"
    )

    await c.message.edit_text(text, reply_markup=result_kb())

    user_id = c.from_user.id

    # 🚀 дожимы
    send_delayed(user_id, "⚡ Могу зафиксировать цену прямо сейчас", 600)       # 10 мин
    send_delayed(user_id, "📉 Цена может измениться сегодня", 3600)             # 1 час
    send_delayed(user_id, "🔥 Осталось мало мест на приём", 86400)              # 24 часа

    await state.clear()


@router.callback_query(F.data == "take")
async def take(c: CallbackQuery):
    await c.message.answer("Отлично! Оставь номер телефона 📞")


@router.callback_query(F.data == "contact")
async def contact(c: CallbackQuery):
    await c.message.answer("Напиши номер или @username")