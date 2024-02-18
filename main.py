import socket


def main():

    ping = "+PONG\r\n"
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept()
    with conn:
        while(message:=conn.recv) == True:
            conn.sendall(ping.encode())


if __name__ == "__main__":
    main()
