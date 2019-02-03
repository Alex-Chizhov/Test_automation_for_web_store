class Product:

    def __init__(self, name=None, date_from=None, date_to=None, short_description=None, description=None,
                 USD=None, id=None):
        self.name = name
        self.date_from = date_from
        self.date_to = date_to
        self.short_description = short_description
        self.description = description
        self.USD = USD
        self.id = id

    def __repr__(self):
        return f"name={self.name} | USD={self.USD} | id={self.id}"

    def __eq__(self, other):
        return self.name == other.name and \
               self.USD == other.USD and \
               self.id == other.id or  self.id == None and \
               self.date_to == other.date_to or self.date_to == None and \
               self.date_from == other.date_from or self.date_from == None and \
               self.description == other.description or self.description == None and \
               self.short_description == other.short_description or self.short_description == None



    def sort_key_name(self):
        return self.name