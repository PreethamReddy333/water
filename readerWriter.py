import threading
import time
import random

shared_data =0
read_count=0
read_count_lock = threading.Lock()
resource_lock = threading.Lock()
MAX_OPERATIONS = 3

def reader(reader_id):
    global read_count
    for i in range(MAX_OPERATIONS):
        time.sleep(random.uniform (0.5, 1))
        with read_count_lock:
            read_count += 1
            if read_count == 1:
                resource_lock.acquire()
        print(f"Reader {reader_id} is reading: {shared_data}")
        time.sleep(random.uniform (0.1, 0.3))
        with read_count_lock:
            read_count-=1
            if read_count == 0:
		resource_lock.release()

def writer(writer_id):
    global shared_data
    for i in range (MAX_OPERATIONS):
        time.sleep(random.uniform (1, 2)
        with resource_lock:
            shared_data = random.randint(1, 100)
            print(f"Writer {writer_id} wrote: {shared_data}")
            time.sleep(random.uniform (0.2, 0.4))

reader_threads = []
for i in range(3):
    t = threading.Thread(target=reader, args=(i,))
    reader_threads.append(t)
    t.start()

writer_threads = []
for i in range(2):
    t = threading.Thread(target=writer, args=(i,))
    writer_threads.append(t)
    t.start()

for t in reader_threads + writer_threads:
    t.join()

print("All reading and writing operations are completed.")

