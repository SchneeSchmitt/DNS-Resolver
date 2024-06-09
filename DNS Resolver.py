import socket

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address, None  # If success, the second value will be "None"
    except socket.error as err:
        return None, f"Error resolving hostname: {err}"  # if failed, the first value will be "None"

hostname = input('Input the domain name here:\n')
ip_address, error = resolve_hostname(hostname)

if ip_address:
    print(f"The IP address of {hostname} is {ip_address}")
else:
    print(error)

input("Press Enter to exit...")  # Prevents Windows terminal from closing immediately