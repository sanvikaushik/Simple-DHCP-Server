# Simple DHCP Server

## Duration: February 1st, 2024 (3 hours)

## Overview
SimpleDHCP is a console-based tool for dynamically managing IP addresses. It simulates the core functionalities of a DHCP server, allowing users to allocate, release, and check the availability of IP addresses efficiently.

---

## Features
- **Allocate IP Addresses**: Dynamically assign the next available IP address in sequence.
- **Release IP Addresses**: Free up a previously allocated IP address.
- **Check IP Availability**: Verify whether a specific IP address is currently available.

---

## How It Works
### IP Allocation
- Starts with `0.0.0.0` as the first IP address.
- Subsequent IPs are calculated by incrementing the last octet, with overflow carried to the preceding octets.
- Example progression: `0.0.0.0`, `0.0.0.1`, ..., `0.0.0.255`, `0.0.1.0`.

### IP Release
- Removes a specified IP address from the leased pool, making it available for reallocation.

### IP Availability Check
- Confirms if a specified IP address is currently in the leased pool or available.

---

## Commands
- **`ASK`**: Allocates a new IP address.
- **`RELEASE`**: Releases a specified IP address back to the pool.
- **`STATUS`**: Checks the availability of a specific IP address.
- **`EXIT`**: Ends the session.

---

## Example Usage

```text
Enter command (ASK/RELEASE/STATUS/EXIT): ASK
Allocated IP: 0.0.0.0

Enter command (ASK/RELEASE/STATUS/EXIT): STATUS
Enter IP to check availability: 0.0.0.0
IP 0.0.0.0 is available: False

Enter command (ASK/RELEASE/STATUS/EXIT): RELEASE
Enter IP to release: 0.0.0.0
Released IP: 0.0.0.0

Enter command (ASK/RELEASE/STATUS/EXIT): EXIT
Exiting.
