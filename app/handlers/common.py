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
):
    try:
        await message.answer(f"Привет, {message.from_user.first_name}! Мы тебя приветствуем в нашем боте...")
        await message.answer(
            f"Но сначала тебе нужно сказать кто ты воин. Зачем сюда пришел?",
            reply_markup=await create_inline_keyboard(
                [("Я продавец", "new_user#seller"), ("Я покупатель", "new_user#buyer")])
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке /start: {e}")
        await message.answer("Ошибка при обработке /start")
        # await message.answer("⚠️ Произошла ошибка при регистрации. Попробуйте позже.")
