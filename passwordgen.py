import random
from string import ascii_letters, punctuation, digits

char_pass_all = ascii_letters + digits + punctuation
char_pass_ld = ascii_letters + digits
char_pass_p = ascii_letters + punctuation
char_pass_l = ascii_letters

def passwAll(n):
    password = ''.join([random.choice(char_pass_all) for p in range(n)])
    return password
 
def passwLd(n):
    password = ''.join([random.choice(char_pass_ld) for p in range(n)])
    return password
 
def passwL(n):
    password = ''.join([random.choice(char_pass_l) for p in range(n)])
    return password

def passP(n):
    password = ''.join([random.choice(char_pass_p) for p in range(int(n))])
    return password