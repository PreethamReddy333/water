import threading
import time
import random

N=5

forks = [threading.Lock() for i in range(N)]


def philosopher (philosopher_id):
    left_fork = philosopher_id
    right_fork= (philosopher_id + 1)%N

    for i in range(2):
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(random.uniform(1, 3))

        if philosopher_id == N-1:
            with forks[right_fork]:
                with forks[left_fork]: 
                    print(f"Philosopher {philosopher_id} is eating.")
                    time.sleep(random.uniform(1, 2)) 
        else:
            with forks[left_fork]:
                with forks[right_fork]:
                    print(f"Philosopher {philosopher_id} is eating.")
                    time.sleep(random.uniform(1, 2))
        print(f"Philosopher {philosopher_id} has finished eating and is now thinking again.")
philosophers = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    philosophers.append(t)
    t.start()
for t in philosophers:
    t.join()
print("All philosophers have finished eating and thinking.")
