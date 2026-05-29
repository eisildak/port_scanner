import socket
from concurrent.futures import ThreadPoolExecutor

# Target configuration
TARGET = "www.erolisildak.com"
TIMEOUT = 1.0  # Connection timeout in seconds
MAX_THREADS = 100  # Number of concurrent threads

def scan_port(ip, port):
    """Scans the given IP and port, prints it if open."""
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            # connect_ex returns 0 if the port is open
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port:<5} OPEN")
    except Exception:
        # Ignore connection errors or interruptions
        pass

def main():
    try:
        print(f"[*] Resolving target: {TARGET}")
        target_ip = socket.gethostbyname(TARGET)
        print(f"[*] Target IP: {target_ip}")
        print(f"[*] Starting scan (1-1024)...")
        print("-" * 40)

        # Manage multiple threads with ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            # Distribute ports 1-1024 across the thread pool
            for port in range(1, 1025):
                executor.submit(scan_port, target_ip, port)
                
        print("-" * 40)
        print("[*] Scan complete.")

    except socket.gaierror:
        print("[!] Error: Could not resolve hostname (DNS error).")
    except KeyboardInterrupt:
        print("\n[!] Cancelled by user.")

if __name__ == "__main__":
    main()