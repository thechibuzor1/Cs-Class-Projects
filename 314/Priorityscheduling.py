class Process:
    def __init__(self, process_id, burst_time, priority):
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority

def priority_scheduling(processes):
    # Sort processes based on priority (lower number indicates higher priority)
    sorted_processes = sorted(processes, key=lambda x: x.priority)

    current_time = 0
    total_burst_time = sum([process.burst_time for process in sorted_processes])

    while total_burst_time > 0:
        for process in sorted_processes:
            if process.burst_time > 0:
                print(f"Executing Process {process.process_id} at time {current_time}")
                if process.burst_time > 1:
                    current_time += 1
                    process.burst_time -= 1
                else:
                    current_time += process.burst_time
                    process.burst_time = 0

                total_burst_time -= 1 if process.burst_time > 0 else process.burst_time

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 6, 2),  # Process ID, Burst Time, Priority
        Process(2, 4, 1),
        Process(3, 8, 4),
        Process(4, 2, 3)
    ]

    priority_scheduling(processes)
