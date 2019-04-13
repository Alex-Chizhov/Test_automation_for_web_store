from Parameter_Object.user import User
import random
import string
import os
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "d:f:", ["amount_of_data=","file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

data_amount = 5
file = 'users.json'

for option, argument  in opts:
    if option in ['-d', '--amount_of_data']:
        data_amount = int(argument)
    elif option in ['-f', '--file']:
        file = argument

def random_string(minlen, maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(minlen, maxlen))])

def random_digits(minlen, maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(minlen, maxlen))])

testdata = [
User(
    tax_id=random_digits(6, 7),
    company=random_string(5, 10),
    firstname=random_string(5, 10),
    lastname=random_string(5, 10),
    email=random_string(5, 10)+'@mail.com',
    password=random_string(8, 10),
    address1=random_string(10, 20)+random_string(2, 6),
    city=random_string(5, 10),
    phone='+'+random_digits(8,11),
    postcode=random_digits(6, 7)
    )

    for i in range(data_amount)
]


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Tests_data\\", file)
with open(data_file, 'w') as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))