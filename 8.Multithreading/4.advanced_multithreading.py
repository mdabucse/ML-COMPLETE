# Multithreading With Thread Pool Executor
from concurrent.futures import ThreadPoolExecutor
import time
def print_numbers(number):
    time.sleep(2) # Waiting for I/O
    print(f'Number:{number}')

numbers = [1,2,3,4,5]

#Create the ThreadPoolExecutor  (max_workers = ?) No Of Threads 

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers,numbers)

for i in results:
    print(i)

