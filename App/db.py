import mysql.connector
from Parameter_Object.user import User


class DbFixture:


    def __init__(self, host, database, user, passwd):
        self.host = host,
        self.database = database,
        self.user = user,
        self.passwd = passwd
        self.connection = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

    def get_user_list(self):
        list_with_objs = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT email, tax_id, company, firstname, lastname FROM lc_customers")
            for row in cursor:
                type_fixed_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                (email, tax_id, company, firstname, lastname) = type_fixed_row
                list_with_objs.append(User(tax_id=tax_id, company=company, firstname=firstname, lastname=lastname,
                                           email=email,))

        finally:
            cursor.close()

        return list_with_objs

    def get_product_count_from_db(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM lc_products")
        result = cursor.fetchall()

        return len(result)

    def destroy(self):
        self.connection.close()