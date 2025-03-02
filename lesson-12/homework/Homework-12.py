# Homework-12

#1. Write a Python program that checks whether a given range of numbers contains prime numbers.
# Divide the range among multiple threads to parallelize the prime checking process. 
# Each thread should be responsible for checking a subset of the range
#  and the main program should print the list of prime numbers found.

import threading
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end, primes):
    local_primes = [num for num in range(start, end) if is_prime(num)]
    primes.extend(local_primes) 

def main():
    start_range = int(input("Enter start of range: "))
    end_range = int(input("Enter end of range: "))
    num_threads = 4 
    
    thread_list = []
    primes = []  
    step = (end_range - start_range) // num_threads
    
    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i != num_threads - 1 else end_range
        thread = threading.Thread(target=find_primes_in_range, args=(start, end, primes))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()
    
    primes.sort()
    print("Prime numbers in range:", primes)

if __name__ == "__main__":
    main()

#2. Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. 
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading
from collections import Counter

def count_words(lines, word_count):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    
    with lock:
        word_count.update(local_counter)

def main():
    filename = input("Enter the filename: ")
    num_threads = 4  
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    chunk_size = len(lines) // num_threads
    threads = []
    global word_count, lock
    word_count = Counter()
    lock = threading.Lock()
    
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], word_count))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("Word Frequency:")
    for word, count in word_count.most_common(10): 
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
