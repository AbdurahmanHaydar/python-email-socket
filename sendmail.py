import socket


host = '127.0.0.1'
port = 50003

#addressfamily internet, and SOCK_STREAM is for the tcp packets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


sender = raw_input("Enter the sender address: ")
recipient = raw_input("Enter the recipient address: ")
subject = raw_input("Enter the subject: ")


message = []
inp = ''
print "Type your message"
while inp != '.':
    user_inp=raw_input()
    arr = message.append(user_inp +' \n')
    if user_inp=='.':
        break
msg = "".join(str(i) for i in message)


payload = {'sender':sender,'recipient':recipient,'subject':subject,'message':msg}
s.sendall(str(payload))




print 'Email sent'


































#
# # Echo client program
# import socket
# import sys
#
# HOST = '127.0.0.1'    # The remote host
# PORT = 50007              # The same port as used by the server
# s = None
# for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
#     af, socktype, proto, canonname, sa = res
#     try:
#         s = socket.socket(af, socktype, proto)
#     except socket.error as msg:
#         s = None
#         continue
#     try:
#         s.connect(sa)
#     except socket.error as msg:
#         s.close()
#         s = None
#         continue
#     break
# if s is None:
#     print 'could not open socket'
#     sys.exit(1)
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
