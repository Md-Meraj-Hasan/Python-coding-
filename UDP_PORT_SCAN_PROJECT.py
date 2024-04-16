import socket
import threading

def ipAddress(host):
    try:
        ip_address = socket.gethostbyname(host)
        print("IP Address:", ip_address)
        return ip_address
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return None

def scanUDP(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(1)  # Set a timeout for the socket
        MESSAGE = "Hello, UDP server!"
        client.sendto(MESSAGE.encode('utf-8'), (host, port))
        data, addr = client.recvfrom(1024)
        return True
    except socket.error as e:
        if e.errno == socket.errno.ECONNREFUSED:
            return False
    finally:
        client.close()

def multipleThreading(host, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=portService, args=(host, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def portService(host, port):
    try:
        service_name = socket.getservbyport(port)
        if scanUDP(host, port):
            print('UDP Port {}: Open service: {}'.format(port, service_name))
    except OSError:
        pass  # Ignore ports with no associated service

host = input('Enter host name: ')
ip_address = ipAddress(host)
if ip_address:
    start_port = int(input('Enter start port: '))
    end_port = int(input('Enter end port: '))
    ports = range(start_port, end_port + 1)
    multipleThreading(host, ports)