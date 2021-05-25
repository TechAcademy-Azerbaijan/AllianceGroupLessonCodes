import time
import concurrent.futures

t1 = time.time()

def do_something(sleep_time):
    # print('started')
    time.sleep(sleep_time)
    # print('finished')
    return f'finished in {sleep_time} seconds'

results = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    results = executor.map(do_something, seconds)

    for result in results:
        print(result)


t2 = time.time()

print('netice', t2-t1)
