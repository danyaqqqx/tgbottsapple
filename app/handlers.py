from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states import Form
from app.pricing import calculate_trade_in, calculate_upgrade
from app.db import save_lead
from app.config import ADMIN_CHAT_ID

router = Router()

MODELS = [
    "iPhone 15 Pro Max",
    "iPhone 15 Pro",
    "iPhone 14 Pro Max",
    "iPhone 14 Pro",
    "iPhone 13 Pro Max"
]


@router.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    await message.answer("Выберите модель iPhone:\n" + "\n".join(MODELS))
    await state.set_state(Form.model)


@router.message(Form.model)
async def model(message: Message, state: FSMContext):
    await state.update_data(model=message.text)

    await message.answer("Есть ли трещина на экране? (да/нет)")
    await state.set_state(Form.screen_crack)


@router.message(Form.screen_crack)
async def screen(message: Message, state: FSMContext):
    await state.update_data(screen_crack=message.text.lower() == "да")

    await message.answer("Face ID работает? (да/нет)")
    await state.set_state(Form.face_id)


@router.message(Form.face_id)
async def faceid(message: Message, state: FSMContext):
    await state.update_data(face_id_broken=message.text.lower() == "нет")

    await message.answer("Есть ли проблемы с камерой? (да/нет)")
    await state.set_state(Form.camera)


@router.message(Form.camera)
async def camera(message: Message, state: FSMContext):
    await state.update_data(camera_issue=message.text.lower() == "да")

    await message.answer("Есть ли повреждения корпуса? (да/нет)")
    await state.set_state(Form.body)


@router.message(Form.body)
async def body(message: Message, state: FSMContext):
    await state.update_data(body_damage=message.text.lower() == "да")

    await message.answer("Батарея ниже 85%? (да/нет)")
    await state.set_state(Form.battery)


@router.message(Form.battery)
async def battery(message: Message, state: FSMContext):
    data = await state.get_data()

    condition = {
        "screen_crack": data["screen_crack"],
        "face_id_broken": data["face_id_broken"],
        "camera_issue": data["camera_issue"],
        "body_damage": data["body_damage"],
        "battery_low": message.text.lower() == "да"
    }

    model = data["model"]

    trade_in = calculate_trade_in(model, condition)
    doplata, monthly = calculate_upgrade(trade_in)

    await state.update_data(trade_in=trade_in, doplata=doplata)

    await message.answer(
        f"💰 Trade-in: {trade_in} ₽\n"
        f"📱 Доплата: {doplata} ₽\n"
        f"💳 ~ {monthly} ₽/мес +15k"
    )

    await message.answer("Оставь имя:")
    await state.set_state(Form.name)


@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Оставь телефон:")
    await state.set_state(Form.phone)


@router.message(Form.phone)
async def phone(message: Message, state: FSMContext):
    data = await state.get_data()

    save_lead(
        data["name"],
        message.text,
        data["model"],
        data["trade_in"],
        data["doplata"]
    )

    await message.answer("Заявка отправлена!")

    # notify admin
    await message.bot.send_message(
        ADMIN_CHAT_ID,
        f"📩 NEW LEAD\n"
        f"{data['model']}\n"
        f"Trade-in: {data['trade_in']} ₽\n"
        f"Доплата: {data['doplata']} ₽\n"
        f"Клиент: {data['name']} / {message.text}"
    )

    await state.clear()