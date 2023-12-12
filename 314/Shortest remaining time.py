class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def shortest_remaining_time(processes):
    current_time = 0
    total_burst_time = sum([process.burst_time for process in processes])
    completed_processes = []

    while total_burst_time > 0:
        min_remaining_time = float('inf')
        selected_process = None

        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if process.remaining_time < min_remaining_time:
                    min_remaining_time = process.remaining_time
                    selected_process = process

        if selected_process is None:
            current_time += 1
            continue

        print(f"Executing Process {selected_process.process_id} at time {current_time}")

        selected_process.remaining_time -= 1
        current_time += 1
        total_burst_time -= 1

        if selected_process.remaining_time == 0:
            completed_processes.append(selected_process)

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),  # Process ID, Arrival Time, Burst Time
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]

    shortest_remaining_time(processes)
