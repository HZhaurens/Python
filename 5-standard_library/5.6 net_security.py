import socket
import hashlib

# socket示例
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("example.com", 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    print("响应:", s.recv(1024))

# hashlib示例
m = hashlib.sha256()
m.update(b"password")
print("SHA256哈希:", m.hexdigest())