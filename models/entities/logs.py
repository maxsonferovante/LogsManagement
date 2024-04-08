import datetime

from models.settings.base import Base
from models.constants import tags_enum
from sqlalchemy import Column, Integer, String, DateTime, Enum


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    log = Column(String, nullable=False)
    tag = Column(Enum("INFO", "ERROR", "WARNING", "DEBUG"), nullable=False)
    created_at = Column(DateTime, onupdate=True, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=True, default=datetime.datetime.now)

    def __repr__(self):
        return f"<Log = id={self.id} (tag = {self.tag}): , log = {self.log}, created_at = {self.created_at}>"
