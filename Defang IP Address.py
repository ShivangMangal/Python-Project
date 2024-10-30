def defang_ip_address(ip):
    """
    Defangs the given IP address by replacing dots with '[.]'.

    Parameters:
        ip (str): The IP address to defang.

    Returns:
        str: The defanged IP address.
    """
    return ip.replace('.', '[.]')


ip_address = "192.168.1.1"
defanged_ip = defang_ip_address(ip_address)
print("Original IP address:", ip_address)
print("Defanged IP address:", defanged_ip)
