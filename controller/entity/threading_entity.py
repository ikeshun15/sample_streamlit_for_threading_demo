import threading
import time

class ThreadingWorkerEntity(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        self.should_stop = threading.Event()

    def run(self):
        while not self.should_stop.wait(0):
            time.sleep(1)
            self.counter += 1