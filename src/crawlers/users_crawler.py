import sqlalchemy
import sqlalchemy.orm
import models.api_models as api_models
import models.models as models
import utils


def create_users(records: list[api_models.User], session: sqlalchemy.orm.Session):

    users = [
        {
            **rec.dict(exclude={"profile", "subscription"}),
            **rec.profile.dict(),
            "email_domain": rec.email_domain,
        }
        for rec in records
    ]
    utils.create(session, users, models.User)


def create_subscriptions(
    records: list[api_models.User], session: sqlalchemy.orm.Session
):
    subscriptions = [
        {"user_id": rec.id, **subscription.dict()}
        for rec in records
        for subscription in rec.subscription
    ]
    utils.create(session, subscriptions, models.Subscription)


def load(data: dict, session: sqlalchemy.orm.Session):
    records = [api_models.User(**ele) for ele in data]
    create_users(records, session)
    create_subscriptions(records, session)
