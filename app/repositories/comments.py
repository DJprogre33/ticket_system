from app.models.comments import Comments
from app.utils.base_repository import SQLAlchemyRepository


class CommentsRepository(SQLAlchemyRepository):
    model = Comments
    pass
