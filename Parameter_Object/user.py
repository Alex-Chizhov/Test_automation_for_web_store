class User:

    def __init__(self, tax_id=None, company=None, firstname=None, lastname=None, email=None,
                 password=None, address1=None, city=None, phone=None, postcode=None):
        self.tax_id = tax_id
        self.company = company
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.address1 = address1
        self.city = city
        self.phone = phone
        self.postcode = postcode

    def __repr__(self):
        return f"tax_id={self.tax_id}, company={self.company}, firstname={self.firstname}, " \
               f"lastname={self.lastname}, email={self.email}, password={self.password}  " \
               f"address1={self.address1}, city={self.city}, phone={self.phone}, postcode={self.postcode}"

    def __eq__(self, other):
        return  self.tax_id == other.tax_id or self.tax_id == None and \
                self.company == other.company and\
                self.firstname == other.firstname and\
                self.lastname == other.lastname and\
                self.email == other.email and\
                self.password == other.password or self.password == None

    def sort_key_firstname(self):
        return self.firstname