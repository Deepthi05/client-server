 
import socket, select
 
#Function to send messages to all connected clients
def send_message (sock, message):
  
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)
 
if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(100)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:
        # Get the list sockets which are ready to be read through select, with timeout of 5 seconds
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[],5)
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
				try:
					# Handle the case in which there is a new connection recieved through server_socket
					sockfd, addr = server_socket.accept()
					CONNECTION_LIST.append(sockfd)
					print "Client (%s, %s) connected" % addr
					 
					send_message(sockfd, "[%s:%s] entered room\n" % addr)
				expect socket.timeout:
					print "Timeout"
             
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                   data = sock.recv(RECV_BUFFER)
                    if data:
                        send_message(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
                 
                except:
                    send_message(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()