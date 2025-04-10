from aiogram import F, Router, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery

from app.database.models.user import UserType
from app.utils.logger import logger

from app.services.user_service import UserService
from keyboards.reply import buyer_main_menu, seller_main_menu, main_menu

router = Router()


@router.callback_query(F.data.startswith("new_user"))
async def create_new_user(
        callback: CallbackQuery,
        user_service: UserService
):
    try:
        user_type = callback.data.split("#")[1]
        user = await user_service.register_user(
            id=callback.from_user.id,
            username=callback.from_user.username,
            first_name=callback.from_user.first_name,
            last_name=callback.from_user.last_name,
            user_type=user_type,
        )

        if user is False:
            await callback.message.answer(
                "Вы уже зарегестрированы. Выберите пункт меню",
                reply_markup=main_menu.get(user_type)
            )
            await callback.answer()

        else:
            await callback.message.answer(
                "Вы успешно зарегистрировались! Выберите пункт меню",
                reply_markup=main_menu.get(user_type)
            )
            await callback.answer()

    except Exception as e:
        logger.error(f"Ошибка при регистрации регистрации: {e}")
        await callback.message.answer("⚠️ Произошла ошибка при регистрации. Попробуйте позже.")
