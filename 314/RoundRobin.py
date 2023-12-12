class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, time_slice):
    queue = []  # Queue to hold processes
    current_time = 0  # Current time
    n = len(processes)  # Number of processes
    total_burst_time = sum([process.burst_time for process in processes])  # Total burst time

    while total_burst_time > 0:
        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if process not in queue:
                    queue.append(process)

        if len(queue) == 0:
            current_time += 1
            continue

        running_process = queue.pop(0)  # Get the first process from the queue
        print(f"Executing Process {running_process.process_id} at time {current_time}")

        if running_process.remaining_time > time_slice:
            current_time += time_slice
            running_process.remaining_time -= time_slice
        else:
            current_time += running_process.remaining_time
            running_process.remaining_time = 0

        total_burst_time -= time_slice if running_process.remaining_time > 0 else running_process.remaining_time

        if running_process.remaining_time > 0:
            queue.append(running_process)

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]

    time_slice = 2
    round_robin(processes, time_slice)
