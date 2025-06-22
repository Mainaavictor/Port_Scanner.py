import socket
import threading
import time

target = input("Enter the target host (IP or domain): ")
start_port = int(input("Enter starting port (e.g., 1): "))
end_port = int(input("Enter ending port (e.g., 1000): "))

print(f"\n🔎 Scanning {target} from port {start_port} to {end_port} using multithreading...\n")

open_ports = []  # Thread-safe list can be added later, for now simple list works

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    except:
        pass

start_time = time.time()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()
print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")
print(f"Open ports found: {sorted(open_ports)}")
print("🔍 Scan complete.")
