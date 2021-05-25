import time
import threading

t1 = time.time()

def do_something(sleep_time):
    print('started')
    time.sleep(sleep_time)
    print('finished')
    return f'finished in {sleep_time} seconds'

threads = []

for _ in range(50):
    thread = threading.Thread(target=do_something, args=[2,])
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()



t2 = time.time()

print('netice', t2-t1)

