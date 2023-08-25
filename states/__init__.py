from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext



class FeedBackState(StatesGroup):
    feeedback = State()
    

class CatologState(StatesGroup):
    catologs = State()


