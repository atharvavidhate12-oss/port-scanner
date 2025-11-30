# main.py

import argparse
from scanner import scan_ports

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")

    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")

    args = parser.parse_args()

    open_ports = scan_ports(
        target=args.target,
        start_port=args.start,
        end_port=args.end,
        threads=args.threads
    )

    print("\n🎯 Scan Completed!")
    print("=================================")
    if open_ports:
        print("🔓 Open Ports Found:")
        for p in open_ports:
            print(f" → {p}")
    else:
        print("❌ No open ports found.")

if __name__ == "__main__":
    main()
