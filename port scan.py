import socket
import threading
 
log_file = "scan_results.txt"

def scan_port(host,port,timeout=1):
    try: 
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host,port))
        sock.close()
        if result == 0:
            output = f"[OPEN] port {port}"
        else:
            output = f"[CLOSED] port {port}"

    except socket.timeout:
        output = f"[TIMEOUT] port {port}"
    except Exception as e:
        output = f"[ERROR] port {e}"

    print(output)
    with open(log_file, "a") as f :
        f.write(output + "/n")

def port_scanner(host,start_port,end_port):
    print(f"/nscanning {host} from port { start_port} to {end_port}/n")
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host,port))
        threads.append(t)
        t.start()

        for t in threads:
            t.join()
            print("/nscan completed. results saved to scan_results.txt")


if __name__ == "__main__":
    target = input("Enter target host (IP or domain ):")
    start = int(input("Enter start port:"))
    end = int(input("enter end port:"))
    port_scanner(target ,start,end)
                                                          
