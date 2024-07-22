# When we Use the Multithreading
'''
* I/O Tasks that spend More time waiting for I/O Operations
* Concurrent Execution 
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2) # Waiting for I/O
        print(f'Number:{i}')

def print_letter():
    for i in 'abcde':
        time.sleep(2) # Waiting for I/O
        print(f'Alphabets:{i}')


# Create a Thread
t1 = threading.Thread(target=print_letter)
t2 = threading.Thread(target=print_numbers)

# Start The Thread
t = time.time()

#Run the Thread
t1.start()
t2.start()

#Wait for the thread , Connect The threads -> It means the One of the Thread goes to the I/O That time another Thread Goes to The Execution
t1.join() 
t2.join()
t = time.time() - t
print(f"The Thread Time Taken :{t}")


#Without Threading 
t = time.time()
print_numbers()
print_letter()
finished_time = time.time() - t
print(f"The Non Thread Finishing Time {finished_time}")