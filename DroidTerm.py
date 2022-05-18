#! /bin/python
# _*_ ecoding: utf-8 _*_
import os
from getpass import getuser
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan

## Variables Defaults
logfile = ""
portB = 3304
user = getuser()
sh = os.system
protocols = ['TCP', 'UDP', 'ICMP', 'tcmp','VoIP', 'SERCOS', 'IP', 'HTTP', 'TLS', 'SSL', 'GET', 'POST']
protocols2 = ['tcp', 'udp', 'icmp','tcmp', 'voip', 'sercos', 'ip', 'http', 'tls', 'ssl', 'get', 'post']

def clear():
    sh("clear")
def banner():
    print(O+"""
 ____     ___ ______  __ __  __ __  ____   ______    ___  ____  
|    \   /  _]      ||  |  ||  |  ||    \ |      |  /  _]|    \ 
|  _  | /  [_|      ||  |  ||  |  ||  _  ||      | /  [_ |  D  )
|  |  ||    _]_|  |_||  _  ||  |  ||  |  ||_|  |_||    _]|    / 
|  |  ||   [_  |  |  |  |  ||  :  ||  |  |  |  |  |   [_ |    \ 
|  |  ||     | |  |  |  |  ||     ||  |  |  |  |  |     ||  .  \ 
|__|__||_____| |__|  |__|__| \__,_||__|__|  |__|  |_____||__|\_|
                                                                By Mrx04programmer
"""+W)
def catch():
    print(O)
    sh("cat "+logfile+" | grep 'Host:'")    
