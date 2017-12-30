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

    attrs = {}
    for key in keys:
        field_kw = {}
        if 'password' in key:
            field_kw['widget'] = forms.PasswordInput
        attrs[key] = forms.CharField(**field_kw)

    metaclass = type(forms.Form)
    return metaclass('CredentialForm', (forms.Form,), attrs)


def get_credential_class2(service, *args, **kwargs):
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

    attrs = {}
    for key in keys:
        field_kw = {}
        if 'password' in key:
            field_kw['widget'] = forms.PasswordInput
        attrs[key] = forms.CharField(**field_kw)

    metaclass = type(forms.Form)
    cls = metaclass('CredentialForm', (forms.Form,), attrs)
    return cls(*args, **kwargs)

