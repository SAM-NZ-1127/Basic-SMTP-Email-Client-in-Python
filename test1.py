from socket import *
import base64
import ssl
import sys

valid_domain = ['gmail.com','getnede.com','zohomail.com','uwm.edu','uic.edu','hotmail.com','yahoo.com', 'outlook.com','example.com']

sender = []
recipient = []
subjects = []
body = []

def read_files():
    for i in range(1,len(sys.argv)):
        with open(sys.argv[i]) as f:
            for line in f:
                line = line.split()
                try:
                    if line[0] == "From:":
                        sender.append(line[2].strip())
                    elif line[0] == "To:":
                        recipient.append(line[2].strip())
                    elif line[0] == "Subject:":
                        subjects.append(" ".join(line))
                    else:
                        body.append(" ".join(line))
                except:
                    pass

read_files()
print(sender)
print(recipient)
print(subjects)
print(body)

for i in range(1,len(sys.argv)):
    print(sys.argv[i], 'i=',i )
    c = i-1

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    mail_server = ("smtp.gmail.com", 465)
    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        clientSocket = context.wrap_socket(clientSocket)
        clientSocket.connect(mail_server)
        recv = clientSocket.recv(1024)
        recv = recv.decode()

    print("\nMessage after connection request:" + recv)
    if recv[:3] != '220':
        print('Error 220: No Response From Server')

    helloCommand = 'EHLO Shivam\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    print("Message after EHLO command:" + recv1)
    if recv1[:3] != '250':
        print('Error 250: No Response From Serve')

    # Info for username and password
    username = 'shivamnz.mehta1234@gmail.com'
    password = "sotudukalfrfafiz"
    base64_str = ("\x00" + username + "\x00" + password).encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print("output:",recv_auth.decode())
    try:

        email_ID = recipient[c].split('@')[-1]
        email_ID = email_ID.replace('>', '')
        print(email_ID)

        if email_ID in valid_domain:

            mail_from = "MAIL FROM: {mailer}\r\n".format(mailer = sender[c])
            clientSocket.send(mail_from.encode())
            recv2 = clientSocket.recv(1024)
            recv2 = recv2.decode()
            print("After MAIL FROM command: " + recv2)

            rcptTo = "RCPT TO: {rcpt}\r\n".format(rcpt = recipient[c])
            clientSocket.send(rcptTo.encode())
            recv3 = clientSocket.recv(1024)
            recv3 = recv3.decode()
            print("After RCPT TO command: " + recv3)

            data = "DATA\r\n"
            clientSocket.send(data.encode())
            recv4 = clientSocket.recv(1024)
            recv4 = recv4.decode()
            print("After DATA command: " + recv4)

            subject = "{subject}\r\n\r\n".format(subject=subjects[c])
            clientSocket.send(subject.encode())

            message = "\r\n{msg}".format(msg=data[c])
            end_message = "\r\n.\r\n"
            clientSocket.send(message.encode())
            clientSocket.send(end_message.encode())
            recv_msg = clientSocket.recv(1024)
            print("After Body is sent:" + recv_msg.decode())

            connection_close = "QUIT\r\n"
            clientSocket.send(connection_close.encode())
            recv5 = clientSocket.recv(1024)
            print(recv5.decode())
            clientSocket.close()
        else:
            print("Invalid email domain or format")
    except:
        print("Invalid email format")