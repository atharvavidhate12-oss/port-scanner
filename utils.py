# utils.py
import socket

def scan_single_port(host: str, port: int, timeout: float = 1.0):
    """
    Attempts to connect to <host>:<port>.
    Returns True if port is open, False otherwise.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)

        try:
            s.connect((host, port))
            return True
        except:
            return False
