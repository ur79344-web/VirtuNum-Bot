from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards import main_menu, subscribe_keyboard

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "📢 Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling.",
        reply_markup=subscribe_keyboard
    )


@router.callback_query(lambda c: c.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    await callback.message.delete()

    await callback.message.answer(
        "✅ Obunangiz tasdiqlandi!\n\n"
        "🏠 Asosiy menyudasiz.",
        reply_markup=main_menu
    )

    await callback.answer()