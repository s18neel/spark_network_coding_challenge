import functools
import requests

import sqlalchemy
import sqlalchemy.orm

import models.models


# def replace_nan_with_none(df: pd.DataFrame) -> pd.DataFrame:
#     return df.replace({np.nan: None})


def handle_sqlalchemy_error(func):
    @functools.wraps(func)
    def inner(session, *args, **kwargs):
        try:
            func(session, *args, **kwargs)
        except Exception as e:  # handle specific exceptions
            session.rollback()
            print(e)

    return inner


@handle_sqlalchemy_error
def create(
    session: sqlalchemy.orm.Session, records: list[dict], model: models.models.Base
) -> None:
    session.bulk_insert_mappings(model, records)
    session.commit()


def downloader(url: str):
    response = requests.get(url)
    if "error" in response.json():
        raise Exception("Api is not working")

    return response.json()
