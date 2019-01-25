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

def random_string(maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

def random_digits(maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

testdata = [
User(tax_id=random_digits(6), company=random_string(10), firstname=random_string(10),
     lastname=random_string(6), email=random_string(10)+'@mail.com', password=random_string(8))
    for i in range(data_amount)
]


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Tests_data\\", file)
with open(data_file, 'w') as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))