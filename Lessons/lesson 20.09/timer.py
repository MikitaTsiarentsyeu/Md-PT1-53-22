import time

isRun = False

def start():
    global start_time
    global isRun
    isRun = True
    start_time = time.time()

def finish():
    if isRun:
        res = time.time() - start_time
        global isRun
        isRun = False
        return res
