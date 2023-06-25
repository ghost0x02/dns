import socket
import os
import platform
import time
from colorama import Fore, Style

print(Fore.GREEN + """

      .o8
     "888
 .oooo888  ooo. .oo.    .oooo.o
d88' `888  `888P"Y88b  d88(  "8
888   888   888   888  `"Y88b.
888   888   888   888  o.  )88b
`Y8bod88P" o888o o888o 8""888P' """)



def check_dns(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"{hostname} [✓] DNS çözümü başarılı. IP adresi: {ip_address}")
    except socket.gaierror:
        print(f"{hostname} [✓] DNS çözümü başarısız.")


website = input(Fore.YELLOW + "Site adını girin: ")
time.sleep(2)
os.system("nmap -sn -n -v --open")
time.sleep(3)
print(Fore.RED + "======================================")
print("[!] DİG +short")
print("")
os.system("dig +short")
time.sleep(3)

print(Fore.YELLOW + "======================================")
print("CODED BY ENESXSEC - GHOST SEC")
print("")


check_dns(website)
