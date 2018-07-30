import socket



# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect the client
    # client.connect((target, port))
    client.connect(('192.168.1.9', 2020))

    client.settimeout(3)


    while True:
        # send some data (in this case a HTTP GET request)
        client.send(b'g161\r\n')
        # receive the response data (4096 is recommended buffer size)
        response = client.recv(4096)
        response = str(response).split(' ')[1]
        response = float(str(response).split('\\')[0])/10000
        print(response)

except client.timeout:
    print("Time out oluştu")
    client.close()