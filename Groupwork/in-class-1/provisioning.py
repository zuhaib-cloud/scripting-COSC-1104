total_cpu = 8
total_memory = 32
required_cpu = int(input("Enter number of CPUs required: "))
required_mem = float(input("Enter amount of memory requred in GB: "))
available_cpu = 0
available_mem = 0

while True:
    if required_cpu == 0 or required_mem == 0:
        print("Invalid resource request.")
        break
    elif required_cpu > total_cpu or required_mem > total_memory:
        print("Resources exceeds availability limit.\n")
        print(f"Available Resources: CPU cores - {available_cpu} | Memory - {available_mem}\n")
        break    
    elif required_cpu <= 8 and required_mem <= 32.0: 
        available_cpu = total_cpu - required_cpu
        available_mem = float(total_memory - required_mem)
        print(f"CPU cores alloted: {required_cpu} Memory alloted: {required_mem}\n")
        print(f"Available Resources: CPU cores - {available_cpu} | Memory - {available_mem}\n")
        break
