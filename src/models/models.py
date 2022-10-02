import enum
import sqlalchemy
import sqlalchemy.ext.declarative as alchemy_declarative
import sqlalchemy.orm

Base = alchemy_declarative.declarative_base()


class IdMixin:
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)


class User(IdMixin, Base):
    __tablename__ = "user"
    email_domain = sqlalchemy.Column(sqlalchemy.Text)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)
    city = sqlalchemy.Column(sqlalchemy.Text)
    country = sqlalchemy.Column(sqlalchemy.Text)
    gender = sqlalchemy.Column(sqlalchemy.Text)
    is_smoking = sqlalchemy.Column(sqlalchemy.Boolean)
    profession = sqlalchemy.Column(sqlalchemy.Text)
    income = sqlalchemy.Column(sqlalchemy.Float)


class Subscription(IdMixin, Base):
    __tablename__ = "subscription"
    user_id = sqlalchemy.Column(sqlalchemy.ForeignKey("user.id"))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    status = sqlalchemy.Column(
        sqlalchemy.Text
    )  # TODO: use enum for better data insertion
    amount = sqlalchemy.Column(sqlalchemy.Float)


class Message(IdMixin, Base):
    __tablename__ = "message"
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    receiver_id = sqlalchemy.Column(sqlalchemy.Text, primary_key=True)
    sender_id = sqlalchemy.Column(sqlalchemy.Text, primary_key=True)