def scanport(ip):
    sh("""
#!/bin/bash
#count=1
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
grayColour="\e[0;37m\033[1m"


if [ -n " """+ip+""" " ];
then
   echo -e "${greenColour}[*]  PUERTOS ABIERTOS: ${blueColour}"
   nmap -p0-9999 """+ip+""" | grep 'open' | while read line; do
      echo -e "${blueColour}  [*] ${grayColour}$line"
      #count=$(($count + 1))
   done
   echo -e "${greenColour}[*]Finished !"
else
   echo "[-] Error"
fi 
""")
def main():
    while True:
        term = input(G+"root@"+user+" >> "+W)
        if (term == "help"):
            print("""
    server  <port> (need set logfile)     | connect <ip> <port>
    install <package name>  |remove <package name> | whatsystem <ip> 
    burp (need set logfile)| logfile <logfile name> 
    scanport <ip> | (commands of os)
    exit\n""")
        elif "scanport" in term:
            ip = term.split()[1]
            command = sh("which nmap >> /dev/null")
            if command == 0:
                scanport(ip)
            else:
                package = "nmap"
                print(R+"[ERROR] The command Nmap not found .")
                print(G+"["+W+"INSTALL"+G+"] "+W+"Installing "+package+"...")
        elif "connect" in term:
            ip = term.split()[1]
            port = term.split()[2]
            print(O+"[CONFIG] "+W+"Search the command Netcat...")
            netcat = sh("which nc >> /dev/null")
            if (netcat == 0):
                print(G+"[CONNECT] "+W+"127.0.0.1 "+O+"In "+ip+":"+port+"..."+G)    
                sh("nc -v "+ip+" "+port)
            else:
                package = "netcat-openbsd"
                print(R+"[ERROR] The command Netcat not found .")
                print(G+"["+W+"INSTALL"+G+"] "+W+"Installing "+package+"...")
                sh("apt install "+package)

            

        elif "logfile" in term:
            logfile = term.split()[1]
        elif "burp" in term:
            clear()
            banner()
            print(O+"[*] Initializing Burp Service...")
            command = sh("nc -h >> /dev/null")
            if command == 0 or command == 256:
                clear()
                banner()
                print(G+"["+W+"SERVER"+G+"] "+W+"Listening in the network (wlan default / Port 3304)")
                server = sh("nc -lnp "+str(portB)+" -w1 > "+logfile) 
                while True:
                    ro = ''
                    rq = ''
                    print(W)
                    sh("cat "+logfile+" | grep 'Host:'")
                    burp = input(O+"[BurpSuite] >> "+W)
                    if burp == "help":
                        print(W+"""
    
    help : Show help in the commands
    intercept <protocol/tcp/etc>: Intercept a package and edit
    ip : Set IP Local and Spoof
    exit : Exit of the Shell.
    clear : Clear the terminal""")
                    elif burp == "clear":
                        clear()
                    elif burp == "exit":
                        exit()
                    elif burp == "ip":
                        ip = input(C+"SET IP >> "+W)
                        sh("ip addr")
                    elif "intercept" in burp:
                        protocol = burp.split()[-1]
                        print(R+"["+protocol+"] "+W+"Protocol Intercepting...")
                        if protocol in protocols or protocol in protocols2:
                            ro = input(G+"[ORIGINAL REQUEST] >>"+W)
                            rq = input(G+"[MODIFIED REQUEST] >>"+W)
                            print(O)
                            sh("ip ntable | grep 'refcnt'")
                            if ro != '' and rq != '':
                                print(G+"[+] "+W+"REQUEST MODIFIED SUCCESSFUL")
                            elif ro == '' and rq == '':
                                print(G+"[-] "+W+"REQUESTS ARE NULL !")
                        else:
                            print(R+"[ERROR] Unknown Protocol "+protocol)
                    
                    

            else:
                print(R+"[-] No can run the Burp Service")
        elif "remove" in term:
            package = term.split()[1]
            print(G+"["+R+"REMOVE"+G+"] "+W+"Removing "+package+"...")
            sh("apt remove "+package)
        elif "server" in term:
            port = term.split()[1]
            print(B+"[*] "+W+"Starting server in "+port+"...")
            command = sh("nc -h >> /dev/null")
            if command == 0 or command == 256:
                clear()
                banner()
                print(G+"[+] Server running in port "+port)
                sh("nc -lnp "+port+" >> "+logfile)
            else:
                print(R+"[-] No can run the server")
                print(R+"Code: "+W+command)
        elif "install" in term:
            package = term.split()[1]
            clear()
            banner()
            print(G+"["+W+"INSTALL"+G+"] "+W+"Installing "+package+"...")
            try:
                sh("apt install "+package)
            except Exception as e:
                print(R+"Error in the proccess , Error: "+W+e)
        elif "whatsystem" in term:
            host = term.split()[1]
            ## Machines
            windows_Workgroups = sh("ping -c1 "+host+"| grep 'ttl=32' >> /dev/null")
            windows_general = sh("ping -c1 "+host+"| grep 'ttl=128' >> /dev/null")
            windows_general2 = sh("ping -c1 "+host+"| grep 'ttl=118' >> /dev/null")
            windows_general3 = sh("ping -c1 "+host+"| grep 'ttl=112' >> /dev/null")
            windows2 = sh("ping -c1 "+host+"| grep 'ttl=127' >> /dev/null")
            linux = sh("ping -c1 "+host+"| grep 'ttl=64' >> /dev/null")
            linux2 = sh("ping -c1 "+host+"| grep 'ttl=63' >> /dev/null")
            linux3 = sh("ping -c1 "+host+"| grep 'ttl=255' >> /dev/null")
            linux4 = sh("ping -c1 "+host+"| grep 'ttl=103' >> /dev/null")
            mac = sh("ping -c1 "+host+"| grep 'ttl=60' >> /dev/null")
            if windows_general == 0:
                print('OS Windows Generico')
            elif windows_general2 == 0:
            
                print('OS Windows Generico')
            elif windows_general3 == 0:
            
                print('OS Windows Generico')
            elif windows_Workgroups == 0:
            
                print('OS Windows Workgroups')
            elif windows2 == 0:
            
                print('OS Windows Generico')
            elif linux == 0:
            
                print('OS Linux')
            elif linux2 == 0:
            
                print('OS Linux')
            elif linux3 == 0:
            
                print('OS Linux')
            elif linux4 == 0:
                print('OS Linux')
            elif mac == 0:
                print('OS MacOS')
            else:
                print("OS Unknown")
        else:
            sh(term)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(R+"Error "+W+str(e))