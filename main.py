import socket
import threading


def handle_client(conn):
    ping = "+PONG\r\n"
    with conn:
        while True:
            conn.recv(1024)
            conn.sendall(ping.encode())


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()


if __name__ == "__main__":
    main()
