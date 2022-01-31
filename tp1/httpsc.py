#lib imports.
#Note : all libraries are already installed no need for pip
import socket, sys
from urllib.parse import urlparse

def request(PORT, HOST, URI, BODY, METHOD):

    #Creating the request string here for code readability
    REQUEST = '%s %s HTTP/1.1\r\nHost: %s\r\n\r\n%s' % (METHOD, URI, HOST, BODY)

    #debug print
    print(REQUEST)
    print("===============================================")

    #Creating the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(REQUEST.encode())
        response = s.recv(1024)

    #Parsing the response from bytes to UTF-8 str
    str_res = str(response, 'utf-8')
    #Parsing of the response code
    try :
        print("Got response : " + str_res.split("\n")[0])
        print("===============================================")
        if str_res.split(' ')[1][0] == "1" or str_res.split(' ')[1][0] == "2":
            print(str_res)

        #Handling of redirection
        if str_res.split(' ')[1][0] == "3":
            print("Redirection to : " + str_res.split("Location: ")[1])
            print("===============================================")
            #We need a try/except combo if the PORT is not specified in the Location field
            try :
                print(str_res.split("Location: ")[1].split("\n")[0])
                parsed = urlparse(str_res.split("Location: ")[1].split("\n")[0])
                try :
                    PORT = int(parsed.netloc.split(':')[1])
                except :
                    PORT = 80
                try :
                    HOST = parsed.netloc.split(':')[0]
                except :
                    print("COULD NOT FIND HOST")
                    sys.exit(1)
                URI = parsed.path
                request(PORT, HOST, URI, BODY, METHOD)
            except :
                print("COULD NOT REQUEST AFTER REDIRECTION")

        if str_res.split(' ')[1][0] == "4" or str_res.split(' ')[1][0] == "5":
            print("You got an error. Check the response below :")
            print(str_res)
    except:
        print("Could not read response. Is this really HTTP ?")

http_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

#URL parsing for all the variables
try :
    parsed = urlparse(sys.argv[1])
    try :
        PROTOCOL = parsed.scheme
        URI = parsed.path
    except :
        PROTOCOL = "http://"

    try :
        HOST = parsed.netloc.split(':')[0]
        PORT = int(parsed.netloc.split(':')[1])
    except :
        HOST = parsed.netloc.split(':')[0]
        PORT = 80
#If we can't extract all the needed information we stop the program
except :
    print("COULD NOT PARSE THE URL. CHECK THE FORMAT ?")
    sys.exit(1)

#Parsing of the method. Default is GET
try :
    METHOD = sys.argv[2].upper()
    if METHOD not in http_methods :
        print("YOUR HTTP METHOD IS NOT CORRECT. TRY ANOTHER ONE.")
        sys.exit(1)
except :
    METHOD = "GET"

#If we don't have an URI we simply ask for index.html
if URI == '':
    URI = "/index.html"


#Parsing of the request body if needed
BODY = ''
request_with_bodies = ["POST", "PUT", "PATCH", "CONNECT"]
if METHOD in request_with_bodies:
    try :
        BODY = sys.argv[3]
    except :
        print("No body was provided, please input one :")
        BODY = input()

request(PORT, HOST, URI, BODY, METHOD)