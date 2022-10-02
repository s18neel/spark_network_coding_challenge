import sqlalchemy
import sqlalchemy.orm
import models.api_models as api_models
import models.models as models
import utils


def create_messages(records: list[api_models.Message], session: sqlalchemy.orm.Session):
    utils.create(session, [rec.dict() for rec in records], models.Message)


def load(data: dict, session: sqlalchemy.orm.Session):
    records = [api_models.Message(**ele) for ele in data]
    create_messages(records, session)
