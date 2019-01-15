class User:

    def __init__(self, tax_id=None, company=None, firstname=None, lastname=None, email=None,
                 password=None):
        self.tax_id = tax_id
        self.company = company
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password