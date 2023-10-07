import time

class Periodic:
    def __init__(self, wait_time=2):
        self.wait_time = wait_time
        self.running = False

    def start(self):
        print("Starting")
        self.running = True
        while self.running:
            self.show_time()
            time.sleep(self.wait_time)
    def stop(self):
        print("Stopping")
        self.running = False

    def show_time(self):
         print(time.ctime(time.time()))

p = Periodic()
p.start()
time.sleep(6)
print("Tryting to stop")
p.stop()