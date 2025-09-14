import socket, sys
import threading


def tcp_scan(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            print(f"{port}/tcp open")
        except (socket.timeout, ConnectionRefusedError):
            pass

def threaded_scan(host, ports, timeout=0.5):
    threads = []
    for port in ports:
        thread = threading.Thread(target=tcp_scan, args=(host, port, timeout))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
