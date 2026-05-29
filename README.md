# Port Scanner

A multi-threaded TCP port scanner. Scans ports 1–1024 on a given target in parallel and reports all open ports.

## Features

- Supports hostnames and IP addresses via DNS resolution
- Concurrent scanning with `ThreadPoolExecutor`
- Configurable timeout and thread count

## Requirements

- Python 3.x (standard library only, no extra packages needed)

## Usage

```bash
python3 "import socket v2.py"
```

Edit the variables at the top of the file to change the target:

```python
TARGET = "www.example.com"   # Hostname or IP address
TIMEOUT = 1.0                # Connection timeout in seconds
MAX_THREADS = 100            # Number of concurrent threads
```

## Example Output

```
[*] Resolving target: www.example.com
[*] Target IP: 93.184.216.34
[*] Starting scan (1-1024)...
----------------------------------------
[+] Port 80    OPEN
[+] Port 443   OPEN
----------------------------------------
[*] Scan complete.
```

## Legal Disclaimer

This tool should only be used on systems you **own or have explicit permission to test**. Unauthorized port scanning may be illegal.
# port_scanner
