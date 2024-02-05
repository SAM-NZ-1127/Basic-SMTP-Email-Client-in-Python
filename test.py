from socket import *
import base64
import ssl
import sys

valid_domains = ['gmail.com', 'getnede.com', 'zohomail.com', 'uwm.edu', 'uic.edu', 'hotmail.com', 'yahoo.com', 'outlook.com', 'example.com']

senders = []
recipients = []
subjects = []
bodies = []

def read_files():
    for arg in sys.argv[1:]:
        with open(arg) as file:
            for line in file:
                parts = line.split()
                try:
                    if parts[0] == "From:":
                        senders.append(parts[2].strip())
                    elif parts[0] == "To:":
                        recipients.append(parts[2].strip())
                    elif parts[0] == "Subject:":
                        subjects.append(" ".join(parts))
                    else:
                        bodies.append(" ".join(parts))
                except IndexError:
                    pass

read_files()

for i in range(len(sys.argv) - 1):
    print(f"{sys.argv[i + 1]} i={i}")
    c = i

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    mail_server = ("smtp.gmail.com", 465)
    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        clientSocket = context.wrap_socket(clientSocket)
        clientSocket.connect(mail_server)
        recv = clientSocket.recv(1024).decode()

    print("\nMessage after connection request:" + recv)
    if recv[:3] != '220':
        print('Error 220: No Response From Server')

    helloCommand = 'EHLO Shivam\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print("Message after EHLO command:" + recv1)
    if recv1[:3] != '250':
        print('Error 250: No Response From Server')

    username = 'shivamnz.mehta1234@gmail.com'
    password = "sotudukalfrfafiz"
    base64_str = (f"\x00{username}\x00{password}").encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print("output:", recv_auth.decode())
    
    try:
        recipient_email = recipients[c].split('@')[-1].replace('>', '')

        if recipient_email in valid_domains:
            mail_from = f"MAIL FROM: {senders[c]}\r\n"
            clientSocket.send(mail_from.encode())
            recv2 = clientSocket.recv(1024).decode()
            print("After MAIL FROM command: " + recv2)

            rcptTo = f"RCPT TO: {recipients[c]}\r\n"
            clientSocket.send(rcptTo.encode())
            recv3 = clientSocket.recv(1024).decode()
            print("After RCPT TO command: " + recv3)

            data = "DATA\r\n"
            clientSocket.send(data.encode())
            recv4 = clientSocket.recv(1024).decode()
            print("After DATA command: " + recv4)

            subject = f"{subjects[c]}\r\n\r\n"
            clientSocket.send(subject.encode())

            message = f"\r\n{bodies[c]}"
            end_message = "\r\n.\r\n"
            clientSocket.send(message.encode())
            clientSocket.send(end_message.encode())
            recv_msg = clientSocket.recv(1024).decode()
            print("After Body is sent:" + recv_msg)

            connection_close = "QUIT\r\n"
            clientSocket.send(connection_close.encode())
            recv5 = clientSocket.recv(1024).decode()
            print(recv5)
            clientSocket.close()
        else:
            print("Invalid email domain, format, or recipient")
    except:
        print("Invalid email")
