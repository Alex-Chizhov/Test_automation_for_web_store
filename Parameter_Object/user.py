class User:

    def __init__(self, tax_id=None, company=None, firstname=None, lastname=None, email=None,
                 password=None):
        self.tax_id = tax_id
        self.company = company
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return f"tax_id={self.tax_id}, company={self.company}, firstname={self.firstname}, " \
               f"lastname={self.lastname}, email={self.email}, password={self.password}"