from aiogram.fsm.state import State, StatesGroup

class Flow(StatesGroup):
    model = State()
    screen = State()
    battery = State()
    camera = State()
    faceid = State()
    body = State()
    name = State()
    phone = State()