from aiogram import F, Router, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from app.utils.logger import logger

from app.services.user_service import UserService

router = Router()


@router.callback_query(F.data.startswith("new_user"))
async def create_new_user(
        callback: CallbackQuery,
        user_service: UserService
):
    try:
        user_type = callback.data.split("#")[1]
        await user_service.register_user(
            id=callback.message.from_user.id,
            username=callback.message.from_user.username,
            first_name=callback.message.from_user.first_name,
            last_name=callback.message.from_user.last_name,
            user_type=user_type,
        )

        await callback.answer()
        await callback.message.answer("Вы успешно зарегистрировались!")

    except Exception as e:
        logger.error(f"Ошибка при регистрации регистрации: {e}")
        await callback.message.answer("⚠️ Произошла ошибка при регистрации. Попробуйте позже.")


