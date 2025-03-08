from scanning.port_scanner import scan_ports
from scanning.enumeration import enumerate_target
from exploits.ssh_bruteforce import ssh_brute_force
from exploits.ftp_bruteforce import ftp_brute_force

def menu():
    print("\n🔹 Automated Pentest Tool 🔹")
    print("1. Port Scan")
    print("2. SSH Brute Force")
    print("3. FTP Brute Force")
    print("4. Enumeration")
    choice = input("\nSelect option: ")

    if choice == "1":
        target = input("\nEnter target IP: ")
        scan_ports(target)
    elif choice == "2":
        target = input("\nEnter target IP: ")
        user = input("Enter SSH username: ")
        passwords = ["admin", "123456", "password", "root"]
        ssh_brute_force(target, user, passwords)
    elif choice == "3":
        target = input("\nEnter target IP: ")
        user = input("Enter FTP username: ")
        passwords = ["admin", "123456", "password", "root"]
        ftp_brute_force(target, user, passwords)
    elif choice == "4":
        target = input("\nEnter target IP: ")
        enumerate_target(target)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    menu()
