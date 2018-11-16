from db.models import DatabaseModelBase


class DBTestTable1(DatabaseModelBase):
    _data_fields = ['id', 'name', 'description', 'deleted', 'created', 'updated', 'deleted_at']


class DBTestTable2(DatabaseModelBase):
    _data_fields = ['id', 'name', 'age', 'deleted', 'created', 'updated', 'deleted_at']
