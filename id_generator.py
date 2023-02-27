import random
import string


def gen_tick():
    x= ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))
    return x;



def gen_pass():
    x= ''.join(random.choices(string.ascii_lowercase+string.digits, k=9))
    return x;



    