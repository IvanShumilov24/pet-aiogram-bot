from app.database.dao.project_dao import ProjectDAO


class BuyerService:
    def __init__(self, project_dao: ProjectDAO):
        self.project_dao = project_dao

