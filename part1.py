class IPManager:
    def __init__(self):
        self.leased_ips = set()

    def allocate_ip(self):
        if not self.leased_ips:
            # If no leased IPs, create the first one
            ip = "0.0.0.0"
        else:
            # Find the highest leased IP and increment it, handling carryover
            highest_ip = max(self.leased_ips)
            ip_parts = list(map(int, highest_ip.split('.')))
            ip_parts[3] += 1

            for i in range(3, 0, -1):
                if ip_parts[i] > 255:
                    ip_parts[i] = 0
                    ip_parts[i-1] += 1

            ip = ".".join(map(str, ip_parts))

        self.leased_ips.add(ip)
        return ip

    def release_ip(self, ip):
        if ip in self.leased_ips:
            self.leased_ips.remove(ip)
            return ip
        return None

    def is_ip_available(self, ip):
        return ip not in self.leased_ips

# # Example Usage
ip_manager = IPManager()


# # Allocate IP
# allocated_ip = ip_manager.allocate_ip()
# print(f"Allocated IP: {allocated_ip}")

# # Release IP
# released_ip = ip_manager.release_ip(allocated_ip)
# print(f"Released IP: {released_ip}")

# # Check Availability
# ip_to_check = "0.0.0.0"
# availability_status = ip_manager.is_ip_available(ip_to_check)
# print(f"IP {ip_to_check} is available: {availability_status}")


while True:
    user_input = input("Enter command (ASK/RELEASE/STATUS/EXIT): ").upper()

    if user_input == "ASK":
        allocated_ip = ip_manager.allocate_ip()
        print(f"Allocated IP: {allocated_ip}")

    elif user_input == "RELEASE":
        ip_to_release = input("Enter IP to release: ")
        released_ip = ip_manager.release_ip(ip_to_release)
        if released_ip:
            print(f"Released IP: {released_ip}")
        else:
            print(f"IP {ip_to_release} not found in leased IPs.")

    elif user_input == "STATUS":
        ip_to_check = input("Enter IP to check availability: ")
        availability_status = ip_manager.is_ip_available(ip_to_check)
        print(f"IP {ip_to_check} is available: {availability_status}")

    elif user_input == "EXIT":
        print("Exiting.")
        break

    else:
        print("Invalid command. Valid commands are ASK, RELEASE, STATUS, and EXIT.")
