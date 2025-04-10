from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.services.user_service import UserService
from app.utils.logger import logger
from keyboards.builder import create_inline_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(
        message: Message,
        another_service: UserService,
):
    try:
        await message.answer(
            f"Привет, {message.from_user.username}! Кто ты?",
            reply_markup=await create_inline_keyboard(
                [("Продавец", "new_user#seller"), ("Покупатель", "new_user#buyer")])
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке /start: {e}")
        await message.answer("⚠️ Произошла ошибка при регистрации. Попробуйте позже.")
