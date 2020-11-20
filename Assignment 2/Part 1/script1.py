# IP address 
  
# Importing socket library 
import socket 
from time import sleep   
  
# Function to display hostname and 
# IP address 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
        
    sleep(5)                                                                       
    print('End of process 1')

# Driver code 
get_Host_name_IP() #Function call

                                                       
                                                                                
