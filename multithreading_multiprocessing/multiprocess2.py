import time
import requests
from multiprocessing import Pool

t1 = time.time()

def download(index):
    response = requests.get('https://picsum.photos/200/300')
    with open(f'./images/image_{index}.jpg', 'wb') as f:
        f.write(response.content)
    print(f'{index}. downloaded')

threads = []

with Pool(100) as p:
    print(p.map(download, range(100)))


t2 = time.time()

print('netice', t2-t1)
