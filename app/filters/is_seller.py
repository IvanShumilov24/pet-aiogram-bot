from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsSeller(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool:
        user = get_user_by_user_id(event.from_user.id)
        if user.type == "seller":
            return True
        else:
            return False
