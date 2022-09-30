from dataclasses import dataclass

import yaml
from dotenv import dotenv_values
from sqlalchemy import create_engine


@dataclass(slots=True, frozen=True)
class DBConfig:
    host: str
    port: str
    name: str


@dataclass(slots=True, frozen=True)
class DBLogin:
    user: str
    password: str


class DB:
    def __init__(self):
        db_config = self._read_database_config_from("configs/db.yaml")
        login_db_config = DBLogin(**dotenv_values("envs/.db"))

        connection_string = f'postgresql://{login_db_config.user}:{login_db_config.password}@{db_config.host}:{db_config.port}/{db_config.name}'

        self.engine = create_engine(connection_string)

    @staticmethod
    def _read_database_config_from(file: str) -> DBConfig:
        with open(file, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                config = DBConfig(**config)

                return config
            except yaml.YAMLError as exc:
                print(exc)

    def create(self):
        self.engine.execute("CREATE TABLE IF NOT EXISTS languages(title varchar(10));")
