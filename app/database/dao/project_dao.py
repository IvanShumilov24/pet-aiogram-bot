from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.project import Project
from app.database.models.user import User
from app.utils.logger import logger


class ProjectDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_project_by_id(self, project_id: int) -> Project | None:
        try:
            query = select(Project).where(Project.id == project_id)
            result = await self.session.execute(query)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при получении проекта {project_id}: {e}")
            await self.session.rollback()
            raise

    async def create_project(
            self,
            **project_data: dict,
    ) -> Project:
        try:
            project = Project(**project_data)
            self.session.add(project)
            await self.session.commit()
            logger.info(f"Создан проект: {project.id}")
            return project
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при создании проекта: {e}")
            await self.session.rollback()
            raise

    async def get_or_create_project(self, project_data: dict) -> tuple[User, bool]:
        project = await self.get_project_by_id(project_data['id'])
        if project:
            return project, False
        try:
            project = await self.create_project(project_data)
            return project, True
        except Exception as e:
            logger.error(f"Ошибка при получении или создании проекта: {e}")
            raise

    async def get_all_projects_by_seller_id(self, seller_id: int) -> list[Project] | None:
        try:
            query = select(Project).where(Project.seller_id == seller_id)
            result = await self.session.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при получении всех проектов: {e}")
            raise
