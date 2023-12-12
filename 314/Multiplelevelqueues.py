class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

def multi_level_queues(processes):
    queues = {}  # Dictionary to hold multiple queues
    total_burst_time = sum([process.burst_time for process in processes])  # Total burst time of all processes

    # Initialize queues based on priority levels
    for process in processes:
        if process.priority not in queues:
            queues[process.priority] = []
        queues[process.priority].append(process)

    current_time = 0
    while total_burst_time > 0:
        for priority in sorted(queues.keys()):
            if len(queues[priority]) == 0:
                continue

            running_process = queues[priority].pop(0)  # Get the first process from the queue
            print(f"Executing Process {running_process.process_id} at time {current_time}")

            if running_process.remaining_time > 1:
                current_time += 1
                running_process.remaining_time -= 1
            else:
                current_time += running_process.remaining_time
                running_process.remaining_time = 0

            total_burst_time -= 1 if running_process.remaining_time > 0 else running_process.remaining_time

            if running_process.remaining_time > 0:
                queues[priority].append(running_process)

    print("All processes executed.")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5, 1),  # Process ID, Arrival Time, Burst Time, Priority
        Process(2, 1, 3, 2),
        Process(3, 2, 8, 1),
        Process(4, 3, 6, 3)
    ]

    multi_level_queues(processes)
