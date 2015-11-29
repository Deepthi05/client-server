# client-server
Server program in Python that mimics a simple request/response stateless transactional server.
"""
You are to write a small server program in Python that mimics a simple request/response stateless transactional server. 
If a client sends a request to the server, the server responds with a response. Assume that request is always a printable text 
and response is simply the ‘reverse text’ of the received request. The program must be able to handle at least 100 concurrent 
sessions, though design should not have any limits per se. Each session consists of:
 
- Client first opens a TCP connection to the server
 
- Client then repeats a series of request/response as follows: 
a) send a request text on the connection and 
b) receive the response from server
 
- Client may then close the connection or the server closes the connection if no request is received on server side for more than
5 seconds
 
Server program should be in Python and use tcp/ip sockets programming. Ideally implemented this using asynch communication
as a single-process event-driven methods instead of threads"""
