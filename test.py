import socket
import threading

port = 5050
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, port)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def handle_client(conn, addr):
    print(addr, "bağlandı")
    connected = True

    while connected:
        msg_length = conn.recv(64).decode("utf-8")
        if msg_length:
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            if msg == "kapatlan":
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()




def start():
    server.listen()
    print(f"[DİNLE] {Server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("başladı")

print("Server başlıyor")
start()
