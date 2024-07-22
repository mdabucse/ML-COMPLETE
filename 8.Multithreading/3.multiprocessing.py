# Process the that run in Parallel
# Where we use -> CPU BOUND TASKS -> There is an Task Heavy On CPU We Use the Multi Processing
# Access the Multiple Core In The CPU
# 'IMP' Whenever we use the Multiprocessing We Must use the __name__=='__main__'

import multiprocessing
import time


def squre():
    for i in range(5):
        time.sleep(1)
        print(f'Square {i*i}')

def cube():
    for i in range(5):
        time.sleep(1)
        print(f'Cube {i*i*i}')

if __name__ =='__main__':
    # without Process
    t = time.time()
    squre()
    cube()
    print(f"Without Process The Calculated time is {time.time()-t}")

    # Creating The Process
    p1 = multiprocessing.Process(target=squre)
    p2 = multiprocessing.Process(target=cube)

    # Calculate The Timing
    t = time.time()

    # Start The Process
    p1.start()
    p2.start()

    # Waiting for The Process
    p1.join()
    p2.join()

    print(f"Process The Calculated time is {time.time()-t}")