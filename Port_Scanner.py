import socket
import subprocess
import datetime

def portScanner(target):
    try:
        ip = socket.gethostbyname(target)
        
        print(f"Scannaing the target {ip}")
        print(f"Time started: {datetime.datetime.now()}")

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port Open {}".format(port))
            sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")

    except socket.error:
        print("Could not connect to the server")
    
target = input("Enter the targe IP address: ")
portScanner(target)