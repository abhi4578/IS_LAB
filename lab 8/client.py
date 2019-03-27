# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12349				

# connect to the server on local computer 
s.connect(('192.168.43.194', port)) 
#10.53.124.251
#10.53.97.21
# receive data from the server 

s.send('104034'.encode()) 
# close the connection 
s.close()



    