import time
import requests
from multiprocessing import Process

t1 = time.time()

def download(index):
    response = requests.get('https://picsum.photos/200/300')
    with open(f'./images/image_{index}.jpg', 'wb') as f:
        f.write(response.content)
    print(f'{index}. downloaded')

threads = []

for index in range(100):
    thread = Process(target=download, args=[index])
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

t2 = time.time()

print('netice', t2-t1)
