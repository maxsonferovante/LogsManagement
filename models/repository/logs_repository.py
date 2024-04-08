from models.settings.connection import db_connection_handler
from models.entities.logs import Logs

from typing import List

from sqlalchemy.orm.exc import NoResultFound

import uuid

class LogsRepository:

    def add_log(self, log: Logs):
        with db_connection_handler as database:
            try:

                log = Logs(
                    log=log.get("log"),
                    tag=log.get("tag")
                )

                database.session.add(log)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_log_by_id(self, log_id: int) -> Logs:
        with db_connection_handler as database:
            try:
                log = database.session.query(Logs).filter(Logs.id == log_id).one()
                return log
            except NoResultFound as exception:
                raise exception

    def count_logs_by_tag(self, tag: str) -> int:
        with db_connection_handler as database:
            try:
                count = database.session.query(Logs).where(Logs.tag == tag).count()
                return count
            except Exception as exception:
                raise exception

    def get_all_logs(self) -> List[Logs]:
        with db_connection_handler as database:
            try:
                logs = database.session.query(Logs).all()
                return logs
            except NoResultFound as exception:
                raise exception
