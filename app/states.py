from aiogram.fsm.state import State, StatesGroup

class Flow(StatesGroup):
    model_from = State()
    model_to = State()
    condition = State()
    battery = State()