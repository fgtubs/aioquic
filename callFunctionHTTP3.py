import threading
import multiprocessing
import os
import time

from numpy import random


# Constants
numOfCalls = 100
numOfParallelProcesses = 200

def call():
    os.system("python3 /home/student/PycharmProjects/aioquic/examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://192.168.1.2:4433/ws")
    # os.system("python3 /home/student/PycharmProjects/aioquic/examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://192.168.1.4:4433/ws")
    # os.system("python3 /home/student/PycharmProjects/aioquic/examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://localhost:4433/ws")

def calls_in_thread():
    time_delay = random.normal(1,0.15,numOfCalls)
    for _ in range(numOfCalls):
        time.sleep(time_delay[_])
        call()

for _ in range(numOfParallelProcesses):
    t = threading.Thread(target=calls_in_thread)
    t.start()

# for _ in range(numOfParallelProcesses):
#     p = multiprocessing.Process(target=calls_in_thread)
#     p.start()