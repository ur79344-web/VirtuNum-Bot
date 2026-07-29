from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards import main_menu, subscribe_keyboard

router = Router()


@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling.",
        reply_markup=subscribe_keyboard
    )


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    await callback.message.answer(
        "✅ Obunangiz tasdiqlandi!\n\n"
        "🏠 Asosiy menyudasiz.",
        reply_markup=main_menu
    )

    await callback.answer()