from sqlalchemy import MetaData
from sqlalchemy import orm
from sqlalchemy.orm import exc as orm_exc
from sqlalchemy import Table


def map(engine):
    from db.data_models import test1

    meta = MetaData()
    meta.bind = engine
    if mapping_exists(test1.DBTestTable1):
        return

    tables = {
        "test1": test1.DBTestTable1,
        "test2": test1.DBTestTable2,
        "configurations": test1.DBConfiguration,
        "configuration_parameters": test1.DBConfigurationParameter
    }

    for table_name, data_model in tables.items():
        orm.mapper(data_model, Table(table_name, meta, autoload=True))


def mapping_exists(model):
    try:
        orm.class_mapper(model)
        return True
    except orm_exc.UnmappedClassError:
        return False
