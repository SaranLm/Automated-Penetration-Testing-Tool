import nmap

def enumerate_target(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-O -sV')

    print("\n[+] Enumerating Target: ", target)
    
    if "osmatch" in scanner[target]:
        print(f"[*] Detected OS: {scanner[target]['osmatch'][0]['name']}")

    for proto in scanner[target].all_protocols():
        print(f"\n[*] Protocol: {proto}")
        ports = scanner[target][proto].keys()
        for port in ports:
            state = scanner[target][proto][port]['state']
            service = scanner[target][proto][port]['name']
            print(f"  Port {port} | State: {state} | Service: {service}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    enumerate_target(target_ip)
