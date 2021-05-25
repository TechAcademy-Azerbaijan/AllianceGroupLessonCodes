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
    for _ in range(50):
        result = executor.submit(do_something, 2)
        results.append(result)

    for result in concurrent.futures.as_completed(results):
            print(result.result())



t2 = time.time()

print('netice', t2-t1)

