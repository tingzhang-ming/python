# vim: tabstop=4 shiftwidth=4 softtabstop=4

# from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData

from db.sqlalchemy.migrate_repo.schema import create_tables
from db.sqlalchemy.migrate_repo.schema import DateTime
from db.sqlalchemy.migrate_repo.schema import drop_tables
from db.sqlalchemy.migrate_repo.schema import Integer
from db.sqlalchemy.migrate_repo.schema import BigInteger
from db.sqlalchemy.migrate_repo.schema import String
from db.sqlalchemy.migrate_repo.schema import Table


meta = MetaData()

test1 = Table(
    'test1',
    meta,
    Column('id', String(36), primary_key=True, nullable=False),
    Column('created', DateTime()),
    Column('updated', DateTime()),
    Column('name', String(255)),
    Column('description', String(255)),
    Column('deleted', Integer),
    Column('deleted_at', DateTime())
    )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    create_tables([test1])


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    drop_tables([test1])
