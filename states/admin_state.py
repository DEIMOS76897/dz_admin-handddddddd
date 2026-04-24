from aiogram.fsm.state import StatesGroup, State

class AdminState(StatesGroup):
    add_lessons = State()
    delete_lessons = State()
    broadcast_message = State()
    edit_lesson_name = State()
    view_users = State()
    view_records = State()
    view_lessons = State()