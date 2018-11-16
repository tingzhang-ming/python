from sqlalchemy import ForeignKey
from sqlalchemy.exc import OperationalError
from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData

from db.sqlalchemy.migrate_repo.schema import create_tables, drop_tables
from db.sqlalchemy.migrate_repo.schema import DateTime
from db.sqlalchemy.migrate_repo.schema import Boolean
from db.sqlalchemy.migrate_repo.schema import String
from db.sqlalchemy.migrate_repo.schema import Table
import logging

logger = logging.getLogger('trove.db.sqlalchemy.migrate_repo.schema')

meta = MetaData()

configurations = Table(
    'configurations',
    meta,
    Column('id', String(36), primary_key=True, nullable=False),
    Column('name', String(64), nullable=False),
    Column('description', String(256)),
    Column('deleted', Boolean(), nullable=False, default=False),
    Column('deleted_at', DateTime()),
)

configuration_parameters = Table(
    'configuration_parameters',
    meta,
    Column('configuration_id', String(36), ForeignKey("configurations.id"),
           nullable=False, primary_key=True),
    Column('configuration_key', String(128), nullable=False, primary_key=True),
    Column('configuration_value', String(128)),
    Column('deleted', Boolean(), nullable=False, default=False),
    Column('deleted_at', DateTime()),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine

    # since the downgrade is a no-op, an upgrade after a downgrade will
    # cause an exception because the tables already exist
    # we will catch that case and log an info message
    try:
        create_tables([configurations])
        create_tables([configuration_parameters])

        # instances = Table('instances', meta, autoload=True)
        # instances.create_column(Column('configuration_id', String(36),
        #                                ForeignKey("configurations.id")))
    except OperationalError as e:
        logger.info(e)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    # Not dropping the tables for concern if rollback needed would cause
    # consumers to recreate configurations.
