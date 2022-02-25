# test

from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1', debug=False):

    def print_debug(msg):
        if debug:
            print(msg)

    msg = "Hello, World!\r\n\r\nPutin sucks!"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    def receive(expected):
        recv = clientSocket.recv(1024).decode()
        print_debug(recv) #You can use these print statement to validate return codes from the server.
        if (expected and recv[:3] != expected):
            print_debug(expected,'reply not received from server.')

    receive('220')

    def send(command,expected=None):
        clientSocket.send(command.encode())
        if expected:
             receive(expected)

    # Send HELO command and print server response.
    send('HELO Alice\r\n', '250')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    send('MAIL FROM: <wbc2025@nyu.edu>\r\n', '250')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    send('RCPT TO: <wbc2025@nyu.edu>\r\n', '250')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    send('DATA\r\n', '354')
    # Fill in end

    # Send message data.
    # Fill in start
    send(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    send(endmsg, '250')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    send('QUIT\r\n', '221')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

    # nyu mail server while on VPN
    # smtp_client(1025, 'smtp.nyu.edu',True)