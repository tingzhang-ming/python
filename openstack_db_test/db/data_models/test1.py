from db.models import DatabaseModelBase


class DBTestTable1(DatabaseModelBase):
    _data_fields = ['id', 'name', 'description', 'deleted', 'created', 'updated', 'deleted_at']


class DBTestTable2(DatabaseModelBase):
    _data_fields = ['id', 'name', 'age', 'deleted', 'created', 'updated', 'deleted_at']


class DBConfiguration(DatabaseModelBase):
    _data_fields = ['id', 'name', 'description', 'deleted', 'deleted_at']


class DBConfigurationParameter(DatabaseModelBase):
    _data_fields = ['id', 'configuration_id', 'configuration_key',
                    'configuration_value', 'deleted',
                    'deleted_at']

    def __hash__(self):
        return self.configuration_key.__hash__()
