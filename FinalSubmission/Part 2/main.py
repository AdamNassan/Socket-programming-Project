from socket import *  # call socket library.
server_address = ('', 9977)
serverSocket = socket(AF_INET, SOCK_STREAM)   # create tcp socket.
serverSocket.bind(server_address)
serverSocket.listen(1)  # port can listen to one connection only at the time
while True:
    print("THE SERVER IS READY TO RECEIVE <->")
    connection, client_address = serverSocket.accept()    # accept a new connection.
    data = connection.recv(1024).decode()   # receive the request
    print("IP: " + client_address[0] + ", Port: " + str(client_address[1]))
    print(data)
    ip = client_address[0]
    port = client_address[1]
    request_lines = data.split('\n')
    request_line = request_lines[0]
    request_uri = ''
    if len(request_lines) > 1:
        request_uri = request_line.split()[1]
    # Receive the data in small chunks and retransmit it
    try:
        # Check if the request is for /, /en, /index.h
        # tml,/ /main_en.html
        if request_uri == '/' or request_uri == '/en' or request_uri == '/index.html' or request_uri == '/main_en.html':
            connection.send("HTTP/1.1 200 OK\r\n".encode())  # print the HTTP requests on the terminal window
            connection.send('Content-Type: text/html \r\n'.encode())  # data type html
            connection.send('\r\n'.encode())
            f = open("EN.html", "rb")    # open html file
            connection.send(f.read())       # read it and sent
        elif request_uri == '/ar':           # if request /ar -->send arabic version
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: text/html \r\n'.encode())
            connection.send('\r\n'.encode())
            f = open("ar.html", "rb")
            connection.send(f.read())
            # Check if the request is for /go ,/so ,/bzu and send them to the specific wep.
        elif request_uri == '/yt':
            # Redirect to the Google website
            response_headers = b'HTTP/1.1 307 Temporary Redirect\nLocation: https://www.youtube.com/\n\n'
            connection.sendall(response_headers)
        elif request_uri == '/so':
            # Redirect to the Stack Overflow website
            response_headers = b'HTTP/1.1 307 Temporary Redirect\nLocation:https://stackoverflow.com/\n\n'
            connection.sendall(response_headers)
        elif request_uri == '/rt':
            # Redirect to the Birzeit University website
            response_headers = b'HTTP/1.1 307 Temporary Redirect\nLocation: https://ritaj.birzeit.edu/register/\n\n'
            connection.sendall(response_headers)
        elif request_uri.endswith(".png"):
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: image/png \r\n'.encode())
            connection.send('\r\n'.encode())
            testF = open("bzu.png", "rb")
            connection.send(testF.read())
        elif request_uri.endswith(".jpg"):
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: image/jpg \r\n'.encode())
            connection.send('\r\n'.encode())
            testF = open("llan.jpg", "rb")
            connection.send(testF.read())
        elif request_uri.endswith(".html"):
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: text/html \r\n'.encode())
            connection.send('\r\n'.encode())
            s = open("t.html", "rb")
            connection.send(s.read())
        elif request_uri.endswith(".css"):
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: text/css \r\n'.encode())
            s = open("TCSS.css", "rb")
            connection.send(s.read())     # send css file
        else:  # if the request does not found then send this error html file
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send('Content-Type: text/html\r\n'.encode())
            connection.send('\r\n'.encode())
            s = ("""
              <html>\n"
                 "                              <head>\n"
                 "	                               <title>Error</title>\n"
                 "                            </head>\n"
                 "<body>\n"
                 "	<h1>HTTP/1.1 404 Not Found</h1>\n"
                 "	<h2>Error 404</h2>\n"
                 "	<p style=\"color:red;\">The file is not found</p>\n"
                 "	<p><strong>Hidaya Mustafa 1201910<br>Rana Odeh 1201750<br>Adam Nassan 1202076</strong></p>"
                 "  <h1> IP: " + str(ip) + ", Port: " + str(port) + "</h1>\n"
                                                                    "</body>\n"
                                                         "</html>
                 """)
            connection.send(s.encode())

    finally:
        # Close the connection
        connection.close()