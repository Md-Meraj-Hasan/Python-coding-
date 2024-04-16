import socket
import threading
print("MD MERAJ HASAN\nWelcome to Port Scan Project.")
def ipAddress(host):
    try:
        ip_address = socket.gethostbyname(host)
        print("IP ADDRESS: {}: {}".format(host, ip_address))
        return ip_address
    except socket.gaierror:
        return None
def portScan(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    except Exception:
        return None
host = input("Enter host/IP address: ")
def multipleThreading(host, ports):
    threads=[]
    ip_address = ipAddress(host)
    if ip_address:
        for port in ports:
            try:
                thread = threading.Thread(target=portService,args=(host, port))
                threads.append(thread)
                thread.start()
            except:
                return None 
    else:
        print("host or ip couldn't resolved: ",host)               
def portService(host, port):
    if portScan(host, port):
        try:
            service_name = socket.getservbyport(port)
            print("Port {} is open: service {}".format(port, service_name))
        except OSError:
            pass
start_port= int(input('enter start Port: ')) 
end_port= int(input('enter end port: '))        
ports = range(start_port,end_port +1)
multipleThreading(host, ports)