#Domain to ip
#!/usr/bin/python3
import socket
import pyfiglet
import colorama

banner=pyfiglet.figlet_format("Domain To IP")
print(colorama.Fore.GREEN+banner)
print("************** Created By 0xbokhtiar ****************")
print("   ")
domain_name=input("Enter your Domain : ")
print("   ")
ip=socket.gethostbyname(domain_name)
print("IP For {} : {}".format(domain_name,ip))
print("   ")
