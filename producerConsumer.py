import threading
import queue
import time
import random
buffer = queue.Queue(maxsize = 10)
def consumer() :
    for i in range(5):
        item = buffer.get()
        print(f"Consumed :{item}",end = '\n')
        buffer.task_done()
        time.sleep(random.uniform(0.2,0.6))
def producer() :
    for i in range(5):
        item = random.randint(1,100)
        buffer.put(item)
        print(f"Produced :{item}",end = '\n')
        time.sleep(random.uniform(0.1,0.5))
producer_thread = threading.Thread(target = producer)
consumer_thread = threading.Thread(target = consumer)

producer_thread.start()

consumer_thread.start()


producer_thread.join()
consumer_thread.join()

buffer.join()
print("All items P and C.")
