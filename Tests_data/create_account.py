from Parameter_Object.user import User
import random
import string

def random_string(maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

def random_digits(maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

testdata = [
User(address1='123', tax_id=random_digits(6), company=random_string(10), firstname=random_string(10),
     lastname=random_string(6), email=random_string(10)+'@mail.com', password=random_string(8))
    for i in range(10)
]