
from sqlalchemy import String, BigInteger, Integer, Boolean, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class BaseConfig(Base):
    __tablename__ = 'base_configs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    new_message_notifications: Mapped[bool] = mapped_column(Boolean, default=True)
    blacklist_buyers: Mapped[list[str]] = mapped_column(JSON, default=list)
    
class User(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)