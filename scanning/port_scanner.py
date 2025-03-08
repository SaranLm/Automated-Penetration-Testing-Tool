import nmap

def scan_ports(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p 1-1000 -sV')
    for host in scanner.all_hosts():
        print(f"\n[+] Target: {host}")
        for port, info in scanner[host]['tcp'].items():
            print(f"  Port {port} | State: {info['state']} | Service: {info['name']}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_ports(target_ip)
