from app.database.dao.project_dao import ProjectDAO
from app.database.models.project import Project
from app.utils.logger import logger


class ProjectService:
    def __init__(self, project_dao: ProjectDAO):
        self.project_dao = project_dao

    async def get_project_by_id(self, project_id: int) -> Project:
        try:
            project = await self.project_dao.get_project_by_id(project_id)
            if not project:
                raise ValueError("Проект не найден")
            return project
        except Exception as e:
            logger.error(f"Ошибка получения профиля {project_id}: {e}")
            raise