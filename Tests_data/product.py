from Parameter_Object.product import Product
import random
import string

def random_string(maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

def random_digits(maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

testdata = [
Product(name=random_string(10), short_description=random_string(10), description=random_string(100),
        USD=random_digits(3)) for i in range(10)]