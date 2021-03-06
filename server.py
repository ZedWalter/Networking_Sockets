
#import the socket library
import socket
  
# next create a socket object
s = socket.socket()
print ("Socket successfully created")
  
# reserve a port on your computer
port = 12345
  

# Bind port, typing in empty string to allow server to listen to requests
s.bind(('', port))
print (f"socket binded to {port}")
  
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")
  
# Loop until error or end program
while True:
  
    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )
  
    # send a thank you message to the client.
    c.send(b'Thank you for connecting')
  
    # Close the connection with the client
    c.close()