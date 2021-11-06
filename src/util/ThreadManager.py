import threading
import sys

class ThreadManager():
    __threads = []
    run_threads = True

    def addThread(thread):
        ThreadManager.__threads.append(thread)

    def closeThreads():
        ThreadManager.run_threads = False
        for t in ThreadManager.__threads:
            t.join()