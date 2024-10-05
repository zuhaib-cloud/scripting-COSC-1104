#Total Resources and constants
total_cpu = 8
total_memory = 32
allocated_resources = []
pending_requests = []
used_cores = 0
used_mem = 0


while True:
    #user details and resources required
    username = input("Enter your username: ")
    required_cpu = int(input("Enter number of CPUs required: "))
    required_mem = float(input("Enter amount of memory requred in GB: "))
   
    if required_cpu <= 0 or required_mem <= 0:
        print("Invalid resource request. Resource request cannot be negative.")
        break
    
    elif required_cpu > total_cpu or required_mem > total_memory:
        print("Resources exceeds availability limit.\n")
        print(f"Available Resources: CPU cores - {total_cpu} | Memory - {total_memory}\n")
        break  

    elif (required_cpu + used_cores <= total_cpu) and (required_mem + used_mem <= total_memory):
        # Resources are available; allocate them
        allocated_resources.append([username, required_cpu, required_mem])
        used_cores += required_cpu
        used_mem += required_mem
        print(f"Resources allocated to {username}: {required_cpu} CPU cores and {required_mem} GB memory.\n")
        break 

    elif (required_cpu + used_cores > total_cpu) and (required_mem + used_mem > total_memory):
        # Resources are available; allocate them
        pending_requests.append([username, required_cpu, required_mem])
        print(f"Resources allocated to {username}: {required_cpu} CPU cores and {required_mem} GB memory.\n")
        break  
    
   

    else:
        # Resources are not available; add to pending requests
        pending_requests.append([username, required_cpu, required_mem])
        print(f"Request from {username} is pending due to insufficient resources.\n")
        another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
        if another_request != 'yes':
         break
        break

# Display Output
#available resources
print("\nAllocated Resources:")
print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<12}")
print("-" * 37)
for allocation in allocated_resources:
    print(f"{allocation[0]:<15}{allocation[1]:<10}{allocation[2]:<12}")
#pending requests
if pending_requests:
    print("\nPending Requests:")
    print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<12}")
    print("-" * 37)
    for request in pending_requests:
        print(f"{request[0]:<15}{request[1]:<10}{request[2]:<12}")
else:
    print("\nNo pending requests.")
