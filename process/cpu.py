from multiprocessing import Process
import sys, os
import time


def timetask(times):
    pass


def works_multi_process(func, worknum):
    proc_record = []
    for i in range(worknum):
        p = Process(target=func, args=(i,))
        p.start()
        proc_record.append(p)
    for p in proc_record:
        p.join()


def works_single_process(func, worknum):
    proc_record = []
    for i in range(worknum):
        p = Process(target=func, args=(i,))
        p.start()
        p.join()


if __name__ == '__main__':
    while True:
        procs = 10
        works_multi_process(timetask, procs)
    pass
