#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import multiprocessing

def read(position):
    file_name = "file"+str(position)+".txt"
    arr=[]
    f = open(file_name, 'r')
    for line in f:
        arr.append(line)
    f.close()
    return arr

def func(position):
    arr = read(position)
    start_ind = len(arr)-5-position
    for pos in range(start_ind, len(arr)):
        arr.insert(pos-start_ind, arr.pop(pos))
    return arr

def file_wr(position, file):
    start_time = time.time()
    res = func(position)
    file_name = file+str(position)+".txt"
    f=open(file_name, 'w')
    for item in res:
        f.write(item)
    finish_time = time.time() - start_time
    f.write(str(finish_time))
    f.close()

def potoki():
    threads = []
    for i in range(1,4):
        threads.append(threading.Thread(target=file_wr, args=(i, "potok")))
    for thread in threads:
        thread.start()
        thread.join()
        thread._delete()

def processes():
    process = []
    for i in range(1, 4):
        process.append(multiprocessing.Process(target=file_wr, args=(i, "process")))
    for proc in process:
        proc.start()
    for proc in process:
        proc.join()
    for proc in process:
        proc.kill()

if __name__=='__main__':
    potoki()
    processes()