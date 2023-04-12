import socket
import time

turn = 0

with socket.socket() as s:
    s.connect(('localhost',11111))
    while True:
        if turn == 0:
            inp = input('Введите что-то чтоб начать игру:')
            print()
            data = s.recv(1024)
            print(data.decode())
            turn += 1
        else:
            inp = input('Введите номер поля:')
            s.send(inp.encode())
            data = s.recv(1024)
            print()
            print(data.decode())
            data2 = s.recv(1024)
            if data2.decode() != '123':
                print(data2.decode())
                time.sleep(10)
                break