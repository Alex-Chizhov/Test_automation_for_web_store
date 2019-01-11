class Product:

    def __init__(self, name=None, date_from=None, date_to=None, short_description=None, description=None,
                 purchase_price=None):
        self.name = name
        self.date_from = date_from
        self.date_to = date_to
        self.short_description = short_description
        self.description = description
        self.purchase_price = purchase_price