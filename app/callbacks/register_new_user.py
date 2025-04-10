from aiogram import F, Router, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery

from app.services.user_service import UserService

router = Router()


@router.callback_query(F.data.startswith("new_user"))
async def create_new_user(
        message: Message,
        callback: CallbackQuery,
        user_service: UserService
):
    role = F.data.split("#")[1]
    await user_service.register_user()
    pass

