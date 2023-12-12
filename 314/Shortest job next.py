class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def shortest_job_next(processes):
    current_time = 0
    total_burst_time = sum([process.burst_time for process in processes])
    completed_processes = []

    while total_burst_time > 0:
        available_processes = [process for process in processes if process.arrival_time <= current_time and process.burst_time > 0]

        if len(available_processes) == 0:
            current_time += 1
            continue

        shortest_process = min(available_processes, key=lambda x: x.burst_time)
        print(f"Executing Process {shortest_process.process_id} at time {current_time}")

        shortest_process.burst_time -= 1
        current_time += 1
        total_burst_time -= 1

        if shortest_process.burst_time == 0:
            completed_processes.append(shortest_process)

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),  # Process ID, Arrival Time, Burst Time
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]

    shortest_job_next(processes)
