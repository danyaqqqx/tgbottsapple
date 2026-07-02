from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    model = State()
    screen_crack = State()
    face_id = State()
    camera = State()
    body = State()
    battery = State()
    name = State()
    phone = State()