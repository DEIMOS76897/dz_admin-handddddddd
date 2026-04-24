from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from states.admin_state import AdminState
from keyboards.menu import admin_menu,main_menu

rt = Router()


@rt.callback_query(F.data == "admin_users")
async def admin_users_list(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.view_users)
    await callback.message.answer("Список пользователей:")
    await callback.answer()

@rt.callback_query(F.data == "admin_records")
async def admin_records_list(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.view_records)
    await callback.message.answer("Все записи:")
    await callback.answer()

@rt.callback_query(F.data == "admin_lessons")
async def admin_lessons_list(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.view_lessons)
    await callback.message.answer("Список предметов:")
    await callback.answer()

@rt.callback_query(F.data == "admin_add_lesson")
async def admin_add_lesson_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.add_lessons)
    await callback.message.answer("Введите название нового предмета:")
    await callback.answer()

@rt.message(add_lessons)
async def process_lesson_name(message: Message, state: FSMContext):
    lesson_name = message.text.strip()
    await state.update_data(lesson_name=lesson_name)
    await state.set_state(AdminState.edit_lesson_name)
    await message.answer("Введите новое название предмета если хотите изменить:")

@rt.message(edit_lesson_name)
async def process_edit_lesson_name(message: Message, state: FSMContext):
    new_lesson_name = message.text.strip()
    data = await state.get_data()
    old_lesson_name = data.get("lesson_name")
    await state.clear()
    await message.answer(f"Предмет {old_lesson_name} изменен на {new_lesson_name}.", reply_markup=admin_menu())

@rt.callback_query(F.data == "back_main_menu")
async def back_to_main_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Главное меню",reply_markup = main_menu())
    await callback.answer()