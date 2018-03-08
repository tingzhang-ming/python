import csv


def get_credential_class(service):
    """
    Return a class representing a credential for the given service with
    an attribute representing the expected keys.
    """
    # Open our "database"
    keys = []
    with open('creds.csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            if row[0].lower() != service.lower():
                continue
            keys.append(row[1])

    class Credential(object):
        expected_keys = keys

        def __init__(self, **kwargs):
            if set(self.expected_keys) != set([i for i in kwargs.keys()]):
                raise ValueError('Keys do not match')

            for k, v in kwargs.items():
                setattr(self, k, v)
    return Credential

