# -*- coding:utf-8 -*-
from multiprocessing import Pool
from threading import Thread
import threading
from multiprocessing import Process
from random import random
from time import clock
lock = threading.Lock()
def comput():
    DARTS=100000
    hits = 0.0
    a=1

    while True:
        clock()
        lock.acquire()
        for i in range(1,DARTS+1):
            x,y = random(),random()
            dist = pow(x ** 2 + y ** 2,0.5)
            if dist<=1.0:
                hits = hits + 1

            if i== DARTS*0.01*a :
                a+=3
        pi = 4* (hits/DARTS)
        lock.release()
        pass

def comout():
    DARTS=100000
    hits = 0.0
    a=1

    while True:
        clock()
        lock.acquire()
        for i in range(1,DARTS+1):
            x,y = random(),random()
            dist = pow(x ** 2 + y ** 2,0.5)
            if dist<=1.0:
                hits = hits + 1

            if i== DARTS*0.01*a :
                a+=3
        pi = 4* (hits/DARTS)
        lock.release()
        pass

def comerr():
    DARTS=100000
    hits = 0.0
    a=1

    while True:
        clock()
        lock.acquire()
        for i in range(1,DARTS+1):
            x,y = random(),random()
            dist = pow(x ** 2 + y ** 2,0.5)
            if dist<=1.0:
                hits = hits + 1

            if i== DARTS*0.01*a :
                a+=3
        pi = 4* (hits/DARTS)
        lock.release()
        pass

def loop():
    while True:
        num = 1/3
        pass

if __name__ == '__main__':
    for i in range(32):
        t1 = Thread(target=comput)
        t2 = Thread(target=loop)
        t3 = Thread(target=comout)
        t4 = Thread(target=comerr)
        t1.start()
        t2.start()
        t3.start()
        t4.start()

    while True:
        pass