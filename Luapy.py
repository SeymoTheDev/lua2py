import time
import random
import sys
import os
def WaitFor():
    time.sleep(1)


def WaitFor(secs):
    time.sleep(secs)

def dofilelua(dir, msg):
    d = open(f'{dir}.lua', 'w')
    d.write(f'{msg}')
    d.close

def dofiletxt(dir, msg):
    d = open(f'{dir}.txt', 'w')
    d.write(f'{msg}')
    d.close


def kill():
    quit()
    
def waitforuser(prmpt):
    print(prmpt)
    wfifunc = input('>')

def waitrepeat(prmpt):
    print(prmpt)
    while True:
        s = input('>')
        print(s)

def write(secs, s):
    msg = f'{s}'

    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(secs)
    
def local(func):
    if func == 'Connect':
        socket = 'localhost'
    elif func == 'GetUser':
        user = 'root'


def GetUserData(inputs, stat, output):
        print(inputs)
        usus = input('>')
        if usus.strip() == stat:
            print(output)
    
def end():
    quit()

def snap():
    quit()

def calcp(num1, num2, num3, num4, num5):
    print(num1 + num2 + num3 + num4 + num5)

def calcp(num1, num2, num3, num4):
    print(num1 + num2 + num3 + num4)

def calcp(num1, num2, num3):
    print(num1 + num2 + num3)

def calcp(num1, num2):
    print(num1 + num2)

def lib(name):
    os.mkdir(name)

def checkFor(ftcf):
    if ftcf == vars:
        print("Checked for extra variables. Found them!")

def reset():
    print("Resetting")
    quit()

def build():
    print("Currently Running Luapy 1.30 BETA!")


def range(a, b, c, d, e, f):
    r = [a, b, c, d, e, f]

    print(random.choice(r))

    
snap