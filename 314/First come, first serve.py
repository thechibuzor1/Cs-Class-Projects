class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def first_come_first_serve(processes):
    current_time = 0
    total_burst_time = sum([process.burst_time for process in processes])
    completed_processes = []

    while total_burst_time > 0:
        available_processes = [process for process in processes if process.arrival_time <= current_time and process.burst_time > 0]

        if len(available_processes) == 0:
            current_time += 1
            continue

        executing_process = available_processes[0]
        print(f"Executing Process {executing_process.process_id} at time {current_time}")

        executing_process.burst_time -= 1
        current_time += 1
        total_burst_time -= 1

        if executing_process.burst_time == 0:
            completed_processes.append(executing_process)

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),  # Process ID, Arrival Time, Burst Time
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]

    first_come_first_serve(processes)
