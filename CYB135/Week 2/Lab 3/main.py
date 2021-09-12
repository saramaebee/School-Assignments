import random

def create_random_open_ports():
  #Create empty list / dictionary
  port = []
  ports = {}

  #Fill list with 100 random port numbers from 10 - 100
  for i in range(1,101):
    random_port = random.randint(10, 100)
    port.append(random_port)

  #Create a new dictionary with ports numbers as keys
  new_ports = ports.fromkeys(port, 0)

  #Iterate through new dictionary add random 0 / 1
  #Closed port = 0, Open port = 1
  for key in new_ports:
    r1 = random.randint(0,1)
    new_ports[key] = r1
  return new_ports
  
# TODO: create a function called create_host_IPs() that randomly generates a list of 10 IP addresses
# concatenating the 4 values into a string and appending it to a host list.  The function returns the generated
# host list
def create_host_IPs():
    host = []
    octet1 = ""
    octet2 = ""
    octet3 = ""
    octet4 = ""
    #Add loop with range 1 - 11 to create the 10 host IPs EX: 192.123.11.1
    for i in range(10):
        octet1 = random.randint(10, 200)
        octet2 = random.randint(10, 200)
        octet3 = random.randint(10, 200)
        octet4 = random.randint(10, 200)
        host.append(f'{octet1}.{octet2}.{octet3}.{octet4}')
    return host

# TODO: create a function called simulate_scan(h) that iterates through the host list (received as h ) and 
# then creates a new list called open_ports.  The function should use a nested for loop that iterates 
# through the host list, and then iterates through the returned list from a call to create_random_open_ports(). 
# If the returned list value is 1, then append it to your open_ports list. 
# This simulates a scan of all the IPs in the host list and creates randomly generated open ports.
# Finally it should print the host IP and a list of open ports as displayed in assignment information. 
def simulate_scan(h):
    host_port_list = []
    
    for i in range(len(h)):
        ports = {}
        ports['ip'] = h[i]
        port_array = []
        
        open_ports = create_random_open_ports()
        # print(open_ports)
        
        for key in open_ports:
            if open_ports[key] == 1:
                port_array.append(key)
        
        ports['ports'] = port_array
        host_port_list.append(ports)
    
    for element in host_port_list:
        # print(element['ip'])
        ip = element['ip']
        ports = element['ports']
        print(f'Host IP: {ip}')
        print(f'Open ports are: {ports}')
    
if __name__ == "__main__":
  
  #Simulate port scanning for open ports
  active_hosts = create_host_IPs()
  simulate_scan(active_hosts)
 
  
