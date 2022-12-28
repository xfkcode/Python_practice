"""
多线程编程
"""
import time
import threading

def sing(msg:str):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing,args=('我在唱歌',))
    dance_thread = threading.Thread(target=dance,kwargs={'msg':'我在唱歌'})
    sing_thread.start()
    dance_thread.start()