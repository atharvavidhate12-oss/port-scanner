# scanner.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from utils import scan_single_port

def scan_ports(target: str, start_port: int, end_port: int, threads: int = 100):

    open_ports = []

    print(f"\n🔍 Scanning Target: {target}")
    print(f"📌 Port Range: {start_port} → {end_port}")
    print(f"⚡ Threads Used: {threads}\n")

    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_single_port, target, port): port for port in ports}

        for future in tqdm(as_completed(futures), total=len(ports), desc="Scanning Ports"):
            port = futures[future]
            is_open = future.result()

            if is_open:
                print(f"🟢 OPEN PORT: {port}")
                open_ports.append(port)

    return open_ports
