from app.database.dao.project_dao import ProjectDAO
from app.database.models.project import Project
from app.utils.logger import logger


class SellerService:
    def __init__(self, project_dao: ProjectDAO):
        self.project_dao = project_dao

    async def get_projects_by_seller_id(self, seller_id: int) -> list[Project] | None:
        try:
            projects = await self.project_dao.get_all_projects_by_seller_id(seller_id)
            return projects
        except Exception as e:
            logger.error(f"Ошибка получения проектов по seller_id {seller_id}: {e}")
            raise

    async def create_project(self, **project_data) -> Project:
        try:
            project = await self.project_dao.create_project(**project_data)
            logger.success(f"Успешно создан проект: {project.id}")
            return project
        except Exception as e:
            logger.error(f"Ошибка создания проекта: {e}")
            raise
