# Socket Programming Project
## Part1: UDP client and server 
This project involves implementing UDP client and server applications in Go, Python, Java, or C. The server listens on port 8855, and the client sends broadcast messages every 2 seconds. Each message contains the sender's name (First name Last name). The server displays the last received message from each client, listing them in the format:
Server First name Last name:  
&nbsp;&nbsp;&nbsp;&nbsp;1- received message from First name Last name at Time  
&nbsp;&nbsp;&nbsp;&nbsp;2- received message from First name Last name at Time  
&nbsp;&nbsp;&nbsp;&nbsp;3- received message from First name Last name at Time  
Where "First name Last name" represents the sender's first and last names, and "Time" indicates the last time a message was received from that sender. IP addresses are used to distinguish between different senders.  

## Part2: Simple Web Server

Using socket programming, implement a simple but complete web server in Go, Python, Java, or C that listens on port 9977. The user can type URLs in the browser like http://localhost:9977/ar or http://localhost:9977/en. The server should handle various requests as follows:

-If the request is /, /index.html, /main_en.html, or /en (e.g., localhost:9977/ or localhost:9977/en), the server should send main_en.html file with Content-Type: text/html. The main_en.html file should contain an HTML webpage with:
  - "ENCS3320-My Tiny Webserver" in the title.
  - "Welcome to our course Computer Networks, This is a tiny webserver" (part of the phrase is in Blue).
  - Group members' names and IDs.
  - Information about the group members (projects, skills, hobbies, etc.).
  - CSS to style the page.
  - Division of the page into different boxes with student information.
  - An image with extension .jpg and an image with extension .png.
  - A link to a local HTML file.
  - A link to https://www.w3schools.com/python/gloss_python_multi_line_strings.asp.
  - If the request is /ar, the server responds with main_ar.html, which is the Arabic version of main_en.html.
  - If the request is a .html file, the server sends the requested HTML file with Content-Type: text/html.
  - If the request is a .css file, the server sends the requested CSS file with Content-Type: text/css.
  - If the request is a .png file, the server sends the requested PNG image with Content-Type: image/png.
  - If the request is a .jpg file, the server sends the requested JPG image with Content-Type: image/jpeg.
- Use the status code 307 Temporary Redirect to redirect the following:
  - If the request is /yt, redirect to the YouTube website.
  - If the request is /so, redirect to stackoverflow.com.
  - If the request is /rt, redirect to the ritaj website.
- If the request is wrong or the file doesn't exist, the server should return a simple HTML webpage with:
  - "HTTP/1.1 404 Not Found" in the response status.
  - "Error 404" in the title.
  - "The file is not found" in the body in red.
  - Your names and IDs in bold.
  - The IP and port number of the client.
- The program should print the HTTP requests on the terminal window (command line window).

## Setup Instructions
1. Ensure that all computers are within the same subnet.
2. Run a client or server application for each student, with at least 2 clients and one server in a group of 3 students.
