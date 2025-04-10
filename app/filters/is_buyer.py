from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from app.database.models.user import UserType
from app.services.user_service import UserService


class IsBuyer(BaseFilter):

    async def __call__(
            self,
            event: Message | CallbackQuery,
            user_service: UserService
    ) -> bool:
        user = user_service.get_user_profile(user_id=event.from_user.id)
        if user.user_type == UserType.buyer:
            return True
        else:
            return False
