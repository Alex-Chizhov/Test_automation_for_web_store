from Parameter_Object.user import User
import random
import string
import os
import json

def random_string(maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

def random_digits(maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

testdata = [
User(tax_id=random_digits(6), company=random_string(10), firstname=random_string(10),
     lastname=random_string(6), email=random_string(10)+'@mail.com', password=random_string(8))
    for i in range(10)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\Tests_data\\users.json')
with open(file, 'w') as f:
    f.write(json.dumps(testdata, default=lambda i: i.__dict__, indent=2))