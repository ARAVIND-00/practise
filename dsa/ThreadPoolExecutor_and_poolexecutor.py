import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_task(power):
    count = 0
    for i in range(10**power):
        count += 1
    return count

if __name__ == "__main__":
    num_tasks = 2
    power = 3

    print("Comparing ThreadPoolExecutor vs ProcessPoolExecutor (CPU-bound Task)")

    # ThreadPoolExecutor
    start_time_thread = time.time()
    with ThreadPoolExecutor(max_workers=num_tasks) as executor:
        results_thread = list(executor.map(cpu_task, [power] * num_tasks))
    end_time_thread = time.time()
    print(f"ThreadPoolExecutor Time Taken: {end_time_thread - start_time_thread:.4f} seconds")
    print(f"Thread Results: {results_thread}\n")

    # ProcessPoolExecutor
    start_time_process = time.time()
    with ProcessPoolExecutor(max_workers=num_tasks) as executor:
        results_process = list(executor.map(cpu_task, [power] * num_tasks))
    end_time_process = time.time()
    print(f"ProcessPoolExecutor Time Taken: {end_time_process - start_time_process:.4f} seconds")
    print(f"Process Results: {results_process}\n")

import time
from concurrent.futures import ThreadPoolExecutor

def watch_file(input_tuple):
    thread_id, file_path, thread_name = input_tuple
    count = 0
    print(f"Watching {file_path} on {thread_name}")
    while count < 5:
        print(f"{thread_name}: watching file {file_path} (iteration {count + 1})")
        time.sleep(2)
        count += 1
    print(f"{thread_name} done watching {file_path}")
    return f"Completed: {file_path}"

a = [
    (1, "a.txt", "thread_1"),
    (2, "b.txt", "thread_2"),
    (3, "c.txt", "thread_3"),
    (4, "d.txt", "thread_4"),
]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(watch_file, a))

    print("All threads completed.")
    print("Results:", results)
