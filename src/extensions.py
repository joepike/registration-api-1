# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
"""
Extensions module.

Each extension is initialized in the app factory located in __init__.py
"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
