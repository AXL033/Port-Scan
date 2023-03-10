# usr/bin/env python

import socket
import ipinfo
import subprocess as sb
from threading import Thread
from colorama import init, Fore
from progress.bar import IncrementalBar


class Main:

    def __init__(self):
        # Colorama init
        init()
        self.clear()
        # IPInfo
        self.handler = ipinfo.getHandler("cda874226c0c24")
        # Ports
        self.open_ports = []
        self.ports = {
        1: "TCPMUX",2: "COMPRESSNET",17: "QOTD",18: "MSP",19: "CHARGEN",
        20: "FTP-DATA",21: "FTP",22: "SSH",23: "Telnet",24: "PRIV-MAIL",
        25: "SMTP",26: "RSFTP",27: "NSW-FE",43: "WHOIS",53: "DNS",
        80: "http",100: "NEWACCT",115: "SFTP",119: "NNTP",120: "CFDPTKT",
        123: "NTP",143: "IMAP",161: "SNMP",179: "BGP",443: "HTTPS",445: "MICROSOFT-DS",
        514: "SYSLOG",515: "PRINTER",993: "IMAPS",995: "POP3S",1000: "CADLOCK2",
        1001: "sabserv",1002: "cogbot",1010: "SURF",1080: "SOCKS",
        1194: "OpenVPN",1433: "SQL Server",1723: "PPTP",3128: "HTTP",
        3268: "LDAP",3306: "MySQL",3389: "RDP",5432: "PostgreSQL",5900: "VNC",
        8080: "Tomcat",10000: "Webmin",10001: "Lantronix",10050: "Zabbix-Agent",
        10008: "Octopus Multiplexer",10051: "Zabbix-Trapper"
        }
        # Colors
        self.red, self.green = Fore.RED, Fore.GREEN
        self.yellow, self.magenta = Fore.YELLOW, Fore.MAGENTA
        # Logo
        print(f"""{self.green}
        █▀█ █▀█ █▀█ ▀█▀ ▄▄ █▀ █▀▀ ▄▀█ █▄░█
        █▀▀ █▄█ █▀▄ ░█░ ░░ ▄█ █▄▄ █▀█ █░▀█{self.magenta}
        [+] Created By AXL033
        [+] Found a mistake? Let me know on Telegram: https://t.me/axl033
        """)
        # Getting informations
        self.url = input(f"{self.yellow}[?] Enter the URL address (example.com): ")
        self.ip = socket.gethostbyname(self.url)
        try:
            self.portsBrute()
        except:
            print(f"{self.red}[-] Enter the correct URL address.")

    def portScan(self, portNumber):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        if sock.connect_ex((self.ip, portNumber)) == 0:
            self.open_ports.append(portNumber)
        sock.close()

    def portsBrute(self):
        # Scaning open ports
        with IncrementalBar("[/] Scaning ports", max=len(self.ports)) as bar:
            for port in self.ports.keys():
                Thread(target=self.portScan(port))
                bar.next()

            print("\n")

            for i in self.open_ports:
                print(f"{self.magenta}[+] PORT: {i} IS OPEN <=> {self.ports[i]}")

            # Get information about IP
            self.details = self.handler.getDetails(self.ip)
            print(f"""{self.magenta}
            - - - - - - - - -
            |IP Information|
            - - - - - - - - -
            [+] HostName: {self.details.hostname}
            [+] City: {self.details.city}
            [+] Region: {self.details.region}
            [+] Country: {self.details.country}
            [+] Location: {self.details.loc}
            [+] Organization: {self.details.org}
            [+] TimeZone: {self.details.timezone}
            """)

    def clear(self):
        try:
            sb.call(["cls"], shell=1)
        except:
            sb.call(["clear"], shell=1)


if __name__ == "__main__":
    Main()
