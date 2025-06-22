import socket

# Get target from user input
target = input("Enter the target host (IP or domain): ")

# Common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

print(f"🔎 Scanning {target}...\n")

for port in common_ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")

        sock.close()
        
    except KeyboardInterrupt:
        print("❗ Scan interrupted by user.")
        break
    except socket.gaierror:
        print("❗ Hostname could not be resolved.")
        break
    except socket.error:
        print("❗ Couldn't connect to server.")
        break
print("\n🔍 Scan complete.")
# End of portscanner.py
