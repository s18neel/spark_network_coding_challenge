import sqlalchemy.orm
from crawlers import users_crawler, messages_crawler
import models.models as models
import settings.config as config
import utils

mapper = {
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users": users_crawler.load,
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages": messages_crawler.load,
}


def run():
    session = sqlalchemy.orm.Session(bind=config.engine)
    for key in mapper:
        data = utils.downloader(key)
        mapper[key](data, session)


def startup():
    models.Base.metadata.drop_all(bind=config.engine)
    models.Base.metadata.create_all(bind=config.engine)


if __name__ == "__main__":
    startup()
    run()
