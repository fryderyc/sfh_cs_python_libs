import psutil

def get_system_info():
    cpu_usage = psutil.cpu_percent()
    mem_stats = psutil.virtual_memory()
    
    print("CPU Usage:", cpu_usage, "%")
    print("Total Memory:", round(mem_stats.total/(1024*1024*1024), 2), "GB")
    print("Available Memory:", round(mem_stats.available/(1024*1024*1024), 2), "GB")

def main():
    get_system_info()

if __name__ == '__main__':
    main()