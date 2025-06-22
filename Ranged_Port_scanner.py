# Port_Scanner.py
#A python based Port Scanner on a wider range of ports...within a specific Domain... 
import socket
import time

# Get target host and port range from user
target = input("Enter the target host (IP or domain): ")
start_port = int(input("Enter starting port (e.g., 1): "))
end_port = int(input("Enter ending port (e.g., 1000): "))

print(f"\n🔎 Scanning {target} from port {start_port} to {end_port}...\n")
start_time = time.time()

# Loop through the range of ports
for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        sock.close()

    except KeyboardInterrupt:
        print("\n❗ Scan interrupted by user.")
        break
    except socket.gaierror:
        print("❗ Hostname could not be resolved.")
        break
    except socket.error:
        print("❗ Couldn't connect to server.")
        break

end_time = time.time()
print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")
